# Revisão de Agentes & Oportunidades de Melhoria

Data: 2026-02-11 | Analisado com: agenticflow-skills, mcp-builder, skill-creator, coding-agent

---

## 📊 Resumo Executivo

| Agente | Status | Prioridade | Ação |
|--------|--------|-----------|------|
| **main** (Amadeus) | ⚠️ Sub-otimizado | 🔴 Alta | Melhorar modelo primary + adicionar identity |
| **claude-analyst** | ✅ Bem Configurado | 🟢 Baixa | Adicionar skills específicas |
| **claude-coder** | ✅ Bem Configurado | 🟢 Baixa | Integrar coding-agent skill |
| **perplexity-synthesizer** | ✅ Bem Configurado | 🟡 Média | Ativar web search |
| **grok-scout** | ✅ Bem Configurado | 🟡 Média | Configurar identity + fallbacks |
| **gemini-fallback** | ❌ Mal Nomeado | 🔴 Alta | Renomear para qwen-vision |

---

## 🔍 Análise Detalhada

### 1️⃣ **main** (Amadeus - Mission Control)

**Configuração Atual:**
```json
{
  "primary": "kimi-coding/k2p5",
  "fallbacks": ["qwen-portal/vision-model"],
  "subagents": 5 agents
}
```

**Problemas Identificados:**
- ❌ **Primary model inadequado**: Kimi K2.5 é coding-focused, não ideal para "Mission Control"
- ❌ **Sem identity**: Amadeus existe em config mas sem emoji/avatar definido
- ❌ **Fallback limitado**: Apenas 1 fallback para 5 subagents
- ❌ **Sem SOUL.md próprio**: Cada agent deve ter sua própria personalidade

**Oportunidades:**

| # | Melhoria | Impacto | Dificuldade |
|---|----------|--------|------------|
| **1** | Trocar primary para `anthropic/claude-opus-4-5` | 🟢 Alto | 🟢 Fácil |
| **2** | Adicionar mais fallbacks (Sonnet, Gemini 3 Pro) | 🟢 Alto | 🟢 Fácil |
| **3** | Definir identity completa (emoji, avatar) | 🟢 Alto | 🟢 Fácil |
| **4** | Criar `/home/node/.openclaw/agents/main/SOUL.md` | 🟡 Médio | 🟡 Médio |
| **5** | Configurar `contextPruning` (atualmente global) | 🟡 Médio | 🟡 Médio |

**Recomendação:**
```json
// Trocar para:
{
  "id": "main",
  "name": "Amadeus - Mission Control",
  "model": {
    "primary": "anthropic/claude-opus-4-5",
    "fallbacks": [
      "anthropic/claude-sonnet-4-5",
      "gemini/gemini-3-pro-preview",
      "xai/grok-4-1-fast-reasoning",
      "kimi-coding/k2p5"
    ]
  },
  "identity": {
    "name": "Amadeus",
    "emoji": "🎼",
    "avatar": "path/to/amadeus.png",
    "theme": "Maestro de coordenação, orquestra agents especializados"
  }
}
```

---

### 2️⃣ **claude-analyst** 🔬

**Configuração Atual:**
```json
{
  "model": "anthropic/claude-sonnet-4-5",
  "identity": {
    "name": "Claude Analyst",
    "theme": "Analista profundo especializado em tarefas complexas",
    "emoji": "🔬"
  }
}
```

**Status:** ✅ **BEM CONFIGURADO**

**Oportunidades:**

| # | Melhoria | Impacto | Dificuldade |
|---|----------|--------|------------|
| **1** | Adicionar fallback (Gemini 3 Pro para reasoning) | 🟢 Alto | 🟢 Fácil |
| **2** | Integrar `agenticflow-skills` para workflows | 🟡 Médio | 🟡 Médio |
| **3** | Criar próprio `SOUL.md` com tone/guidelines | 🟡 Médio | 🟡 Médio |
| **4** | Finalizar avatar (*(pending)) | 🟢 Alto | 🟡 Médio |

**Recomendação:**
```json
{
  "model": {
    "primary": "anthropic/claude-sonnet-4-5",
    "fallbacks": ["gemini/gemini-3-pro-preview"]
  },
  "skills": ["agenticflow-skills"],
  "identity": {
    "avatar": "avatars/analyst.png"
  }
}
```

---

### 3️⃣ **claude-coder** 💻

**Configuração Atual:**
```json
{
  "model": "anthropic/claude-opus-4-5"
}
```

**Status:** ✅ **BEM CONFIGURADO** (Opus é excelente para coding)

**Oportunidades:**

| # | Melhoria | Impacto | Dificuldade |
|---|----------|--------|------------|
| **1** | Integrar `coding-agent` skill | 🟢 Alto | 🟢 Fácil |
| **2** | Adicionar fallback (Qwen Coder) | 🟢 Alto | 🟢 Fácil |
| **3** | Definir identity (emoji 💻, avatar) | 🟢 Alto | 🟡 Médio |
| **4** | Criar `SOUL.md` com coding guidelines | 🟡 Médio | 🟡 Médio |
| **5** | Ativar `workspace-claude-coder` específico | 🟡 Médio | 🟢 Fácil |

**Recomendação:**
```json
{
  "id": "claude-coder",
  "name": "Claude Coder",
  "model": {
    "primary": "anthropic/claude-opus-4-5",
    "fallbacks": ["qwen-portal/coder-model"]
  },
  "skills": ["coding-agent"],
  "identity": {
    "name": "Claude Coder",
    "emoji": "💻",
    "theme": "Engenheiro de código, especialista em arquitetura e debugging"
  }
}
```

---

### 4️⃣ **perplexity-synthesizer** 📊

**Configuração Atual:**
```json
{
  "name": "Perplexity - Info Synthesizer",
  "model": "perplexity/sonar-pro"
}
```

**Status:** ✅ **BEM CONFIGURADO** (Sonar Pro é excelente para pesquisa)

**Oportunidades:**

| # | Melhoria | Impacto | Dificuldade |
|---|----------|--------|------------|
| **1** | Ativar `web.search` (disabled globalmente) | 🟢 Alto | 🟡 Médio |
| **2** | Adicionar fallback (Sonnet com web) | 🟢 Alto | 🟢 Fácil |
| **3** | Definir identity (emoji 📚, avatar) | 🟢 Alto | 🟡 Médio |
| **4** | Integrar `agenticflow-skills` para workflows | 🟡 Médio | 🟡 Médio |
| **5** | Criar `SOUL.md` com pesquisa guidelines | 🟡 Médio | 🟡 Médio |

**Recomendação:**
```json
{
  "id": "perplexity-synthesizer",
  "name": "Perplexity Synthesizer",
  "model": {
    "primary": "perplexity/sonar-pro",
    "fallbacks": ["anthropic/claude-sonnet-4-5"]
  },
  "tools": {
    "web": {
      "search": true,  // Override global disable
      "fetch": true
    }
  },
  "skills": ["agenticflow-skills"],
  "identity": {
    "name": "Perplexity Scout",
    "emoji": "📚",
    "theme": "Pesquisadora de informações, sintetiza dados em insights"
  }
}
```

---

### 5️⃣ **grok-scout** ⚡

**Configuração Atual:**
```json
{
  "name": "Grok - Real-time Scout",
  "model": "xai/grok-4-1-fast-reasoning"
}
```

**Status:** ✅ **BEM CONFIGURADO** (Grok 4.1 é excelente para reasoning + real-time)

**Oportunidades:**

| # | Melhoria | Impacto | Dificuldade |
|---|----------|--------|------------|
| **1** | Definir identity (emoji ⚡, avatar) | 🟢 Alto | 🟡 Médio |
| **2** | Adicionar fallback (Gemini 3 Pro) | 🟢 Alto | 🟢 Fácil |
| **3** | Criar `SOUL.md` com reasoning guidelines | 🟡 Médio | 🟡 Médio |
| **4** | Integrar `agenticflow-skills` para workflows | 🟡 Médio | 🟡 Médio |

**Recomendação:**
```json
{
  "id": "grok-scout",
  "name": "Grok Scout",
  "model": {
    "primary": "xai/grok-4-1-fast-reasoning",
    "fallbacks": ["gemini/gemini-3-pro-preview"]
  },
  "skills": ["agenticflow-skills"],
  "identity": {
    "name": "Grok",
    "emoji": "⚡",
    "theme": "Scout em tempo real, raciocínio rápido e profundo"
  }
}
```

---

### 6️⃣ **gemini-fallback** 🟠

**Configuração Atual:**
```json
{
  "id": "gemini-fallback",
  "name": "Qwen Vision Fallback",  // ⚠️ MISMATCH!
  "model": "qwen-portal/vision-model"
}
```

**Status:** ❌ **NOME INCORRETO / CONFUSO**

**Problemas:**
- ❌ ID diz "gemini" mas model é "qwen"
- ❌ Nome é "Qwen Vision Fallback" mas ID sugere Gemini
- ❌ Sem identity completa
- ❌ Sem fallback configurado

**Oportunidades:**

| # | Melhoria | Impacto | Dificuldade |
|---|----------|--------|------------|
| **1** | Renomear para `qwen-vision` | 🔴 Crítico | 🟢 Fácil |
| **2** | Atualizar `name` para "Qwen Vision" | 🟢 Alto | 🟢 Fácil |
| **3** | Definir identity completa | 🟢 Alto | 🟡 Médio |
| **4** | Adicionar fallback (Gemini Flash) | 🟢 Alto | 🟢 Fácil |
| **5** | Integrar `agenticflow-skills` | 🟡 Médio | 🟡 Médio |

**Recomendação:**
```json
{
  "id": "qwen-vision",
  "name": "Qwen Vision",
  "model": {
    "primary": "qwen-portal/vision-model",
    "fallbacks": ["gemini/gemini-2.5-flash-lite"]
  },
  "skills": ["agenticflow-skills"],
  "identity": {
    "name": "Qwen",
    "emoji": "👁️",
    "theme": "Especialista em visão e análise visual, processamento de imagens"
  }
}
```

---

## 🎯 Plano de Ação Priorizado

### 🔴 **URGENTE** (Hoje)
1. Renomear `gemini-fallback` → `qwen-vision`
2. Atualizar main: Opus primary + mais fallbacks
3. Definir identities em todos os agentes

### 🟡 **MÉDIO PRAZO** (Esta semana)
4. Criar `SOUL.md` para cada agente
5. Integrar skills (agenticflow, coding-agent)
6. Finalizar avatares

### 🟢 **LONGO PRAZO** (Este mês)
7. Ativar web.search para perplexity-synthesizer
8. Estruturar workflows com agenticflow
9. Criar MCP servers (mcp-builder)

---

## 📋 Script de Configuração Recomendado

Usar `skill-creator` para:
1. Criar agent-specific SOUL.md files
2. Documentar cada agent's capabilities
3. Estruturar agent interactions

Usar `agenticflow-skills` para:
1. Desenhar workflows entre agents
2. Orquestrar passagem de contexto
3. Gerenciar estado de conversas multi-agent

Usar `coding-agent` para:
1. Automatizar tarefas de code
2. Integrar com repos GitHub
3. Deploy via CI/CD

---

## 📝 Conclusão

**Pontuação Geral:** 6.5/10

| Métrica | Score |
|---------|-------|
| Configuração de Modelos | 8/10 ✅ |
| Identidade & Personalidade | 3/10 ❌ |
| Integração de Skills | 2/10 ❌ |
| Fallbacks & Resiliência | 5/10 ⚠️ |
| Documentação | 1/10 ❌ |

**Próximos Passos:**
1. Aplicar mudanças config (30 min)
2. Criar SOUL.md files (2h)
3. Testar cada agent em isolamento (1h)
4. Integrar skills (2h)

Total estimado: **5.5 horas** para otimização completa.

---

Quer que eu **aplique as mudanças** agora?
