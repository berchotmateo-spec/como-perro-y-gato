# -*- coding: utf-8 -*-
"""
============================================================
  Arma la copia para la vista previa privada (Artifact)
------------------------------------------------------------
  La vista previa de claude.ai pone ella sola el <html>, el
  <head> y el <body>. Este script saca eso de index.html y deja
  el resto igual: título corto, fuentes, estilos y contenido.
  También saca lo que ahí no carga (un mapa embebido) y copia
  las carpetas de imágenes.

  Uso (copiarlo a la raíz del proyecto del cliente):
      python3 vista-previa.py <carpeta-destino> ["Título corto"] ["Texto de la banda"]

  - El título es el nombre del local, dos a cuatro palabras
    ("Augustus Heladería"). Si no se pasa, usa el <title> hasta
    el primer guion.
  - El tercer dato es opcional: agrega una banda fija arriba
    ("Propuesta · no es la página oficial").

  Después se publica <carpeta-destino>/index.html, siempre con
  la MISMA ruta, para que el link no cambie. Si hay fotos, se
  mandan todas en "files".

  No toca index.html. Lo que escribe NO es lo que va al dominio:
  para eso está publicar.py.
============================================================
"""
import os
import pathlib
import re
import shutil
import sys

RAIZ = pathlib.Path(__file__).resolve().parent
# PAGINA=panel.html python3 vista-previa.py <carpeta> "Título" → arma la vista previa del panel del local
html = (RAIZ / os.environ.get("PAGINA", "index.html")).read_text(encoding="utf-8")

estilos = "\n".join(re.findall(r"<style[^>]*>.*?</style>", html.split("<body")[0], re.S))
cuerpo = re.search(r"<body[^>]*>(.*)</body>", html, re.S)
if not estilos or not cuerpo:
    sys.exit("index.html tiene que tener <style> en el <head> y un <body>.")
cuerpo = cuerpo.group(1)
fuentes = re.findall(r'<link[^>]+href="(https://fonts\.googleapis\.com/css[^"]+)"', html)

titulo = sys.argv[2] if len(sys.argv) > 2 else re.split(r"\s+[—–|·-]\s+", re.search(r"<title>(.*?)</title>", html, re.S).group(1).strip())[0]
banda = sys.argv[3] if len(sys.argv) > 3 else ""

# Los mapas embebidos no cargan en la vista previa.
cuerpo = re.sub(r"\s*<iframe\b.*?</iframe>", "", cuerpo, flags=re.S)

partes = ["<title>%s</title>" % titulo]
partes += ['<link rel="stylesheet" href="%s">' % f.replace("&amp;", "&").replace("&", "&amp;") for f in fuentes]
partes.append(estilos)
if banda:
    partes.append('<style>.banda-previa{position:sticky;top:env(safe-area-inset-top,0px);z-index:99;margin:0;'
                  'padding:6px 16px;background:#111;color:#fff;font:600 12px/1.3 system-ui,sans-serif;text-align:center}</style>')
    cuerpo = '<p class="banda-previa">%s</p>\n%s' % (banda, cuerpo)
partes.append(cuerpo.strip())

destino = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "vista-previa")
destino.mkdir(parents=True, exist_ok=True)
salida = "\n".join(partes) + "\n"
(destino / "index.html").write_text(salida, encoding="utf-8")
for carpeta in ("fotos", "img", "assets"):
    if (RAIZ / carpeta).is_dir():
        shutil.copytree(RAIZ / carpeta, destino / carpeta, dirs_exist_ok=True)
print("Vista previa en %s (%d KB) · título: %s" % (destino / "index.html", len(salida.encode("utf-8")) // 1000, titulo))
