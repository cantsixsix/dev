# Mapa de ideias

Cada repositório, cada mini-app e cada módulo reaproveitável é tratado como **uma ideia separada, ainda a validar**.
Cada ideia se divide em **variações**: versões menores e mais focadas da mesma ideia (um nicho, um público, um módulo). A ideia é testar a variação mais barata primeiro.

## Como usar

| Ícone | Estágio | Significa |
|---|---|---|
| 💡 | Ideia | Só conceito, sem código útil |
| 🧪 | Protótipo | Tem código ou tela, ninguém de fora usou |
| 🚀 | No ar | Tem deploy/domínio, dá pra mostrar |
| ✅ | Validada | Alguém de fora usou e voltou / pagou / pediu mais |
| 🗄️ | Arquivada | Testou e não passou |

**Regra:** antes de mais código, rodar o *teste* da variação. Sem reação em 2 semanas → 🗄️.
**No GitHub:** *topics* `ideia` + área (`saude`, `jogos`…) + estágio (`prototipo`, `no-ar`).
**Números de mercado** (custo, MRR, concorrentes) das ideias A* vêm do `20-startup-ideas.jsx` do `startup-portfolio-20apps` — são estimativas suas, não dados verificados.

---

## 1. Produtividade e organização

### P1 · Tarefas — `todo-list` 🧪
App de tarefas com listas, recorrência e offline (Expo + Supabase).
- **P1.a Tarefas pessoais** — o app como está. *Teste:* build web + 10 pessoas por 1 semana.
- **P1.b Listas compartilhadas** — mercado/casa para casal ou família. *Teste:* 5 casais.
- **P1.c Rotinas recorrentes** — usar o motor de recorrência que já existe (`recurrence.ts`) para hábitos diários. *Teste:* landing "rotina sem esquecer".
- **P1.d Task AI** — IA quebra um objetivo em passos (case `Beaqme/new/cases/task-ai.html`). *Teste:* botão "quebrar em passos" no P1.a e medir uso.

### P2 · Calendário BR — `calendario` 🧪
Calendário Android com feriados brasileiros.
- **P2.a Calendário de feriados** — o app atual. *Teste:* teste interno da Play Store.
- **P2.b API/biblioteca de feriados BR** — extrair `BrazilianHolidays.java` como lib aberta (feriados móveis, Carnaval, Corpus Christi). *Teste:* publicar e contar estrelas/downloads.
- **P2.c Calendário escolar/empresa** — eventos compartilhados para um grupo. *Teste:* 1 escola ou equipe.

### P3 · Kies — cofre de chaves — `kies` 💡
- **P3.a CLI de `.env`** — guarda chaves por projeto e injeta no `.env` local (resolveria o problema de chaves vazadas que você mesmo teve). *Teste:* usar nos seus próprios repos por 2 semanas.
- **P3.b Scanner de segredos** — avisa antes do commit se tem keystore/`.env`/chave de API. *Teste:* hook de pre-commit open source.
- **P3.c Cofre de senhas pessoal** — gerenciador de senhas simples. *Teste:* pesquisa: por que não usam Bitwarden?
- **P3.d Rotação de chaves** — lembrete/automação para trocar chaves de API periodicamente.

### P4 · WhatsApp Desktop — `wpp-navegador-wrapper` 🧪
- **P4.a WhatsApp no WSL** — o app atual. *Teste:* *release* com instalador e contar downloads.
- **P4.b Wrapper genérico** — transforma qualquer site (Gmail, Notion, Trello) em app de janela. *Teste:* trocar a URL e publicar.
- **P4.c Multi-contas** — duas contas de WhatsApp lado a lado (pessoal + trabalho).

## 2. Saúde e bem-estar

### S1 · AquaTrack — `aquatrack` 🧪
Micro-SaaS de hidratação (Next.js + Supabase).
- **S1.a App de hidratação** — o atual. *Teste:* deploy + botão de plano pago fake no `/pricing`.
- **S1.b Hidratação para atletas/academia** — meta pelo treino e pelo clima.
- **S1.c Bem-estar corporativo** — desafio de hidratação por equipe, painel para RH. *Teste:* oferecer para 1 empresa.
- **S1.d Lembrete via WhatsApp** — sem app, só mensagens (combina com P4).

### S2 · Health Pro — `Beaqme/health.html` (app), `new/cases/health-pro.html` 🧪
- **S2.a Painel de hábitos** — sono, água, exercício num lugar só (S1 vira um módulo).
- **S2.b Diário de sintomas** — para levar ao médico.

## 3. Finanças

### F1 · Finance — `Finance-` 💡
- **F1.a Gastos pessoais** — registro rápido + resumo do mês. *Teste:* planilha para 5 pessoas.
- **F1.b Orçamento de casal** — divisão de contas.
- **F1.c Saída de dívidas** — plano de quitação.
- **F1.d Finance Dashboard PJ** — painel para pequena empresa (case `Beaqme/new/cases/finance-dashboard.html`).

### F2 · Investing — `investing` 🧪
Python + yfinance: calcula indicadores e dá uma nota para cada ativo.
- **F2.a Ações BR** — `agora.py`. *Teste:* relatório semanal num canal e ver se alguém pede o próximo.
- **F2.b Ações internacionais** — `internacional.py` (hoje vazio).
- **F2.c Alerta de nota** — avisa quando um ativo muda de nota.
- **F2.d Newsletter de análise** — o relatório vira conteúdo.

### F3 · GreenPulse — ESG para PMEs — portfolio `esg` 🧪
Estimativa: $10-30k MRR · lacuna: só existe opção enterprise.
- **F3.a Calculadora ESG grátis** — gera lead. **F3.b Relatório pronto pago** — para fornecedor de empresa grande que exige ESG.

## 4. Jogos e 3D

### J1 · Corrida 3D — `corrida` 🚀
Three.js: carro, mundo, monstro perseguidor, NPCs, chuva/poeira, áudio.
- **J1.a Fuga do monstro** — o modo atual. *Teste:* clipe de 15 s no TikTok/Reels com o link.
- **J1.b Corrida contra NPCs** — usar `NPCSystem.js` como modo competitivo.
- **J1.c Pacote de efeitos Three.js** — `Effects.js` (chuva, poeira, nuvens) como lib/asset vendável.

### J2 · Joguinho — mundo aberto — `joguinho-` 🧪
- **J2.a Direção livre** — explorar sem pista. *Teste:* fazer rodar e publicar na itch.io.
- **J2.b Entregas** — missões de levar coisas de um ponto a outro.
- **J2.c Gerador de cidade** — mundo procedural reaproveitável.

### J3 · Mundo Infinito — `Mundo_infinito` 🧪
Sistema solar 3D interativo (CSS 3D + jQuery).
- **J3.a Material educativo** — para aulas de ciências. *Teste:* 3 professores.
- **J3.b Wallpaper/tela de descanso animada.**

## 5. Entretenimento

### E1 · Místico — `mistico` 🚀
Tarot e horóscopo (site + app Android).
- **E1.a Tarot** — tiragem diária. **E1.b Horóscopo** — diário por signo.
- **E1.c Leitura completa paga** — *teste:* botão de compra e medir cliques.
- **E1.d Horóscopo por WhatsApp/e-mail** — assinatura diária.

## 6. Vendas, e-commerce e ofertas

### V1 · Anunciador ML — `dev/ai/prompts/anunciador-ml.md` 🧪
- **V1.a Publicação em massa** — o que existe. *Teste:* 3 vendedores com muitos produtos.
- **V1.b Respondedor de perguntas** — o app já pede permissão do tópico `questions`; IA responde perguntas dos compradores.
- **V1.c Gerador de título/descrição** — IA otimiza o anúncio.
- **V1.d Painel de pedidos** — tópico `orders_v2`.

### V2 · PromoTech — canal de ofertas — `promotech-landing` 🧪
- **V2.a Grupo de ofertas tech** — *teste:* criar o grupo e medir entradas em 1 semana.
- **V2.b Robô de ofertas** — posta automaticamente ofertas com link de afiliado.

### V3 · MyLoja / Beaqme Store — `myloja` 🧪
- **V3.a Loja da marca** — definir 1 produto e colocar à venda.

### V4 · PriceRadar — portfolio `price-monitor` 🧪
$10-30k MRR · lacuna: ninguém atende lojas pequenas.
- **V4.a Monitor para lojas Shopify.** **V4.b Monitor para vendedores do ML** (junta com V1). **V4.c Alerta de queda de preço para consumidor** (alimenta V2).

### V5 · BoxCrate — portfolio `sub-box` 🧪
$5-20k MRR · lacuna: Cratejoy fechou.
- **V5.a Gestão de clube de assinatura para creators.**

### V6 · ProofPulse — portfolio `social-proof` 🧪
$5-15k MRR.
- **V6.a Popup de prova social** — *teste:* instalar no PromoTech e medir conversão.
- **V6.b Copy do popup feita por IA.**

### V7 · LoveWall — portfolio `testimonials` 🧪
$10-25k MRR · lacuna: vídeo-first.
- **V7.a Mural de depoimentos em texto.** **V7.b Coleta de depoimento em vídeo.** **V7.c IA corta os melhores trechos.**

### V8 · LaunchPad — portfolio `waitlist` 🧪
$5-15k MRR.
- **V8.a Waitlist com indicação** — **usar como ferramenta de validação de todas as outras ideias.**
- **V8.b Página de lançamento + A/B test.**

## 7. Ferramentas de IA para negócios
Do `startup-portfolio-20apps` (`public/apps/`). Todas 🧪.

| # | Ideia | Variações (nichos) | MRR estimado |
|---|---|---|---|
| A1 | **CodeSnap** · `screenshot-to-code` | a) print → landing page · b) print → componente React · c) clonar landing de concorrente | $10-30k |
| A2 | **ColdReach** · `cold-email` | a) gerador de e-mail · b) checador de entregabilidade grátis (`dnsChecks.js` já existe) · c) sequência de follow-up | $15-50k |
| A3 | **ProposalCraft** · `proposals` | a) proposta para freelancer · b) orçamento → fatura · c) proposta para agência | $10-30k |
| A4 | **HireWave** · `job-board` | a) job board white-label · b) board de nicho (ex.: vagas de dev BR) | $5-25k |
| A5 | **ShipLog** · `changelog` | a) changelog a partir de texto · b) changelog direto do GitHub · c) widget "novidades" no site | $5-15k |
| A6 | **PulseMetrics** · `analytics` | a) analytics sem cookie · b) insights automáticos por IA · c) alertas de queda de tráfego | $10-40k |
| A7 | **MeetingPad** · `meeting-notes` | a) vendas · b) clínicas/dentistas · c) advogados · d) imobiliárias | $15-50k |
| A8 | **BrandForge** · `brand-kit` | a) paleta + fontes · b) guia de marca completo · c) templates de post | $10-30k |
| A9 | **ClientHub** · `client-portal` | a) status de projeto · b) entrega de arquivos · c) aprovação de layout | $10-25k |
| A10 | **ResumeAI** · `resume` | a) currículo por vaga · b) otimização ATS avulsa ($4,99) · c) carta de apresentação | $10-30k |
| A11 | **PodWave** · `podcast` | a) show notes · b) newsletter do episódio · c) cortes/clips | $10-30k |
| A12 | **BlogForge** · `notion-blog` | a) Notion → blog · b) Notion → site · c) SEO automático | $5-20k |
| A13 | **UptimeGuard** · `uptime` | a) monitor + status page · b) IA explica por que caiu | $5-20k |
| A14 | **DeckBuilder** · `pitch-deck` | a) pitch deck · b) one-pager para investidor | $10-30k |

**Teste do grupo A:** colocar todas no ar com o LaunchPad (V8) na frente e ver quais 2–3 recebem inscrições. Só essas ganham repo próprio.

## 8. Plataforma, módulos e marca

### X1 · Mega Repo — plataforma — `mega-repo` 🧪
O que sustenta todas as ideias. Cada parte pode virar produto:
- **X1.a AI Gateway** — `services/ai-gateway`: uma API única para qualquer provedor de IA (troca de modelo sem mexer no app).
- **X1.b App Hub** — `services/app-hub`: roda qualquer mini-app por rota.
- **X1.c Widget embed** — `shared/utils/embedRenderer.js`: qualquer mini-app vira um `<script>` para colar em outro site.
- **X1.d Gerador de documentos** — `shared/pdf/generateDocument.js`: base para propostas, relatórios, currículos.
- **X1.e Kit de MVP** — `createApp` + `memoryStore` + `idGenerator`: template para subir um micro-SaaS em 1 dia.

### X2 · Startup Portfolio — vitrine — `startup-portfolio-20apps` 🧪
- **X2.a Vitrine das ideias** — `public/` com todas as ferramentas do grupo A e V.
- **X2.b Banco de ideias** — `20-startup-ideas.jsx` (custo, MRR, concorrentes, lacuna) pode virar conteúdo/newsletter "1 ideia de micro-SaaS por semana".

### X3 · Beaqme — marca — `Beaqme` + `myloja` (`beaqme.com`) 🚀
- **X3.a Site da agência** — "construímos produtos digitais que escalam".
- **X3.b Labs** — seção que lista as ideias deste mapa como experimentos.
- **X3.c Blog** — `new/blog/` com o conteúdo de X2.b.

### X4 · Link in Bio — `saas-landing-template` 🧪
- **X4.a Template grátis** — gera lead. **X4.b Link in bio pago para criadores.** **X4.c Hub de links da Beaqme.**

### X5 · Dotfiles — `dotfiles` (ferramenta, não produto)
- **X5.a Script de pós-instalação Ubuntu/Fedora** — pode virar repo público útil para outros devs.

---

## Fora do mapa
- `assetsv1`, `aassmetnsv-2`, `voxel` — a apagar.
- `autoPreenchimmento` — não é ideia de produto.

## Totais
40 ideias e 115 variações para testar.
