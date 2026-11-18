# Endereza el cartel "PET SHOP / como Perro y Gato" de la foto del frente.
# Uso: python3 herramientas/enderezar.py referencia/cartel-captura-whatsapp.webp /tmp/logo-recto.png
#      python3 herramientas/limpiar-logo.py /tmp/logo-recto.png /tmp/logo-limpio.png  (y recortar a img/logo-cartel.webp)
import sys
from PIL import Image, ImageEnhance
import numpy as np
im = Image.open(sys.argv[1]).convert("RGB")
src = [(80,120),(446,54),(410,448),(64,466)]   # esquinas del cartel negro en referencia/cartel-captura-whatsapp.webp (arriba-izq, arriba-der, abajo-der, abajo-izq)
W, H = 620, 600
dst = [(0,0),(W,0),(W,H),(0,H)]
def coeffs(pa, pb):
    A=[];B=[]
    for (x,y),(X,Y) in zip(pa,pb):
        A.append([X,Y,1,0,0,0,-x*X,-x*Y]); A.append([0,0,0,X,Y,1,-y*X,-y*Y]); B+= [x,y]
    return np.linalg.solve(np.array(A,float), np.array(B,float)).tolist()
out = im.transform((W,H), Image.PERSPECTIVE, coeffs(src,dst), Image.BICUBIC)
out.save(sys.argv[2])
