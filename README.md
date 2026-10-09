# dev

Repositório "gaveta" com material solto: prompts de IA, rascunhos de landing pages e builds antigos.
Não é um projeto executável — serve de arquivo e área de triagem.

## Estrutura

| Pasta | Conteúdo | Destino sugerido |
|---|---|---|
| `ai/prompts/` | `anunciador-ml.md` — prompt para gerar um anunciador em massa no Mercado Livre (Node.js) | Fica aqui |
| `_review/markin-rascunhos/` | Rascunhos de landing pages de ofertas (PromoZap / PromoTech / Canal de Ofertas) e um "link in bio" (`aaa.html`). `FINAL.html` é a versão final | Mover a versão final para o repo `promotech-landing` e apagar o resto |
| `_archive/flutter-calendar-build/` | Build web compilado (Flutter) de um calendário — ~32 MB | Não versionar build; código-fonte deve viver em `calendario` |
| `_archive/ml-anunciador.zip` | Código gerado pelo prompt acima (contém um `.env`) | Extrair para repo **privado** próprio, sem o `.env` |
| `_archive/mistico-google-play-package.zip` | APK/AAB do app Místico + **chave de assinatura** | Tirar do Git (ver alerta abaixo); o código já está no repo `mistico` |
| `_archive/AppImages.zip` | Ícones/tiles do app (Windows 11 etc.) | Mover para o repo `mistico` |

## ⚠️ Alerta de segurança

Este repositório é **público** e o histórico contém:

- `signing.keystore` + `signing-key-info.txt` (dentro de `mistico-google-play-package.zip`) — a chave que assina o app na Play Store.
- `.env` (dentro de `ml-anunciador.zip`) — possivelmente credenciais OAuth do Mercado Livre.

Remover os arquivos num commit novo **não basta**: eles continuam no histórico. Passos:

1. Revogar/gerar novas credenciais no DevCenter do Mercado Livre.
2. Se o app usa Play App Signing, pedir reset da *upload key* no Play Console.
3. Tornar o repo privado e/ou reescrever o histórico (`git filter-repo`) para apagar os arquivos.

## Organização dos demais repositórios

Inventário de `cantsixsix` (out/2026). Sugestão de ação para cada um:

### Manter (projetos com conteúdo/deploy)
| Repo | Linguagem | Observação |
|---|---|---|
| `mistico` | Java | App tarot/horóscopo, deploy Vercel. Receber os assets do `_archive` |
| `corrida` | JavaScript | Deploy Vercel. 53 MB — checar se há build/`node_modules` commitado |
| `voxel` | TypeScript | Deploy Vercel |
| `aquatrack` | TypeScript | Único privado |
| `calendario` | Java | Projeto mais recente |
| `Beaqme`, `Mundo_infinito`, `myloja`, `investing`, `wpp-navegador-wrapper`, `dotfiles` | vários | Adicionar README e descrição |

### Consolidar
| Repos | Sugestão |
|---|---|
| `promotech-landing`, `saas-landing-template`, `startup-portfolio-20apps`, `mega-repo` | Landing pages/templates HTML — juntar num repo `landing-pages` com uma pasta por página (ou manter separados só os que têm deploy) |
| `assetsv1`, `aassmetnsv-2` | Duas versões do mesmo conteúdo — manter uma (`assets`) e arquivar a outra |
| `joguinho-`, `autoPreenchimmento` | Muito pequenos — mover para uma pasta `experimentos/` aqui ou arquivar |

### Apagar ou arquivar (vazios)
`kies`, `Finance-`, `todo-list` — 0 KB, sem código.

### Padrões gerais
- Todo repo com: descrição no GitHub, `README.md`, `.gitignore` (nunca `.env`, keystore, `node_modules`, builds).
- Nomes em minúsculo com hífen, sem erros de digitação (`autoPreenchimmento` → `auto-preenchimento`, `aassmetnsv-2` → apagar).
- Projetos com segredos ou dados de clientes → privados.
