# 🎨 Anhangá Theme para Ghost

Tema customizado para o blog da Anhangá Viagens, alinhado com a identidade visual do site principal.

## ✨ Características

- **Identidade Visual Anhangá**: Cores azul oceano (#1E88E5), laranja (#FF6B35) e areia (#F5F5DC)
- **Fonts**: Montserrat (títulos) e Open Sans (corpo)
- **Design Responsivo**: Mobile-first
- **Header Integrado**: Links para o site principal (anhanga.tur.br)
- **CTA Estratégico**: Botão "Solicitar Orçamento" no header
- **SEO Optimizado**: Estrutura semântica, meta tags, Open Graph

## 📁 Estrutura

```
ghost-theme-anhanga/
├── assets/
│   ├── css/
│   │   └── screen.css      # Estilos principais
│   └── js/
│       └── main.js         # Scripts (menu mobile, smooth scroll)
├── partials/
│   ├── header.hbs          # Header com navegação
│   └── footer.hbs          # Footer com links sociais
├── default.hbs             # Layout base
├── index.hbs               # Página inicial (lista de posts)
├── post.hbs                # Página de post individual
└── package.json            # Configuração do tema
```

## 🚀 Instalação

### 1. Compactar o tema

```bash
cd ghost-theme-anhanga
zip -r anhanga-theme.zip .
```

### 2. Upload no Ghost Admin

1. Acesse: `https://blog.anhanga.tur.br/ghost/#/settings/design`
2. Clique em "Change theme" → "Upload theme"
3. Selecione o arquivo `anhanga-theme.zip`
4. Ative o tema

### 3. Configurar (opcional)

No Ghost Admin:
- **Settings > General**: Upload logo da Anhangá
- **Settings > Design**: Personalizar cores se necessário
- **Settings > Navigation**: Ajustar links do menu

## 📝 Personalização

### Cores

Edite `assets/css/screen.css`:

```css
:root {
    --color-primary: #1E88E5;      /* Azul Oceano */
    --color-secondary: #FF6B35;    /* Laranja */
    --color-accent: #F5F5DC;       /* Areia */
}
```

### Links do Header

Edite `partials/header.hbs`:

```html
<nav class="main-nav">
    <a href="https://anhanga.tur.br" class="nav-link">Início</a>
    <a href="/" class="nav-link active">Blog</a>
    <!-- Adicione mais links -->
</nav>
```

### CTA no Final dos Posts

Edite `post.hbs` na seção `post-cta`:

```html
<div class="post-cta">
    <h3>Quer viver essa experiência?</h3>
    <a href="https://anhanga.tur.br/orcamento" class="btn btn-primary">
        Solicitar Orçamento
    </a>
</div>
```

## 🔗 Integração com Site Principal

O tema já inclui:
- ✅ Header com links para anhanga.tur.br
- ✅ Logo apontando para site principal
- ✅ CTA "Solicitar Orçamento" no header
- ✅ Footer com links para redes sociais
- ✅ CTA no final de cada post

## 📱 Responsivo

O tema é totalmente responsivo:
- **Desktop**: Layout completo com navegação horizontal
- **Tablet**: Grid de posts adaptativo
- **Mobile**: Menu hambúrguer, cards empilhados

## 🎨 Próximos Passos Sugeridos

1. **Upload do logo** no Ghost Admin
2. **Criar páginas**: Sobre, Contato (se necessário no blog)
3. **Configurar newsletter** (Ghost tem nativo)
4. **Integrar com n8n**: Webhook quando post for publicado
5. **Analytics**: Adicionar GA4 ao tema

## 📄 Licença

MIT - Anhangá Viagens
