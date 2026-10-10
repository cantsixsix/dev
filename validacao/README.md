# Validação rápida das ideias

Tudo parte de **`ideias.json`**: para cada ideia, o problema, o público, como funciona, como ganha dinheiro e o teste de 7 dias (título da landing, canal onde divulgar, preço e meta).

| Arquivo | O que é |
|---|---|
| `ideias.json` | Fonte única das 39 ideias. Edite aqui. |
| `site/` | Uma landing por ideia (`site/a3/`, `site/p1/`…), com lista de espera e botão **“Eu pagaria isso”**. Gerado por `scripts/gerar_landings.py`. |
| `quadro.html` | A **Bancada de Ideias** (publicada como Artifact): explica cada ideia e guarda os resultados. Gerado por `scripts/gerar_quadro.py`. |

## Colocar as landings no ar (1 minuto)

O site **validar-ideias** já foi criado na sua conta da Netlify, com os formulários ativados, e a Bancada já aponta para `https://validar-ideias.netlify.app`. Falta só subir os arquivos:

1. Abra https://app.netlify.com/projects/validar-ideias/deploys
2. Arraste a pasta `validacao/site` (deste repo) para a área **“Drag and drop your project folder here”**.
3. Pronto: `https://validar-ideias.netlify.app/p3/`, `/a3/` etc. ficam no ar, e as inscrições aparecem em **Forms → lista-de-espera**.

Depois de juntar esta branch na `main`, você pode trocar o passo 2 por deploy automático: *Project configuration → Build & deploy → Link repository* → repo `dev`. O `netlify.toml` já diz o que publicar.

## Rodar um teste

1. Na Bancada, mude a ideia para **Testando** e anote a data nas anotações.
2. Poste o link da landing no canal indicado na ficha.
3. Depois de 7 dias, veja em **Netlify → Forms → lista-de-espera** quantas inscrições têm `ideia = <ID>` e quantas têm `quer-pagar = sim`. Anote na Bancada.
4. Bateu a meta → **Validada**. Não bateu → **Arquivada** (e mude o emoji no `IDEIA.md` do repo para o painel semanal acompanhar).

Dica: rode 3 a 5 testes por semana, começando pelos do tipo *landing* (são os mais baratos). Em 2 meses todas as ideias têm resposta.
