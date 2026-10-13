# PFO1 · Landing de portafolio personal

**Sebastián Fernández** · Desarrollo de Sistemas Web (Front End) · 2° A
Tecnicatura en Desarrollo de Software · 2do cuatrimestre 2026

Landing de una sola página construida con **HTML5 semántico, CSS3 propio y JavaScript**, sin frameworks
ni librerías externas. Presenta mi perfil profesional, experiencia laboral, habilidades, tres proyectos, formación, intereses personales y contacto directo.
Incluye un CV descargable en PDF, generado desde el contenido del HTML.

- 🌐 **Sitio publicado:** https://pfo1-dsw-front.vercel.app
- 👤 **Perfil de GitHub:** https://github.com/Fernandez-Sebastian
- 💼 **LinkedIn:** https://www.linkedin.com/in/sebasti%C3%A1n-fern%C3%A1ndez-aa2b572a1

---

## Contenido de la landing

| Sección | Qué contiene |
|---|---|
| Presentación | Nombre y apellido, rol actual, bio y datos de trayectoria |
| Experiencia | Laborem desde julio de 2022; desarrollador desde marzo de 2023 |
| Formación | Tecnicatura Superior en Desarrollo de Software, IFTS 29, desde febrero de 2025 |
| Habilidades | Cinco tarjetas agrupadas por área: backend, front end, herramientas, equipo y exploración |
| Proyectos | HuFly Fishing, Barbería 1997 y Resultado Final (prode del Mundial 2026, +8.000 usuarios) |
| Personal | Tarjetas de intereses personales y fotografía del Monumental |
| Contacto | Enlaces directos a email y LinkedIn, GitHub y ubicación |

---

## Estructura del proyecto

```
PFO1-DSW-FRONT/
├── index.html          # Estructura semántica completa
├── css/
│   └── styles.css      # Estilos propios y adaptación responsive
├── img/
│   ├── perfil.png      # Foto de perfil actual, proporcionada por Sebastián
│   ├── perfil.jpg      # Foto anterior, conservada como recurso
│   └── monumental.jpg  # Foto anterior de la sección personal, conservada
├── output/pdf/Sebastian-Fernandez-CV.pdf  # CV descargable
├── scripts/generate_cv.py                # Generador desde index.html
└── README.md
```

---

## Requisitos técnicos de la consigna original

La versión actual está orientada a postulaciones laborales: reemplaza el formulario
sin backend por contacto directo y mantiene la sección personal visual. No conserva todos los
elementos de la entrega académica original.

| Requisito | Dónde se cumple |
|---|---|
| HTML semántico (`header`, `nav`, `main`, `footer`) | `index.html`, más `section`, `article` y `aside` |
| CSS propio | `css/styles.css`, escrito íntegramente para esta entrega |
| Google Fonts | Space Grotesk, Inter y JetBrains Mono, vinculadas con `preconnect` |
| Flexbox o Grid | Ambos, combinados (ver justificación abajo) |
| Diseño responsive | Unidades relativas, `clamp()`, `auto-fit` y dos breakpoints |
| Transición o animación | 3 animaciones `@keyframes` propias y transiciones en toda la interfaz |
| Imágenes con `alt` | La foto de perfil tiene texto alternativo descriptivo |
| Formulario con `label` | Reemplazado por enlaces de contacto directo en la versión profesional |
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

### Contacto y CV

El contacto se realiza mediante email y LinkedIn. El sitio no recibe ni almacena mensajes.
El botón **Descargar CV (PDF)** entrega un documento de una página con texto seleccionable
y enlaces. Para regenerarlo después de cambiar el perfil, la experiencia, las habilidades,
los proyectos o la formación en `index.html`:

```bash
python -m pip install reportlab
python scripts/generate_cv.py
```

El generador utiliza el HTML como fuente de contenido. Revisar la paginación al agregar
información: el PDF no se actualiza automáticamente durante el despliegue.
Las capturas de los proyectos y el detalle de los módulos desarrollados pueden incorporarse
cuando estén disponibles. No se agregaron tecnologías ni responsabilidades no confirmadas
para Barbería 1997.

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

Las fotografías guardadas en el repositorio son **propias**. No hay imágenes generadas por IA en este proyecto.

| Archivo | Origen | Intervención |
|---|---|---|
| `img/perfil.png` | Foto personal proporcionada por Sebastián | Archivo original de 1080×1080 px, sin modificaciones; presentación circular mediante CSS |
| `img/perfil.jpg` | Foto personal anterior, sin uso en la página | Recorte cuadrado centrado en el rostro, redimensionado a 640×640 px y compresión JPEG progresiva |
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

## Actualización profesional

Se utilizó Codex (OpenAI) para incorporar la foto proporcionada, ampliar el stack,
reorganizar experiencia y formación, simplificar el contacto y generar el CV en PDF.
Las fechas laborales, la institución y el proyecto Barbería 1997 fueron aportados por Sebastián.
La declaración anterior documenta la creación de la entrega académica original.

### Portfolio visual e interacción

Se recuperó la sección personal original con tarjetas, foto del Monumental y efectos al
pasar el cursor. La portada prioriza explorar los proyectos; el PDF es una descarga secundaria.
`js/main.js` permite filtrar las habilidades por área con botones accesibles y estado anunciado.
Sin JavaScript, todas las habilidades siguen visibles. La experiencia tiene un desplegable
nativo para consultar las responsabilidades. Se mantiene la preferencia de movimiento reducido.
