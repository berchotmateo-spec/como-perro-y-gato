# Como Perro y Gato — sitio web

Memoria del proyecto para cualquier sesión de Claude que lo retome. Se trabaja
con la skill `metodo-web-negocio-local`. **Este archivo puede quedar en un repo
público:** nada de montos del abono, contraseñas ni datos privados del dueño.

## ⚠️ HAY OTRO PET SHOP CON EL MISMO NOMBRE: no mezclar datos

Este proyecto es el pet shop **Como Perro y Gato de Teodoro Bronzini 614**
(cerca de Ituzaingó, Villa Primera), el que Mateo vio en persona. **Un solo local y sin
vivero.**

Hay **otro negocio** que se llama igual en **San Martín 4090** (San Martín y
Olazábal), **con vivero**. Mateo lo confirmó el 18/11/2026: "el vivero y la
sucursal de San Martín no son de este pet shop". Todo esto es **del otro** y
**no va en la web**:

- La dirección San Martín 4090 y el teléfono de Google Maps 0223 565-5986.
- La ficha de Google (4,7 estrellas, 64 reseñas, "Entrega a domicilio").
- El Instagram @comoperroygato__ (tiene la destacada "Vivero" y la ubicación
  de San Martín), con su horario de la bio (lunes a sábado 9 a 19).
- El Facebook facebook.com/comoperroygatomdq (Mateo lo encontró junto con lo
  anterior: se trata como del otro hasta que el dueño diga que es suyo).
- La tienda online comoperroygato.com, sus marcas y su "10 % OFF en efectivo".

Al buscar algo nuevo online de "Como Perro y Gato", **revisar que sea de Bronzini**.

## Qué es

Web de una página para **Como Perro y Gato**, pet shop en Villa Primera, Mar
del Plata: alimento y accesorios para perros y gatos.

- Estado: **demo de venta (fase 0), todavía no es cliente**. Armada el 18/11/2026.
- Sitio: sin dominio ni publicación todavía.
- Repo: `berchotmateo-spec/como-perro-y-gato`, rama de trabajo `claude/relaxed-planck-ci1kz7`.
- Vista previa (Artifact): https://claude.ai/artifact/WfXrpRJ33jyFa9YkrRnuFP — se arma con `python3 vista-previa.py <carpeta> "Como Perro y Gato"` y se publica siempre en la misma ruta, con `img/logo-cartel.webp` en `files` (desde otra conversación, pasando este link). Hoy está compartida como "cualquiera con el link".

Marcas de demo (se sacan el día que el dueño compra):
`VISTA_PREVIA` (barra amarilla arriba), `DEMO = true` (aviso en el pie y debajo
del botón de pedido), `<meta name="robots" content="noindex">`, el WhatsApp de
Mateo (`WHATSAPP_DEMO`), y los chips punteados "A confirmar".

## Datos del local

| Dato | Valor en la web | Fuente | Estado |
|---|---|---|---|
| Nombre | Como Perro y Gato · "Pet Shop" | cartel del frente | ok |
| Dirección | Teodoro Bronzini 614 · "Cerca de Ituzaingó" (Villa Primera) | Mateo, 18/11/2026 | ok (sin chip) |
| Horario | **"Horario a confirmar"** (`HORARIO = null`: no se calcula abierto/cerrado) | — | falta |
| WhatsApp vidriera | 223 598-2258 | foto del frente | **encontrado, no puesto** (Mateo: "todavía no lo pongas") |
| WhatsApp en la web | 5492235337853 (el de Mateo) | demo | se cambia al cerrar |
| Envío a domicilio | Opción en el pedido, "costo y zona a confirmar" | lo pidió Mateo para la demo | **no sabemos si hacen envíos**; `ENVIO.hay = false` lo saca |
| Medios de pago | Efectivo, transferencia, débito | **los puso Claude** | a confirmar |
| Promo | "Pagando en efectivo, 10 % de reintegro en alimentos" | cartel de la vidriera de este local | a confirmar (chip) |
| Marcas | Sileoni, Royal Canin, Bonelo | carteles del frente, cartel de la vidriera y pizarrón | lista de referencia |
| Redes | ninguna (`LOCAL.instagram` y `facebook` vacíos) | las encontradas son del otro | preguntar si tienen |
| Logo | `img/logo-cartel.webp`: el cartel del frente, enderezado y limpio | captura que mandó Mateo, 18/11/2026 | provisorio: pedir el archivo original |
| Coordenadas | — | — | no hacen falta: "Cómo llegar" busca la esquina |
| Colores | ver Diseño | medidos sobre la foto del frente | provisorios |

## Productos: qué es real y qué es de referencia

Todo va **sin precio** (`MOSTRAR_PRECIOS = false`) y con la nota visible "Lista
de referencia". Tres categorías: Perros, Gatos, Accesorios. En `CATEGORIAS`,
`visto: true` marca lo que se ve en la vidriera de la foto:

- **Visto:** alimento para perro y para gato (Sileoni perros y gatos urinary,
  Royal Canin, Bonelo), snacks (Dentastix), sanitarios con tapa, casitas de colores.
- **Clásicos del rubro, sin fuente:** correas y pecheras, juguetes, piedras
  sanitarias, comederos, camas, transportadoras, higiene. Confirmar con el dueño.
- Las marcas no se asignan a perro o gato a propósito: en el pedido el cliente
  escribe para quién es.

## Lo que NO va en la web

Al sacar algo, buscarlo en **todo** el `index.html` (el JSON-LD lo arma el JS
con los mismos datos, así que se va solo).

- **Nada del otro Como Perro y Gato** (ver arriba): ni vivero, ni plantas, ni
  San Martín, ni sus redes, horario, reseñas, marcas o tienda.
- Precios (no hay ninguno confirmado).
- Fotos de stock o de IA. Tampoco la gráfica de Sileoni (es del proveedor).
- Consejos veterinarios.
- `aggregateRating` en el JSON-LD.

## Diseño (decisiones, respetarlas)

- **Identidad sacada del frente real** (foto de Mateo): negro del cartel
  `#17151A`, **verde lima de la pared** `#7EBC06` (medido), fucsia de "PET SHOP"
  (`#C02A6B`, oscurecido para que se lea sobre blanco), amarillo de "Como Perro
  y Gato" `#F0DC4A` (solo sobre negro). Provisorios hasta ver el logo original.
- Letras: **Lilita One** (títulos) + **Manrope** (texto) + **Caveat Brush**
  (la "y" de la cabecera y las volantas). No repetidas en el registro.
- **Logo:** `img/logo-cartel.webp` es el cartel de la foto **enderezado y
  limpio**, no redibujado (`herramientas/enderezar.py` corrige la perspectiva;
  `herramientas/limpiar-logo.py` saca el reflejo y deja los tres colores). Va
  grande en la portada (es el `<h1>`, con su `alt`) y chico en el pie. La
  cabecera lleva el nombre en letras (en chico el cartel no se lee). Si llega
  el original, reemplaza `img/logo-cartel.webp` con el mismo nombre.
- **Sileoni no se usa en el diseño:** el cartel que sigue al logo es
  publicidad del proveedor. Solo aparece como nombre en la lista de marcas.
- Ilustración propia en la portada: círculo lima, gato negro con collar
  fucsia, comedero fucsia con alimento y huellas de perro que llegan.
- Cada forma, un solo trabajo (está arriba del CSS): punteado = "A confirmar";
  rayado diagonal = "foto pendiente"; fucsia = lo que suma al pedido; verde
  oscuro = WhatsApp; lima = fondos, nunca texto sobre blanco.
- **Guiño: "como perro y gato".** Al pie de la portada, huellas de perro
  (negras) entran por la izquierda y huellas de gato (fucsia, más chicas y
  redondas) por la derecha, pisando de a una y alternadas, y se cruzan en el
  medio. Una sola vez al cargar, el estado final queda visible, no come clics,
  con "reducir movimiento" aparece quieto; en el celular, la mitad. Posiciones
  en `PERRO` y `GATO` (paso "guiño").
  (Hasta el 18/11 el guiño eran "pisadas que brotan" por el vivero: se cambió
  al saber que el vivero es del otro local.)
- Fondo claro, celular primero, probado a 1366, 390 y 320 px.
- Crédito al pie: "Diseñado por connectHUB" con botón a @connect.hub.consultora.

## El pedido por WhatsApp

- Catálogo con − y + por producto y por marca. En "Tu pedido" cada producto
  tiene un campo libre "marca, kilos o presentación" (con un ejemplo propio en
  `ej`), y "Escribir otro producto" agrega una línea libre con su cantidad.
- Datos: retiro o envío (dirección y entre calles solo con envío), nombre,
  pago (opcional), comentario. Si algún día hay más de un local en
  `SUCURSALES`, aparece "¿A qué local?" y el mensaje dice cuál (probado).
- El mensaje termina con **"¿Me confirmás precio y disponibilidad?"**.
- Se guarda en el celular (`cpyg-pedido-v1`). Barra fija abajo en el celular;
  el botón verde no la tapa.
- Abierto/cerrado con la hora de Argentina, desde `HORARIO` (por día, con
  turnos partidos). Hoy `null` → "Horario a confirmar" y la cabecera no muestra
  estado. Probado con un horario de prueba cortado al mediodía.

Mensaje de prueba real (18/11/2026):

```
*Pedido web · Como Perro y Gato*

*Productos*
• 2 × Alimento balanceado para perro: Adulto raza grande, 15 kg
• 1 × Alimento Royal Canin: Gato castrado, 3 kg
• 1 × Pipeta para perro de 10 kg
• 1 × Rascador para gato

*Entrega:* Envío a domicilio (costo a confirmar)
*Dirección:* Ituzaingó 5000
*Entre calles:* Bronzini y Garay
*Nombre:* Prueba Mateo
*Pago:* Efectivo
*Comentario:* Si no hay Royal, otra parecida

¿Me confirmás precio y disponibilidad?
```

## Panel del local (facturación y control de stock)

Pedido de Mateo (18/11/2026): "que tenga sistema de facturación y control de stock".
Es `panel.html`, **privado del local** y separado de la página pública (no hay
link desde la web; `noindex`). Vista previa aparte: https://claude.ai/artifact/Ks192RKDtiVX26yDHCmGeS
(privada, con permiso `downloads` para la planilla). Se arma con
`PAGINA=panel.html python3 vista-previa.py <carpeta> "Panel Como Perro y Gato"`
y se publica con `capabilities: {downloads: true}`.

- **Vender (caja):** buscador, tocar para sumar, − y +, descuento %, medio de
  pago (efectivo, transferencia, débito, crédito), cliente opcional, **Cobrar**.
  No deja vender más de lo que hay. Al cobrar descuenta el stock y abre el comprobante.
- **Comprobante:** numerado (N° 0001…), con los datos del local, y la leyenda
  **"Documento no válido como factura"**. Se manda por WhatsApp (texto) o se imprime.
  Una venta se puede **anular** (dos toques) y devuelve el stock.
- **Stock:** lista con "Sin stock" / "Quedan N" según el mínimo de cada producto,
  filtros, **Ingreso** de mercadería (con nota: proveedor, remito) y **Corregir**
  por conteo. Todo queda en "Últimos movimientos". Aviso de stock bajo en Vender
  y globito en el menú. El stock de un producto existente solo cambia por
  ingreso, corrección, venta o anulación (queda registrado).
- **Ventas:** cierre de caja por día (total, cantidad, productos, total por medio
  de pago), lista de comprobantes y **Planilla del mes** (CSV con `;`, para Excel
  y el contador).
- **Ajustes:** datos del comprobante (nombre, dirección, CUIT, condición IVA,
  texto al pie), la tarjeta de factura electrónica y la **Prueba**: "Cargar
  productos de ejemplo" (8 productos genéricos, sin marcas, precios inventados,
  marcados "ejemplo") y "Borrar todo" (dos toques).

**Factura electrónica (ARCA): NO está conectada, y a propósito.** El panel no
inventa CAE ni imita una factura. Para facturar de verdad hace falta: CUIT y
condición (monotributo → factura C), un punto de venta para web service, el
certificado digital (lo saca el dueño con su clave fiscal) y **un servidor** que
firme (el certificado nunca va en el HTML). Caminos: un servicio de facturación
con API (pago mensual) o una función propia en Supabase. Hasta entonces, el
dueño puede seguir facturando en "Comprobantes en línea" de ARCA con los datos
del comprobante.

**Dónde se guardan los datos:** hoy, en el navegador de ese aparato
(`localStorage`, clave `cpyg-panel-v1`). Sirve para la demo, pero **no** para
usarlo de verdad: si el celular se borra, se pierde, y la compu y el celular no
ven lo mismo. Cuando compre: Supabase como en `zoo-center` (tablas productos,
ventas y movimientos con RLS sin políticas, solo funciones, y una clave del local;
la venta descuenta el stock en la base, en una sola operación). Todo el acceso a
los datos está en `cargar()` / `guardar()` / `mover()` para cambiarlo en un lugar.

Probado (18/11/2026) en celular y compu con Playwright: cargar ejemplo, vender
sin pasarse del stock, cobrar sin medio de pago (no deja), descuento, comprobante,
ingreso, corrección, filtros, producto nuevo, cierre del día, planilla CSV,
anular (devuelve stock), recargar (sigue todo), sin errores ni desborde a 1366,
390 y 320 px. La impresión y la descarga dentro de la vista previa no se pudieron
probar desde acá.

## PENDIENTES PARA EL DUEÑO

- [ ] **Horario** (días y horas; ¿cortan al mediodía?) → `HORARIO` (hay un ejemplo comentado arriba).
- [ ] **WhatsApp para pedidos** (¿el 223 598-2258 de la vidriera?) → `whatsapp` cuando Mateo diga.
- [ ] **¿Hacen envíos?** Zona, costo, mínimo y días → `ENVIO` (o `hay: false`).
- [ ] **Medios de pago** (los puse yo: efectivo, transferencia, débito) → `PAGOS`.
- [ ] **10 % en efectivo**: ¿sigue? ¿solo alimentos? → `PROMOS`.
- [ ] **Qué venden de verdad** y qué **marcas** trabajan → `CATEGORIAS` y `MARCAS`.
- [ ] **¿Tienen Instagram o Facebook propios?** → `LOCAL.instagram` / `facebook`.
- [ ] **Fotos reales**: frente y adentro → `SUCURSALES[0].foto`. La foto del frente de Mateo podría ir, pero muestra el WhatsApp de la vidriera: esperar a que se pueda publicar ese número.
- [ ] **Logo original** (archivo).
- [ ] ¿Quieren **precios** en la web? Solo si los pasa el dueño, con fecha.
- [ ] **Panel:** ¿necesita **factura electrónica** de verdad (ARCA) o le alcanza el comprobante? Si sí: CUIT, condición (¿monotributo?) y si ya tiene punto de venta.
- [ ] **Panel:** ¿quién lo usa y en qué aparatos (celular del mostrador, compu)? Define si hace falta Supabase desde el día uno (sí, si son dos o más aparatos).
- [ ] **Panel:** su lista de productos con precio y stock (puede ser una planilla; se carga de una vez).

## PROVISORIO

| Qué | Por qué hay duda | Desde |
|---|---|---|
| Opción de envío a domicilio | No sabemos si hacen envíos | 18/11/2026 |
| Medios de pago | Los puso Claude (el formulario los necesita) | 18/11/2026 |
| Productos sin `visto` | Clásicos del rubro | 18/11/2026 |
| Colores y logo | Sacados de una foto (luz del día, cartel algo gastado) | 18/11/2026 |
| Nombre "Villa Primera" en la tarjeta del local | Es el barrio que dijo Mateo, no un nombre del local | 18/11/2026 |

## Para la venta (no va en la web)

- **Local sin web**, y encima **con un homónimo**: quien busca "Como Perro y
  Gato Mar del Plata" en Google hoy encuentra al de San Martín (ficha, Instagram
  y tienda online). Una web propia con dominio y su ficha de Google es la forma
  de que lo encuentren **a ellos** y no al otro. Decirlo sin nombrar ni criticar
  al otro negocio.
- Pedido directo por WhatsApp sin precios que mantener (sirve aunque cambien
  los precios todas las semanas), abierto/cerrado en vivo, "Cómo llegar", y
  "los cambios del mes los hago yo".

## Fotos

- Con foto: 0. Todo funciona sin fotos: el hueco del local dice "Foto del local pendiente".
- `referencia/frente-foto-mateo.webp`: la foto del frente (18/11/2026). Sirvió para medir los colores. No publicada (muestra el WhatsApp de la vidriera).
- `referencia/cartel-captura-whatsapp.webp`: la misma foto, más de cerca (de una captura de Mateo, recortada para que no se vean su navegador ni el chat). De ahí sale el logo.
- Cuando lleguen: a `fotos-originales/` → `python3 hacer-fotos.py` → `img/…webp` y `foto:` del local.

## Estado técnico

- [ ] Sacar las marcas de demo (ver arriba) al cerrar.
- [ ] GitHub Pages (`python3 publicar.py`; mientras sea demo el `noindex` ya va en el `index.html`), dominio, Search Console, Perfil de Empresa (ojo con el homónimo: que la ficha quede con Teodoro Bronzini 614).
- [ ] QR.
- [ ] Panel: pasar los datos a Supabase (ver "Panel del local") y, si lo contrata, conectar la factura electrónica.

## Cómo se trabaja acá

1. Los datos están arriba del `<script>` de `index.html`: `LOCAL`, `SUCURSALES`, `HORARIO`, `ENVIO`, `PAGOS`, `PROMOS`, `CATEGORIAS`, `MARCAS`.
2. Verificar: `node verificar.mjs index.html` (de la skill) a 1366, 390 y 320 px, y un pedido de punta a punta leyendo el mensaje.
3. Commit + push → `python3 vista-previa.py <carpeta> "Como Perro y Gato"` → publicar el Artifact en la misma ruta.
4. Panel: `PAGINA=panel.html python3 vista-previa.py <otra-carpeta> "Panel Como Perro y Gato"` → publicar en su ruta, con `capabilities: {downloads: true}`.

## Registro de cambios

Una línea por pedido, la más nueva arriba.

- 18/11/2026 — Mateo: "que tenga sistema de facturación y control de stock" → `panel.html`, panel privado del local: caja, comprobante no fiscal numerado (WhatsApp / imprimir / anular), stock con ingresos, correcciones, mínimos y movimientos, cierre del día y planilla del mes. Factura electrónica ARCA explicada y sin conectar (necesita CUIT, certificado y servidor). Datos en el navegador para la demo; Supabase al vender.
- 18/11/2026 — Mateo: "Teodoro Bronzini 614 es la altura del local" → dirección, "Cómo llegar" y ficha de Google con el 614; abajo, "Cerca de Ituzaingó". Ya no lleva chip "A confirmar" (el horario sigue a confirmar).
- 18/11/2026 — Mateo: "quitá el vivero y la sucursal de San Martín, no son de este pet shop" → un solo local (Bronzini e Ituzaingó), sin vivero (sección, categoría y botón). Se sacó también todo lo que venía de ese otro negocio: Instagram, Facebook, horario de la bio (queda "Horario a confirmar"), marcas de su tienda (quedan las del frente: Sileoni, Royal Canin, Bonelo). Guiño nuevo "como perro y gato" (huellas que se cruzan) y comedero en lugar de la maceta.
- 18/11/2026 — Mateo mandó el cartel de cerca ("lo que sería el logo") → logo enderezado y limpio en la portada y el pie (`img/logo-cartel.webp`). Sileoni no se usa en el diseño (es del proveedor). El WhatsApp de la vidriera sigue sin ponerse, como pidió.
- 18/11/2026 — Armado inicial de la demo de venta con los datos que investigó Mateo y la foto del frente. Pedido por WhatsApp con presentación libre, locales y crédito connectHUB.
