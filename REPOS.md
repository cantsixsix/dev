# Análise dos repositórios — cantsixsix

> **Atualização:** a organização agora é por ideias — ver **[IDEIAS.md](IDEIAS.md)**. `kies`, `Finance-`, `mega-repo` e `joguinho-` deixaram de ser "apagar" e viraram ideias a validar; `voxel`, `assetsv1` e `aassmetnsv-2` serão apagados.

Revisão feita em 09/10/2026, olhando o conteúdo de cada repo (último commit da branch padrão).
Renomear no GitHub: *Settings → General → Repository name*. O GitHub redireciona o nome antigo, então links e clones continuam funcionando.

## ✅ Já feito (09/10/2026)

| Repo | O que mudou |
|---|---|
| todos | `IDEIA.md` com a ficha da ideia + workflow **Segredos** (bloqueia `.env`, keystore, chaves) |
| `corrida` | Música de 53 MB → 5,5 MB (6 min em loop), README de verdade |
| `joguinho-` | Virou projeto Vite que roda (`npm run dev`); botão Start que não clicava foi corrigido |
| `Beaqme` | Removidos os 4 arquivos-lixo do terminal |
| `investing` | Código movido de `test/agora.py` para `agora.py`; `requirements.txt` e README |
| `calendario` | `.codex` removido; CI Android corrigido (pacote `tools` saiu do SDK) |
| `wpp-navegador-wrapper` | `.claude/settings.local.json` fora do Git |
| `aquatrack` | README corrigido (Next 16; Stripe ainda não implementado) |
| `dotfiles` | Hook `git-hooks/pre-commit` que bloqueia segredos no seu computador |
| `dev` | Painel automático de ideias (`PAINEL.md`, toda segunda) |

**Continua pendente (só você pode fazer):** apagar `assetsv1`, `aassmetnsv-2`, `voxel`; revogar a chave do Gemini; resetar a upload key do Místico e tirar a keystore do `mistico` (o workflow Segredos de lá vai ficar vermelho até isso); gerar novas credenciais do Mercado Livre.

## 🚨 Prioridade 1 — segurança

| Repo | Problema | O que fazer |
|---|---|---|
| `mistico` (público) | `signing.keystore`, `signingKey.keystore` e `signing-key-info.txt` commitados | Mesma chave que está no `dev`. Resetar a upload key no Play Console, apagar do repo e do histórico, tornar privado |
| `dev` (público) | Mesma keystore + `.env` do anunciador ML dentro de zips | Ver README deste repo |
| `voxel` (público, deploy Vercel) | `vite.config.ts` injeta `GEMINI_API_KEY` no JavaScript do navegador — qualquer visitante do site pode copiar a chave | Revogar a chave no Google AI Studio e mover a chamada ao Gemini para uma função serverless (`/api/generate`) na Vercel |
| `wpp-navegador-wrapper` | `.claude/settings.local.json` commitado (config local, sem segredo) | Adicionar `.claude/settings.local.json` ao `.gitignore` |
| `calendario` | Arquivo `.codex` vazio na raiz | Apagar e ignorar |

## Repo por repo

### Projetos de verdade (manter)

**`todo-list` → renomear para `tarefas`**
App Expo/React Native + Supabase, com testes, e2e, outbox offline e tarefas recorrentes — é o projeto mais completo da conta. O nome e a descrição ("testing") não fazem jus.
- Trocar descrição para "App de tarefas (Expo + Supabase) com listas, recorrência e modo offline".
- Falta `README.md` (tem `AGENTS.md`, mas nada para humanos).
- Depois de renomear, alinhar `slug`/`scheme` em `app.json` se for publicar.

**`aquatrack`** (privado) — Next.js 16 + Supabase + next-intl.
- README diz "Next.js 14" e "Stripe", mas o código está em Next 16 e não há nenhuma integração Stripe (`stripe` só no `package.json`). Atualizar o README ou implementar o checkout.
- Só existe uma rota de API (`water-logs`); página `/pricing` não tem cobrança real.

**`calendario` → `calendario-android`**
App Android em Java com testes unitários (feriados BR, codec de eventos) e CI no GitHub Actions — bem organizado.
- Trocar o pacote `com.example.calendario` por um ID real (ex.: `com.cantsixsix.calendario`) antes de publicar na Play Store — `com.example` é rejeitado.
- O build Flutter em `dev/_archive/flutter-calendar-build` é de outra versão; pode ser apagado.

**`mistico` → `mistico-android`**
Só contém o pacote TWA (wrapper Android do site) gerado pelo PWABuilder, não o código do site.
- Remover `.apk`, `.aab`, `.idsig` e keystores — binários não vão no Git (usar *Releases*).
- A pasta `Místico - Google Play package/` tem espaço e acento: mover o conteúdo de `source/` para a raiz.
- O TWA abre `dainty-alfajores-b56885.netlify.app`, mas o site listado no repo é `mistico-drab.vercel.app`. Confirmar qual é o domínio de verdade e alinhar (inclusive o `assetlinks.json`).
- Onde está o código do site? Se não estiver no GitHub, criar `mistico-web`.

**`voxel`** (mantém o nome)
Além da chave exposta (acima): README tem só uma linha ("primiero teste do vexel app").

**`corrida` → `corrida-3d`**
Jogo de corrida em React + Three.js, deploy Vercel.
- `src/assets/phonk.mp3` tem **53 MB** — é 99% do tamanho do repo. Comprimir (≈3 MB a 128 kbps), carregar de um CDN, ou usar Git LFS. Se a música não for sua, trocar por uma livre de direitos.
- README ainda é o template padrão do Vite.
- Nome do pacote é `corridas`; alinhar.

**`wpp-navegador-wrapper` → `whatsapp-desktop-wsl`**
Electron que abre o WhatsApp Web como app no Windows via WSL. README bom.
- Há 6 scripts diferentes para criar atalho (`.vbs`, `.js`, `.sh`, `.bat`). Manter um por sistema e apagar o resto.
- `testing.js` solto na raiz — mover para `test/` ou apagar.

**`dotfiles`** — ok.
- `zsh/.zshrc2` é um backup → apagar ou renomear com o propósito.
- `ai-prompts/anunciador-ml.md` é cópia do que está em `dev/ai/prompts/`. Manter só num lugar.

### Sites / landing pages

**`Beaqme` + `myloja` → juntar em `beaqme-site`**
Os dois são o site da marca BeaqME (`myloja` tem o `CNAME` de `beaqme.com`).
- `Beaqme` tem 4 arquivos-lixo criados por engano no terminal: `e`, `et -e`, `timentos"` (cópias do help do `less`) e `tartup-portfolio-20apps` (saída de `git log`). Apagar.
- `index copy.html`, `index copy 2.html`, `newHome.html` e a pasta `new/` são versões do mesmo site. Escolher a versão final, apagar as outras (o Git guarda o histórico).
- `server.js` serve qualquer caminho de arquivo sem validar (`"." + req.url`) — ok para testar localmente, nunca para produção. Pode trocar por `npx serve`.

**`promotech-landing`** — `index.html` é idêntico a `dev/_review/markin-rascunhos/FINAL.html`. Repo ok; os rascunhos do `dev` podem ser apagados.

**`saas-landing-template` → `link-in-bio-template`**
O conteúdo é um template de "Link in Bio", não uma landing de SaaS. Versão evoluída de `dev/_review/markin-rascunhos/aaa.html`.

**`Mundo_infinito` → `sistema-solar-3d`** (ou `mundo-infinito`)
Visualização do sistema solar em CSS 3D + jQuery. Sem README. Nome em minúsculo com hífen.

**`startup-portfolio-20apps` + `mega-repo` → manter só `startup-portfolio-20apps`**
Mesmo projeto (hub de 20 mini-apps + AI gateway); `mega-repo` é a versão mais antiga (fev) e `startup-portfolio-20apps` a mais nova (mar). Arquivar `mega-repo`. README fala de uma pasta `apps/` com 20 pastas que não existe — atualizar.

**`assetsv1` + `aassmetnsv-2`** — duas versões da mesma página de serviços acadêmicos. Manter uma só (privada); `aassmetnsv-2` é nome com erro de digitação.

### Pequenos / experimentos

**`joguinho-`** — um único `.jsx` de "open world drive" em Three.js, mesma ideia do `corrida`. O `package.json` tem dependências erradas (`install`, `npm`) e nenhum script, então não roda. Mover o arquivo para `corrida-3d/experimentos/` e apagar o repo.

**`autoPreenchimmento`** — script de console que marca respostas de um questionário. Tornar privado ou apagar.

**`investing`** — `agora.py` e `internacional.py` estão **vazios (0 bytes)**; o único código está em `test/agora.py`. Mover o código para a raiz, adicionar `requirements.txt` e README.

### Vazios — apagar
`kies`, `Finance-` (nenhum commit).

## Resumo dos nomes

| Atual | Sugerido | Ação |
|---|---|---|
| `todo-list` | `tarefas` | renomear |
| `calendario` | `calendario-android` | renomear |
| `mistico` | `mistico-android` | renomear + limpar binários/chaves |
| `voxel` | — | apagar (revogar a chave do Gemini antes) |
| `corrida` | `corrida-3d` | renomear + reduzir mp3 |
| `wpp-navegador-wrapper` | `whatsapp-desktop-wsl` | renomear |
| `Beaqme` + `myloja` | `beaqme-site` | juntar |
| `saas-landing-template` | `link-in-bio-template` | renomear |
| `Mundo_infinito` | `sistema-solar-3d` | renomear |
| `startup-portfolio-20apps` | — | manter |
| `mega-repo` | — | vira a plataforma (ver IDEIAS.md) |
| `assetsv1` / `aassmetnsv-2` | — | apagar |
| `joguinho-` | — | ideia própria (mundo aberto) |
| `autoPreenchimmento` | — | privado ou apagar |
| `investing` | `investing` | corrigir arquivos vazios |
| `dev` | `rascunhos` (opcional) | limpar |
| `kies`, `Finance-` | — | ideias a validar |
| `aquatrack`, `dotfiles`, `promotech-landing` | — | manter |

Todos os repos ficam, exceto os dois `assets*`; cada um representa uma ideia (ver IDEIAS.md).
