# Mission Control Task Schema & Routing

## Task Schema (Contract)

Minimal task object:

```json
{
  "id": "task-{timestamp}-{hash}",
  "title": "string",
  "description": "string",
  "assignee": "agent|user|null",
  "column": "backlog|ready|in-progress|review|blocked|done",
  "priority": "low|normal|high|critical",
  "tags": ["string"],
  "blocked": false,
  "blockReason": "string|null",
  "dueDate": "ISO-8601|null",
  "createdAt": "ISO-8601",
  "updatedAt": "ISO-8601",
  "createdBy": "string",
  "idempotencyKey": "string|null"
}
```

### Field Guidance

- **assignee**: `seo-auditor`, `main`, `felipe`, or `null` (unassigned)
- **column**: Single source of truth for task stage; filters primary
- **tags**: Examples: `urgent`, `waiting-approval`, `pr-review`, `analytics`, `content`
- **blocked**: Boolean; triggers automation if true
- **blockReason**: Why is it blocked? (missing data, approval pending, depends on task X)
- **idempotencyKey**: Unique job ID for deduplication (see Idempotency section)

---

## Routing Rules

### Agent Wake Triggers (openclaw tag)

```
IF task.tags contains "openclaw" THEN
  → Assign to "main" agent
  → Set column to "ready"
  → Schedule wake (execute immediately or queue)
  → Remove "openclaw" tag after assignment
```

**Use case**: External events (GitHub PR, email, webhook) tag with `openclaw` to wake main agent.

### Agent Assignment by Domain

| Domain       | Primary Agent    | Assignee Column | Default Tags |
|--------------|------------------|-----------------|--------------|
| SEO/Content  | seo-auditor      | assigned        | `content`, `seo` |
| Coordination | main             | inbox           | `urgent`, `openclaw` |
| Approvals    | felipe           | review          | `approval-needed` |
| Bug Fix      | seo-auditor      | assigned        | `bug`, `fix` |

---

## Automations

### Poller 1: Wake Agent on openclaw Tag

**Trigger**: Task created/updated with `tags` containing `"openclaw"`

**Actions**:
1. Set `assignee` → `"main"`
2. Set `column` → `"ready"`
3. Remove `"openclaw"` from tags
4. Emit event: `task:wake-agent` → notify main agent
5. Record timestamp for idempotency deduplication

**Interval**: Poll every 30-60 seconds (check for new tasks with openclaw tag)

**Idempotency**: Use `idempotencyKey` to prevent duplicate wakes; if key exists and was processed <5 min ago, skip.

---

### Poller 2: Ask Felipe When Task Blocked

**Trigger**: Task with `blocked = true` for >15 minutes

**Actions**:
1. Check if already messaged (via tag `"asked-felipe"`)
2. If not asked: Send Telegram message to Felipe:
   ```
   ⚠️ Task blocked: "{task.title}"
   Reason: {task.blockReason}
   Task ID: {task.id}
   
   React with ✅ to unblock, or reply with next steps.
   ```
3. Add tag `"asked-felipe"` + `timestamp`
4. Wait for Felipe's reaction or reply
5. If unblocked externally (column changes), remove `blocked` flag

**Interval**: Poll every 5 minutes

**Idempotency**: Tag `"asked-felipe"` prevents re-messaging same block; only re-ask if `blockReason` changes or >1 hour has passed.

---

## Example Tasks

### Example 1: Content Task (SEO Agent)

```json
{
  "id": "task-2026-02-11-abc123",
  "title": "Draft blog post: Top 10 travel apps 2026",
  "description": "Research trends from Semrush, draft outline, create in Ghost CMS",
  "assignee": "seo-auditor",
  "column": "in-progress",
  "priority": "high",
  "tags": ["content", "seo", "blog-draft"],
  "blocked": false,
  "blockReason": null,
  "dueDate": "2026-02-15T18:00Z",
  "createdAt": "2026-02-11T10:00Z",
  "updatedAt": "2026-02-11T14:00Z",
  "createdBy": "main",
  "idempotencyKey": "content-semrush-2026-02-11"
}
```

### Example 2: Blocked Task (Waiting Approval)

```json
{
  "id": "task-2026-02-11-def456",
  "title": "Publish guest blog post",
  "description": "Draft review complete; waiting Felipe approval before Ghost publish",
  "assignee": "seo-auditor",
  "column": "blocked",
  "priority": "normal",
  "tags": ["content", "approval-needed", "asked-felipe"],
  "blocked": true,
  "blockReason": "Waiting Felipe approval on final draft",
  "dueDate": "2026-02-12T09:00Z",
  "createdAt": "2026-02-10T12:00Z",
  "updatedAt": "2026-02-11T13:45Z",
  "createdBy": "seo-auditor",
  "idempotencyKey": "publish-guest-2026-02-10"
}
```

### Example 3: Incoming Webhook Task (Wake Agent)

```json
{
  "id": "task-2026-02-11-ghi789",
  "title": "New PR: SEO metadata improvements",
  "description": "GitHub PR #42 opened by contributor; review & merge",
  "assignee": null,
  "column": "backlog",
  "priority": "normal",
  "tags": ["openclaw", "pr-review", "github"],
  "blocked": false,
  "blockReason": null,
  "dueDate": null,
  "createdAt": "2026-02-11T14:05Z",
  "updatedAt": "2026-02-11T14:05Z",
  "createdBy": "webhook:github",
  "idempotencyKey": "gh-pr-42-2026-02-11"
}
```

→ **Poller 1 action**: Within 1 min, adds `assignee="main"`, moves to `ready`, removes `openclaw` tag, wakes main agent.

---

## Defaults

| Field      | Default |
|------------|---------|
| priority   | `normal` |
| column     | `backlog` |
| blocked    | `false` |
| dueDate    | `null` (no deadline) |
| assignee   | `null` (unassigned) |
| tags       | `[]` (empty) |

---

## Idempotency & Deduplication

### Strategy

**idempotencyKey** = stable identifier for the "work intent"

Pattern: `{source}-{domain}-{date}` or `{source}-{identifier}`

Examples:
- `content-semrush-2026-02-11` (weekly Semrush report)
- `gh-pr-42-2026-02-11` (GitHub PR #42)
- `email-urgent-2026-02-11-14:00` (urgent email at specific time)

### Dedup Rules

1. **Same idempotencyKey within 5 minutes** → Skip (task already exists or poller already processed)
2. **Blocked task, already asked Felipe** → Skip re-ask unless blockReason changed or >1 hour elapsed
3. **Task moved to done/review** → Remove from automation loops
4. **Duplicate webhook** (e.g., GitHub retry) → Check idempotencyKey before creating

### Implementation Checklist

- [ ] Every task has an `idempotencyKey` (auto-generated from source + domain + timestamp if not provided)
- [ ] Poller checks: `IF task.idempotencyKey in processed_keys AND timestamp < 5min → SKIP`
- [ ] Automation updates include: `updated_at` timestamp (enables age-based re-checks)
- [ ] Store processed keys in a TTL cache (5 min for wake, 1 hour for block asks)
- [ ] Alert on conflict: if idempotencyKey matches but content differs, log warning

---

## Filtering & Columns

### Typical Filters (Mission Control UI)

```
Assignee: [main] [seo-auditor] [felipe] [unassigned]
Column:   [backlog] [ready] [in-progress] [review] [blocked] [done]
Priority: [low] [normal] [high] [critical]
Tags:     [content] [seo] [bug] [urgent] [approval-needed] ...
Blocked:  [Blocked] [Unblocked]
Due Date: [Today] [This week] [Overdue] [No deadline]
```

---

## Recommended Workflow

```
1. New task arrives (webhook, Felipe, manual)
   ↓
2. Tag with "openclaw" if needs main agent wake
   ↓
3. Poller 1 assigns to agent, moves to "ready"
   ↓
4. Agent picks up, moves to "in-progress"
   ↓
5. If stuck, agent sets blocked=true + blockReason
   ↓
6. Poller 2 (after 15 min) asks Felipe
   ↓
7. Felipe reacts/replies → unblock or provides guidance
   ↓
8. Agent resumes, completes, moves to "done"
```

---

## Summary

- **Schema**: 11-field minimal contract; idempotencyKey for dedup
- **Routing**: 3 rules (seo-auditor, main, felipe) by domain
- **Automations**: 
  - ✅ Wake (openclaw tag → main agent)
  - ❓ Block (blocked=true + 15 min → ask Felipe)
- **Defaults**: normal priority, backlog column, no deadline
- **Dedup**: idempotencyKey + 5-min/1-hour TTL cache
