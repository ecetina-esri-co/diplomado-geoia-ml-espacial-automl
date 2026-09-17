# Diplomado GeoIA - Vault de notas

![Obsidian](https://img.shields.io/badge/Obsidian-vault-7C3AED?logo=obsidian&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-notas-000000?logo=markdown&logoColor=white)
![ArcGIS](https://img.shields.io/badge/ArcGIS-plataforma-2C7AC3?logo=arcgis&logoColor=white)
![GeoAI](https://img.shields.io/badge/GeoAI-diplomado-2EA043)
![GitHub](https://img.shields.io/badge/GitHub-repositorio-181717?logo=github&logoColor=white)
![Idioma](https://img.shields.io/badge/Idioma-espa%C3%B1ol-D4A017)

Bienvenido al vault de estudio del **Diplomado en Inteligencia Artificial Geoespacial con Plataforma ArcGIS**. Este repositorio se concentra en los **módulos 5 y 6: Machine Learning Espacial y AutoML**, con nueve sesiones de dos horas; no reúne todos los módulos del diplomado.

**Docente:** Fabian Cetina

El vault es un **mapa de conocimiento**: las notas de clase se conectan con conceptos, herramientas, prácticas y preguntas. No necesitas leer archivos sueltos en orden alfabético: comienza por el índice y sigue las relaciones que ayuden a entender cada problema.

> **Material disponible:** Clase 01 (14 de septiembre) y Clase 02 (15 de septiembre de 2026), y Clase 03 (16 de septiembre) como borrador migrado, con seis notebooks en total. Disponibilidad no significa aprobación académica ni ejecución completa de todas las prácticas. Consulta el estado de cada nota y la tabla de prácticas de esta guía.

## Ruta rápida

1. Descarga [Obsidian desde su sitio oficial](https://obsidian.md/download).
2. Clona este repositorio o descarga el ZIP, según las opciones siguientes.
3. En Obsidian, elige **Open folder as vault / Abrir carpeta como bóveda** y selecciona la carpeta del repositorio.
4. Abre [00 - Índice.md](00%20-%20%C3%8Dndice.md) para elegir la clase; usa el [Mapa del diplomado](00%20-%20Mapa%20del%20diplomado.canvas) como entrada visual.

No necesitas Obsidian Sync, Publish ni plugins adicionales para comenzar. GitHub permite consultar los Markdown y notebooks, pero la navegación con enlaces internos y Canvas se aprovecha mejor en Obsidian.

## Cómo abrir el vault en Obsidian

### Opción recomendada: clonar con Git

Si aún no tienes Git, puedes obtenerlo en [git-scm.com/downloads](https://git-scm.com/downloads). En una terminal, dentro de la carpeta donde quieras guardar el material:

```bash
# Descarga una copia con historial y posibilidad de recibir actualizaciones.
git clone https://github.com/ecetina-esri-co/diplomado-geoia-ml-espacial-automl.git
```

En Obsidian, selecciona **Abrir carpeta como bóveda** y abre **`diplomado-geoia-ml-espacial-automl`**, no únicamente `01 - Clases` o `99 - Recursos`. La raíz contiene el índice y las demás carpetas necesarias para resolver los enlaces.

### Opción simple: descargar ZIP

1. Descarga el [ZIP de la rama main](https://github.com/ecetina-esri-co/diplomado-geoia-ml-espacial-automl/archive/refs/heads/main.zip).
2. Extrae todo su contenido. **Un archivo `.zip` no se puede abrir directamente como vault.**
3. Abre en Obsidian la carpeta extraída que contiene `00 - Índice.md`, normalmente `diplomado-geoia-ml-espacial-automl-main`.

Git permite actualizar la misma copia; con ZIP, las actualizaciones se descargan y extraen manualmente.

## Por dónde navegar

| Entrada | Para qué sirve |
| --- | --- |
| [00 - Índice.md](00%20-%20%C3%8Dndice.md) | Punto de partida para sesiones y recursos disponibles. |
| [00 - Mapa del diplomado.canvas](00%20-%20Mapa%20del%20diplomado.canvas) | Vista ligera de las relaciones principales. |
| [01 - Clases](01%20-%20Clases/) | Notas docentes, objetivos, explicaciones y prácticas. |
| [02 - Conceptos](02%20-%20Conceptos/) | Definiciones y relaciones para profundizar. |
| [03 - Herramientas](03%20-%20Herramientas/) | Uso y límites de herramientas del flujo de trabajo. |
| [04 - Proyectos](04%20-%20Proyectos/) | Entrada para aplicación y seguimiento; no implica proyectos terminados. |
| [05 - Preguntas](05%20-%20Preguntas/) | Preguntas y temas por resolver. |
| [99 - Recursos](99%20-%20Recursos/) | Bibliografía, diapositivas, gráficas y evidencia complementaria. |
| [Notebooks](99%20-%20Recursos/notebooks/) | Prácticas ejecutables; requieren un entorno adecuado. |
| [Datos](99%20-%20Recursos/datos/) | Entradas seleccionadas y notas de procedencia. |

**Clases disponibles:**

- [Clase 01 — Clustering espacial](01%20-%20Clases/2026-09-14%20-%20Clase%2001%20-%20Clustering%20espacial.md).
- [Clase 02 — OPTICS y autocorrelación espacial incremental](01%20-%20Clases/2026-09-15%20-%20Clase%2002%20-%20OPTICS%20y%20autocorrelaci%C3%B3n%20espacial%20incremental.md).

- [Clase 03 — Cubos espacio-temporales y patrones emergentes](01%20-%20Clases/2026-09-16%20-%20Clase%2003%20-%20Cubos%20espacio-temporales%20y%20patrones%20emergentes.md): borrador migrado; video parcialmente revisado, no clase procesada completa.

Los seis notebooks están enlazados en **Cómo ejecutar las prácticas**. El calendario no implica que ya existan notas para las nueve sesiones.

## Cómo leer una clase

1. Entra desde el índice y comprueba fecha, tema y estado de la nota.
2. Lee objetivos, agenda e ideas principales: identifica qué problema se quiere resolver y por qué importa.
3. Revisa **Diapositivas de referencia**, situadas al inicio de la nota, junto con sus pies e interpretaciones.
4. Sigue los enlaces a conceptos cuando necesites una definición, un supuesto o una limitación.
5. Relaciona las herramientas con el problema y lee el código explicado antes de abrir el notebook.
6. Trabaja la práctica, interpreta las salidas y vuelve a la nota para conectar resultados, preguntas y posibles aplicaciones en un proyecto.

Las notas no son transcripciones literales. Separan contenido de las fuentes, explicaciones docentes y resultados observados; un ejemplo o una ejecución histórica no garantiza el mismo resultado en otro entorno.

## Cómo usar el Canvas

Abre el mapa desde el índice o directamente en Obsidian. Acércate a una tarjeta para leerla y abre su nota para profundizar; sigue las conexiones para ubicar conceptos y clases relacionadas. Vuelve al índice si necesitas una lista ordenada.

El Canvas es una **entrada visual ligera**, no un grafo exhaustivo de todos los archivos ni una certificación del estado de las clases.

## Convenciones del vault

### Enlaces internos

En Obsidian, los enlaces con doble corchete conectan notas existentes. Por ejemplo:

- `[[Aprendizaje no supervisado]]`: sitúa el problema de aprender estructuras sin una etiqueta objetivo.
- `[[DBSCAN]]`: desarrolla agrupamiento por densidad y su relación con ruido y parámetros.
- `[[HDBSCAN y OPTICS]]`: permite comparar alternativas y escalas de densidad.
- `[[ArcGIS Pro - Density-based Clustering]]`: conecta los conceptos con la herramienta.

Sigue los enlaces para entender la relación, no solo para acumular lecturas. Los enlaces Markdown de esta guía también funcionan desde GitHub.

### Tags

Las etiquetas del encabezado ayudan a reconocer el tipo, tema y estado de una nota. Ejemplos presentes en Clase 02: `tipo/clase`, `estado/borrador`, `tema/geoia`, `tema/estadistica-espacial` y `fuente/grabacion`. Puedes buscarlas en Obsidian; una etiqueta de borrador es una advertencia de estado, no una aprobación.

### Diapositivas clave

Las imágenes fuente se encuentran bajo el encabezado real **Diapositivas de referencia**, con atribución, localizador y una interpretación de su propósito. No las confundas con los diagramas Mermaid y las gráficas SVG explicativas: estos complementan la lectura, pero no sustituyen las diapositivas originales.

Consulta [Enlaces y bibliografía](99%20-%20Recursos/Enlaces%20y%20bibliograf%C3%ADa.md) y las referencias junto a cada afirmación. Conserva las atribuciones al reutilizar material y respeta los derechos de sus fuentes.

## Cómo ejecutar las prácticas

**Obsidian sirve para leer las notas; no ejecuta archivos `.ipynb`.** Abre el notebook en **ArcGIS Pro**, o en Jupyter/VS Code con un kernel del entorno Python de ArcGIS Pro y una licencia disponible. Python genérico y Colab no aportan ArcPy; no intentes resolverlo con `pip install arcpy`.

El entorno observado es **ArcGIS Pro 3.6.2, ArcInfo (Advanced)**. La licencia importa: por ejemplo, la operación Identity de Clase 01 P02 requiere el nivel adecuado. Antes de ejecutar, revisa requisitos y entradas de la práctica.

| Práctica | Notebook | Última evidencia disponible |
| --- | --- | --- |
| Clase 01 · P01 | [Comparación DBSCAN/HDBSCAN sintética](99%20-%20Recursos/notebooks/Clase%2001%20-%20Practica%2001%20-%20Comparacion%20DBSCAN%20HDBSCAN%20sintetica.ipynb) | Ejecución reciente completa; datos sintéticos, sin georreferenciación. |
| Clase 01 · P02 | [Clustering Bomberos con ArcGIS Pro](99%20-%20Recursos/notebooks/Clase%2001%20-%20Practica%2002%20-%20Clustering%20Bomberos%20con%20ArcGIS%20Pro.ipynb) | Ejecución reciente completa. |
| Clase 02 · P01 | [OPTICS y abejas](99%20-%20Recursos/notebooks/Clase%2002%20-%20Practica%2001%20-%20OPTICS%20y%20abejas.ipynb) | Ejecución reciente completa. |
| Clase 02 · P02 | [Colegios y escala espacial](99%20-%20Recursos/notebooks/Clase%2002%20-%20Practica%2002%20-%20Colegios%20y%20escala%20espacial.ipynb) | Última ejecución guardada detenida por licencia; nueva ejecución pendiente. |
| Clase 02 · P03 | [Viviendas turísticas y Moran](99%20-%20Recursos/notebooks/Clase%2002%20-%20Practica%2003%20-%20Viviendas%20turisticas%20y%20Moran.ipynb) | Última ejecución guardada detenida por licencia; nueva ejecución pendiente. |
| Clase 03 · P01 | [Cubos espacio-temporales y patrones emergentes](99%20-%20Recursos/notebooks/Clase%2003%20-%20Practica%2001%20-%20Cubos%20espacio-temporales%20y%20patrones%20emergentes.ipynb) | 21 celdas de código completadas y 16 visuales PNG guardados; el kernel falló al cerrar. No acredita ejecución integral limpia ni reproducibilidad sin errores. |

> La incorporación de los datos locales de colegios no reejecutó ni modificó los notebooks. Los errores guardados de P02/P03 son anteriores a esa copia; sus resultados históricos no acreditan una ejecución nueva completa.

**Secuencia de trabajo:** lee primero los objetivos en Markdown; después revisa la primera celda de configuración (`ROOT`, `DATA_DIR`, `OUTPUT_DIR` y, cuando corresponda, `PREPARED_JURIS`). Reinicia el kernel y ejecuta todas las celdas en orden (**Run All**). Si una celda falla, detente e interpreta el error antes de continuar: evita mezclar resultados anteriores con una ejecución incompleta.

`ROOT = None` busca el vault desde la carpeta de trabajo y sus ancestros. Si inicias Jupyter fuera de ese árbol, sustituye **la primera asignación** por `ROOT = Path('/ruta/a/tu/vault')`, usando la ruta real de tu copia y conservando el import de `Path` que ya incluye la celda.

| Práctica | Configuración de entrada desde la raíz del vault |
| --- | --- |
| C01 P01 | `DATA_DIR`: `99 - Recursos/datos`; genera la muestra sintética. Conserva el auxiliar local declarado por el notebook. |
| C01 P02 | `DATA_DIR`: `Datos`; `PREPARED_JURIS`: `99 - Recursos/datos/p02_jurisdicciones_preparadas/jurisdicciones.gdb/Jurisdicciones_Bomberos`. |
| C02 P01 | `DATA_DIR`: `Datos`. |
| C02 P02 | Cambia la ruta externa predeterminada por `99 - Recursos/datos/clase_02_colegios/colegios.gdb`, como se muestra abajo. |
| C02 P03 | `DATA_DIR`: `99 - Recursos/datos/clase_02_viviendas_turisticas/viviendas.gdb`. |
| C03 P01 | `DATA_DIR`: `99 - Recursos/datos/clase_03`; cuatro entidades en `entradas.gdb` y un cubo NetCDF. `OUTPUT_DIR`: `99 - Recursos/salidas_clase_03/practica_01`, con una subcarpeta nueva por ejecución. |

En **C02 P02**, después de resolver `ROOT`, reemplaza únicamente la asignación de `DATA_DIR` en tu copia de estudiante:

```python
# Usa la copia local de colegios como entrada de solo lectura.
DATA_DIR = ROOT / '99 - Recursos/datos/clase_02_colegios/colegios.gdb'
```

El código posterior ya añade `Colegios_Colombia`; no agregues ese nombre a `DATA_DIR`. El notebook aún muestra la ruta anterior al vault hermano en su configuración y explicación: **para esta copia distribuida, aplica el cambio anterior antes de Run All**. La [procedencia de colegios](99%20-%20Recursos/datos/clase_02_colegios/README.md) registra 10.617 puntos y las comprobaciones de conservación; no se trata de un censo exhaustivo.

Mantén todas las entradas en solo lectura y configura `OUTPUT_DIR` en una carpeta de resultados separada. No sobrescribas originales ni ejecuciones que quieras conservar. Revisa la [guía de datos](99%20-%20Recursos/datos/README.md) y los requisitos de cada notebook para interpretar las entradas y los insumos preparados.

## Rutina recomendada para estudiar

1. Ubica la sesión en el índice y formula una pregunta que quieras responder.
2. Lee los objetivos y relaciona el tema con lo que ya conoces.
3. Revisa las diapositivas y explica con tus palabras una idea principal.
4. Consulta conceptos y herramientas; anota supuestos y límites.
5. Prepara el entorno y los datos antes de ejecutar la práctica.
6. Interpreta mapas, gráficas y métricas: distingue observación, explicación y limitaciones.
7. Escribe una conclusión, una pregunta pendiente y una posible aplicación; vuelve a la nota para conectar lo aprendido.

## Cómo recibir nuevas clases

Clona una sola vez y actualiza cuando se publique nuevo material. Después, abre el índice para ver qué cambió: no todas las sesiones del calendario tienen todavía una nota disponible.

### Si clonaste con Git

Antes de actualizar, revisa tus cambios locales:

```bash
# Desde la carpeta del repositorio, comprueba si tienes cambios propios.
git status --short
```

Si aparecen cambios o archivos nuevos, revísalos y respalda tus apuntes antes de continuar. No uses un reset ni un stash a ciegas para eliminar un conflicto. Cerrar Obsidian puede evitar ediciones simultáneas, pero **no demuestra que tu copia esté limpia**.

### Ejemplo completo

Desde la carpeta que contiene el repositorio, y una vez preservados tus cambios:

```bash
cd diplomado-geoia-ml-espacial-automl
# Comprueba el estado antes de traer material publicado.
git status --short
# Continúa solo si el estado está resuelto; no crea una fusión automática.
git pull --ff-only
```

Si Git informa un conflicto o que no puede avanzar, detente y revisa la situación sin descartar archivos. Las novedades pueden aparecer en el índice, `01 - Clases`, conceptos, herramientas, notebooks o recursos; vuelve al índice después de actualizar.

### Si descargaste ZIP

Descarga nuevamente el ZIP, extráelo en **otra carpeta** y abre esa carpeta como vault. Conserva o respalda tus notas antes de cambiar de copia. Una descarga ZIP no tiene el historial de Git: **no se actualiza con `git pull`**.

## Si haces apuntes propios

Para simplificar las actualizaciones, guarda tus apuntes en un vault o carpeta personal fuera del clon, con enlaces o referencias a las clases. Si decides anotarlos dentro de tu copia, mantén un respaldo y revisa el estado de Git antes de actualizar.

No sobrescribas ni elimines apuntes personales al reemplazar carpetas o extraer un ZIP. Separa tus conclusiones de las notas docentes para reconocer la fuente y el estado de cada idea.

## Si quieres colaborar

Leer, clonar o descargar no requiere permisos de escritura. Para enviar cambios al repositorio necesitas **autorización y permisos de colaborador**; si no los tienes, conserva tus apuntes y comparte la propuesta con el docente.

Con autorización, actualiza primero una copia limpia, revisa `git status --short` y edita notas conectadas con el índice o con una clase. Comprueba enlaces y atribuciones. No publiques transcripciones crudas, logs, temporales, capturas sin valor conceptual, credenciales ni datos personales.

Ejemplo para una contribución autorizada sobre el README; cambia la selección solo por los archivos que realmente hayas revisado:

```bash
# Comprueba y preserva cambios locales antes de actualizar.
git status --short
git pull --ff-only
# Después de editar, revisa exactamente lo que vas a compartir.
git diff -- README.md
git diff --check
git add -- README.md
git diff --cached -- README.md
git commit -m "Aclara la guía de estudio del diplomado"
# Solo para colaboradores autorizados y en la rama acordada.
git push
```

Selecciona rutas explícitas; evita `git add .`, que puede incorporar archivos ajenos, como `__pycache__`. No publiques datos ni recursos de terceros sin comprobar su autorización de redistribución.

## Calendario definitivo

Septiembre de **2026**. Cada sesión dura **2 horas**: nueve sesiones, **18 horas** en total. Actualmente están disponibles las notas de Clase 01 (14/09) y Clase 02 (15/09); también está disponible localmente Clase 03 (16/09) como borrador migrado, con revisión parcial del video y fallo de cierre del kernel. Las demás fechas son programación, no enlaces a material ya publicado.

| Módulo | Tema | Horas | Fechas definitivas — septiembre de 2026 |
| --- | --- | ---: | --- |
| 5. Aprendizaje No Supervisado | 5.1. Clustering espacial | 4 | 14 y 15 |
| 5. Aprendizaje No Supervisado | 5.2. Minería de patrones espacio-temporales | 6 | 16, 17 y 21 |
| **Subtotal módulo 5** | | **10** | **5 sesiones** |
| 6. Aprendizaje Supervisado y AutoML | 6.1. Regresión y clasificación basada en bosques | 6 | 22, 23 y 24 |
| 6. Aprendizaje Supervisado y AutoML | 6.2. Automatización de modelos (AutoML) | 2 | 28 |
| **Subtotal módulo 6** | | **8** | **4 sesiones** |
| **Total del bloque** | | **18** | **9 sesiones** |

Vuelve al [índice](00%20-%20%C3%8Dndice.md) para comenzar o retomar tu estudio.
