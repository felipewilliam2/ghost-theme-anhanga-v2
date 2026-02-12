# goals.md — Felipe + Amadeus

Última atualização: 2026-02-12

## Objetivo-mestre
Construir um sistema operacional de conteúdo + automações (SEO → social) e um MVP de trading/simulação (Polymarket) com base em dados, mantendo a stack OpenClaw segura, barata e estável.

---

## Agora (esta semana)

### 1) Polymarket MVP — simulation-first
- Dataset: top 20 mercados por liquidez (Gamma + Data API; aceitar limite de offset 3000 por token).
- Implementar simulador de market making (`simulate_mm.py`) + `reports/summary.md`.
- Métricas-alvo: PnL líquido (fees/slippage), drawdown, fill rate, adverse selection, inventory drift.
- Repo: **private** https://github.com/felipewilliam2/polymarket-mvp

### 2) SEO Auditor + n8n repurpose (com aprovação manual)
- Redes: IG, FB, TikTok, LinkedIn, X, Threads.
- Fila de aprovação: **Google Sheets** (MVP).
- Sempre **PT-BR**.
- Imagens no **Canva** (por enquanto): n8n gera texto por slide/roteiro/copy.
- "Contrato" de saída do post (SEO Auditor):
  - TL;DR em 5 bullets
  - checklist passo-a-passo
  - FAQ (3–5)
  - 1 CTA único + UTM

### 3) Obsidian — dailies automáticas
- Criar daily às **07:00 America/Sao_Paulo** usando `Tpl_Daily_Note_Automatico.md`.
- Script: `/home/node/.openclaw/workspace/scripts/obsidian_daily_note.py`
- Vault versionado: https://github.com/felipewilliam2/felipe-obsidian-vault

### 4) Segurança / hardening
- Política: admin **só Tailscale**, público **só 80/443**.
- Status: hardening aplicado e validado externamente (nc): 3456/3457/5678 fechadas; 80/443 abertas.
- Rotas Tailscale 172.20/16 e 172.21/16: aprovadas.

---

## Depois (backlog)
- Refinar simulador (modelo de fill mais realista; latência; book snapshots se viável).
- Attention Markets (quando existirem): módulo de correlação/regime + medição de lag do oracle + flags de manipulação.
- Hardening extra (quando sobrar tempo):
  - allowlist de plugins do OpenClaw
  - socket-proxy (se voltar a precisar de docker.sock)
  - auditoria periódica (portas publicadas + DOCKER-USER)

---

## Regras do jogo (defaults)
- Quando Felipe disser **"Responda apenas: OK"**, responder literalmente **OK**.
- Estilo: **amigo zoeiro leve**, direto, com gírias; palavrão ocasional ok (sem agressividade).
- Ações externas relevantes (publicar em rede social, etc.) começam com aprovação manual.
