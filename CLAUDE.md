# Como Perro y Gato — sitio web

Memoria del proyecto para cualquier sesión de Claude que lo retome. Se trabaja
con la skill `metodo-web-negocio-local`. **Este archivo puede quedar en un repo
público:** nada de montos del abono, contraseñas ni datos privados del dueño.

## ⚠️ DUDA PRINCIPAL: ¿una o dos sucursales?

Mateo vio el local **en persona en Teodoro Bronzini e Ituzaingó** (Villa Primera).
Todo lo online (Google Maps, Instagram @comoperroygato__ y su tienda online) da
**San Martín 4090** (San Martín y Olazábal). **No sabemos** si Bronzini es una
segunda sucursal del mismo negocio o **otro negocio con el mismo nombre**.

- La web está armada para las dos: `SUCURSALES` con `mostrar: true` en ambas.
  Si es una sola, poner `mostrar: false` en la que no va y desaparecen la
  tarjeta, el "¿A qué local?" del pedido y su entrada en la ficha de Google
  (probado).
- Pistas a favor de "mismo negocio": la vidriera de la foto del frente tiene el
  cartel "Pago efectivo 10 % reintegro en alimentos", y la tienda online dice
  "10 % OFF en efectivo". Pista en contra (o de dos sucursales): el WhatsApp de
  la vidriera (223 598-2258) **no es** el teléfono de Google Maps (0223 565-5986).
- La foto del frente que mandó Mateo (18/11/2026) **no dice de qué dirección
  es**. Probablemente Bronzini (es la que vio en persona), sin confirmar.
- Mientras no se sepa, el nombre "Villa Primera" para la de Bronzini es mío
  (barrio que dijo Mateo), no del local.

## Qué es

Web de una página para **Como Perro y Gato**, pet shop y vivero de Mar del
Plata: alimento y accesorios para perros y gatos, y plantas.

- Estado: **demo de venta (fase 0), todavía no es cliente**. Armada el 18/11/2026.
- Sitio: sin dominio ni publicación todavía.
- Repo: `berchotmateo-spec/como-perro-y-gato`, rama de trabajo `claude/relaxed-planck-ci1kz7`.
- Vista previa (Artifact, privada): https://claude.ai/artifact/WfXrpRJ33jyFa9YkrRnuFP — se arma con `python3 vista-previa.py <carpeta> "Como Perro y Gato"` y se publica siempre en la misma ruta (desde otra conversación, pasando este link).

Marcas de demo (se sacan el día que el dueño compra):
`VISTA_PREVIA` (barra amarilla arriba), `DEMO = true` (aviso en el pie y debajo
del botón de pedido), `<meta name="robots" content="noindex">`, el WhatsApp de
Mateo en las dos sucursales (`WHATSAPP_DEMO`), y los chips punteados "A confirmar".

## Datos del local

| Dato | Valor en la web | Fuente | Estado |
|---|---|---|---|
| Nombre | Como Perro y Gato · "Pet Shop y Vivero" | cartel del frente, Instagram | ok |
| Sucursal 1 | San Martín 4090 (esquina Olazábal) | Google Maps, Instagram y su tienda online | a confirmar |
| Sucursal 2 | Teodoro Bronzini e Ituzaingó (Villa Primera) | Mateo, en persona | **duda principal** |
| Horario | Lunes a sábado 9 a 19 h; domingo cerrado (las dos) | bio de Instagram | a confirmar (chip) |
| Teléfono Google | 0223 565-5986 | Google Maps | **encontrado, no puesto** |
| WhatsApp vidriera | 223 598-2258 | foto del frente (vidriera); Mateo lo volvió a mostrar el 18/11/2026 | **encontrado, no puesto** (Mateo: "todavía no lo pongas") |
| WhatsApp en la web | 5492235337853 (el de Mateo) en las dos | demo | se cambia al cerrar |
| Envío a domicilio | Sí; "costo y zona a confirmar" | Google Maps ("Entrega a domicilio"); su tienda tiene zona de envíos | a confirmar |
| Medios de pago | Efectivo, transferencia, débito | **los puso Claude** | a confirmar |
| Promo | "Pagando en efectivo, 10 % de reintegro en alimentos" | cartel de la vidriera + "10 % OFF en efectivo" de su tienda | a confirmar (chip) |
| Marcas de alimento | Royal Canin, Eukanuba, Excellent, Agility, Estampa, Dogui, Bonelo | su tienda online | lista de referencia |
| Marca extra | Sileoni | carteles del frente (foto) | lista de referencia (solo el nombre, ver Diseño) |
| Google | 4,7 estrellas, 64 reseñas | Google Maps | **no se usa** (ni reseñas ni frases) |
| Instagram | @comoperroygato__ (~7.600 seguidores). Destacadas: "Dto Especial", "Vivero", "¡Promos!", perros, gatos, ubicación | Instagram | en el pie + "promos del momento" |
| Facebook | facebook.com/comoperroygatomdq | Facebook | en el pie |
| Tienda online | comoperroygato.com | Mateo | **no se enlaza ni se nombra** (ver venta) |
| Coordenadas | — | — | faltan (no hacen falta: "Cómo llegar" busca la dirección) |
| Colores | ver Diseño | medidos sobre la foto del frente | provisorios |
| Logo | `img/logo-cartel.webp`: el cartel "PET SHOP / como Perro y Gato" de la foto, enderezado y limpio | captura que mandó Mateo, 18/11/2026 | provisorio: pedir el archivo original |

## Productos: qué es real y qué es de referencia

Todo va **sin precio** (`MOSTRAR_PRECIOS = false`) y con la nota visible "Lista
de referencia". En `CATEGORIAS`, `visto: true` marca lo que tiene fuente:

- **Visto** (su tienda online o la vidriera de la foto): alimento para perro y
  para gato (tienda online; Sileoni perros/gatos urinary en el frente), snacks
  (Dentastix en la vidriera), sanitarios con tapa y casitas de colores (vidriera).
- **Clásicos del rubro, sin fuente**: correas y pecheras, juguetes, piedras
  sanitarias, comederos, camas, transportadoras, higiene, y **todo el vivero**
  (plantas de interior/exterior, macetas, tierra). Confirmar con el dueño.
- Las marcas no se asignan a perro o gato a propósito: en el pedido el cliente
  escribe para quién es.

## Lo que NO va en la web

Al sacar algo, buscarlo en **todo** el `index.html` (el JSON-LD lo arma el JS
con los mismos datos, así que se va solo).

- Precios (no hay ninguno confirmado). **Nunca** copiar los de su tienda online.
- Fotos de su tienda online, de stock o de IA.
- Reseñas, estrellas o frases de clientes de Google.
- Nombrar o criticar la tienda online ni a quien la hizo.
- Consejos sobre plantas tóxicas para mascotas o cualquier consejo veterinario,
  salvo que el dueño lo escriba o lo apruebe.
- `aggregateRating` en el JSON-LD.

## Diseño (decisiones, respetarlas)

- **Identidad sacada del frente real** (foto de Mateo, 18/11/2026), no de un
  rubro genérico: negro del cartel `#17151A`, **verde lima de la pared**
  `#7EBC06` (medido), fucsia de "PET SHOP" (`#C02A6B`, oscurecido para que se
  lea sobre blanco), amarillo de "Como Perro y Gato" `#F0DC4A` (solo sobre
  negro). Por el vivero: verde hoja `#2F5D14` y tierra `#8A4F2A` / `#EBDCC6`.
  Provisorios hasta ver el logo original.
- Letras: **Lilita One** (títulos, gordita como el cartel) + **Manrope** (texto)
  + **Caveat Brush** (solo la "y" y las volantas). No repetidas en el registro.
- Distinto de Zoo Center (violeta/naranja, Baloo 2 + Nunito) y de todas las del registro.
- **Logo** (18/11/2026, Mateo mostró el cartel como "lo que sería el logo"):
  `img/logo-cartel.webp` es el cartel de la foto **enderezado y limpio**, no
  redibujado: se corrigió la perspectiva (`herramientas/enderezar.py`) y se le
  sacaron el reflejo y la bruma dejando tres colores (`herramientas/limpiar-logo.py`).
  Va grande en la portada (es el `<h1>`, con su `alt`) y chico en el pie. La
  cabecera sigue con el nombre en letras (en chico el cartel no se lee). Si llega
  el original, reemplaza `img/logo-cartel.webp` con el mismo nombre.
- Debajo del logo dice solo "y Vivero" (el cartel ya dice PET SHOP).
- **Sileoni no se usa en el diseño**: el cartel blanco, marrón y rojo que sigue
  al logo es publicidad del proveedor, no la marca del local. Sileoni aparece
  solo como nombre en la lista de marcas.
- La ilustración de la portada (maceta, gato negro con collar, huellas) es propia.
- Cada forma, un solo trabajo (está arriba del CSS): punteado = "A confirmar";
  rayado diagonal = "foto pendiente"; fucsia = lo que suma al pedido; verde
  oscuro = WhatsApp; lima = fondos, nunca texto sobre blanco.
- **Guiño:** "pisadas que brotan". Al pie de la portada hay una franja de
  tierra; unas huellas la cruzan una por una y de cada una brota una plantita
  (pet shop + vivero). Corre una sola vez al cargar, el estado final queda
  visible, no come clics y con "reducir movimiento" aparece quieto. En el
  celular se dibujan la mitad. Posiciones en `PISADAS`.
- Fondo claro, celular primero, probado a 1366, 390 y 320 px.
- Crédito al pie: "Diseñado por connectHUB" con botón a @connect.hub.consultora.

## El pedido por WhatsApp

- Catálogo con − y + por producto y por marca. En "Tu pedido" cada producto
  tiene un campo libre "marca, kilos o presentación" (con un ejemplo propio en
  `ej`), y "Escribir otro producto" agrega una línea libre con su cantidad. El
  botón del vivero suma una línea "Planta: …".
- Datos: local (si hay más de uno visible), retiro o envío (dirección y entre
  calles solo con envío), nombre, pago (opcional), comentario.
- El mensaje termina con **"¿Me confirmás precio y disponibilidad?"**.
- Se guarda en el celular (`cpyg-pedido-v1`), con − y + compartidos entre el
  catálogo y el pedido. Barra fija abajo en el celular; el botón verde no la tapa.
- Abierto/cerrado con la hora de Argentina, desde `HORARIO` (por día).

Mensaje de prueba real (18/11/2026):

```
*Pedido web · Como Perro y Gato*
Local: Villa Primera (Teodoro Bronzini e Ituzaingó)

*Productos*
• 2 × Alimento balanceado para perro: Adulto raza grande, 15 kg
• 1 × Alimento Royal Canin: Gato castrado, 3 kg
• 1 × Pipeta para perro de 10 kg
• 1 × Planta: potus

*Entrega:* Envío a domicilio (costo a confirmar)
*Dirección:* Ituzaingó 5000
*Entre calles:* Bronzini y Garay
*Nombre:* Prueba Mateo
*Pago:* Efectivo
*Comentario:* Si no hay Royal, otra parecida

¿Me confirmás precio y disponibilidad?
```

## PENDIENTES PARA EL DUEÑO

- [ ] **¿Bronzini e Ituzaingó es sucursal de ustedes?** → `SUCURSALES[1].mostrar`.
- [ ] Si son dos: **WhatsApp de cada local** (¿el 223 598-2258 de la vidriera es de cuál? ¿el 0223 565-5986 de Google?) → `whatsapp` de cada sucursal.
- [ ] **Horario** de cada local (hoy lunes a sábado 9 a 19, de la bio de Instagram). ¿Cortan al mediodía? → `HORARIO` o `horario` por sucursal; `confirmado: true`.
- [ ] **¿En qué local está el vivero?** → `VIVERO_DONDE`.
- [ ] **Envío**: zona, costo, mínimo y días → `ENVIO`.
- [ ] **Medios de pago** (los puse yo: efectivo, transferencia, débito) → `PAGOS`.
- [ ] **10 % en efectivo**: ¿sigue? ¿solo alimentos? ¿descuento o reintegro? → `PROMOS`.
- [ ] **Qué venden de verdad** en cada categoría y en el vivero → `CATEGORIAS` (sacar lo que no tienen).
- [ ] **Marcas** que trabajan (hoy: las de su tienda + Sileoni del cartel) → `MARCAS`.
- [ ] **Fotos reales**: frente de cada local, adentro, y el vivero → `SUCURSALES[].foto` y la sección vivero. La foto del frente de Mateo está en `referencia/` (falta saber de qué local es).
- [ ] **Logo original** (archivo): hoy es el cartel sacado de una foto → `img/logo-cartel.webp`.
- [ ] ¿Quieren **precios** en la web? Solo si los pasa el dueño, con fecha.

## PROVISORIO

| Qué | Por qué hay duda | Desde |
|---|---|---|
| Sucursal de Bronzini | Puede ser otro negocio | 18/11/2026 |
| Horario de las dos | Sale de la bio de Instagram | 18/11/2026 |
| Medios de pago | Los puso Claude (el formulario los necesita) | 18/11/2026 |
| Productos sin `visto` y todo el vivero | Clásicos del rubro | 18/11/2026 |
| Colores | Medidos sobre una foto (luz del día, cartel algo gastado) | 18/11/2026 |

## Para la venta (no va en la web)

**Pendiente de definir hasta saber lo de Bronzini.**

- **Si es el mismo negocio que San Martín 4090:** ya tienen tienda online
  (comoperroygato.com). No competir con ella ni hablar mal: esta web la suma.
  El ángulo: pedido directo por WhatsApp sin carrito con precios que mantener
  (sirve aunque cambien los precios todas las semanas); **las dos sucursales y
  el vivero en un solo lugar**; abierto/cerrado en vivo; aparecer en Google con
  dominio propio; y "los cambios del mes los hago yo".
- **Si Bronzini es otro negocio:** el ángulo es "local sin web": hoy todo pasa
  por Instagram y el mostrador; la web les da Google, el pedido por WhatsApp y
  el vivero a la vista.
- Dato para el video: 4,7 estrellas con 64 reseñas en Google (solo como dato
  de venta, nunca en la web).
- Idea para ofrecer: una sección "plantas que conviven con perros y gatos",
  **solo** si el dueño la escribe o la revisa.

## Fotos

- Con foto: 0. Todo funciona sin fotos: los huecos dicen "Foto del local pendiente" / "Foto del vivero pendiente".
- `referencia/cartel-captura-whatsapp.webp`: la misma foto, más de cerca (de una captura de Mateo, recortada para que no se vean su navegador ni el chat). De ahí sale el logo.
- `referencia/frente-foto-mateo.webp`: la foto del frente que mandó Mateo (18/11/2026). Sirvió para medir los colores. **No está publicada**: no sabemos de qué local es, y muestra el WhatsApp de la vidriera. Cuando se sepa, puede ir como `foto` de esa sucursal.
- Cuando lleguen: a `fotos-originales/` → `python3 hacer-fotos.py` → `img/…webp` y `foto:` de la sucursal.

## Estado técnico

- [ ] Sacar las marcas de demo (ver arriba) al cerrar.
- [ ] GitHub Pages (`python3 publicar.py`; mientras sea demo el `noindex` ya va en el `index.html`), dominio, Search Console, Perfil de Empresa.
- [ ] QR.

## Cómo se trabaja acá

1. Los datos están arriba del `<script>` de `index.html`: `SUCURSALES`, `HORARIO`, `ENVIO`, `PAGOS`, `PROMOS`, `CATEGORIAS`, `MARCAS`, `VIVERO_DONDE`.
2. Verificar: `node verificar.mjs index.html` (de la skill) a 1366, 390 y 320 px, y un pedido de punta a punta leyendo el mensaje.
3. Commit + push → `python3 vista-previa.py <carpeta>` → publicar el Artifact en la misma ruta.

## Registro de cambios

Una línea por pedido, la más nueva arriba.

- 18/11/2026 — Mateo mandó el cartel de cerca ("lo que sería el logo") → logo enderezado y limpio en la portada y el pie (`img/logo-cartel.webp`); debajo, solo "y Vivero". Sileoni no se usa en el diseño (es del proveedor). El WhatsApp de la vidriera sigue sin ponerse, como pidió.
- 18/11/2026 — Armado inicial de la demo de venta con los datos que investigó Mateo (dos direcciones, horario de Instagram, marcas de su tienda online) y la foto del frente (colores, Sileoni, cartel del 10 %). Pedido por WhatsApp con presentación libre, vivero, locales y crédito connectHUB.
