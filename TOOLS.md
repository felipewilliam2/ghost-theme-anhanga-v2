# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## SEO Auditor Agent Integrations

### Google Search Console (GSC)

- **Purpose**: Monitor search performance, click data, impressions
- **Auth**: OAuth via Google account
- **Access**: seo-auditor agent reads GSC data via API
- **Credentials**: `/home/node/.openclaw/agents/seo-travel-optimizer/config/gsc/`
  - `credentials.json` — OAuth client (client_id, client_secret)
  - `token.json` — OAuth token (access_token, refresh_token)
- **Client ID**: `461394934538-8snpeeephqeb9166dvj21hv99le4t708.apps.googleusercontent.com`
- **Project ID**: `gen-lang-client-0806339089`
- **Permissions**: View-only (search performance, clicks, impressions, CTR)

### Google Analytics 4 (GA4)

- **Purpose**: Traffic analysis, user behavior, conversions, user journey
- **Auth**: Service Account (OAuth not needed for SA)
- **Access**: seo-auditor agent reads GA4 data via API
- **Credentials**: `/home/node/.openclaw/agents/seo-travel-optimizer/config/ga4/service-account.json`
- **Service Account Email**: `ga4-reader@amadeus-calendar.iam.gserviceaccount.com`
- **Project ID**: `amadeus-calendar`
- **Permissions**: View-only (analytics, traffic, conversions, user behavior)

### Semrush Reports

- **Purpose**: Weekly competitive analysis, keyword trends
- **Delivery**: Email to Felipe
- **Frequency**: Weekly
- **Access**: seo-auditor reads reports, extracts trending topics for blog

### Ghost CMS

- **Purpose**: Create & publish blog drafts
- **URL**: [To be added by Felipe]
- **API Key**: [To be added by Felipe]
- **Access**: seo-auditor creates draft posts, notifies Felipe for review
- **Restrictions**: Draft mode only (Felipe approves before publish)

### AV SITE Repository

- **Type**: GitHub/GitLab [To be confirmed]
- **URL**: [To be added by Felipe]
- **Credentials**: SSH key / OAuth token stored securely
- **Access**: seo-auditor clones, creates branches, commits, opens PRs
- **Branch Strategy**: `seo-auditor-YYYY-MM-DD-topic` (Felipe reviews before merge)
- **Restrictions**: Read+Write, but commits must be PR'd for approval

---

Add whatever helps you do your job. This is your cheat sheet.
