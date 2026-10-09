# Mapa de ideias

Cada repositório (e cada mini-app dentro deles) é tratado como **uma ideia separada, ainda a validar**.
O objetivo é saber, para cada uma: o que é, de onde veio, em que estágio está e qual o próximo teste barato que diz se vale continuar.

## Como usar

**Estágios**

| Ícone | Estágio | Significa |
|---|---|---|
| 💡 | Ideia | Só nome/conceito, sem código útil |
| 🧪 | Protótipo | Tem código ou tela, ninguém de fora usou |
| 🚀 | No ar | Tem deploy/domínio, dá pra mostrar para alguém |
| ✅ | Validada | Alguém de fora usou e voltou / pagou / pediu mais |
| 🗄️ | Arquivada | Testou e não passou — fica guardada |

**Regra de validação (igual para todas):** antes de escrever mais código, rodar o *próximo teste* da tabela. Se em 2 semanas ninguém reagir, a ideia vai para 🗄️ e libera espaço para outra.

**No GitHub:** marcar cada repo com *topics* `ideia` + a categoria (ex.: `saude`, `jogos`) + o estágio (`prototipo`, `no-ar`). Assim dá para filtrar a conta inteira por ideia sem precisar renomear tudo.

---

## 1. Produtividade e organização

| # | Ideia | Origem | Estágio | O que é | Próximo teste |
|---|---|---|---|---|---|
| P1 | **Tarefas** | `todo-list` | 🧪 | App de tarefas com listas, recorrência e modo offline (Expo + Supabase) | Publicar build web e colocar 10 pessoas usando por 1 semana |
| P2 | **Calendário BR** | `calendario` | 🧪 | Calendário Android com feriados brasileiros e eventos locais | Subir no teste interno da Play Store e ver se alguém usa mais de 3 dias |
| P3 | **Kies — cofre de chaves** | `kies` | 💡 | Guardar chaves de API, senhas e tokens dos seus projetos num lugar só (ex.: CLI que injeta no `.env`) | Escrever a página de uma frase + lista de espera; perguntar em grupos de devs |
| P4 | **WhatsApp Desktop no WSL** | `wpp-navegador-wrapper` | 🧪 | WhatsApp Web como app nativo no Windows a partir do WSL | Publicar uma *release* com instalador e contar downloads |
| P5 | **Task AI** | `Beaqme/new/cases/task-ai.html`, `tools/task.html` | 💡 | Tarefas com IA que quebra objetivos em passos | Juntar com P1 como recurso ou testar separado com landing |

## 2. Saúde e bem-estar

| # | Ideia | Origem | Estágio | O que é | Próximo teste |
|---|---|---|---|---|---|
| S1 | **AquaTrack** | `aquatrack` | 🧪 | Micro-SaaS de controle de hidratação (Next.js + Supabase) | Deploy + plano pago fake na página `/pricing` para medir cliques |
| S2 | **Health Pro** | `Beaqme/new/cases/health-pro.html`, `tools/health.html` | 💡 | Painel de saúde (hábitos, métricas) | Decidir se é a mesma ideia que S1 ou algo maior |

## 3. Finanças

| # | Ideia | Origem | Estágio | O que é | Próximo teste |
|---|---|---|---|---|---|
| F1 | **Finance — finanças pessoais** | `Finance-` | 💡 | Controle de gastos e orçamento pessoal | Planilha/protótipo simples para 5 pessoas e ver quem continua usando |
| F2 | **Investing** | `investing` | 🧪 | Scripts Python de análise de investimentos (nacional e internacional) | Rodar 1 relatório semanal e compartilhar; ver se alguém pede o próximo |
| F3 | **Finance Dashboard** | `Beaqme/new/cases/finance-dashboard.html`, `tools/finance.html` | 💡 | Dashboard financeiro para pequenas empresas | Juntar com F1 (pessoa física) ou separar para PJ |
| F4 | **GreenPulse — ESG** | `startup-portfolio-20apps/public/apps/esg.html` | 🧪 | Calculadora de score ESG com IA | Mostrar para 3 empresas que precisam de relatório ESG |

## 4. Jogos e 3D

| # | Ideia | Origem | Estágio | O que é | Próximo teste |
|---|---|---|---|---|---|
| J1 | **Corrida 3D** | `corrida` | 🚀 | Corrida em Three.js com monstro perseguindo, NPCs e trilha phonk | Postar um clipe de 15s no TikTok/Reels com o link |
| J2 | **Joguinho — mundo aberto** | `joguinho-` | 🧪 | Direção livre em mundo aberto (Three.js), diferente da corrida: sem pista, exploração | Fazer rodar (ajustar `package.json`) e publicar na itch.io |
| J3 | **Voxel** | `voxel` | 🚀 | Montar e destruir brinquedos em voxel, gerados por IA (Gemini) | Corrigir a chave exposta, depois testar com crianças/pais |
| J4 | **Mundo Infinito** | `Mundo_infinito` | 🧪 | Sistema solar 3D interativo | Testar como material educativo com professores |

## 5. Entretenimento e consumo

| # | Ideia | Origem | Estágio | O que é | Próximo teste |
|---|---|---|---|---|---|
| E1 | **Místico** | `mistico` | 🚀 | App de tarot e horóscopo (site + app Android) | Ver número de instalações/visitas; testar 1 recurso pago (leitura completa) |

## 6. Vendas, e-commerce e ofertas

| # | Ideia | Origem | Estágio | O que é | Próximo teste |
|---|---|---|---|---|---|
| V1 | **Anunciador em massa ML** | `dev/ai/prompts/anunciador-ml.md`, `dev/_archive/ml-anunciador.zip` | 🧪 | Publica vários produtos no Mercado Livre via API | Oferecer para 3 vendedores do ML que têm muitos produtos |
| V2 | **PromoTech — canal de ofertas** | `promotech-landing` | 🧪 | Landing de canal de ofertas/afiliados | Criar o grupo e medir quantos entram em 1 semana |
| V3 | **MyLoja** | `myloja` | 🧪 | Loja online da marca | Definir o que vende; 1 produto à venda |
| V4 | **PriceRadar** | `startup-portfolio-20apps` → `price-monitor` | 🧪 | Monitor de preços de concorrentes com IA | Combina com V1/V2 — testar com os mesmos vendedores |
| V5 | **BoxCrate** | → `sub-box` | 🧪 | Gestão de clube de assinatura | Achar 1 clube de assinatura pequeno para usar |
| V6 | **ProofPulse** | → `social-proof` | 🧪 | Popups de prova social para sites | Instalar no próprio PromoTech/MyLoja e medir conversão |
| V7 | **LoveWall** | → `testimonials` | 🧪 | Coletar e exibir depoimentos | Mesmo teste do V6 |
| V8 | **LaunchPad** | → `waitlist` | 🧪 | Lista de espera viral com indicação | **Usar como ferramenta de validação de todas as outras ideias** |

## 7. Ferramentas de IA para negócios
Vindas do `startup-portfolio-20apps` — cada uma é uma página em `public/apps/`.

| # | Ideia | App | Estágio | O que é |
|---|---|---|---|---|
| A1 | **BrandForge** | `brand-kit` | 🧪 | Identidade visual com IA a partir da descrição do negócio |
| A2 | **ShipLog** | `changelog` | 🧪 | Changelog/release notes automático |
| A3 | **ColdReach** | `cold-email` | 🧪 | E-mail frio personalizado com checagem de entregabilidade |
| A4 | **MeetingPad** | `meeting-notes` | 🧪 | Notas e tarefas a partir da transcrição de reunião |
| A5 | **DeckBuilder** | `pitch-deck` | 🧪 | Pitch deck estruturado com IA |
| A6 | **PodWave** | `podcast` | 🧪 | Show notes e timestamps de podcast |
| A7 | **ProposalCraft** | `proposals` | 🧪 | Proposta comercial a partir de briefing |
| A8 | **ResumeAI** | `resume` | 🧪 | Currículo otimizado para ATS |
| A9 | **CodeSnap** | `screenshot-to-code` | 🧪 | Gera HTML/CSS a partir de descrição de tela |
| A10 | **BlogForge** | `notion-blog` | 🧪 | CMS de blog estilo Notion |
| A11 | **HireWave** | `job-board` | 🧪 | Job board com IA |
| A12 | **ClientHub** | `client-portal` | 🧪 | Portal de projetos para clientes de freelancer |
| A13 | **PulseMetrics** | `analytics` | 🧪 | Analytics focado em privacidade |
| A14 | **UptimeGuard** | `uptime` | 🧪 | Monitor de disponibilidade + status page |

**Próximo teste para o grupo A:** são 14 ideias parecidas (IA gera texto a partir de um input). Em vez de validar uma por uma, colocar todas no ar com o LaunchPad (V8) na frente de cada uma e ver quais 2–3 recebem inscrições. Só essas ganham repo próprio.

## 8. Plataforma e marca (o que sustenta as ideias)

| # | Ideia | Origem | Estágio | O que é |
|---|---|---|---|---|
| X1 | **Mega Repo — hub de micro-SaaS** | `mega-repo` | 🧪 | A *plataforma*: AI gateway único + app hub que roda qualquer mini-app por rota. Infra para lançar ideias rápido |
| X2 | **Startup Portfolio** | `startup-portfolio-20apps` | 🧪 | A *vitrine* das 20 ideias (grupo A + V4–V8 + F4) |
| X3 | **Beaqme** | `Beaqme` + `myloja` (`beaqme.com`) | 🚀 | Marca "Digital Product House" que apresenta todos os produtos acima |
| X4 | **Link in Bio** | `saas-landing-template` | 🧪 | Template de link na bio para criadores — pode virar produto ou ser o hub de links da Beaqme |
| X5 | **Dotfiles** | `dotfiles` | — | Seu ambiente de desenvolvimento (não é produto) |

### Como mega-repo e startup-portfolio se separam
Hoje os dois têm o mesmo código. Proposta para virarem coisas diferentes:
- **`mega-repo`** fica só com `services/` + `shared/` → é a plataforma (X1).
- **`startup-portfolio-20apps`** fica só com `public/apps/` → é a vitrine das ideias (X2), consumindo a API do mega-repo.

---

## Fora do mapa
- `assetsv1`, `aassmetnsv-2` — serão apagados.
- `autoPreenchimmento` — não é uma ideia de produto.

## Totais
42 ideias: 5 💡, 33 🧪, 4 🚀 — mais o `dotfiles`, que é ferramenta (contando cada mini-app do portfolio e cada case da Beaqme separadamente).
