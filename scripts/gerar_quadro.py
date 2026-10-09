#!/usr/bin/env python3
"""Gera validacao/quadro.html (o Quadro de validação publicado como Artifact) a partir de validacao/ideias.json."""
import json, os
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "validacao")
ideias = json.load(open(os.path.join(RAIZ, "ideias.json"), encoding="utf-8"))
dados = json.dumps(ideias, ensure_ascii=False).replace("</", "<\\/")
html = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "quadro.template.html"), encoding="utf-8").read()
open(os.path.join(RAIZ, "quadro.html"), "w", encoding="utf-8").write(html.replace("__IDEIAS__", dados))
print("validacao/quadro.html gerado com", len(ideias), "ideias")
