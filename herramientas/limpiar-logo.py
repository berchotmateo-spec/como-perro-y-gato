import sys
import numpy as np
from PIL import Image, ImageFilter
img = Image.open(sys.argv[1]).convert("RGB").resize((1240,1200), Image.LANCZOS)
a = np.asarray(img).astype(float); r,g,b = a[...,0],a[...,1],a[...,2]
fondo = np.asarray(Image.fromarray(a.min(axis=2).astype(np.uint8)).filter(ImageFilter.MinFilter(41)).filter(ImageFilter.GaussianBlur(30))).astype(float)
rosa = np.clip(((r - g) - 22) / 20, 0, 1)
amar = np.clip(((g - fondo) - 45) / 25, 0, 1) * np.clip(((r+g)/2 - b - 12) / 20, 0, 1)
def limpiar(m, n):
    im = Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.MedianFilter(n))
    im = im.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3))   # cierra agujeritos
    return np.asarray(im.filter(ImageFilter.GaussianBlur(1.2))).astype(float)/255
rosa, amar = limpiar(rosa, 7), limpiar(amar, 5)
amar = amar * (1 - rosa)
NEG = np.array([0x17,0x15,0x1A]); ROSA = np.array([0xD8,0x3E,0x87]); AMA = np.array([0xF2,0xDC,0x3C])
out = NEG*(1-rosa-amar).clip(0,1)[...,None] + ROSA*rosa[...,None] + AMA*amar[...,None]
Image.fromarray(out.clip(0,255).astype(np.uint8)).resize((620,600), Image.LANCZOS).save(sys.argv[2])
