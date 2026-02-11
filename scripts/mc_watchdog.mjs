import fs from 'fs';
import http from 'http';

// Watchdog: if a scheduled recurring task stays in `ready` too long, mark blocked and ping Felipe.
// Designed for Mission Control internal network: http://mission-control:3000
// Uses x-api-key from /home/node/.openclaw/credentials/mission_control_agent_key

const MC_URL = process.env.MISSION_CONTROL_URL || 'http://mission-control:3000';
const KEY_PATH = process.env.MISSION_CONTROL_API_KEY_FILE || '/home/node/.openclaw/credentials/mission_control_agent_key';

// Defaults for the SEO weekly task
const TASK_ID = Number(process.env.MC_WATCH_TASK_ID || '22');
const TZ = process.env.MC_WATCH_TZ || 'America/Sao_Paulo';
const MAX_READY_MINUTES = Number(process.env.MC_WATCH_MAX_READY_MINUTES || '30');
const TAG_ALERTED = process.env.MC_WATCH_ALERT_TAG || 'watchdog-alerted';

function nowInTzParts(tz) {
  const d = new Date();
  const fmt = new Intl.DateTimeFormat('en-US', {
    timeZone: tz,
    weekday: 'short',
    year: 'numeric', month: '2-digit', day: '2-digit',
    hour: '2-digit', minute: '2-digit', second: '2-digit',
    hour12: false,
  });
  const parts = Object.fromEntries(fmt.formatToParts(d).filter(p => p.type !== 'literal').map(p => [p.type, p.value]));
  return parts;
}

function reqJson(method, path, bodyObj) {
  const key = fs.readFileSync(KEY_PATH, 'utf8').trim();
  const u = new URL(MC_URL);
  const body = bodyObj ? Buffer.from(JSON.stringify(bodyObj)) : null;
  const opts = {
    method,
    hostname: u.hostname,
    port: u.port || 80,
    path,
    headers: {
      'Accept': 'application/json',
      'x-api-key': key,
      ...(body ? { 'Content-Type': 'application/json', 'Content-Length': body.length } : {}),
    },
  };
  return new Promise((resolve, reject) => {
    const r = http.request(opts, (res) => {
      let data = '';
      res.on('data', (c) => data += c);
      res.on('end', () => {
        if (res.statusCode && res.statusCode >= 200 && res.statusCode < 300) {
          try { resolve(data ? JSON.parse(data) : {}); } catch { resolve({}); }
        } else {
          reject(new Error(`HTTP ${res.statusCode}: ${data.slice(0, 300)}`));
        }
      });
    });
    r.on('error', reject);
    if (body) r.write(body);
    r.end();
  });
}

function minutesBetween(aIso, bIso) {
  const a = new Date(aIso).getTime();
  const b = new Date(bIso).getTime();
  return Math.floor((b - a) / 60000);
}

async function main() {
  // Only enforce weekly watchdog on Mondays after 09:00 local.
  const p = nowInTzParts(TZ);
  const weekday = p.weekday; // Mon/Tue...
  const hour = Number(p.hour);
  if (weekday !== 'Mon' || hour < 9) {
    console.log(JSON.stringify({ok: true, skipped: true, reason: 'not Monday 09:00+ local'}));
    return;
  }

  const task = await reqJson('GET', `/api/tasks/${TASK_ID}?schema=minimal`);

  // Expect minimal schema fields
  const { column, tags = [], updatedAt, title } = task;

  if (column !== 'ready') {
    console.log(JSON.stringify({ok: true, skipped: true, reason: `column=${column}`}));
    return;
  }

  if (tags.includes(TAG_ALERTED)) {
    console.log(JSON.stringify({ok: true, skipped: true, reason: 'already alerted'}));
    return;
  }

  const mins = updatedAt ? minutesBetween(updatedAt, new Date().toISOString()) : 999;
  if (mins < MAX_READY_MINUTES) {
    console.log(JSON.stringify({ok: true, skipped: true, reason: `ready for ${mins}m < ${MAX_READY_MINUTES}m`}));
    return;
  }

  // Mark blocked + add tag + log activity. Poller2 will ping Felipe.
  await reqJson('PATCH', `/api/tasks/${TASK_ID}`, {
    blocked: true,
    blocker_reason: `Watchdog: still in READY for ${mins} minutes after scheduled time.`,
    tags: [...tags, TAG_ALERTED],
    column: 'blocked',
  });

  await reqJson('POST', `/api/tasks/${TASK_ID}/activity`, {
    action: 'progress',
    user: 'Amadeus',
    details: `Watchdog tripped: task stayed in READY for ${mins}m. Marked blocked + tagged ${TAG_ALERTED}.`,
    type: 'human',
  });

  console.log(JSON.stringify({ok: true, alerted: true, minsReady: mins, task: {id: TASK_ID, title}}));
}

main().catch((e) => {
  console.error(String(e));
  process.exit(1);
});
