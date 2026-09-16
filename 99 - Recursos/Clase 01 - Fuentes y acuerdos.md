---
tags: [tipo/recurso, estado/revision, tema/geoia, fuente/grabacion]
clase_destino: "01"
fecha_destino: 2026-09-14
fecha_registro: 2026-09-15
---

# Clase 01 — Fuentes y acuerdos

**Integración docente con P02 autónoma completa y comprobaciones técnicas terminadas; material listo para revisión académica humana, sin aprobación.** [[01 - Clases/2026-09-14 - Clase 01 - Clustering espacial|Abrir Clase 01]]. P01 preservada sin reejecución. P02 vigente: `ejecucion_20260915T220908_d62e311d`, 25 celdas de código, 355.40 s de kernel, tres métodos, centros/Identity/COUNT/unión y 13 PNG nativos. [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/evidencia.json|Evidencia JSON actual]] y [[99 - Recursos/Clase 01 - Resultados de prácticas|resultados, comprobaciones y límites]]. Las ejecuciones y decisiones anteriores se conservan como historia, no estado vigente. Se reutiliza la verificación fuente registrada; esta integración documental no acredita nueva revisión de video ni cierre académico.

La preparación corresponde a **Clustering espacial**, módulo 5, sesión destino del **2026-09-14**, de 120 minutos. Volver al [[00 - Índice|índice y estado de sesiones]].

## 1. Alcance y decisiones humanas

| Asunto | Acuerdo o límite vigente |
| --- | --- |
| Continuación | El usuario indicó «prosigue» para la Clase 01 seleccionada. No autoriza otras sesiones. |
| Prácticas | Dos notebooks autónomos. **Decisión vigente: P01 exclusivamente sintética con make_moons; P02 Bomberos geográfico completo.** El contraste geográfico de P01 quedó revocado. |
| Precisiones técnicas | **P1–P7 APROBADAS** con notas explicativas; véase sección 7. |
| Insumos | Uso local autorizado de los datos existentes. P02 consumió incidentes originales y jurisdicciones preparadas de solo lectura; modeló una copia nueva, sin modificar entradas. |
| Avance documentado | P02 autónoma ejecutada e integrada en la nota central; tres métodos, centros medios y superposición según DOCX. Pendientes comprobación visual final de notas y revisión académica. |
| Ejecución local histórica (versión anterior) | P01 se conserva sin ejecutar ni escribir. P02 completó 13 celdas en kernel nuevo: DBSCAN/HDBSCAN sobre 90 443 puntos, tres mapas y seis gráficos ArcGIS. No se repararon geometrías. Siguen prohibidos instalaciones, créditos, modificación de originales, PPTX, staging, commit, push y publicación. |
| Geometría P02 histórica — sustituida, no vigente | El usuario eligió «Continuar sin reparar (Recommended)». Una auto-intersección de jurisdicciones se admite solo como contexto cartográfico advertido, no límites certificados, análisis poligonal, cobertura ni despacho. Errores de puntos, clases desconocidas y pérdida de cobertura siguen siendo fatales. |
| Derechos | El acceso y uso académico local no conceden redistribución de grabación, diapositivas o datos. Licencias y privacidad pendientes. |
| Aprobación | Continuar no demuestra aprobación académica de toda la base ni del paquete; la publicación requiere autorización separada. |

### Decisión vigente: «Actualizar reglas y continuar»

El usuario autorizó explícitamente actualizar las instrucciones y continuar P02 completa según `DiplomadoGeoIA Ejercicio 5A.docx`, en un notebook Python totalmente autosuficiente, sin ModelBuilder manual ni auxiliar personalizado compartido. Históricamente, el ajuste inicial fue solo de texto y la preparación externa posterior no incluía ejecutar notebooks en ese paso. La implementación y ejecución posteriores autorizadas ya completaron P02; la integración documental actual reutiliza esa evidencia sin repetir geoprocesamiento. Originales, DOCX/TXT fuente y skill del otro diplomado no se modifican. P01 queda intacta; P1–P7 y las dos prácticas se conservan.

Objetivos primero en Markdown; primera celda de código corta `DATA_DIR`/`OUTPUT_DIR`. Antes de modelos, EDA visible con diccionario de campos, nulos/ceros, claves, XY, tiempo, CRS y gráficos/mapas ArcGIS. Secuencia autorizada: DBSCAN mínimo 100/350 m → MeanCenter sin ruido por `CLUSTER_ID` → Identity de centros con copia jurisdiccional válida → Statistics COUNT/AddJoin/CopyFeatures → HDBSCAN mínimo 100 → OPTICS mínimo 100/350 m, sensibilidad automática predeterminada y mapa/barras/perfil de alcanzabilidad nativos. Es alcance autorizado del DOCX, no afirmación de nueva lectura o ejecución de la grabación.

Preparar por separado, fuera de la práctica, una copia nueva jurisdiccional en `99 - Recursos/datos/` y comprobar con CheckGeometry. Si persisten errores, RepairGeometry exclusivamente en esa copia con `KEEP_NULL`, sin eliminación implícita; preservar IDs, cantidad y atributos, informar geometrías cambiadas y CheckGeometry posterior. Si ya es válida, no reparar. El notebook no contiene ni ejecuta RepairGeometry ni un script de preparación: consume el insumo preparado de solo lectura, puede comprobar su calidad y se detiene si no es válido para Identity. Configurar su ruta en la primera celda de código junto a `DATA_DIR`/`OUTPUT_DIR`, sin duplicar incidentes. Errores puntuales/desconocidos siguen fatales, pendientes de otra decisión; no deduplicar ni imputar automáticamente. Reportar fronteras/coincidencias múltiples/ausentes sin asignación forzada. Reparar la copia cartográfica no certifica límites legales. No autoriza reparación general ni modificación de originales.

La política anterior «solo contexto/sin Repair» y su evidencia se conservan abajo como historia sustituida, no como prohibición activa. También queda sustituida la formulación intermedia «reparar en una ejecución nueva de P02»: la reparación autorizada pertenece exclusivamente a la preparación externa, nunca al notebook. La nota central y resultados ahora reflejan la ejecución autónoma vigente; el notebook y el informe anteriores permanecen en [[99 - Recursos/salidas_clase_01/practica_02/Resultados_historicos_antes_autonomia.md|historia anterior a la autonomía]].

**Historia — preparación externa observada, interrumpida; estado sustituido por la recuperación siguiente:** copia creada desde `Datos/Datos Ejercicio5A.gdb/Jurisdicciones_Bomberos` en `99 - Recursos/datos/p02_jurisdicciones_preparadas/jurisdicciones.gdb/Jurisdicciones_Bomberos`. CheckGeometry ESRI inicial: 17 polígonos, una incidencia `self intersections`, OBJECTID 5; atributos copiados contrastados con el original. La llamada RepairGeometry `KEEP_NULL`/`ESRI` sobre la selección afectada terminó el proceso con `Fatal Python error: InitDatetime: Could not import datetime C API` e `ImportError: PyCapsule_Import could not import module "datetime"` (salida 127). No se reintentó; se conserva la copia y la comprobación inicial. No se alcanzó validación posterior ni comprobación final de integridad del original: conteo final, IDs/atributos finales, geometrías cambiadas y efectos de la reparación no verificados. **Insumo todavía no validado para Identity**; seguimiento acotado pendiente. Sin ejecución de notebooks ni operaciones sobre puntos. Véase [[99 - Recursos/datos/README|guía de datos]].

**Actualización posterior — recuperación externa validada, 2026-09-15:** CheckGeometry volvió a detectar exclusivamente la auto-intersección OID 5; RepairGeometry `KEEP_NULL`/`ESRI` finalizó en proceso aislado Pro 3.6.2/ArcInfo. Cero errores finales, 17 entidades e IDs/CRS/atributos temáticos preservados; solo geometría OID 5 y sus medidas automáticas `Shape_Length`/`Shape_Area` cambiaron. La validación inicial se detuvo por exigir igualdad también a esas medidas derivadas; se conservó su evidencia y la siguiente comprobación distinguió medidas de atributos temáticos, sin otra reparación. Original consultado antes/después sin cambios en atributos ni WKB. Véanse comando, medidas exactas y dos JSON en [[99 - Recursos/datos/README#Recuperación posterior validada — 2026-09-15|recuperación externa]]. El fallo InitDatetime histórico no reapareció; su causa no está demostrada. Esta actualización sustituye el estado pendiente anterior, sin borrar su historia, certificar límites legales ni acreditar ejecución nueva de P02.

**Lectura directa del DOCX utilizada en la implementación (2026-09-15):** `3. Machine Learning Espacial y AutoML/5. Aprendizaje No Supervisado/DiplomadoGeoIA Ejercicio 5A.docx`, Esri Colombia, *5A Clustering basado en densidad*, edición estudiante, pasos 1–5 y revisión. Se leyó `word/document.xml` en memoria, sin modificar ni extraer un archivo fuente. Secuencia sustantiva: explorar jurisdicciones/estaciones y recuentos de incidentes → DBSCAN → selección `CLUSTER_ID <> -1` → MeanCenter con caso `CLUSTER_ID` → Identity con jurisdicciones y unión de todos los atributos excepto IDs (`NO_FID`) → Statistics con COUNT de `CLUSTER_ID`, caso `CLUSTER_ID` → AddJoin por `CLUSTER_ID` → CopyFeatures a `IncidentesBomberosCentrosGruposDB` → mapa de grupos/ruido/centros y barras → HDBSCAN y OPTICS → mapas, barras por grupo, histograma de probabilidad HDBSCAN y perfil de alcanzabilidad OPTICS → comparación y revisión conceptual. La adaptación autorizada reemplaza los pasos manuales de ModelBuilder por Python autónomo, no los omite.

El DOCX indica mínimo 100 y búsqueda 350 m en el bucle HDBSCAN/OPTICS; aplicar DBSCAN 100/350 m, HDBSCAN mínimo 100 (sin interpretar 350 m como epsilon fijo del método), OPTICS 100/350 m y sensibilidad automática predeterminada conforme al alcance aprobado y E1–E2. Sus expresiones «radio mínimo» o «distancia mínima» no definen correctamente epsilon: es umbral de vecindad, no tamaño total del grupo (P1). Conservar preguntas sobre Kennedy B-5, Restrepo B-3/COMPAÑIA IV, conteos por estación y diferencias entre métodos. Las respuestas impresas —90 443 registros, Kennedy 8 705, Restrepo 4 802, DBSCAN 20 grupos, grupo 1 con 67 429 y ruido 13 446; HDBSCAN tres grupos y OPTICS grupo dominante 16— son **resultados fuente, no resultados de la nueva ejecución**. No forzar coincidencia con ellos; interpretar PROB con P2 y distinguir ruido de incertidumbre. Campos temáticos jurisdiccionales comprobados en esa preparación: `ESTACION`, `NOMBRE_EST`, `COMPAÑIA`, `NOMBRE_CORTO_EST`; para incidentes se reutilizó la inspección inicial de sección 5 y se confirmó el perfil durante la ejecución vigente.

La base normativa se conserva en [[AGENTS]], el calendario en [[README]] y el contrato docente en [[Templates/Plantilla - Clase|la plantilla]]. Sus estados históricos no se reescriben en este avance.

## 2. Identidades y valor probatorio de las fuentes

| ID | Identidad y localizador | Uso y límites |
| --- | --- | --- |
| V13 | Clase fuente **13**, **2026-06-23**. Título visible: *Diplomado Inteligencia Artificial Geoespacial con la Plataforma ArcGIS- V1*. Docente: **José Gómez Romero**, autoidentificación 00:07:30. | Acceso visible autorizado verificado por el orquestador; este escritor recibe su síntesis, sin nueva consulta del video. |
| Localizador V13 | `../diplomado_geoia/99 - Recursos/Enlaces y bibliografía.md`, línea 19. | Se conserva el localizador, no la URL privada completa ni información de acceso. |
| PPT | `3. Machine Learning Espacial y AutoML/5. Aprendizaje No Supervisado/V2_DiplomadoGeoAI_Aprendizaje_No_Supervisado_2026.pptx`; 73 diapositivas según inspección previa transmitida. | Referencia local; no se supone que sea exactamente la presentación grabada. |
| Nota fuente | Nota de Clase 13 del vault original, `../diplomado_geoia/01 - Clases/`. | Frontmatter con fecha mal formada: no modificarlo. Metadatos destino correctos solo en este registro; fuente y destino permanecen separados. |
| Notebook fuente | `../diplomado_geoia/99 - Recursos/notebooks/Clase 13 - Aprendizaje no supervisado y agrupacion espacial.ipynb`. | Adaptación escrita posterior; sus celdas no prueban qué se ejecutó en el video. Lectura de código sin ejecución ni conservación de sus salidas. |

Son ocho grabaciones fuente (13–15 y 16–20) para nueve sesiones destino: esta selección no establece equivalencia uno a uno ni asigna contenidos de las otras clases.

### Diapositivas de referencia identificadas

Se verificaron las posiciones de presentación y los títulos de las diapositivas 8–22 el 2026-09-15, sin modificar el PowerPoint. La presentación contiene 73 diapositivas; solo este segmento tiene correspondencia temática identificada para la sesión.

| Diapositiva | Título verificado |
| --- | --- |
| 8 | La IA y el Aprendizaje de Máquina |
| 9 | Lo que hace especial al ML espacial |
| 10 | Tipos de Aprendizaje de Máquina (ML) |
| 11 | Aprendizaje Supervisado y No Supervisado |
| 12 | Agrupación Espacial |
| 13 | Algoritmos de Agrupación |
| 14 | Agrupación por densidad |
| 15–16 | Algoritmos de agrupación por densidad |
| 17 | DBSCAN |
| 18 | DBSCAN – Tipos de Puntos |
| 19 | HDBSCAN |
| 20 | OPTICS |
| 21 | Agrupación basada en densidad (ArcGIS Pro) |
| 22 | Ejercicio 5A — Clustering basado en densidad (ArcGIS Pro) |

La identificación textual no prueba identidad con cada fotograma de V13. Se exportaron una vez en solo lectura las diapositivas 11/18/19/20 a PNG 1920×1080 y se abrieron las cuatro imágenes. La selección inicial de la nota fue 11/19/20 con interpretación y precisiones; la 18 conserva un diagrama inferior truncado y no se presenta como visual completo. Permisos de redistribución pendientes; exportación local no autoriza publicación.

**Selección vigente — seis como objetivo:** por decisión del usuario se incorporan seis diapositivas fuente al inicio de cada clase, después del encabezado y antes de objetivos/agenda; menos solo si la fuente realmente no ofrece suficientes imágenes aptas, con justificación y sin relleno. En Clase 01 se añadieron 8/9/17 mediante una única exportación autorizada de solo lectura, sin reexportar 11/19/20 ni alterar el archivo 18. Los tres PNG nuevos de 1920×1080 se abrieron: 8 muestra texto y recuadros IA/ML/DL completos; 9 muestra los cuatro paneles espaciales y pie completos; 17 muestra título y lista de parámetros completos. Texto legible, sin controles, participantes ni recortes observados. La selección actual es **8/9/11/17/19/20**, con fuente e interpretación; la 18 sigue archivada y excluida por truncación. Son ilustraciones de la referencia, no fotogramas ni resultados de Bomberos. SHA-256 del PPTX antes y después: `ddba45724a20214198ff4ea97e822ffde0f83760b565b4ec306591ee248671c8`, iguales. Siguen pendientes renderizado final de Mermaid/SVG, revisión académica y derechos de redistribución.

## 3. Cobertura de V13 y destino previsto

Síntesis académica de evidencia transmitida por el orquestador; no transcripción. Los intervalos conservan la secuencia y sus discontinuidades, sin inventar contenido intermedio.

| Tiempo V13 | Contenido mostrado | Tratamiento previsto |
| --- | --- | --- |
| 00:00–00:07:30 | Saludos y espera. | Contexto de apertura; no convertir espera histórica en agenda docente. |
| 00:07:30–00:14:40 | Presentación y diagnóstico; calendario anterior. | Preservar función diagnóstica, distinguir calendario fuente del destino. |
| 00:14:41–00:26:36 | IA/ML/DL; espacial frente a tabular; dependencia, heterogeneidad, autocorrelación y validación cruzada espacial. | Cobertura conceptual y precisiones P4/P7 desarrolladas en la nota y conceptos. |
| 00:26:55–00:27:58 | Taxonomía del aprendizaje. | Conservar marco conceptual. |
| 00:27:58–00:32:20 | Preparación del entorno fuente. | Revisar requisitos actuales; no reproducir credenciales, descargas ni instalaciones. |
| 00:32:27–00:40:17 | Supervisado, no supervisado y refuerzo; calidad y ejemplos. | Conservar; precisión P3 aprobada. |
| 00:40:48–00:50:54 | Clustering y taxonomía. | Conservar diversidad de métodos, sin añadir ejercicio independiente. |
| 00:51:05–01:06:59 | DBSCAN/HDBSCAN/OPTICS; parámetros, ruido, jerarquía y alcanzabilidad. | Conservar comparaciones; P1, P2 y P6 aprobadas. |
| 01:08:11–01:39:38 | P01 sintética: lunas, variación de ruido/muestra y sensibilidad DBSCAN/HDBSCAN. | Mantener unidad práctica; no confundir variaciones con prácticas nuevas. |
| 01:40:28–01:45:38 | Importación Bomberos, jurisdicciones, Data Engineering y barras por estación. | Inicio de P02; evaluar ArcGIS primero sobre copias. |
| 01:45:44–01:56:15 | DBSCAN geográfico 350 m/100; CLUSTER_ID/COLOR_ID, ruido −1 e inspección de pertenencia y frontera. | Preservar configuración histórica, no presentarla como óptimo ni ejecución nueva. |
| 01:56:15–02:01:02 | HDBSCAN 100; comparación geográfica e histogramas de atributos. | Conservar contraste e interpretación con P2 aprobada. |
| 02:01:05–02:02:40 | Se anuncia para la siguiente clase fuente completar OPTICS, centroides/cobertura y HDBSCAN dentro de un grupo. | Registrar continuidad anunciada, **no ejecución en V13**. Históricamente no se incorporó a Clase 01; la decisión vigente incorpora el alcance DOCX a P02, sin crear otra práctica. |

K-means aparece como contraste en la nota fuente, no como ejecución demostrada en V13. Mantener esa distinción; no fabricar un tercer ejercicio.
La nota conserva la cobertura y secuencia en una agenda estimada de 120 minutos: 5+12+10+23+12+18+10+22+8. No se ensayó; no se exige ensayo como preinsumo. Espera/saludos/calendario histórico no consumen entrega; no se omiten ejercicios ni se trasladan las doce sensibilidades.

## 4. Inventario aprobado: dos prácticas, dos notebooks

**Inventario vigente.** Ambos notebooks tienen evidencia de ejecución con kernel nuevo. P01 conserva `clase01_arcgis.py`; P02 define sus funciones dentro del notebook y no importa auxiliares personalizados. El apoyo histórico compartido permanece intacto para P01; no es requisito de P02. La versión anterior geográfica se conserva separada en el informe histórico enlazado en sección 1.

| Práctica | Pregunta y secuencia | Entradas y estado |
| --- | --- | --- |
| P01 | ¿Cómo cambian agrupaciones y ruido al variar parámetros? `make_moons` → EDA tabular ArcGIS → StandardScaler → DBSCAN/HDBSCAN → doce sensibilidades → variación controlada de muestra/perturbación. | Exclusivamente sintéticos; sin Bomberos, mapas ni referencia espacial ficticia. No queda decisión de muestreo geográfico pendiente. |
| P02 | ¿Cómo se agrupan los registros y qué representan sus centros? Configuración/copia/EDA → DBSCAN → selección sin ruido/MeanCenter → Identity → Statistics COUNT/AddJoin/CopyFeatures → mapas/barras → HDBSCAN e histogramas → OPTICS y perfil → comparación. | 90 443 filas preservadas; DBSCAN 20 grupos/13 384 ruido, HDBSCAN 3/1 187, OPTICS 29/17 561. 20 centros/20 filas Identity/finales, sin ausencias, multiplicidad ni frontera a 0.001 m. Jurisdicciones preparadas: 17 entidades, cero errores detectados. 13 PNG y cuatro APRX. |

- P01: [[99 - Recursos/notebooks/Clase 01 - Practica 01 - Comparacion DBSCAN HDBSCAN sintetica.ipynb|Notebook sintético]].
- P02: [[99 - Recursos/notebooks/Clase 01 - Practica 02 - Clustering Bomberos con ArcGIS Pro.ipynb|Notebook geográfico Bomberos]].
- Entradas geográficas **solo de P02**: `Datos/Datos Ejercicio5A.gdb` y `99 - Recursos/datos/p02_jurisdicciones_preparadas/jurisdicciones.gdb/Jurisdicciones_Bomberos`, ambas de solo lectura.
- Salidas P01: `99 - Recursos/salidas_clase_01/practica_01/`.
- Salidas P02: `99 - Recursos/salidas_clase_01/practica_02/`.
- Objetivos primero en Markdown; primera celda de código P02: `DATA_DIR`, `OUTPUT_DIR` y `PREPARED_JURIS`, con rutas externas admitidas y aislamiento comprobado.
- Sin estado oculto entre notebooks; no duplicar originales ni usar una salida de P02 como requisito implícito de P01.

### P01: parámetros que deben conservarse

El código base del notebook fuente usa `n_samples=200`, `noise=0.9999`, `random_state=10`, StandardScaler, DBSCAN `eps=0.3/min_samples=5` y HDBSCAN `min_cluster_size=5/min_samples=5/cluster_selection_epsilon=0`.
Su mensaje impreso dice incorrectamente 300; P01 informa la longitud calculada de 200 observaciones, sin modificar la fuente.
En V13 se variaron muestra y ruido: no mezclar recuentos históricos con ejecuciones nuevas ni afirmar resultados antes de obtenerlos.

| Variante | DBSCAN: eps / min_samples, celda 10 | HDBSCAN: min_cluster_size / min_samples / cluster_selection_epsilon, celda 12 |
| --- | --- | --- |
| 1 | 0.10 / 5 | 5 / 5 / 0.0 |
| 2 | 0.20 / 5 | 10 / 5 / 0.0 |
| 3 | 0.30 / 5 | 15 / 5 / 0.0 |
| 4 | 0.30 / 10 | 5 / 10 / 0.0 |
| 5 | 0.45 / 5 | 10 / 10 / 0.0 |
| 6 | 0.45 / 10 | 10 / 5 / 0.15 |

Celdas numeradas desde cero; se conserva la totalidad de las doce configuraciones del notebook fuente, no doce prácticas.
`make_moons` no representa observaciones geográficas: **nunca asignarle WKID 9377**. Por decisión humana vigente, P01 no tiene contraste Bomberos ni selección geográfica.
E12–E13 respaldan el escalado sintético y el generador; no escalar metros geográficos automáticamente ni atribuir etiquetas sintéticas a hechos territoriales.

## 5. Insumos y entorno: inspección inicial histórica

Se conserva la inspección inicial de solo lectura del **2026-09-15**. Los pendientes de esta tabla son históricos: perfil temporal, nulos, claves, XY, geometría de puntos/preparados y APIs utilizadas fueron comprobados después en P02. Continúan los límites semánticos de despacho, exhaustividad y derechos. Véanse sección 4 e informe vigente; esta integración no repitió ArcPy ni geoprocesamiento.

| Elemento | Disponible/verificado por el orquestador | Pendiente o límite |
| --- | --- | --- |
| Incidentes_Bomberos | 90 443 puntos en `Datos/Datos Ejercicio5A.gdb`. | Calidad geométrica y semántica no verificadas. |
| Jurisdicciones_Bomberos | 17 polígonos en la misma GDB. | Relación operativa con incidentes y calidad no verificadas. |
| SR de ambas capas | MAGNA-SIRGAS_2018_Origen-Nacional, WKID 9377; metro. | No heredarlo a sintéticos ni asumir que prueba calidad posicional. |
| Procedencia | Vault original: `../diplomado_geoia/99 - Recursos/datos`; disponibilidad heredada local. | Versión de datos, licencia y privacidad no verificadas; uso local autorizado, redistribución no concedida. |
| ArcGIS Pro | 3.6.2, build 59527; Advanced NamedUser; ProductInfo ArcInfo. | La licencia observada no verifica requisitos exactos de cada herramienta. |
| Python | 3.13.7 en el entorno Pro inspeccionado. | Ejecutar las prácticas con el intérprete del entorno Pro verificado, no asumir equivalencia con otros entornos. |
| Paquetes | NumPy 2.2.0; pandas 2.3.0; scikit-learn 1.6.1; Matplotlib 3.9.4. | Importación disponible no prueba una práctica reproducible. |
| Apoyo notebook/imagen | nbformat 5.10.4; nbclient 0.8.0; IPython 8.37.0; Pillow 11.3.0. | Sin ejecución ni renderizado comprobados. |
| Nombres ArcPy | Density-based Clustering, CopyFeatures, CheckGeometry, FieldStatisticsToTable; charts.Bar/Histogram/Scatter/Box. | Nombres disponibles; firmas y ejecución locales no verificadas. |
| Apoyo visual | cairosvg y svglib ausentes; PowerPoint COM registrado. | PowerPoint no abierto/probado; no instalar ni inferir renderizado. |

Campos verificados: `IncidentesBomberos_FECHA` (Date), `IncidentesBomberos_NUMERO_INC` (Double), `IncidentesBomberos_ESTACION` (String 254), `Incidentes_Bomberos_AddSpatialJoin_ESTACION` (String 10) y `Incidentes_Bomberos_AddSpatialJoin_NOMBRE_EST` (String 150).
Jurisdicciones incluye `ESTACION`, `NOMBRE_EST`, `COMPAÑIA` y `NOMBRE_CORTO_EST`; no se infieren aquí tipos ni equivalencias semánticas no transmitidas.
Pendientes: cobertura temporal, nulos frente a ceros, significado de claves duplicadas, correspondencia entre campos de estación y calidad geométrica. No imputar, borrar, transformar o deduplicar automáticamente.
No copiar datos ahora: la entrada seleccionada ya existe. Aplicar [[99 - Recursos/datos/README|guía de datos]] y separar futuras copias de trabajo de originales.

## 6. Selección inicial ArcGIS primero — historia de planificación

Los estados pendientes de esta selección se conservan como planificación histórica. La ejecución vigente utilizó perfil, tres métodos, centros/Identity/COUNT, cuatro mapas, seis barras, dos histogramas y un perfil Line nativos; Data Engineering manual no fue requisito ni acción acreditada. Consultar [[99 - Recursos/Matriz - Análisis exploratorio y ArcGIS|matriz EDA y ArcGIS]]: es capacidad documental, no validación automática del entorno o de los datos de Clase 01.

| Necesidad | Capacidad priorizada y motivo | Estado |
| --- | --- | --- |
| Calidad y perfil | Data Engineering; evaluar CheckGeometry y FieldStatisticsToTable sobre copias. | Selección pertinente inicial; firmas, licencias y comportamiento pendientes. |
| Estaciones | Frecuencias y barras ArcGIS, conservando pregunta y gráfico fuente. | Definir campo semánticamente correcto antes de contar. |
| Agrupaciones | Mapas ArcGIS de entradas, ruido y grupos; barras por CLUSTER_ID. | API cartográfica y subclases de gráficos pendientes de consulta exacta. |
| HDBSCAN | Comparación cartográfica e histograma PROB según salida real. | No inventar campos ni sustituir gráficos bloqueados por Matplotlib. |
| Mecanismo sintético | scikit-learn conserva generador, escalado y experimentos controlados de P01. | Complemento metodológico justificado, no reemplazo geográfico. |
| Resúmenes y figuras fuente | pandas/NumPy para resúmenes; Matplotlib para figuras sintéticas de la fuente. | Complementan, no sustituyen mapas ni gráficos ArcGIS obligatorios. |

Data Engineering es una vista, no `arcpy.DataEngineering`. No imponer Moran, inferencia, modelado supervisado o reducción dimensional como EDA básica nueva.
E1 documenta parámetros `in_features`, `output_features`, `cluster_method`, `min_features_cluster`, `search_distance` opcional, `cluster_sensitivity`, `time_field` y `search_time_interval`, y ejemplo HDBSCAN con cuatro argumentos posicionales. Esto no prueba firma local ejecutada ni niveles de licencia.

## 7. Precisiones P1–P7 — APROBADAS con notas explicativas

**El usuario aprobó P1–P7 con explicaciones docentes.** La propuesta inicial se conserva en contenido, ahora con estado aprobado. No se modifica la fuente histórica.
Las referencias E se identifican íntegramente en la sección 8; todas fueron consultadas por el orquestador el 2026-09-15, no recuperadas de nuevo por este escritor.

| ID y localizador V13 | Precisión propuesta y respaldo próximo | Estado |
| --- | --- | --- |
| P1 — 00:58:46–01:01:15; 01:18:13–01:18:37; 01:54:25–01:55:52 | DBSCAN: un punto frontera puede pertenecer sin reunir MinPts por sí mismo; el mínimo del núcleo incluye el propio punto. Eps delimita vecindad, no diámetro/radio total del grupo ni una cota de 350 m para todo él. Esri Pro 3.6, E2 Search Distance/How methods work; scikit-learn 1.6, E3 eps/min_samples. | APROBADA con nota explicativa |
| P2 — 01:58:20–02:00:49 | HDBSCAN construye jerarquía y extrae grupos planos estables; etiqueta/probabilidad individual no es la jerarquía. PROB no es verdad absoluta ni valor p; 0.9 no implica significancia automática. Esri define probabilidad del grupo asignado; sklearn define fuerza proporcional a persistencia, sin equivalencia automática entre implementaciones. E1–E2 Outputs; E4 attributes/Notes; E5 algorithm steps. | APROBADA con nota explicativa |
| P2, campos | Esri Pro 3.6 documenta PROB, OUTLIER y EXEMPLAR; no inventar STABILITY hasta revisar salida real. Valores de esos campos para ruido pueden no ser significativos. CLUSTER_ID distingue grupos; COLOR_ID puede reutilizar colores. E1–E2 Outputs. | APROBADA con nota explicativa |
| P3 — 00:35:11–00:36:37 | Refuerzo: agente, estado, acción, recompensa y retorno esperado acumulado; no predicción ordinaria de etiquetas reservadas. OpenAI Spinning Up, E7 Key Concepts/Terminology y The RL Problem. | APROBADA con nota explicativa |
| P4 — 00:24:11–00:26:21 | Separar índice Moran I de z y p; no significancia no prueba aleatoriedad. Validación espacial evalúa transferencia según objetivo, no descubre clusters. Esri Pro 3.6, E6 Interpretation; Roberts et al. 2017, E11 pp. 913–919: bloques pueden reducir optimismo e inducir extrapolación. | APROBADA con nota explicativa |
| P5 — 01:09:46–01:10:20 y preparación histórica | Pro ya incluye numerosas bibliotecas; no exigir instalador de deep learning para imports disponibles. Conservar contexto histórico, revisar requisitos actuales. Esri Pro 3.6, E8 Third-party libraries; imports locales transmitidos en sección 5. | APROBADA con nota explicativa |
| P6 — 01:08:42–01:09:21; 00:54:45–00:56:36 | DBSCAN surge en bases espaciales (E10, resumen AAAI 1996). Acotar orientación de rendimiento a Pro (E1), no universalizar DBSCAN < HDBSCAN < OPTICS entre implementaciones; E3/E9 Notes describen costes propios de sklearn y efecto de max_eps. | APROBADA con nota explicativa |
| P7 — taxonomía 00:26:55–00:27:58 y 00:40:48–00:50:54 | Ausencia de etiquetas objetivo no elimina conocimiento de dominio ni supuestos; no todos los métodos de clustering evitan elegir k. Respaldo de los métodos por densidad en E1–E5 no debe universalizarse a toda la taxonomía; E14 documenta `n_clusters` en K-means. Este contraste procede de la nota, no de ejecución del video. | APROBADA con nota explicativa |

Estas precisiones no añaden prácticas ni eliminan las doce sensibilidades. El mensaje fijo de 300 se corrigió en P01 mediante longitud calculada: 200 observaciones base. Es adaptación verificada, no cambio del original.

## 8. Referencias verificadas por el orquestador

**Fecha común de consulta: 2026-09-15.** Títulos, editor, versión y secciones corresponden a lectura de páginas originales transmitida al escritor. No se afirma consulta web independiente. IDs exclusivos de este registro.

- **E1 — Esri, ArcGIS Pro 3.6, [Density-based Clustering](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-statistics/densitybasedclustering.htm)**. Summary/Usage/Parameters/Code sample: métodos, parámetros y campos PROB/OUTLIER/EXEMPLAR; DBSCAN más rápido en el contexto Pro y OPTICS intensivo, especialmente con distancia grande. Tabla exacta de licencias aún no recuperada.
- **E2 — Esri, ArcGIS Pro 3.6, [How Density-based Clustering works](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-statistics/how-density-based-clustering-works.htm)**. Search Distance/How methods work/Outputs: núcleo incluye punto propio; frontera sin mínimo propio; ruido no núcleo ni frontera; grupos estables, alcanzabilidad y campos de salida.
- **E3 — scikit-learn 1.6, [DBSCAN](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.DBSCAN.html)**. eps/min_samples/Notes: vecindad no limita distancias totales dentro del grupo; incluye punto propio; memoria de peor caso O(n²) en esta implementación.
- **E4 — scikit-learn 1.6, [HDBSCAN](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.HDBSCAN.html)**. Parameters/Attributes/Notes: min_samples=None adopta min_cluster_size; epsilon de selección fusiona grupos bajo distancia; probabilities_ expresa fuerza de pertenencia proporcional a persistencia. min_samples incluye punto propio, a diferencia de contrib; no trasladar toda semántica a Esri.
- **E5 — Desarrolladores HDBSCAN, [How HDBSCAN Works](https://hdbscan.readthedocs.io/en/latest/how_hdbscan_works.html)**. Página rotulada documentación 0.8.1; introducción/algorithm steps: transformación de densidad, árbol de expansión mínima, jerarquía, condensación y extracción plana estable. No demuestra instalación de ese paquete.
- **E6 — Esri, ArcGIS Pro 3.6, [How Spatial Autocorrelation (Global Moran's I) works](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-statistics/h-how-spatial-autocorrelation-moran-s-i-spatial-st.htm)**. Introducción/Interpretation: I, z y p; atributo y localización; no rechazo del modelo nulo ante resultado no significativo, no prueba de aleatoriedad.
- **E7 — OpenAI Spinning Up, [Key Concepts in RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)**. Documento en línea sin versión numérica indicada; Key Concepts/Terminology/The RL Problem: agente, acción, recompensa y maximización del retorno esperado acumulado.
- **E8 — Esri, ArcGIS Pro 3.6, [ArcGIS Pro Python environment](https://pro.arcgis.com/en/pro-app/3.6/arcpy/get-started/available-python-libraries.htm)**. Third-party libraries: cientos de bibliotecas, Python 3.13.7 y versiones NumPy/pandas/Matplotlib indicadas en sección 5. Disponibilidad sklearn respaldada por comprobación local, no por una lista documental no leída.
- **E9 — scikit-learn 1.6, [OPTICS](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.OPTICS.html)**. max_eps/Attributes/implementation notes: reducir max_eps puede reducir tiempo; ordering_ y reachability_ preceden extracción; implementación O(n²). Uso conceptual de la API sklearn; la P02 sí ejecutó OPTICS mediante ArcGIS Pro, sin atribuir a sklearn sus campos o tiempos.
- **E10 — Ester, Kriegel, Sander y Xu (1996), [A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise](https://aaai.org/papers/kdd96-037-a-density-based-algorithm-for-discovering-clusters-in-large-spatial-databases-with-noise/)**. AAAI, resumen leído: origen espacial, ruido, formas arbitrarias, datos sintéticos y SEQUOIA 2000 reales. No usar «un parámetro» del resumen para negar los dos parámetros prácticos.
- **E11 — Roberts et al. (2017), [Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure](https://www.biom.uni-freiburg.de/mitarbeiter/dormann/roberts-et-al-2017-ecography.pdf)**. Ecography 40:913–929; doi:10.1111/ecog.02881; PDF institucional del autor. Leídas pp. 913–919, resumen, Blocking p. 917 y Box 2 p. 919 (telemetría de 43 hembras de alce, Alberta). Sustenta límites de transferencia, no exige práctica nueva.
- **E12 — scikit-learn 1.6, [StandardScaler](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.StandardScaler.html)**. Definición: z=(x−u)/s por variable, sensible a atípicos. Respaldo del escalado sintético, no de transformar metros sin justificación.
- **E13 — scikit-learn 1.6, [make_moons](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_moons.html)**. API: dos semicírculos sintéticos entrelazados, n_samples como cantidad, noise como desviación del ruido gaussiano y random_state para reproducibilidad; no observaciones geográficas.

- **E14 — scikit-learn 1.6, [KMeans](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.KMeans.html)**. Parameters → n_clusters: número de grupos y centroides que se formarán. Contraejemplo documentado a la generalización de que todo clustering evita especificar k; no añade una práctica ejecutada.

## 9. Pendientes y siguiente decisión

- [x] P1–P7 aprobadas con notas explicativas.
- [x] P01 exclusivamente sintética; decisión geográfica anterior sustituida, sin muestra pendiente.
- [x] Decisión geométrica histórica, sustituida por sección 1: continuar sin reparar, jurisdicciones exclusivamente como contexto advertido. Semántica operativa y licencias siguen pendientes.
- [x] Verificar orden y títulos 8–22 del PowerPoint de referencia.
- [x] Exportar y abrir cuatro capturas de referencia; selección inicial de tres para exposición y advertencia del recorte original visible en la 18. Redistribución sigue pendiente.
- [x] Ampliar después la selección a seis: nuevas 8/9/17 exportadas y abiertas; orden actual 8/9/11/17/19/20 al inicio de la nota, sin exhibir la 18.
- [x] Recibir documentación exacta, inspeccionar firmas instaladas y abrir Blank autorizado. P01 ejecutó FieldStatisticsToTable/Scatter/Bar/exportToPNG; P02 verificó también modelos, mapas e histogramas nativos.
- [x] Hito histórico: crear ambos notebooks y apoyo explícito; P01 ejecutada con nueve PNG y doce sensibilidades. P02 vigente ya no depende del auxiliar.
- [x] Hito histórico: ejecutar y verificar la P02 anterior con contexto geométrico no validado y baseline/finally persistidos. Su política y limitaciones visuales quedaron sustituidas por la P02 autónoma actual; evidencia histórica conservada.
- [x] Escribir [[01 - Clases/2026-09-14 - Clase 01 - Clustering espacial|nota central]], cinco conceptos y dos herramientas, con código, Mermaid, SVG, capturas y resultados incrustados. Renderizado local aislado de Mermaid/SVG comprobado; disposición nativa de Obsidian no comprobada.
- [x] Ajustar agenda estimada de 120 minutos preservando ejercicios y secuencia. No ensayada; tiempo medido de kernels separado.
- [x] Recuperar y validar la preparación geométrica externa; evidencia posterior en sección 1 y guía de datos.
- [x] Actualizar y ejecutar P02 con el alcance DOCX de sección 1: 25 celdas, 355.40 s de kernel, insumo preparado de solo lectura y ninguna reparación en el notebook. Evidencia anterior y P01 preservadas.
- [x] Integrar resultados vigentes, tres métodos, centros/Identity/COUNT y 13 visuales P02 en la nota central; actualizar las afirmaciones afectadas de herramienta y concepto.
- [ ] Comprobar renderizado final local de Mermaid/SVG e incrustaciones de las notas; la inspección previa de PNG no sustituye esta revisión.
- [ ] Revisar el paquete completo con la persona responsable; publicación y siguiente clase siguen sin autorización.

**Estado vigente:** P01 preservada (10 celdas/nueve PNG); P02 autónoma completa e integrada (25 celdas/13 PNG/cuatro APRX), kernel 355.40 s y operaciones 333.30 s. DBSCAN/HDBSCAN/OPTICS: 24.35/122.76/69.16 s; no ranking universal. Insumos y plantilla íntegros según evidencia de `ejecucion_20260915T220908_d62e311d`. Los 13 PNG P02 tienen inspección visual registrada, incluidos ocho reutilizados tras comprobar identidad píxel a píxel; nueve bloques Mermaid y cinco SVG únicos de las ocho notas fueron renderizados e inspeccionados en Chrome aislado con Mermaid 11.13.0, legibles y sin recortes. Enlaces, anclas e incrustaciones resueltos; detalle y límites en [[99 - Recursos/Clase 01 - Resultados de prácticas]]. No se comprobó la disposición nativa de Obsidian ni se añadió revisión de video. Queda revisión académica humana; no se autoriza publicación.

**Límite observado:** DBSCAN devolvió grupos 10→81, 15→99, 16→66, 18→96 y 20→76 pese al mínimo suministrado de 100. COUNT de puntos y COUNT materializado concuerdan; suma de asignados 77 059. Causa específica no diagnosticada, sin reclasificación ni explicación atribuida a fronteras o duplicados. OPTICS omitió sensibilidad y el mensaje informó elegida 1, segunda opción 0; perfil `REACHORDER`/`REACHDIST`, 90 443 valores representables. Los centros no certifican cobertura o límites legales.

**Cierre histórico preservado:** la versión `ejecucion_20260915T171532_430b1cca` completó 13 celdas/nueve PNG en 113.29 s; sus 65 archivos GDB no .lock y Blank coincidieron antes/después. `ejecucion_20260915T164859_ab02a4a0` permanece fallida y sin integridad demostrada: no se le atribuyen hashes posteriores retroactivamente.

## 10. Revisión vigente y referencias de implementación

**Traza de revisión:** después del acuerdo inicial «Dos notebooks con contraste geográfico», el usuario aprobó P1–P7 y precisó: «la practica sintética dejmemosla sintetica sin datos geograficos, usemos moon de sklearn o loq ue se menciona ahi». Se sustituye exclusivamente el contraste geográfico de P01 por make_moons sin mapas ni CRS ficticio. Es una excepción pedagógica acotada: P01 mantiene EDA y gráficos tabulares ArcGIS; P02 mantiene mapas y gráficos ArcGIS obligatorios. No se alteran originales, se recortan sensibilidades ni se añaden prácticas. P01 controla ruido 0/0.2/0.8/0.9999 con N=200 y N=200/500/1000 con ruido 0.9999; es adaptación controlada de la variación manual, no identidad de realizaciones del video.

Perfil de solo lectura transmitido por el orquestador: 90 443 filas, fechas 2022-01-01 a 2024-12-31; 60 711 números de incidente nulos; 29 165 IDs no nulos distintos, 494 claves repetidas y 567 filas excedentes; 82 770 pares XY distintos, 5 670 claves XY repetidas y 7 673 filas excedentes; cero XY no finitas. No prueba duplicación de eventos. Se preservan todas las filas y se enlazan salidas por SOURCE_ID/OID de la copia. `IncidentesBomberos_ESTACION` conserva la estación reportada; no se valida equivalencia de despacho con el campo de unión espacial.

**Lecturas oficiales registradas, 2026-09-15, Esri ArcGIS Pro 3.6:** se reutilizan sus pasajes, sin atribuir consultas web nuevas a esta integración. Las firmas y Blank fueron comprobados en la implementación; la ejecución efectiva y sus resultados están separados de capacidad documental en el informe vigente.

| Referencia | Secciones transmitidas y aplicación |
| --- | --- |
| [Bar](https://pro.arcgis.com/en/pro-app/3.6/arcpy/charts/bar.htm) | Parameters; exportToPNG. x categórico, y numérico, opcionales por nombre; etiquetas nominales de cluster convertidas en texto. |
| [Scatter](https://pro.arcgis.com/en/pro-app/3.6/arcpy/charts/scatter.htm) | x/y, splitCategory, dataSource y exportToPNG. Dispersión sintética sin referencia espacial. |
| [Histogram](https://pro.arcgis.com/en/pro-app/3.6/arcpy/charts/histogram.htm) | binCount/showMedian/dataSource/exportToPNG. PROB/OUTLIER solo de asignados; sin ajuste gaussiano. |
| [Field Statistics To Table](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/data-management/field-statistics-to-table.htm) | Python/Parameters: in_table, in_fields, out_location, out_tables y out_statistics; ALL produce texto; evitar medias de IDs. |
| [Check Geometry](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/data-management/check-geometry.htm) | Python/Usage: ESRI sobre copias; vacío significa sin problemas detectados, sin reparación. |
| [Copy Features](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/data-management/copy-features.htm) y [Create File GDB](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/data-management/create-file-gdb.htm) | Python: rutas literales completas, copia nueva de geometrías/atributos y GDB local CURRENT. |
| [ArcGISProject](https://pro.arcgis.com/en/pro-app/3.6/arcpy/mapping/arcgisproject-class.htm) | Constructor por archivo; createMap/createLayout/createTextElement/saveACopy. Únicamente Blank instalado derivado de InstallDir; nunca save sobre plantilla. |
| [Map](https://pro.arcgis.com/en/pro-app/3.6/arcpy/mapping/map-class.htm) | createMap fuera de Pro incorpora mapa base: retirar capas antes de añadir datos locales; spatialReference real. |
| [Layout](https://pro.arcgis.com/en/pro-app/3.6/arcpy/mapping/layout-class.htm) y [PNGFormat](https://pro.arcgis.com/en/pro-app/3.6/arcpy/mapping/pngformat-class.htm) | createMapFrame/createMapSurroundElement/export; CreateExportFormat PNG, resolución 180. Extensión común de entrada para mapas generales. |
| [UniqueValueRenderer](https://pro.arcgis.com/en/pro-app/3.6/arcpy/mapping/uniquevaluerenderer-class.htm), [Symbol](https://pro.arcgis.com/en/pro-app/3.6/arcpy/mapping/symbol-class.htm) y [LegendElement](https://pro.arcgis.com/en/pro-app/3.6/arcpy/mapping/legendelement-class.htm) | fields/groups/items; RGB y alfa 0–100; size/outlineColor; fittingStrategy/columnCount. CLUSTER_ID nominal, ruido explícito, colores no equivalentes entre métodos. |

### Ayuda instalada utilizada en P02 autónoma

**Esri, ayuda Python instalada de ArcGIS Pro 3.6.2, consulta registrada 2026-09-15 mediante `inspect.getdoc`.** Localizador: símbolo Python indicado dentro del entorno instalado de Pro; no se inventa URL ni se atribuye lectura de página web. Los pasajes y su uso están registrados junto a las celdas Markdown del notebook vigente.

| Símbolo/título de ayuda local | Secciones leídas y aplicación |
| --- | --- |
| `arcpy.stats.MeanCenter` — Mean Center | Input_Feature_Class/Case_Field/Output_Feature_Class: media de posiciones por `CLUSTER_ID`, sin ruido ni pesos adicionales. |
| `arcpy.analysis.Identity` — Identity | join_attributes/cluster_tolerance: `NO_FID`, sin alterar tolerancia; conservar y diagnosticar coincidencias ausentes o múltiples. |
| `arcpy.analysis.Statistics` — Summary Statistics | statistics_fields/case_field: COUNT de `CLUSTER_ID` sobre puntos asignados, caso `CLUSTER_ID`; no contar centros. |
| `arcpy.management.AddJoin` — Add Join | join_type/index_join_fields/join_operation: unión por `CLUSTER_ID`, `KEEP_ALL`; materializar con CopyFeatures sin índices sobre originales. |
| `Geometry.touches`, `Geometry.boundary`, `Geometry.distanceTo` | Diagnóstico de fronteras; distancia mínima y requisito de misma proyección. Tolerancia XY observada 0.001 m, no asignación por proximidad. |
| `arcpy.charts.Line` — Line | x/y/aggregation/dataSource: x numérico/fecha, y numérico; sin agregación se representan valores individuales. Perfil de campos reales `REACHORDER`/`REACHDIST`; ausencias no se convierten en cero. |
| `arcpy.stats.DensityBasedClustering` — Density-based Clustering | cluster_sensitivity: selección automática por divergencia Kullback–Leibler al omitir el parámetro. La ejecución omitió sensibilidad; el valor 1 informado no fue un argumento prefijado. |

### 11. Corrección histórica de P02 y ejecución observada (política sustituida)

Todo este apartado describe la versión previa `ejecucion_20260915T171532_430b1cca`, no las guardas ni resultados de P02 autónoma actual.

La puerta anterior confundía la validez de puntos analíticos con la de polígonos usados solo como contexto. Ahora CLASS se compara por rutas completas normalizadas; nombres sueltos o clases ajenas fallan cerrados. CheckGeometry permanece conservado y emite advertencia explícita sobre `self intersections: 1`; cero errores de puntos y cero clases desconocidas en la ejecución actual. No se reparó, filtró, imputó ni calculó sobre polígonos.

Se persistieron hashes antes de copiar y en finally posterior al cierre del kernel para los tres intentos nuevos, incluidos dos fallos de integración en gráficos. El primero falló con SystemError; el cambio de codificación CSV a UTF-8 con BOM no resolvió el fallo. El segundo expuso ImportError de DLL en pyarrow; la introspección comprobó que se estaba resolviendo una instalación de usuario ajena a Pro. Se excluyó user-site del runner y del kernel (`PYTHONNOUSERSITE=1`), sin leer perfiles privados, instalar ni modificar paquetes. La importación aislada y el tercer intento completo funcionaron. No se atribuye al BOM la resolución del fallo.

Se agotaron exactamente los dos ciclos de corrección/reintento autorizados. El verificador de solo lectura aprobó puntos, filas, enlaces por SOURCE_ID, nueve PNG incorporados y hashes actuales; P01 se comprobó sin ejecutarla. DBSCAN 350 m/100: 7.98 s; HDBSCAN 100: 64.82 s. La duración computacional no equivale a ensayo docente.

El escritor abrió satisfactoriamente la plantilla instalada Blank: un mapa inicial y cero layouts; no la guardó. Los notebooks usan solo copias locales y no proyectos privados. La ejecución autónoma conserva evidencia agregada e integridad SHA-256; la presencia de APIs o imports no demuestra exportaciones ni ejecución satisfactoria.
