#!/usr/bin/env python3
"""Gera PAINEL.md: estado de cada ideia lendo o IDEIA.md de todos os repos da conta.

Roda no GitHub Actions toda semana (.github/workflows/painel.yml), mas também localmente:
    GITHUB_TOKEN=... python3 scripts/painel.py
Sem token funciona para repos públicos (limite de 60 chamadas/hora da API).
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

OWNER = os.environ.get("PAINEL_OWNER", "cantsixsix")
# Dias sem commit para uma ideia em 💡/🧪 ser marcada para teste ou arquivo (regra das 2 semanas).
DIAS_PARADA = int(os.environ.get("PAINEL_DIAS", "14"))
# Repos que não são ideia de produto.
IGNORAR = {"dev", "dotfiles"}
ESTAGIOS = {"💡": "Ideia", "🧪": "Protótipo", "🚀": "No ar", "✅": "Validada", "🗄️": "Arquivada"}
TOKEN = os.environ.get("PAINEL_TOKEN") or os.environ.get("GITHUB_TOKEN")
SAIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "PAINEL.md")

HEADING = re.compile(r"^## ([A-Z]\d+) · (.+?)\s*(💡|🧪|🚀|✅|🗄️)?\s*$", re.M)
# Linhas de tabela (ferramentas A1…A14): "| A1 | **Nome** · `app` | ... |". Estágio = emoji na linha, padrão 🧪.
LINHA_TABELA = re.compile(r"^\| ([A-Z]\d+) \| \*\*(.+?)\*\*.*$", re.M)
EMOJI = re.compile(r"💡|🧪|🚀|✅|🗄️")


def get(url, raw=False, auth=True):
    req = urllib.request.Request(url, headers={"User-Agent": "painel-ideias"})
    if TOKEN and auth:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Accept", "application/vnd.github.raw" if raw else "application/vnd.github+json")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode("utf-8")
            return body if raw else json.loads(body)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def listar_repos():
    repos, page = [], 1
    while True:
        lote = get(f"https://api.github.com/users/{OWNER}/repos?per_page=100&page={page}&type=owner")
        if not lote:
            break
        repos += lote
        page += 1
    # Com token do próprio dono, inclui privados.
    if TOKEN and os.environ.get("PAINEL_TOKEN"):
        privados = get("https://api.github.com/user/repos?per_page=100&affiliation=owner&visibility=private") or []
        nomes = {r["name"] for r in repos}
        repos += [r for r in privados if r["name"] not in nomes]
    return repos


def ultimo_commit(repo):
    branch = repo.get("default_branch") or "main"
    commits = get(f"https://api.github.com/repos/{OWNER}/{repo['name']}/commits?sha={branch}&per_page=1")
    if not commits:
        return None
    data = commits[0]["commit"]["committer"]["date"]
    return datetime.fromisoformat(data.replace("Z", "+00:00"))


def ler_ideia(repo):
    branch = repo.get("default_branch") or "main"
    try:
        texto = get(f"https://api.github.com/repos/{OWNER}/{repo['name']}/contents/IDEIA.md?ref={branch}", raw=True)
    except urllib.error.HTTPError:
        texto = None
    if texto is None and not repo.get("private"):
        # Repos públicos: lê direto, sem token (o GITHUB_TOKEN do Actions só vale para este repo).
        texto = get(f"https://raw.githubusercontent.com/{OWNER}/{repo['name']}/{branch}/IDEIA.md", raw=True, auth=False)
    return texto


def main():
    agora = datetime.now(timezone.utc)
    linhas, sem_ficha, alertas = [], [], []
    contagem = {k: 0 for k in ESTAGIOS}

    for repo in sorted(listar_repos(), key=lambda r: r["name"].lower()):
        nome = repo["name"]
        if nome in IGNORAR or repo.get("archived"):
            continue
        texto = ler_ideia(repo)
        if not texto:
            sem_ficha.append(nome)
            continue
        quando = ultimo_commit(repo)
        dias = (agora - quando).days if quando else None
        link = f"[`{nome}`](https://github.com/{OWNER}/{nome})"
        if repo.get("private"):
            link += " 🔒"
        itens = HEADING.findall(texto)
        for m in LINHA_TABELA.finditer(texto):
            achado = EMOJI.search(m.group(0))
            itens.append((m.group(1), m.group(2), achado.group(0) if achado else "🧪"))
        for ident, titulo, emoji in itens:
            titulo = re.sub(r"\s+—\s+(portfolio\s+)?`.*$", "", titulo).strip()
            emoji = emoji or "💡"
            contagem[emoji] += 1
            parada = dias is not None and dias >= DIAS_PARADA and emoji in ("💡", "🧪")
            if parada:
                alertas.append(f"- **{ident} {titulo}** ({nome}) — {dias} dias sem commit: rodar o teste ou arquivar.")
            linhas.append(
                f"| {ident} | {titulo} | {link} | {emoji} {ESTAGIOS[emoji]} | "
                f"{quando.strftime('%d/%m/%Y') if quando else '—'} | "
                f"{'⚠️ ' if parada else ''}{dias if dias is not None else '—'} |"
            )

    linhas.sort(key=lambda l: (l.split("|")[1].strip()[0], int(re.sub(r"\D", "", l.split("|")[1]) or 0)))
    resumo = " · ".join(f"{k} {v}" for k, v in contagem.items() if v)
    out = [
        "# Painel de ideias",
        "",
        f"Gerado automaticamente em {agora.strftime('%d/%m/%Y %H:%M')} UTC por `scripts/painel.py` "
        "(roda toda segunda-feira e pode ser disparado em *Actions → Painel de ideias → Run workflow*).",
        "Não edite à mão: mude o estágio no `IDEIA.md` do repo da ideia (o emoji no fim do título) e o painel acompanha.",
        "",
        f"**Total:** {sum(contagem.values())} ideias — {resumo}",
        "",
        f"## ⚠️ Paradas há {DIAS_PARADA}+ dias",
        "",
        *(alertas or ["Nenhuma. 🎉"]),
        "",
        "## Todas as ideias",
        "",
        "| # | Ideia | Repo | Estágio | Último commit | Dias parado |",
        "|---|---|---|---|---|---|",
        *linhas,
        "",
        "## Repos sem `IDEIA.md`",
        "",
        *([f"- [`{n}`](https://github.com/{OWNER}/{n}) — criar a ficha ou arquivar o repo." for n in sem_ficha] or ["Nenhum."]),
        "",
    ]
    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"PAINEL.md: {sum(contagem.values())} ideias, {len(alertas)} paradas, {len(sem_ficha)} sem ficha")


if __name__ == "__main__":
    sys.exit(main())
