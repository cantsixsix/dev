#!/usr/bin/env python3
"""Gera uma landing de validação por ideia a partir de validacao/ideias.json.

Saída: validacao/site/ (index.html + uma pasta por ideia). Publicar na Netlify:
os formulários usam Netlify Forms, então cada inscrição aparece em
Netlify → Site → Forms, já marcada com o id da ideia e se a pessoa clicou no preço.

    python3 scripts/gerar_landings.py
"""
import html
import json
import os
import shutil

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "validacao")
SAIDA = os.path.join(RAIZ, "site")
e = html.escape

CSS = """
:root{--bg:#fafaf9;--card:#fff;--ink:#1c1917;--muted:#57534e;--line:#e7e5e4;--accent:#4f46e5;--accent-ink:#fff;--ok:#15803d}
@media (prefers-color-scheme:dark){:root{--bg:#0c0a09;--card:#1c1917;--ink:#f5f5f4;--muted:#a8a29e;--line:#292524;--accent:#818cf8;--accent-ink:#0c0a09;--ok:#4ade80}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:640px;margin:0 auto;padding:56px 16px 72px}
.tag{display:inline-block;font-size:13px;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:2px 10px;margin-bottom:20px}
h1{font-size:clamp(30px,6vw,44px);line-height:1.1;letter-spacing:-.02em;margin:0 0 14px}
.sub{font-size:19px;color:var(--muted);margin:0 0 32px}
.box{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px}
.box h2{font-size:15px;margin:0 0 6px;color:var(--muted);font-weight:600}
.box p{margin:0}
.grid{display:grid;gap:12px;margin:0 0 32px}
form{display:flex;gap:8px;flex-wrap:wrap}
input[type=email]{flex:1 1 220px;min-width:0;font:inherit;padding:14px 16px;border-radius:12px;border:1px solid var(--line);background:var(--card);color:var(--ink)}
button{font:inherit;font-weight:600;padding:14px 20px;border-radius:12px;border:0;background:var(--accent);color:var(--accent-ink);cursor:pointer}
button.ghost{background:transparent;color:var(--accent);border:1px solid var(--line)}
.preco{margin:20px 0 0;display:flex;align-items:center;gap:12px;flex-wrap:wrap;color:var(--muted)}
.ok{color:var(--ok);font-weight:600;margin-top:16px;display:none}
.hide{display:none}
footer{margin-top:48px;font-size:13px;color:var(--muted)}
ul.lista{list-style:none;padding:0;margin:0;display:grid;gap:8px}
ul.lista a{display:block;padding:14px 16px;border:1px solid var(--line);border-radius:12px;background:var(--card);color:var(--ink);text-decoration:none}
ul.lista small{color:var(--muted);display:block}
"""

JS = """
const f=document.querySelector('form[name=lista-de-espera]');
const pago=document.getElementById('quer-pagar');
document.getElementById('btn-preco')?.addEventListener('click',()=>{
  pago.value='sim';
  document.getElementById('aviso-preco').classList.remove('hide');
  f.querySelector('input[type=email]').focus();
});
f.addEventListener('submit',async ev=>{
  ev.preventDefault();
  const dados=new URLSearchParams(new FormData(f)).toString();
  try{await fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:dados});}catch(_){}
  f.classList.add('hide');document.querySelector('.ok').style.display='block';
});
"""


def pagina(i):
    t = i["teste"]
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(i['nome'])}</title><meta name="description" content="{e(t['subtitulo'])}">
<link rel="stylesheet" href="../estilo.css"></head>
<body><main>
<span class="tag">Em breve</span>
<h1>{e(t['titulo'])}</h1>
<p class="sub">{e(t['subtitulo'])}</p>
<div class="grid">
  <div class="box"><h2>O problema</h2><p>{e(i['problema'])}</p></div>
  <div class="box"><h2>Como funciona</h2><p>{e(i['como'])}</p></div>
</div>
<form name="lista-de-espera" method="POST" data-netlify="true" netlify-honeypot="bot">
  <input type="hidden" name="form-name" value="lista-de-espera">
  <input type="hidden" name="ideia" value="{e(i['id'])}">
  <input type="hidden" name="quer-pagar" id="quer-pagar" value="nao">
  <p class="hide"><label>Não preencha <input name="bot"></label></p>
  <input type="email" name="email" required placeholder="seu@email.com" aria-label="Seu e-mail">
  <button type="submit">{e(t['cta'])}</button>
</form>
<p class="ok">Pronto! Você está na lista e vai ser avisado primeiro. 🙌</p>
<div class="preco"><span>Preço previsto: <strong>{e(t['preco'])}</strong></span>
  <button type="button" class="ghost" id="btn-preco">Eu pagaria isso</button></div>
<p id="aviso-preco" class="hide" style="color:var(--muted)">Obrigado! Ainda não estamos cobrando — deixe seu e-mail acima e você garante o preço de lançamento.</p>
<footer>{e(i['nome'])} · ideia {e(i['id'])}</footer>
</main><script>{JS}</script></body></html>
"""


def indice(ideias):
    itens = "\n".join(
        f'<li><a href="{e(i["id"].lower())}/"><strong>{e(i["id"])} · {e(i["nome"])}</strong>'
        f'<small>{e(i["pitch"])}</small></a></li>' for i in ideias)
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ideias em validação</title><link rel="stylesheet" href="estilo.css"></head>
<body><main><span class="tag">{len(ideias)} ideias</span><h1>Ideias em validação</h1>
<p class="sub">Uma página por ideia. Cada uma tem lista de espera e um botão de preço.</p>
<ul class="lista">{itens}</ul></main></body></html>
"""


def main():
    ideias = json.load(open(os.path.join(RAIZ, "ideias.json"), encoding="utf-8"))
    shutil.rmtree(SAIDA, ignore_errors=True)
    os.makedirs(SAIDA)
    open(os.path.join(SAIDA, "estilo.css"), "w").write(CSS.strip() + "\n")
    open(os.path.join(SAIDA, "index.html"), "w").write(indice(ideias))
    for i in ideias:
        d = os.path.join(SAIDA, i["id"].lower())
        os.makedirs(d)
        open(os.path.join(d, "index.html"), "w").write(pagina(i))
    print(f"{len(ideias)} landings em {os.path.relpath(SAIDA)}")


if __name__ == "__main__":
    main()
