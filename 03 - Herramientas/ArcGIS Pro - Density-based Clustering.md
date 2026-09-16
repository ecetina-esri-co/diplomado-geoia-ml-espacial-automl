---
tags: [tipo/herramienta, tema/geoia, herramienta/arcgis-pro, estado/revision]
---

# ArcGIS Pro - Density-based Clustering

Agrupa entidades puntuales según densidad y devuelve una nueva clase con etiquetas y campos diagnósticos según el método. En [[01 - Clases/2026-09-14 - Clase 01 - Clustering espacial]] es la autoridad geográfica de P02: se trabaja sobre copias, no sobre originales.

## Versión y capacidad usada

**Ejecutado:** ArcGIS Pro 3.6.2, Python 3.13.7, licencia ArcInfo/Advanced observada. **Documentación:** Esri Pro 3.6, [Density-based Clustering, Parameters/Outputs/Code sample](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-statistics/densitybasedclustering.htm), consulta 2026-09-15 (E1). La licencia observada permitió estas ejecuciones; no se afirma el nivel mínimo de licencia de toda la herramienta.

| Parámetro | Uso observado | Precaución |
| --- | --- | --- |
| `in_features` | Copia completa de puntos Bomberos | Los polígonos preparados se usan en Identity, no como entrada del clustering |
| `output_features` | Clase nueva en GDB de trabajo aislada | No sobreescribir insumos |
| `cluster_method` | DBSCAN, HDBSCAN y OPTICS ejecutados | Misma copia completa, no salidas encadenadas entre métodos |
| `min_features_cluster` | 100 en los tres métodos | Distinguir parámetro y tamaños observados; véase límite DBSCAN abajo |
| `search_distance` | `350 Meters` en DBSCAN y OPTICS | Vecindad/búsqueda, no diámetro total; omitida para HDBSCAN |
| `cluster_sensitivity` | Omitido en OPTICS | Selección automática; mensaje observado: elegida 1, segunda opción 0 |
| `time_field` / `search_time_interval` | No usados | Acumulación 2022–2024 no es clustering espacio-temporal |

## Fragmento de las llamadas ejecutadas

```python
# PUNTOS es la copia validada; medir es una función local de P02 para tiempos.
medir('DBSCAN', arcpy.stats.DensityBasedClustering, PUNTOS, DBSCAN, 'DBSCAN', 100, '350 Meters')
# Entre DBSCAN y HDBSCAN se ejecutan centros/Identity/COUNT, detallados abajo.
# HDBSCAN parte de la misma copia y no hereda 350 m.
medir('HDBSCAN', arcpy.stats.DensityBasedClustering, PUNTOS, HDBSCAN, 'HDBSCAN', 100)
# OPTICS omite sensibilidad para selección automática, sin modelar tiempo.
medir('OPTICS', arcpy.stats.DensityBasedClustering, PUNTOS, OPTICS, 'OPTICS', 100, '350 Meters')
```

Extracto del [[99 - Recursos/notebooks/Clase 01 - Practica 02 - Clustering Bomberos con ArcGIS Pro.ipynb|notebook autónomo P02 ejecutado]], no programa independiente ni nueva ejecución. La primera celda configura DATA_DIR/OUTPUT_DIR/PREPARED_JURIS; el propio notebook crea directorios nuevos, copia y guardas. No importa auxiliares personalizados ni depende de ModelBuilder o P01. Los fragmentos no fueron ejecutados separadamente como bloques de esta nota.

## Inspeccionar antes de agrupar

CopyFeatures conserva la entrada; CheckGeometry diagnostica sin reparar. P02 preserva 90 443 filas, cero errores puntuales detectados y WKID 9377 en metros. La entrada jurisdiccional preparada tiene 17 entidades y cero errores detectados; su reparación se hizo fuera del notebook, exclusivamente en una copia. P02 solo comprueba y consume esa entrada, y se detiene si no es válida. La geometría comprobada permite Identity, pero no certifica límites legales ni cobertura operativa. Nulos y coincidencias no se imputan ni deduplican automáticamente.

Data Engineering es una vista manual para explorar campos; no existe una llamada `arcpy.DataEngineering` usada aquí. El perfil ejecutado usa FieldStatisticsToTable. P02 utiliza Bar, Histogram y Line, subclases nativas de `arcpy.charts`; Scatter se conserva en la práctica sintética, no como mapa geográfico. En P02, los mapas usan la API cartográfica y copia de Blank, no proyectos privados.

Referencias Esri 3.6: [Check Geometry, Python/Usage](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/data-management/check-geometry.htm), [Copy Features, Python](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/data-management/copy-features.htm), [Field Statistics To Table, Parameters](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/data-management/field-statistics-to-table.htm), [Bar](https://pro.arcgis.com/en/pro-app/3.6/arcpy/charts/bar.htm) e [Histogram](https://pro.arcgis.com/en/pro-app/3.6/arcpy/charts/histogram.htm), consulta 2026-09-15; pasajes API reutilizados del registro.

## Centros y conteos después de DBSCAN

La secuencia ejecutada conserva el Ejercicio 5A: seleccionar `CLUSTER_ID <> -1` → MeanCenter con `Case_Field='CLUSTER_ID'` → Identity `NO_FID` con jurisdicciones preparadas → Statistics COUNT de puntos asignados por `CLUSTER_ID` → AddJoin `KEEP_ALL` a los centros por esa clave → CopyFeatures. COUNT no cuenta centros: sumó 77 059 puntos asignados y se contrastó con las etiquetas y los campos materializados.

Se obtuvieron 20 centros, 20 filas Identity y 20 finales, sin ausencia, multiplicidad ni frontera a 0.001 m. Si hubiera varias coincidencias, COUNT aparecería repetido y no debería sumarse como población nueva. Un centro medio puede caer fuera de una forma no convexa: no es estación óptima y su coincidencia jurisdiccional no asigna operativamente todos sus puntos.

Fuente: **Esri Colombia, *DiplomadoGeoIA Ejercicio 5A — Clustering basado en densidad*, edición estudiante, pasos 1–5/revisión**, DOCX leído 2026-09-15. Implementación: **Esri, ayuda Python instalada Pro 3.6.2**, `arcpy.stats.MeanCenter` (Case_Field), `arcpy.analysis.Identity` (join_attributes/cluster_tolerance), `arcpy.analysis.Statistics` (statistics_fields/case_field), `arcpy.management.AddJoin` (join_type) y `Geometry.touches/boundary/distanceTo`, consulta registrada 2026-09-15 en [[99 - Recursos/Clase 01 - Fuentes y acuerdos#Ayuda instalada utilizada en P02 autónoma|ayuda instalada]]. Copy Features conserva la materialización; código y mapas explicados en la nota central.

## Leer la salida sin sobreinterpretar

`CLUSTER_ID` identifica grupos nominales; −1 es ruido. `COLOR_ID` puede reutilizar colores y no empareja métodos. HDBSCAN aporta `PROB`, `OUTLIER`, `EXEMPLAR`; PROB no es valor p, OUTLIER no confirma error y EXEMPLAR no localiza estaciones óptimas. Los histogramas P02 usan solo asignados: 89 256, con ruido informado aparte.

[Esri Pro 3.6, How Density-based Clustering works, Outputs](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-statistics/how-density-based-clustering-works.htm), consulta 2026-09-15 (E2). No equiparar automáticamente PROB con la fuerza sklearn.

DBSCAN produjo 20 grupos/13 384 ruidos; HDBSCAN 3/1 187; OPTICS 29/17 561. Los tiempos vigentes 24.35/122.76/69.16 s son de estas llamadas, no ranking universal. [[99 - Recursos/Clase 01 - Resultados de prácticas]] conserva evidencia, integridad actual e historia fallida sin atribución retroactiva.

**Límite observado DBSCAN:** grupos 10→81, 15→99, 16→66, 18→96 y 20→76 pese al parámetro 100; COUNT y copia materializada concuerdan. Causa específica no diagnosticada: no garantizar 100 filas finales para todos los grupos, atribuirlo a fronteras/duplicados ni reclasificar. La definición formal de densidad se conserva, separada de esta discrepancia de salida.

OPTICS generó `REACHORDER`/`REACHDIST`: el perfil Line usa orden algorítmico y distancia en metros, no tiempo ni OBJECTID; los 90 443 valores fueron representables. Sensibilidad omitida significa selección automática, no suministrar el 1 observado. **Esri, ayuda Python instalada Pro 3.6.2**, DensityBasedClustering (cluster_sensitivity) y Line (x/y/aggregation/dataSource), consulta 2026-09-15, registro anterior. P02 produjo cuatro mapas, seis barras, dos histogramas de 30 intervalos y un perfil de alcanzabilidad, todos nativos, más cuatro APRX; los visuales se interpretan en la nota central.

## Relaciones

[[02 - Conceptos/DBSCAN]] aclara vecindad; [[02 - Conceptos/HDBSCAN y OPTICS]] diferencia jerarquía y extracción; [[02 - Conceptos/Agrupación espacial]] justifica SR y límites; [[02 - Conceptos/Comparación de métodos de clustering]] guía lectura comparativa. El complemento [[03 - Herramientas/scikit-learn - Clustering por densidad]] conserva la práctica sintética, sin reemplazar mapas geográficos.
