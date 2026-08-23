# PFO1 · Landing de portafolio personal

**Sebastián Fernández** · Desarrollo de Sistemas Web (Front End) · 2° A
Tecnicatura en Desarrollo de Software · 2do cuatrimestre 2026

Landing de una sola página construida con **HTML5 semántico y CSS3 propio**, sin frameworks
ni librerías externas. Presenta mi perfil profesional, mis habilidades, dos proyectos
publicados, una sección personal y una vía de contacto.

- 🌐 **Sitio publicado:** https://pfo1-dsw-front.vercel.app
- 👤 **Perfil de GitHub:** https://github.com/Fernandez-Sebastian
- 💼 **LinkedIn:** https://www.linkedin.com/in/sebastian-fernandez-aa2b572a1/

---

## Contenido de la landing

| Sección | Qué contiene |
|---|---|
| Presentación | Nombre y apellido, rol actual, bio y datos de trayectoria |
| Habilidades | Cinco tarjetas agrupadas por área: backend, front end, herramientas, equipo y exploración |
| Proyectos | HuFly Fishing (en línea) y Resultado Final (prode del Mundial 2026, +8.000 usuarios) |
| Personal | Fichas de datos con intereses: videojuegos, anime y fútbol |
| Contacto | Formulario con `label` en todos los campos y datos de contacto directo |

---

## Estructura del proyecto

```
PFO1-DSW-FRONT/
├── index.html          # Estructura semántica completa
├── css/
│   └── styles.css      # Estilos propios, organizados en 13 bloques comentados
├── img/
│   ├── perfil.jpg      # Foto de perfil (recortada y optimizada)
│   └── monumental.jpg  # Foto de la sección personal
└── README.md
```

---

## Requisitos técnicos de la consigna

| Requisito | Dónde se cumple |
|---|---|
| HTML semántico (`header`, `nav`, `main`, `footer`) | `index.html`, más `section`, `article`, `aside`, `figure` |
| CSS propio | `css/styles.css`, escrito íntegramente para esta entrega |
| Google Fonts | Space Grotesk, Inter y JetBrains Mono, vinculadas con `preconnect` |
| Flexbox o Grid | Ambos, combinados (ver justificación abajo) |
| Diseño responsive | Unidades relativas, `clamp()`, `auto-fit` y dos breakpoints |
| Transición o animación | 3 animaciones `@keyframes` propias y transiciones en toda la interfaz |
| Imágenes con `alt` | Las dos imágenes tienen texto alternativo descriptivo |
| Formulario con `label` | Los tres campos tienen `label` asociado por `for` |
| Enlace visible a GitHub | En la cabecera, en la presentación, en contacto y en el pie |

---

## Decisiones que tomé

### Por qué combiné Grid y Flexbox

No son intercambiables y las usé para cosas distintas:

- **Grid gobierna la distribución bidimensional**: la presentación a dos columnas, las
  grillas de habilidades, proyectos y fichas personales, y el bloque de contacto. Usé
  `repeat(auto-fit, minmax(...))` para que las columnas se reacomoden solas según el ancho
  disponible, sin escribir un breakpoint por cada caso.
- **Flexbox gobierna el contenido en una sola dirección**: la barra de navegación, el
  interior de cada tarjeta, las listas de habilidades y las filas de botones y etiquetas.

La regla que seguí: si tenía que alinear elementos en filas *y* columnas a la vez, Grid;
si era una fila o una columna de elementos de tamaño variable, Flexbox.

### Por qué CSS propio y no Bootstrap

En mi trabajo normalmente resuelvo el estilado con Bootstrap o directamente con React, así
que este proyecto fue deliberadamente el ejercicio contrario: escribir el CSS a mano para
entender qué hacen los frameworks por debajo. La grilla, el sistema de espaciado y los
componentes están construidos desde cero.

### Variables CSS

Toda la paleta, la tipografía y el espaciado están declarados como custom properties en
`:root`. Cambiar el color de acento del sitio completo es modificar una línea. Esto también
deja el archivo preparado para agregar un tema claro más adelante.

### Escala tipográfica fluida

En lugar de fijar tamaños por breakpoint, los títulos usan `clamp()` con un mínimo, un valor
proporcional al viewport y un máximo. El texto crece de forma continua entre un teléfono y un
monitor, sin saltos bruscos.

### Identidad visual

Fondo azul-tinta profundo (`#11151C`) con rojo (`#E03A48`) como único color de acento. El
rojo funciona como hilo conductor de la sección personal —River Plate, Dragon Ball— sin
necesidad de usar logos ni personajes de terceros: **no incluí ninguna marca, escudo ni
personaje con derechos de autor**, la estética se construye únicamente con tipografía, color
y formas propias en CSS.

El elemento que se repite como firma visual son los **marcos con esquinas recortadas** sobre
las fotos, hechos con `::before` y `::after`, que remiten a la interfaz de un videojuego sin
copiar nada.

### Accesibilidad

Más allá de lo que pedía la consigna, agregué: enlace de salto al contenido principal,
`aria-label` en las regiones de navegación y contacto, `aria-hidden` en los íconos
decorativos, foco visible con `:focus-visible`, contraste alto entre texto y fondo, y
soporte de `prefers-reduced-motion` para desactivar las animaciones si el sistema
operativo lo pide.

### Sobre el formulario

La consigna es de HTML y CSS, así que el formulario no tiene backend. Está construido con
la semántica correcta y validación nativa del navegador (`required`, `type="email"`), y en
la propia interfaz aclaro que para una respuesta hay que escribir al mail o a LinkedIn.
Preferí decirlo antes que simular un envío que no ocurre.

---

## Declaración de uso de IA

> Requisito transversal de la cátedra.

**Herramienta utilizada:** Claude (Anthropic), interfaz web.
**Plan:** Pro (pago).

**Experiencia previa:** La vengo usando hace menos de un año, principalmente en el trabajo
para reescribir y mejorar respuestas de atención en Zendesk. La primera IA generativa que
había usado fue Lovable.

### Cómo trabajé

Trabajé en una conversación por etapas en la que la herramienta me fue preguntando la información de cada apartado y yo
fui respondiendo y decidiendo. El contenido —quién soy, qué sé hacer, qué proyectos tengo,
qué me representa— es enteramente mío; la herramienta no lo inventó.

El orden fue este:

1. Definí la dirección del proyecto: temática profesional con guiños gamer y otaku
   sutiles, y una paleta acorde a un portfolio.
2. Aporté los datos de cada sección en tandas, corrigiendo lo que venía mal interpretado.
3. Discutí y aprobé el enfoque de cada bloque antes de que se escribiera una línea de
   código: agrupación de habilidades, formato de las fichas personales, campos del
   formulario.
4. Recién entonces se generó el código, siguiendo esas decisiones.
5. Lo revisé, lo modifiqué y lo publiqué.

### Qué hizo la herramienta

- **Generó el HTML y el CSS** a partir de la dirección y las decisiones que definí. Esta es
  la parte más sustancial de su intervención y no la minimizo: la primera versión del
  código salió de ahí.
- **Redactó los textos** sobre la base de los datos que aporté, con revisión y ajustes míos.
- **Respondió consultas técnicas puntuales**: los límites del plan Hobby de Vercel para
  publicar un segundo proyecto, y la estructura de carpetas conveniente para el despliegue.
- **Procesó las dos fotografías propias** (recorte y optimización de peso).

### Qué decidí y revisé con criterio propio

- **Corregí un dato mal tomado**: en la primera versión figuraba "Software Developer en
  Certronic". Certronic es el producto; la empresa es Laborem Certificación Laboral S.A.
- **Rechacé mostrar niveles con barras de progreso o estrellas.** Un "PHP 85%" no informa
  nada real. Preferí una línea de contexto sobre dónde uso cada tecnología.
- **Decidí no usar Bootstrap**, que es mi forma habitual de resolver el estilado, para
  cumplir el requisito de CSS propio y aprovechar el ejercicio de escribirlo a mano.
- **Pedí que no se usara ningún logo, escudo ni personaje de terceros** en la sección
  personal. La estética se resuelve con tipografía, color y formas propias en CSS.

### Qué aprendí en el proceso

Lo más útil fue entender qué resuelven por debajo los frameworks que uso a diario. La línea
`grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr))` hace que las tarjetas se
reacomoden solas según el ancho disponible: es, en una sola declaración, lo que en Bootstrap
resuelvo repartiendo clases `col-md-4` por el HTML. Lo mismo con `clamp()` en los títulos,
que reemplaza tener un tamaño de fuente distinto por cada breakpoint. Después de escribirlo
a mano, las clases del framework dejaron de ser una caja negra.

Sobre el trabajo con IA no descubrí el método, ya lo aplicaba: avanzar por etapas, revisando
y corrigiendo a la par, en lugar de pedir todo de una. Lo que sí confirmé es que el resultado
depende directamente de cuántas decisiones tome uno en el camino. Cada vez que corregí algo
—un dato de la empresa, un formato que no me convencía, un texto que no sonaba a mí— el
proyecto se pareció más a lo que yo quería y menos a una plantilla.

---

## Uso de imágenes

Las dos fotografías son **propias**. No hay imágenes generadas por IA en este proyecto.

| Archivo | Origen | Intervención |
|---|---|---|
| `img/perfil.jpg` | Foto personal | Recorte cuadrado centrado en el rostro, redimensionado a 640×640 px y compresión JPEG progresiva |
| `img/monumental.jpg` | Foto personal en el estadio Monumental | Recorte apaisado, redimensionado a 800×712 px y compresión JPEG progresiva |

El procesamiento fue de recorte y optimización de peso, con la biblioteca Pillow de Python.
No hubo retoque generativo ni modificación del contenido de las imágenes.

---

## Publicación

Desplegado en **Vercel** como sitio estático, conectado a este repositorio: cada push a la
rama principal genera un nuevo deploy automático.

---

## Cómo verlo en local

```bash
git clone https://github.com/Fernandez-Sebastian/PFO1-DSW-FRONT.git
cd PFO1-DSW-FRONT
# Abrir index.html en el navegador, o levantar un servidor local:
python3 -m http.server 5500
```