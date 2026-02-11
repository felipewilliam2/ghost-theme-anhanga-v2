import fs from 'fs';
import crypto from 'crypto';
import https from 'https';

function b64url(input) {
  const buf = Buffer.isBuffer(input) ? input : Buffer.from(typeof input === 'string' ? input : JSON.stringify(input));
  return buf.toString('base64').replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');
}

function signJwtHS256({kid, secretHex, aud}) {
  const now = Math.floor(Date.now() / 1000);
  const header = { alg: 'HS256', typ: 'JWT', kid };
  const payload = { iat: now, exp: now + 5 * 60, aud };
  const unsigned = `${b64url(header)}.${b64url(payload)}`;
  const sig = crypto.createHmac('sha256', Buffer.from(secretHex, 'hex')).update(unsigned).digest();
  return `${unsigned}.${b64url(sig)}`;
}

function requestJson(url, {method='GET', headers={}, bodyObj}={}) {
  return new Promise((resolve, reject) => {
    const u = new URL(url);
    const body = bodyObj ? Buffer.from(JSON.stringify(bodyObj)) : null;
    const opts = {
      method,
      hostname: u.hostname,
      path: u.pathname + u.search,
      headers: {
        'Accept': 'application/json',
        ...(body ? {'Content-Type': 'application/json', 'Content-Length': body.length} : {}),
        ...headers,
      },
    };
    const req = https.request(opts, (res) => {
      let data = '';
      res.on('data', (c) => data += c);
      res.on('end', () => {
        try {
          const parsed = data ? JSON.parse(data) : {};
          if (res.statusCode && res.statusCode >= 200 && res.statusCode < 300) return resolve({status: res.statusCode, json: parsed});
          const err = new Error(`HTTP ${res.statusCode}: ${data}`);
          err.status = res.statusCode;
          return reject(err);
        } catch (e) {
          const err = new Error(`Bad JSON / HTTP ${res.statusCode}: ${data}`);
          err.cause = e;
          err.status = res.statusCode;
          return reject(err);
        }
      });
    });
    req.on('error', reject);
    if (body) req.write(body);
    req.end();
  });
}

// Usage:
// node ghost_create_draft.mjs --url https://blog.example.com --keyfile /path/admin_api_key.txt --title "..." --slug "..." --htmlfile ./post.html --metadesc "..." --tags "tag1,tag2"

function arg(name) {
  const idx = process.argv.indexOf(name);
  return idx >= 0 ? process.argv[idx+1] : undefined;
}

const baseUrl = arg('--url');
const keyfile = arg('--keyfile');
const title = arg('--title');
const slug = arg('--slug');
const htmlfile = arg('--htmlfile');
const metaDesc = arg('--metadesc') || '';
const tagsCsv = arg('--tags') || '';

if (!baseUrl || !keyfile || !title || !slug || !htmlfile) {
  console.error('Missing required args.');
  process.exit(2);
}

const [kid, secretHex] = fs.readFileSync(keyfile, 'utf8').trim().split(':');
if (!kid || !secretHex) {
  console.error('Invalid admin api key format; expected <id>:<secret>.');
  process.exit(2);
}

const token = signJwtHS256({kid, secretHex, aud: '/admin/'});
const html = fs.readFileSync(htmlfile, 'utf8');

const tags = tagsCsv.split(',').map(s => s.trim()).filter(Boolean).map(name => ({name}));

const endpoint = `${baseUrl.replace(/\/$/, '')}/ghost/api/admin/posts/?source=html`;
const payload = {
  posts: [{
    title,
    slug,
    html,
    status: 'draft',
    meta_description: metaDesc,
    tags,
  }]
};

const headers = { Authorization: `Ghost ${token}` };

requestJson(endpoint, {method: 'POST', headers, bodyObj: payload})
  .then(({json}) => {
    const post = json?.posts?.[0];
    console.log(JSON.stringify({ok: true, id: post?.id, url: post?.url, updated_at: post?.updated_at}, null, 2));
  })
  .catch((e) => {
    console.error(String(e));
    process.exit(1);
  });
