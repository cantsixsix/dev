#!/usr/bin/env python3
"""Escreve (ou atualiza) a seção "Como validar" no IDEIA.md de cada repo, a partir de validacao/ideias.json.

    python3 scripts/gerar_fichas.py /caminho/onde/estao/os/clones

A seção fica entre marcadores, então rodar de novo só substitui o bloco.
"""
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
SITE = "https://validar-ideias.netlify.app"
BANCADA = "https://claude.ai/artifact/Y4H9MCxyvwwLDmhL812znj"
INI, FIM = "<!-- validacao:inicio -->", "<!-- validacao:fim -->"
TIPO = {"landing": "Landing + lista de espera", "conteudo": "Post de conteúdo com link",
        "conversa": "Conversar com 3–5 clientes", "uso": "Colocar pessoas usando"}


def bloco(ideias):
    partes = [INI, "", "## 🧪 Como validar", "",
              f"Teste de 7 dias. Resultados vão na [Bancada de Ideias]({BANCADA}).", ""]
    for i in ideias:
        t = i["teste"]
        partes += [
            f"### {i['id']} · {i['nome']}", "",
            f"**Em uma frase:** {i['pitch']}", "",
            f"- **Problema:** {i['problema']}",
            f"- **Para quem:** {i['publico']}",
            f"- **Como funciona:** {i['como']}",
            f"- **Como ganha dinheiro:** {i['dinheiro']}", "",
            f"| Teste | |", "|---|---|",
            f"| Tipo | {TIPO[t['tipo']]} |",
            f"| Página | {SITE}/{i['id'].lower()}/ |",
            f"| Onde divulgar | {t['canal']} |",
            f"| Preço testado | {t['preco']} |",
            f"| Meta em 7 dias | **{t['meta']}** |", "",
        ]
    partes.append(FIM)
    return "\n".join(partes) + "\n"


def main():
    raiz = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, "..", "..")
    ideias = json.load(open(os.path.join(AQUI, "..", "validacao", "ideias.json"), encoding="utf-8"))
    por_repo = {}
    for i in ideias:
        por_repo.setdefault(i["repo"].lower(), []).append(i)
    por_repo.pop("dev", None)  # V1 vive no próprio mapa (IDEIAS.md)
    for repo, lista in sorted(por_repo.items()):
        caminho = os.path.join(raiz, repo, "IDEIA.md")
        if not os.path.exists(caminho):
            print(f"pulado (sem IDEIA.md): {repo}")
            continue
        texto = open(caminho, encoding="utf-8").read()
        novo = bloco(lista)
        if INI in texto:
            texto = re.sub(re.escape(INI) + r".*?" + re.escape(FIM) + r"\n?", lambda _: novo, texto, flags=re.S)
        else:
            texto = texto.rstrip("\n") + "\n\n" + novo
        open(caminho, "w", encoding="utf-8").write(texto)
        print(f"{repo}: {', '.join(i['id'] for i in lista)}")


if __name__ == "__main__":
    main()
