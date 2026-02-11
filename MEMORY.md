# MEMORY.md - Long-Term Memory

## About Felipe
- **ID**: 1810951106
- **Handle**: @ryansants
- **Interests**: Crypto trading, DeFi, Polymarket betting, security/privacy systems
- **Setup Location**: Local OpenClaw instance (loopback:61305)
- **Timezone**: UTC (inferred from cron times)

---

## Active Systems

### Security & Memory (Feb 11, 2026)
- **Prompt-Guard**: v3.1.0, active, blocking injections at CRITICAL/MEDIUM levels
- **Memory**: Memory-Core (built-in, stable) — auto-capture and auto-recall enabled
- **Supermemory Plugin**: Installed (v1.0.4) but not yet activated (awaiting API key + config)
- **Calendar Sync**: Daily iCloud + Google sync via vdirsyncer (05:00 UTC)

### Crypto Trading
- **Bankr CLI**: Installed ✅, Agent API enabled ✅
- **API Key**: `bk_KRJW67CUBD76UXQ57SXL26WA83AUEA94` (active, authenticated)
- **Wallets**: EVM `0x0ce...91c`, Solana `GVRTVyxCXRH7TXdaFGQo1tRTqNadrCBnvuHyewJMZguW` (felipewilliam on Farcaster)
- **Chains**: Base, Ethereum, Polygon, Solana, Unichain (provisioned)
- **⚠️ Blocker**: API response times extremely slow (portfolio queries timeout)
- **Features When Available**: Token swaps, Polymarket betting, portfolio tracking, leverage trading, automation (DCA, limit orders, stop loss)

---

## Key Decisions Made

### Memory System: Memory-Core over LanceDB
- **Why**: Memory-Core is built-in, stable, no external module issues
- **LanceDB Status**: Blocked by missing `openai` module (diagnostic task scheduled, but using Memory-Core for now)
- **Result**: Reliable auto-capture and auto-recall without dependencies

### Supermemory: Postponed
- **Reason**: Awaiting API key from https://console.supermemory.ai (Pro tier required)
- **Status**: Plugin installed but not activated
- **Next Step**: Once API key provided, enable in plugins.entries + apply config patch

### Bankr: Agent API Pending
- **Reason**: CLI installed but key lacks necessary permissions
- **Blocker**: "Agent API access" must be enabled in https://bankr.bot/api settings
- **Next Step**: Once Felipe enables it, can execute Polymarket bets and token trades

---

## Architecture Notes

- **Gateway Version**: v2026.2.9
- **Config File**: `/home/node/.openclaw/openclaw.json`
- **Workspace**: `/home/node/.openclaw/workspace`
- **Skills Location**: `/home/node/.openclaw/workspace/skills/`
- **Extensions**: `/home/node/.openclaw/extensions/` (Supermemory plugin lives here)
- **Cron Jobs**: Weekly compression (Mon/Thu 02:00 UTC), one-shot LanceDB diagnostic (Feb 11 06:00 UTC)

---

## Communication Preferences

- **Platform**: Telegram (configured)
- **Response Style**: Direct, no unnecessary fluff (per SOUL.md)
- **Session Resets**: `/new`, `/reset`, `/limpar`
- **Language**: Portuguese + English (mixed as needed)

---

## Outstanding TODOs

1. **Supermemory API Key**: Waiting for Felipe to generate at https://console.supermemory.ai
   - Once provided: config patch + enable plugin + test auto-recall

2. ✅ **DONE: Bankr Agent API** (enabled 2026-02-11 05:53 UTC)
   - Wallets provisioned, authentication verified
   - ⚠️ Current issue: API performance (slow response times)
   - Monitoring: Follow up if slow responses persist

3. **LanceDB Diagnostic**: Completed 06:00 UTC (Feb 11)
   - Report file should be at `/home/node/.openclaw/workspace/memory/lancedb-diagnostic.md`
   - If file exists: Review findings and decide on re-activation
   - If missing: Diagnostic may not have generated report; may need manual investigation

4. ✅ **SEO Auditor Refactoring** (completed 2026-02-11 07:32 UTC)
   - Refactored qwen-vision → seo-auditor
   - ✅ Found GSC credentials (OAuth) + GA4 Service Account
   - ✅ Created comprehensive SOUL.md with SEO strategy + workflows
   - ✅ Installed skills: sickn33-seo-audit, davila7-seo-fundamentals
   - ✅ Updated TOOLS.md with credential paths
   - ✅ Created SEO-AUDITOR-CONFIG.md (ready to apply)
   - ⏳ Awaiting Felipe:
     - Ghost CMS URL + API Key
     - AV SITE repository URL + credentials (SSH/PAT)
   - ✅ Provided (Ghost URL+Admin key, AV SITE repo URL+token)
   - ✅ Config applied + gateway restarted (2026-02-11 08:15 UTC)
   - ✅ `seo-auditor` added; `qwen-vision` removed; main can delegate to seo-auditor
   - ✅ Skill `sickn33-seo-audit` installed (universal skill store)
   - Next: run smoke-test (trend→outline→Ghost draft)

---

## Session Summary (2026-02-11)

**Major Accomplishments:**
1. ✅ Complete agent system refactoring (6 agents optimized)
2. ✅ SOUL.md created for all agents (683 lines)
3. ✅ Skills integrated (agenticflow, coding-agent, seo-audit, seo-fundamentals)
4. ✅ Config updated (main: Haiku 4.5, fallbacks for all, identities defined)
5. ✅ Cron job: Switch main to Kimi K2.5 on Feb 15
6. ✅ SEO Auditor refactoring (qwen-vision → seo-auditor, ready to deploy)

**Score Improvement:** 6.5/10 → 9/10

**Awaiting Felipe:**
- Supermemory API key (optional, for long-term memory)
- Bankr: Monitor if API performance improves (currently slow)
- Ghost CMS credentials
- AV SITE repository credentials

**Next Steps for Felipe:**
1. Provide Ghost + AV SITE credentials (5 min)
2. Confirm SEO Auditor refactoring (yes/no)
3. Monitor Bankr API performance (currently experiencing slowdowns)
4. Generate Supermemory API key if wanting enhanced memory (optional)

Last Updated: 2026-02-11 07:32 UTC (pre-compaction flush)
