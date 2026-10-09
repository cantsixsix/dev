# Validação rápida das ideias

Tudo parte de **`ideias.json`**: para cada ideia, o problema, o público, como funciona, como ganha dinheiro e o teste de 7 dias (título da landing, canal onde divulgar, preço e meta).

| Arquivo | O que é |
|---|---|
| `ideias.json` | Fonte única das 39 ideias. Edite aqui. |
| `site/` | Uma landing por ideia (`site/a3/`, `site/p1/`…), com lista de espera e botão **“Eu pagaria isso”**. Gerado por `scripts/gerar_landings.py`. |
| `quadro.html` | A **Bancada de Ideias** (publicada como Artifact): explica cada ideia e guarda os resultados. Gerado por `scripts/gerar_quadro.py`. |

## Colocar as landings no ar (uma vez, ~5 minutos)

1. Entre em [app.netlify.com](https://app.netlify.com) → **Add new site → Import an existing project** → escolha o repo `dev` (branch `main`, depois de juntar esta branch). O `netlify.toml` já diz o que publicar.
   *Alternativa sem Git:* rode `python3 scripts/gerar_landings.py` e arraste a pasta `validacao/site` para app.netlify.com/drop.
2. Na Netlify, em **Forms**, ative a detecção de formulários e faça um novo deploy.
3. Copie o endereço do site (ex.: `https://ideias-cantsixsix.netlify.app`) e cole no campo **Endereço das landings** da Bancada. Cada ficha passa a mostrar o link da sua landing.

## Rodar um teste

1. Na Bancada, mude a ideia para **Testando** e anote a data nas anotações.
2. Poste o link da landing no canal indicado na ficha.
3. Depois de 7 dias, veja em **Netlify → Forms → lista-de-espera** quantas inscrições têm `ideia = <ID>` e quantas têm `quer-pagar = sim`. Anote na Bancada.
4. Bateu a meta → **Validada**. Não bateu → **Arquivada** (e mude o emoji no `IDEIA.md` do repo para o painel semanal acompanhar).

Dica: rode 3 a 5 testes por semana, começando pelos do tipo *landing* (são os mais baratos). Em 2 meses todas as ideias têm resposta.
