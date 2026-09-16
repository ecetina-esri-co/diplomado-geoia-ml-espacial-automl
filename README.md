# Diplomado GeoIA · Machine Learning Espacial y AutoML

**Clase 01 lista para revisión académica humana**, dentro de los módulos 5 y 6. La [[01 - Clases/2026-09-14 - Clase 01 - Clustering espacial|nota central]], cinco conceptos y dos herramientas integran P02 autónoma ejecutada con el Ejercicio 5A completo y copia jurisdiccional preparada externamente; P01 permanece intacta, sin reejecución. Las comprobaciones técnicas y el renderizado local aislado están completos según [[99 - Recursos/Clase 01 - Resultados de prácticas]]. No se comprobó la disposición nativa de Obsidian; no se declara aprobación ni publicación.

## Empezar

1. Abrir [[00 - Índice]] y el [Canvas](<00 - Mapa del diplomado.canvas>).
2. Usar [[Templates/Plantilla - Clase|Plantilla de clase]] para escribir pronto la nota, conceptos y visuales de la sesión autorizada; reutilizar acuerdos, fuentes verificadas y resultados, sin esperar informes previos.
3. Integrar las prácticas y hacer una revisión final enfocada: **una clase completa → revisión humana → detenerse**. Publicación y siguiente clase requieren autorización explícita separada.

La [skill integrada](.pi/skills/geoia-ml-espacial-automl/SKILL.md) 2.2 aplica este flujo directo; las dos skills docentes previas están retiradas. Las reglas vigentes de profundidad, seguridad y ejecución están en [AGENTS.md](AGENTS.md). No se exige aprobar cada paso interno ni repetir consultas/notebooks sin cambios o incertidumbre creíble.

## Calendario definitivo

Septiembre de **2026**; cada sesión dura **2 horas**: nueve sesiones, 18 horas.

| Módulo | Tema | Horas | Fechas definitivas — septiembre de 2026 |
| --- | --- | ---: | --- |
| 5. Aprendizaje No Supervisado | 5.1. Clustering espacial | 4 | 14 y 15 |
| 5. Aprendizaje No Supervisado | 5.2. Minería de patrones espacio-temporales | 6 | 16, 17 y 21 |
| **Subtotal módulo 5** | | **10** | **5 sesiones** |
| 6. Aprendizaje Supervisado y AutoML | 6.1. Regresión y clasificación basada en bosques | 6 | 22, 23 y 24 |
| 6. Aprendizaje Supervisado y AutoML | 6.2. Automatización de modelos (AutoML) | 2 | 28 |
| **Subtotal módulo 6** | | **8** | **4 sesiones** |
| **Total del bloque** | | **18** | **9 sesiones** |

Solo está confirmada la identificación Clase 01 para el 14/09. El índice usa fechas para las demás sesiones, sin inventar numeración o enlaces a notas inexistentes.

## Estructura actual

| Ubicación | Estado y función |
| --- | --- |
| `00 - Índice.md` / `00 - Mapa del diplomado.canvas` | Navegación base, no contenido docente terminado |
| `Templates/Plantilla - Clase.md` | Plantilla reutilizable para redactar directamente |
| `01 - Clases/2026-09-14 - Clase 01 - Clustering espacial.md` | Nota central actualizada; comprobaciones técnicas completas, pendiente revisión académica humana |
| `02 - Conceptos/`, `03 - Herramientas/` | Cinco notas de conceptos y dos de herramientas redactadas y enlazadas desde la clase |
| `99 - Recursos/clase-01-*.svg`, `99 - Recursos/clase-01-slide-*.png` | Gráficas y capturas inspeccionadas; renderizado local aislado verificado, no interfaz nativa de Obsidian |
| `04 - Proyectos/`, `05 - Preguntas/` | Notas de entrada con estado pendiente |
| `99 - Recursos/Enlaces y bibliografía.md` | Referencias oficiales reutilizables según afirmación y versión |
| `99 - Recursos/notebooks/` | Dos notebooks de Clase 01 ejecutados; no equivalen al paquete docente completo |
| `99 - Recursos/datos/` | Guía e insumos seleccionados según disponibilidad; reutilizar sin duplicar |
| `.obsidian/` | Cinco JSON reutilizables; Templates activo, Sync y Publish desactivados |
| `.pi/skills/geoia-ml-espacial-automl/` | Única skill integrada 2.2; referencia consultada según necesidad |
| `99 - Recursos/Matriz - Análisis exploratorio y ArcGIS.md` | Contraste documental de antecedentes anteriores a Clase 13 y capacidades; sin ejecución |

`Datos/` y `3. Machine Learning Espacial y AutoML/` son insumos preexistentes, conservados intactos y excluidos de Git por precaución. Los nuevos insumos seleccionados usarán por defecto `99 - Recursos/datos/`, con rutas configurables incluso externas. Las copias y salidas se mantienen separadas en `99 - Recursos/salidas_clase_NN/practica_PP/` o equivalente externo. Las ejecuciones existentes de Clase 01 se conservan; P01 no se repitió y P02 ya ejecutó el alcance actualizado en `ejecucion_20260915T220908_d62e311d`, con copia jurisdiccional preparada fuera del notebook.

## Fuentes y alcance

Las grabaciones **13–15 y 16–20** del vault `../diplomado_geoia` son ocho fuentes, no nueve clases destino. La correspondencia de contenidos se documentará por sesión, sin asumir relación uno a uno. Los PowerPoint locales sirven de referencia; no se producirán nuevos PPTX sin petición explícita. Cada nota de clase incorpora **seis diapositivas fuente como objetivo**, limpias, completas, legibles, pertinentes y distintas, visibles al inicio después del encabezado y antes de objetivos/agenda. Solo se admiten menos si la fuente realmente no ofrece suficientes imágenes aptas, con una breve justificación explícita y sin relleno. Cada captura lleva título, fuente/localizador e interpretación. SVG propios, gráficas y mapas no cuentan entre las seis; Mermaid, gráficas explicativas y mapas ArcGIS pertinentes siguen siendo obligatorios.

Se adaptaron la plantilla y el patrón de navegación original, sin copiar las 39 clases ni su red de conceptos. Se conservan las exigencias de español claro y profundo, fuentes junto a las afirmaciones, Mermaid y gráficas en cada clase/concepto, y notebooks con celdas comentadas, mapas y gráficos ArcGIS interpretados.

## Selección de prácticas y capacidades

Consultar solo secciones pertinentes de la [matriz EDA y ArcGIS](<99 - Recursos/Matriz - Análisis exploratorio y ArcGIS.md>) ante una operación o duda; no convertir antecedentes históricos en evidencia actual. **Una práctica real, un notebook autónomo**, no uno por algoritmo: datos de solo lectura, salidas aisladas y código importante explicado dentro de la nota. Inspeccionar únicamente campos, geometrías y requisitos relevantes; ArcGIS primero sin desplazar las bibliotecas Python justificadas de la fuente.

Los acuerdos P1–P7 y dos notebooks de Clase 01 no se reabren. P01 `make_moons` es exclusivamente sintética: sin contraste Bogotá, EPSG ficticio ni mapas geográficos; mantiene gráficos tabulares ArcGIS y conceptuales. Esta excepción no es general. P02 completa `DiplomadoGeoIA Ejercicio 5A.docx` en un notebook Python autosuficiente, sin ModelBuilder manual ni auxiliar personalizado compartido: objetivos en Markdown, primera celda de código corta `DATA_DIR`/`OUTPUT_DIR`, EDA visible (diccionario de campos, nulos/ceros, claves, XY, tiempo, CRS y gráficos/mapas ArcGIS) antes de modelos; DBSCAN 100/350 m → MeanCenter sin ruido por `CLUSTER_ID` → Identity con copia jurisdiccional válida → Statistics COUNT/AddJoin/CopyFeatures → HDBSCAN 100 → OPTICS 100/350 m y sensibilidad automática predeterminada con mapa, barras y perfil de alcanzabilidad nativos.

La preparación geométrica P02 se realiza por separado, fuera de la práctica: crear una copia nueva jurisdiccional en `99 - Recursos/datos/`, comprobar con CheckGeometry y, solo si persisten errores, aplicar RepairGeometry exclusivamente sobre esa copia con `KEEP_NULL`, preservando IDs/conteo/atributos, informando cambios y CheckGeometry posterior. Si ya es válida, no reparar. El notebook no contiene ni ejecuta RepairGeometry ni un script de preparación: consume el insumo preparado como entrada de solo lectura; puede comprobar su calidad y se detiene si no es válido para Identity. Su ruta puede configurarse en la primera celda de código junto a `DATA_DIR`/`OUTPUT_DIR`, sin duplicar incidentes. Errores puntuales/desconocidos siguen fatales y requieren otra decisión; sin deduplicación, imputación ni asignación jurisdiccional forzada. Reportar frontera/coincidencias múltiples/ausentes; una copia reparada no certifica límites legales. No es permiso general de reparación ni de modificar originales, DOCX/TXT fuente o la skill del otro diplomado.

## Validación y siguiente paso

P02 completó el alcance autorizado; P01 se preservó sin reejecución y la evidencia histórica permanece separada. La comprobación técnica y visual local aislada de Clase 01 está registrada en [[99 - Recursos/Clase 01 - Resultados de prácticas]], junto con sus límites; se reutilizan [[99 - Recursos/Clase 01 - Fuentes y acuerdos|acuerdos y evidencia existentes]]. Nueve Mermaid y cinco SVG únicos se renderizaron e inspeccionaron sin recortes; no se comprobó la disposición nativa de Obsidian. No se requieren informes separados, runners nuevos ni ensayos como preinsumos; se conservan los existentes. Revisar al final coherencia, referencias, enlaces, visuales y salidas, revalidando solo piezas afectadas. La agenda de 120 minutos es estimada; el tiempo de ejecución medido no demuestra un ensayo docente.

**Pendiente:** presentar Clase 01 a revisión académica humana y detenerse, sin iniciar otra clase como parte de este cierre. La verificación técnica no equivale a aprobación académica. Antes de staging o publicación revisar licencias y privacidad; sin autorización automática de commit, push o redistribución. Desactivar Obsidian Sync no desactiva la sincronización externa del sistema de archivos.
