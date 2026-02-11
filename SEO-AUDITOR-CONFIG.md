# SEO Auditor Agent - Configuração Completa

## Status: ✅ READY TO APPLY

Tudo está pronto. Felipe precisa só confirmar se quer aplicar:

---

## O Que Será Feito

### 1. Refatorar Agent Config
**Mudança:** `seo-auditor` → `seo-auditor`

**Antes:**
```json
{
  "id": "seo-auditor",
  "name": "SEO Auditor",
  "model": "anthropic/claude-sonnet-4-5"
}
```

**Depois:**
```json
{
  "id": "seo-auditor",
  "name": "SEO Auditor",
  "workspace": "/home/node/.openclaw/agents/seo-travel-optimizer",
  "model": {
    "primary": "anthropic/claude-sonnet-4-5",
    "fallbacks": ["anthropic/claude-opus-4-5"]
  },
  "skills": ["sickn33-seo-audit", "agenticflow-skills"],
  "identity": {
    "name": "SEO Auditor",
    "emoji": "🔍",
    "theme": "Especialista em SEO, estratégia de ranking e análise de dados (GSC, GA4)"
  },
  "config": {
    "gsc": {
      "credentialsPath": "/home/node/.openclaw/agents/seo-travel-optimizer/config/gsc/credentials.json",
      "tokenPath": "/home/node/.openclaw/agents/seo-travel-optimizer/config/gsc/token.json",
      "clientId": "461394934538-8snpeeephqeb9166dvj21hv99le4t708.apps.googleusercontent.com",
      "projectId": "gen-lang-client-0806339089"
    },
    "ga4": {
      "serviceAccountPath": "/home/node/.openclaw/agents/seo-travel-optimizer/config/ga4/service-account.json",
      "serviceAccount": "ga4-reader@amadeus-calendar.iam.gserviceaccount.com",
      "projectId": "amadeus-calendar"
    },
    "ghost": {
      "url": "[PRECISA: Felipe fornecer]",
      "apiKey": "[PRECISA: Felipe fornecer]"
    },
    "repository": {
      "url": "[PRECISA: Felipe fornecer]",
      "branchPrefix": "seo-auditor-"
    }
  }
}
```

---

## Credenciais Já Encontradas ✅

### Google Search Console (GSC)
- **Status:** ✅ Encontrado
- **Localização:** `/home/node/.openclaw/agents/seo-travel-optimizer/config/gsc/`
- **Files:** `credentials.json`, `token.json`
- **Client ID:** `461394934538-8snpeeephqeb9166dvj21hv99le4t708.apps.googleusercontent.com`
- **Project:** `gen-lang-client-0806339089`

### Google Analytics 4 (GA4)
- **Status:** ✅ Encontrado
- **Localização:** `/home/node/.openclaw/agents/seo-travel-optimizer/config/ga4/`
- **File:** `service-account.json`
- **Service Account:** `ga4-reader@amadeus-calendar.iam.gserviceaccount.com`
- **Project:** `amadeus-calendar`

### Semrush
- **Status:** ⏳ Felipe envia relatórios por email semanalmente
- **Ação:** Agent lê os emails (precisa de configuração)

### Ghost CMS
- **Status:** ❌ PRECISA: Felipe fornecer
- **Precisa de:**
  - URL do Ghost
  - API Key do Ghost

### AV SITE Repository
- **Status:** ❌ PRECISA: Felipe fornecer
- **Precisa de:**
  - URL do repositório (GitHub/GitLab)
  - SSH key ou OAuth token

---

## Arquivos Já Criados ✅

1. **SOUL.md** (7.7 KB)
   - `/home/node/.openclaw/agents/seo-auditor/SOUL.md`
   - Personalidade, workflows, estratégia SEO
   - Weekly process: Analyze → Create → Report

2. **TOOLS.md - Seção SEO** (atualizado)
   - GSC credentials documented
   - GA4 service account documented
   - Integration points clear

3. **CONFIG-READY** (este arquivo)
   - Configuração para aplicar
   - Falta só: Ghost + Repository

---

## Skills Status

| Skill | Status | Notas |
|-------|--------|-------|
| sickn33-seo-audit | 🔄 Installing | Instalação ainda em andamento |
| agenticflow-skills | ✅ Installed | Pronto para usar |

---

## Próximas Ações

### Para Felipe:
1. **Confirmar:** Quer aplicar essa refatoração?
2. **Fornecer:**
   - Ghost CMS URL + API Key
   - Repository URL (GitHub/GitLab) + credentials
   - Email para receber relatórios semanais Semrush

### Para Mim (após confirmação):
1. Aplicar configuração em openclaw.json
2. Atualizar subagents em `main` (seo-auditor → seo-auditor)
3. Restart gateway
4. Testar agent em isolamento

---

## Timeline Estimado

- **Config:** 5 min (quando aplicar)
- **Restart:** 30 seg
- **Testing:** 10 min
- **Total:** ~15 min

---

## Perguntas para Felipe

1. **Refatorar agora ou deixar seo-auditor como fallback visual?**
   - Opção A: Refatorar completamente (seo-auditor só)
   - Opção B: Manter seo-auditor + criar novo seo-auditor agent

2. **Ghost CMS - já tem credential file?**
   - Se sim: onde está?
   - Se não: posso criar script para Felipe fazer OAuth?

3. **Repository - qual platform?**
   - GitHub? GitLab? Gitea?
   - Como passar credenciais (SSH key, OAuth, PAT)?

---

**Status:** 🟡 AWAITING FELIPE CONFIRMATION

Quer que eu aplique agora com as credenciais que já temos?
