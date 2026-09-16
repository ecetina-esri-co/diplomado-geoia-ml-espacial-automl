---
tags: [tipo/recurso, estado/revision, tema/geoia]
---

# Clase 01 — Resultados de prácticas

**Evidencia vigente de P02 autónoma completa integrada al material docente.** [[01 - Clases/2026-09-14 - Clase 01 - Clustering espacial|Nota central]]: ejecución `ejecucion_20260915T220908_d62e311d`, 25 celdas de código, 355.40 s de kernel, tres métodos y secuencia DOCX completa. Los 13 PNG tienen inspección registrada; la comprobación técnica y el renderizado local aislado de Mermaid/SVG y de las notas están completos. Queda revisión académica humana; no se comprobó la disposición nativa de Obsidian. P01 se conserva. No se repitieron notebooks ni geoprocesamiento para esta integración.

Procedencia, decisiones y fuentes: [[99 - Recursos/Clase 01 - Fuentes y acuerdos]].

## Ejecuciones observadas

Kernels nuevos, secuenciales, intérprete explícito de ArcGIS Pro con `-X utf8 -B`; sin instalar kernelspecs.

### P01

[[99 - Recursos/notebooks/Clase 01 - Practica 01 - Comparacion DBSCAN HDBSCAN sintetica.ipynb|Notebook P01]]

Estado: **ejecutado**. Celdas con ejecución: 10; tiempo del kernel: 76.76 s.

Entorno observado: `{"python": "3.13.7", "arcgis_pro": "3.6.2", "licencia": "ArcInfo", "paquetes": {"numpy": "2.2.0", "pandas": "2.3.0", "scikit-learn": "1.6.1", "matplotlib": "3.9.4", "nbclient": "0.8.0", "ipykernel": "6.29.5"}}`.

Tiempo de operaciones del notebook: 40.36 s; no es ensayo docente de 120 minutos.

Evidencia agregada: `99 - Recursos/salidas_clase_01/practica_01/ejecucion_20260915T164803_70b07f40/evidencia.json`.

P01 exclusivamente sintética por decisión humana: sin datos geográficos ni mapas ficticios. La excepción no elimina gráficos ArcGIS ni modifica P02.

Base: `{"DBSCAN": {"filas": 200, "clusters": 5, "ruido": 58, "porcentaje_ruido": 29.0, "mayor_cluster": 66}, "HDBSCAN": {"filas": 200, "clusters": 8, "ruido": 108, "porcentaje_ruido": 54.0, "mayor_cluster": 18}}`.
Tipos DBSCAN: `{"nucleo": 108, "frontera": 34, "ruido": 58}`.

Sensibilidades preservadas: 12; resultados controlados: 14 (dos métodos por caso).

#### Visuales producidos

PNG ArcGIS nativos; Matplotlib solo complementa los experimentos sintéticos. Existencia no equivale a revisión visual humana.

- [[99 - Recursos/salidas_clase_01/practica_01/ejecucion_20260915T164803_70b07f40/arcgis_escalado.png|arcgis_escalado.png]]
- [[99 - Recursos/salidas_clase_01/practica_01/ejecucion_20260915T164803_70b07f40/arcgis_original.png|arcgis_original.png]]
- [[99 - Recursos/salidas_clase_01/practica_01/ejecucion_20260915T164803_70b07f40/arcgis_sensibilidad_clusters.png|arcgis_sensibilidad_clusters.png]]
- [[99 - Recursos/salidas_clase_01/practica_01/ejecucion_20260915T164803_70b07f40/arcgis_sensibilidad_ruido.png|arcgis_sensibilidad_ruido.png]]
- [[99 - Recursos/salidas_clase_01/practica_01/ejecucion_20260915T164803_70b07f40/matplotlib_base.png|matplotlib_base.png]]
- [[99 - Recursos/salidas_clase_01/practica_01/ejecucion_20260915T164803_70b07f40/matplotlib_control_muestra.png|matplotlib_control_muestra.png]]
- [[99 - Recursos/salidas_clase_01/practica_01/ejecucion_20260915T164803_70b07f40/matplotlib_control_ruido.png|matplotlib_control_ruido.png]]
- [[99 - Recursos/salidas_clase_01/practica_01/ejecucion_20260915T164803_70b07f40/matplotlib_sensibilidad_dbscan.png|matplotlib_sensibilidad_dbscan.png]]
- [[99 - Recursos/salidas_clase_01/practica_01/ejecucion_20260915T164803_70b07f40/matplotlib_sensibilidad_hdbscan.png|matplotlib_sensibilidad_hdbscan.png]]

### P02

[[99 - Recursos/notebooks/Clase 01 - Practica 02 - Clustering Bomberos con ArcGIS Pro.ipynb|Notebook P02]]

Estado: **ejecutado**. Celdas: 25; kernel nuevo: 355.40 s.

P02 autónoma: EDA → DBSCAN → selección sin ruido → MeanCenter → Identity NO_FID → Statistics COUNT → AddJoin → CopyFeatures → HDBSCAN → OPTICS con sensibilidad automática. Jurisdicciones preparadas y comprobadas, entrada de solo lectura; sin reparación dentro del notebook.

Historia preservada: [[99 - Recursos/salidas_clase_01/practica_02/Resultados_historicos_antes_autonomia.md|informe anterior]] y [[99 - Recursos/salidas_clase_01/practica_02/Notebook_historico_20260915_171532.ipynb|notebook anterior]]. Los resultados nuevos no se atribuyen a ejecuciones históricas.

Evidencia agregada: [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/evidencia.json|JSON de la ejecución vigente]].

**Lectura comparativa:** DBSCAN 20 grupos/13 384 ruidos (14.80%), HDBSCAN 3/1 187 (1.31%) y OPTICS 29/17 561 (19.42%) describen distintas particiones de 90 443 filas, no grados de exactitud. Los mayores grupos contienen 67 478, 88 919 y 52 889 filas respectivamente; menos ruido puede acompañar una agrupación demasiado amplia para una pregunta local. Los tiempos observados 24.35/122.76/69.16 s no establecen un ranking universal.

**Centros y conteos:** 20 centros medios y 20 filas Identity/finales, sin ausencias, multiplicidad ni proximidad a frontera dentro de 0.001 m. COUNT suma 77 059 puntos asignados; se calculó antes de la unión y no sobre los centros. Si hubiese varias coincidencias por centro, sumar filas unidas repetiría población. Son coincidencias geométricas, no asignación de todos los registros a una estación.

**Parámetro frente a resultado:** pese al mínimo DBSCAN 100, los grupos 10/15/16/18/20 contienen 81/99/66/96/76 filas. Recuento independiente, Statistics y COUNT materializado concuerdan. La causa no está diagnosticada y los resultados no se reclasificaron; no ocultar el límite con una explicación supuesta. El DOCX conserva sus cifras impresas como fuente, no como resultado de esta ejecución.

**OPTICS:** sensibilidad omitida en la llamada; mensaje observado de elegida 1, segunda opción 0. Perfil nativo de REACHORDER/REACHDIST con 90 443 valores representables; orden algorítmico, no tiempo o ruta. Valles no son por sí solos zonas operativas.

Entorno observado: `{"arcgis_pro": "3.6.2", "python": "3.13.7", "licencia": "ArcInfo"}`.

Operaciones del notebook: 333.30 s; no es ensayo docente de 120 minutos.

**parametros:** `{"DBSCAN": {"minimo": 100, "distancia_m": 350}, "HDBSCAN": {"minimo": 100}, "OPTICS": {"minimo": 100, "distancia_m": 350, "sensibilidad": "automatica_omitida"}}`.

**perfil_antes:** `{"filas": 90443, "nulos": {"IncidentesBomberos_FECHA": 0, "IncidentesBomberos_NUMERO_INC": 60711, "IncidentesBomberos_ESTACION": 0, "Incidentes_Bomberos_AddSpatialJoin_ESTACION": 0}, "id_cero": 0, "ids_no_nulos": {"distintas": 29165, "claves_repetidas": 494, "filas_excedentes": 567}, "xy": {"distintas": 82770, "claves_repetidas": 5670, "filas_excedentes": 7673}, "xy_no_finitas": 0, "fecha_min": "2022-01-01T00:00:00", "fecha_max": "2024-12-31T00:00:00", "estaciones": {"B-1  CHAPINERO": 7260, "B-10  MARICHUELA": 4382, "B-11 LA CANDELARIA": 6219, "B-12  SUBA": 5839, "B-13  CAOBOS SALAZAR": 7706, "B-14  BICENTENARIOLA INDEPENDENCIA": 5250, "B-15  GARCÉS NAVAS": 5369, "B-16 VENECIA": 3218, "B-17  CENTRO HISTÓRICO": 3087, "B-2  CENTRAL": 4677, "B-3  RESTREPO": 4802, "B-4  PUENTE ARANDA": 3669, "B-5 KENNEDY": 8705, "B-6  FONTIBÓN": 4441, "B-7  FERIAS": 6205, "B-8 BOSA": 5169, "B-9  BELLAVISTA": 4445}, "jurisdiccion_heredada": {"B-1": 7260, "B-10": 4382, "B-11": 6219, "B-12": 5839, "B-13": 7706, "B-14": 5250, "B-15": 5369, "B-16": 3218, "B-17": 3087, "B-2": 4677, "B-3": 4802, "B-4": 3669, "B-5": 8705, "B-6": 4441, "B-7": 6205, "B-8": 5169, "B-9": 4445}, "anios": {"2022": 29890, "2023": 30821, "2024": 29732}, "wkid": 9377, "crs": "MAGNA-SIRGAS_2018_Origen-Nacional", "unidades": "Meter"}`.

**perfil_despues:** `{"filas": 90443, "nulos": {"IncidentesBomberos_FECHA": 0, "IncidentesBomberos_NUMERO_INC": 60711, "IncidentesBomberos_ESTACION": 0, "Incidentes_Bomberos_AddSpatialJoin_ESTACION": 0}, "id_cero": 0, "ids_no_nulos": {"distintas": 29165, "claves_repetidas": 494, "filas_excedentes": 567}, "xy": {"distintas": 82770, "claves_repetidas": 5670, "filas_excedentes": 7673}, "xy_no_finitas": 0, "fecha_min": "2022-01-01T00:00:00", "fecha_max": "2024-12-31T00:00:00", "estaciones": {"B-1  CHAPINERO": 7260, "B-10  MARICHUELA": 4382, "B-11 LA CANDELARIA": 6219, "B-12  SUBA": 5839, "B-13  CAOBOS SALAZAR": 7706, "B-14  BICENTENARIOLA INDEPENDENCIA": 5250, "B-15  GARCÉS NAVAS": 5369, "B-16 VENECIA": 3218, "B-17  CENTRO HISTÓRICO": 3087, "B-2  CENTRAL": 4677, "B-3  RESTREPO": 4802, "B-4  PUENTE ARANDA": 3669, "B-5 KENNEDY": 8705, "B-6  FONTIBÓN": 4441, "B-7  FERIAS": 6205, "B-8 BOSA": 5169, "B-9  BELLAVISTA": 4445}, "jurisdiccion_heredada": {"B-1": 7260, "B-10": 4382, "B-11": 6219, "B-12": 5839, "B-13": 7706, "B-14": 5250, "B-15": 5369, "B-16": 3218, "B-17": 3087, "B-2": 4677, "B-3": 4802, "B-4": 3669, "B-5": 8705, "B-6": 4441, "B-7": 6205, "B-8": 5169, "B-9": 4445}, "anios": {"2022": 29890, "2023": 30821, "2024": 29732}, "wkid": 9377, "crs": "MAGNA-SIRGAS_2018_Origen-Nacional", "unidades": "Meter"}`.

**geometria:** `{"puntos": 0, "jurisdicciones_preparadas": 0}`.

**DBSCAN:** `{"filas": 90443, "clusters": 20, "ruido": 13384, "porcentaje_ruido": 14.798270734053492, "mayor_cluster": 67478, "conteos": {"-1": 13384, "1": 67478, "2": 579, "3": 2335, "4": 459, "5": 1175, "6": 338, "7": 956, "8": 2175, "9": 232, "10": 81, "11": 230, "12": 132, "13": 161, "14": 182, "15": 99, "16": 66, "17": 107, "18": 96, "19": 102, "20": 76}}`.

**centros:** `{"centros": 20, "filas_identity": 20, "sin_jurisdiccion": [], "multiples": {}, "fronteras": [], "tolerancia_xy_m": 0.001, "filas_finales": 20, "grupos_menores_100": {"10": 81, "15": 99, "16": 66, "18": 96, "20": 76}}`.

**conteos_centros:** `{"1": 67478, "2": 579, "3": 2335, "4": 459, "5": 1175, "6": 338, "7": 956, "8": 2175, "9": 232, "10": 81, "11": 230, "12": 132, "13": 161, "14": 182, "15": 99, "16": 66, "17": 107, "18": 96, "19": 102, "20": 76}`.

**HDBSCAN:** `{"filas": 90443, "clusters": 3, "ruido": 1187, "porcentaje_ruido": 1.3124288225733334, "mayor_cluster": 88919, "conteos": {"-1": 1187, "1": 146, "2": 88919, "3": 191}}`.

**OPTICS:** `{"filas": 90443, "clusters": 29, "ruido": 17561, "porcentaje_ruido": 19.416649160244575, "mayor_cluster": 52889, "conteos": {"-1": 17561, "1": 3935, "2": 134, "3": 992, "4": 357, "5": 280, "6": 379, "7": 699, "8": 1279, "9": 638, "10": 354, "11": 202, "12": 340, "13": 120, "14": 226, "15": 438, "16": 52889, "17": 708, "18": 579, "19": 2335, "20": 454, "21": 1172, "22": 337, "23": 956, "24": 2175, "25": 228, "26": 225, "27": 124, "28": 155, "29": 172}}`.

**comparacion:** `{"DBSCAN_HDBSCAN": {"filas_enlazadas": 90443, "jaccard_copertenencia": 0.5775689341249255}, "DBSCAN_OPTICS": {"filas_enlazadas": 90443, "jaccard_copertenencia": 0.6199117861058122}, "HDBSCAN_OPTICS": {"filas_enlazadas": 90443, "jaccard_copertenencia": 0.3580417895526128}}`.

**tiempos_herramientas:** `{"CopyFeatures_entrada": 9.4378757999948, "CheckGeometry_puntos": 3.9990455000079237, "CheckGeometry_jurisdicciones_preparadas": 1.2603791000001365, "FieldStatisticsToTable": 5.444556299989927, "arcgis_estaciones": 2.757438800006639, "arcgis_jurisdicciones": 0.3470914000063203, "arcgis_anios": 0.37820920000376645, "arcgis_mapa_entrada": 4.1682385000021895, "DBSCAN": 24.354128100007074, "Seleccion_sin_ruido": 0.4950736000027973, "MeanCenter": 10.338556699993205, "Identity": 1.583090700005414, "Statistics_COUNT": 1.775981500002672, "AddJoin": 0.4587169000005815, "CopyFeatures_centros": 0.8825136000086786, "arcgis_mapa_dbscan": 3.351400100000319, "arcgis_poblacion_dbscan": 0.12516579999646638, "HDBSCAN": 122.76150529998995, "arcgis_mapa_hdbscan": 3.757405500000459, "arcgis_poblacion_hdbscan": 0.11696980000124313, "arcgis_hist_prob": 0.6222878999979002, "arcgis_hist_outlier": 0.6069095999991987, "OPTICS": 69.16488620000018, "arcgis_mapa_optics": 4.103954299993347, "arcgis_poblacion_optics": 0.2174109000043245, "arcgis_alcanzabilidad": 21.98581440000271}`.

**histogramas_asignados:** `{"asignados": 89256, "prob_validos": 89256, "prob_mediana": 1.0, "prob_mayor_igual_09": 86731, "outlier_mediana": 0.02555081936288076}`.

**alcanzabilidad:** `{"campo_orden": "REACHORDER", "campo_distancia": "REACHDIST", "filas": 90443, "no_representables": 0}`.

Integridad: `99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/integridad_antes.json` y `integridad_despues.json`; original/plantilla comprobados después del cierre del kernel. `protegidos_antes.json`/`protegidos_despues.json` incluyen jurisdicción preparada y P01; `integridad_notebook_antes.json`/`integridad_notebook_despues.json` comprueban las tres entradas desde el notebook.

#### Visuales producidos

- [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/arcgis_estaciones.png|arcgis_estaciones.png]]
- [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/arcgis_jurisdicciones.png|arcgis_jurisdicciones.png]]
- [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/arcgis_anios.png|arcgis_anios.png]]
- [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/arcgis_mapa_entrada.png|arcgis_mapa_entrada.png]]
- [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/arcgis_mapa_dbscan.png|arcgis_mapa_dbscan.png]]
- [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/arcgis_poblacion_dbscan.png|arcgis_poblacion_dbscan.png]]
- [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/arcgis_mapa_hdbscan.png|arcgis_mapa_hdbscan.png]]
- [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/arcgis_poblacion_hdbscan.png|arcgis_poblacion_hdbscan.png]]
- [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/arcgis_hist_prob.png|arcgis_hist_prob.png]]
- [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/arcgis_hist_outlier.png|arcgis_hist_outlier.png]]
- [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/arcgis_mapa_optics.png|arcgis_mapa_optics.png]]
- [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/arcgis_poblacion_optics.png|arcgis_poblacion_optics.png]]
- [[99 - Recursos/salidas_clase_01/practica_02/ejecucion_20260915T220908_d62e311d/arcgis_alcanzabilidad.png|arcgis_alcanzabilidad.png]]

## Límites y comprobación pendiente

- P01: perturbación gaussiana no equivale a ruido −1; escalado no implica normalidad. IDs y colores nominales no emparejan métodos.
- P02 conserva todas las filas; número nullable y coincidencias XY no prueban duplicación de eventos. Estación reportada no equivale automáticamente a despacho o jurisdicción espacial.
- 2022–2024 se acumula espacialmente; no se ejecuta clustering espacio-temporal. DBSCAN 350 m no garantiza radio total del grupo; HDBSCAN 100 no impone esa distancia.
- P02 ejecutó histogramas de 30 intervalos sobre 89 256 asignados: PROB/OUTLIER no son valores p. Jaccard de co-pertenencia DBSCAN–HDBSCAN 0.57757, DBSCAN–OPTICS 0.61991 y HDBSCAN–OPTICS 0.35804 son descriptivos y están condicionados por grupos muy grandes; no establecen superioridad ni exactitud territorial.
- Data Engineering UI no es una dependencia de ejecución; se emplearon FieldStatisticsToTable, cursores y gráficos ArcGIS. La P02 vigente sí ejecutó OPTICS, centros medios, Identity, Statistics COUNT/AddJoin/CopyFeatures. No se ejecutó subclustering ni se tomaron decisiones de localización de estaciones.
- Referencias API: registro de fuentes, sección 10, y ayuda oficial Python instalada Pro 3.6.2 para MeanCenter, Identity, Statistics, AddJoin, Geometry y Line, leída mediante inspect.getdoc el 15/09/2026. Chrome DevTools no abrió por conflicto de instancia; no se acredita revisión nueva del video ni cierre de clase.
- Cuatro visuales P01 inspeccionados con la herramienta de imágenes: `arcgis_original.png`, `arcgis_sensibilidad_clusters.png`, `matplotlib_base.png` y `matplotlib_sensibilidad_hdbscan.png`. Se vieron ejes, categorías/títulos legibles, ruido negro y paneles diferenciados; la barra nativa muestra las doce variantes. No se inspeccionaron visualmente los otros cinco PNG. Todos los nueve pasaron validación de formato, dimensiones e incorporación al notebook.
- Licencias y privacidad de redistribución pendientes. Sin publicación ni cierre de la clase.

## Validación vigente — P02 autónoma completa

Ejecución vigente: `ejecucion_20260915T220908_d62e311d`. Primera ejecución completa preservada: `ejecucion_20260915T215908_c58e2caa` (278.36 s). Se realizó una segunda ejecución para comprobar la corrección de rutas externas fuera del vault, etiquetas de estación sin truncación, separación del pie cartográfico y validación de COUNT materializado. No hubo ejecuciones P01 ni intentos fallidos nuevos. Comando exacto, ejecutado dos veces:

```bash
PYTHONNOUSERSITE=1 "C:/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe" -X utf8 -B -s "99 - Recursos/notebooks/ejecutar_clase01.py" --practica 02
```

Salida 0: 25 celdas, kernel nuevo 355.40 s; operaciones 333.30 s. DBSCAN 24.35 s, HDBSCAN 122.76 s, OPTICS 69.16 s. Se completó la secuencia DOCX sin ModelBuilder manual ni importación de auxiliar personalizado en el notebook. Se conserva `notebook_ejecutado.ipynb` en la carpeta de la ejecución; el notebook principal añade después solo interpretación Markdown, sin cambiar código ni salidas observadas.

Validaciones ejecutadas con el mismo prefijo `PYTHONNOUSERSITE=1` e intérprete/opciones `-X utf8 -B -s`:

- `99 - Recursos/notebooks/verificar_clase01.py --estructura`: salida 0 antes de ejecutar; schema, sintaxis, autonomía P02, secuencia, parámetros y casos negativos. Se preservaron las pruebas históricas y las aserciones P01.
- `99 - Recursos/notebooks/verificar_clase01.py`: salida 0 después; P01 validada sin ejecutarla, P02 con 13 PNG incrustados válidos, cobertura de tres modelos, 20 centros y cuatro APRX, integridad de entradas y P01.
- Inspección ArcPy de solo lectura: `CentrosIdentidadDBSCAN_CLUSTER_ID`, `ConteosDBSCAN_CLUSTER_ID` y `ConteosDBSCAN_COUNT_CLUSTER_ID` materializados; los 20 COUNT coinciden con el recuento independiente de puntos asignados. Suma 77 059, excluyendo 13 384 filas de ruido.
- SHA-256 de P01 antes/después: `39c2eaab4caa0cc274de4b1b03cca63078c3e10b3ed91a7c5787fb51a8b382e1`, idéntico. Original, jurisdicciones preparadas y plantilla también íntegros; cero incidencias CheckGeometry de puntos y polígonos preparados.
- Inspección visual efectiva: abiertos los 13 PNG de la primera ejecución completa; después, abiertos los cuatro mapas y el gráfico de estaciones corregidos de la ejecución vigente. Los otros ocho PNG actuales son idénticos píxel a píxel a los ya inspeccionados (comparación PIL ImageChops de solo lectura). Mapas 2880×1980, gráficos 1600×1000; contenido, títulos, ejes y leyendas legibles. Ahora los códigos B-1 a B-17 aparecen completos; el CSV y la tabla conservan nombres completos. Pies separados del marco. Los grupos pequeños quedan comprimidos por el dominante; el encuadre común de incidentes no muestra toda la extensión sur de los polígonos. No confundir esos límites con resultados vacíos.

**Resultados actuales:** DBSCAN 20 grupos/13 384 ruido, HDBSCAN 3/1 187, OPTICS 29/17 561. Todos conservan 90 443 claves técnicas. Identity produjo 20 filas para 20 centros, sin centros sin jurisdicción, filas múltiples ni centros a frontera dentro de 0.001 m. OPTICS informó sensibilidad automática elegida 1, segunda opción 0; no se fijó ese valor en la llamada. Perfil real `REACHORDER`/`REACHDIST`, 90 443 valores representables.

**Límite observado que no debe ocultarse:** DBSCAN devolvió cinco grupos menores de 100 filas: 10→81, 15→99, 16→66, 18→96 y 20→76. COUNT y la copia materializada confirman esos tamaños. Se preservó mínimo 100/350 m sin reclasificar resultados. La causa específica no fue diagnosticada; no afirmar que todos los grupos finales cumplen un conteo mínimo de 100 ni atribuir una causa no comprobada. Se documenta en la interpretación del notebook.

Avisos no fatales: DeprecationWarning de nbclient y MissingIDFieldWarning inicial (nbformat añadió IDs al guardar el notebook ejecutado). No se activó TDD estricto; esta evidencia es validación, no RED/GREEN. Esta evidencia de implementación no acredita renderizado final de las notas ni aprobación académica. La integración documental posterior actualizó nota central, registro, herramienta y concepto afectados, sin nuevas corridas ni modificación de AGENTS, skills, P01 o Clase 02; no se publica.

### Cierre técnico — verificación independiente posterior

El verificador independiente ejecutó `verificar_clase01.py --estructura` y `verificar_clase01.py` con Python de ArcGIS Pro, `PYTHONNOUSERSITE=1` y `-X utf8 -B -s`: ambos correctos, sin reejecutar notebooks ni geoprocesamiento. Confirmó autonomía, secuencia, sintaxis, ausencia de errores, nueve PNG P01 y trece P02, evidencia vigente e integridad de entradas. Abrió los cinco PNG P01 antes no inspeccionados: todos legibles. El orquestador confirmó P02 con 25 celdas, 355.40 s, error nulo y ejecución `ejecucion_20260915T220908_d62e311d`; SHA-256 de P01 idéntico al indicado arriba.

Una segunda verificación independiente renderizó e inspeccionó nueve bloques Mermaid y cinco SVG únicos de la clase, cinco conceptos y dos herramientas con Mermaid 11.13.0 instalado en el ASAR de Obsidian 1.13.7 y Chrome headless aislado, sin conexión ni instalaciones. Todos legibles, sin recortes; enlaces wiki, anclas e incrustaciones de las ocho notas resueltos excluyendo bloques de código. Clase y cinco conceptos contienen Mermaid y gráfica interpretada. La evidencia visual fueron capturas inspeccionadas, no aserciones DOM (la captura DOM quedó vacía); el orquestador también abrió la primera vista. El conflicto de perfil de Chrome MCP impidió usar ese navegador compartido, no el renderizado aislado. **No se comprobó la disposición en la interfaz nativa de Obsidian.** Este cierre no agrega revisión de video ni altera su procedencia o la evidencia de seis diapositivas. Material listo para revisión académica humana, no aprobado ni publicado.

## Validación histórica anterior a la corrección P02

Intérprete para los tres comandos Python: `C:/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe -X utf8 -B`.

| Comando/acción | Resultado |
| --- | --- |
| `99 - Recursos/notebooks/verificar_clase01.py --estructura` | Correcto: ambos schemas, sintaxis, comentarios, explicación previa, parámetros exactos; casos negativos de aislamiento y co-pertenencia |
| `99 - Recursos/notebooks/ejecutar_clase01.py` | Salida 1: P01 completa; P02 detenida por puerta geométrica; sin reintentos de modelado |
| `99 - Recursos/notebooks/verificar_clase01.py` | P01 validada con nueve PNG; salida 1 esperada porque P02 está incompleta |
| `git diff --check` | Salida 0; avisos LF→CRLF sobre `.gitignore` y `README.md` preexistentes. Los archivos nuevos siguen sin seguimiento: este comando no valida su whitespace |
| Inspección de fuente notebook original | 24 celdas leídas solo como fuente, sin ejecutar originales ni reutilizar sus salidas |
| Introspección de diagnóstico posterior | Primer comando tuvo SyntaxError por escape de nueva línea; segundo consultó correctamente las salidas y tabla, solo lectura |

No se activó TDD estricto; las comprobaciones anteriores son validación histórica, no evidencia RED/GREEN. La decisión posterior de continuar sin reparar sustituye el bloqueo operativo, no la falta de integridad del intento histórico.

## Validación histórica de P02 — continuación anterior sin reparación

Mismo intérprete absoluto Pro y opciones `-X utf8 -B` indicados arriba. No se ejecutó P01 ni se escribieron sus archivos o salidas; el informe conserva su sección y referencia histórica explícita.

| Comando/acción | Resultado observado |
| --- | --- |
| `99 - Recursos/notebooks/verificar_clase01.py --estructura` | Salida 0 antes del modelado: geometría por CLASS, puntos/desconocidos fatales, contexto advertido; selector cerrado P02, baseline ausente/diferente fatal y finally tras error simulado |
| `99 - Recursos/notebooks/ejecutar_clase01.py --practica 02` | Intento inicial y primer reintento: salida 1 en celda 8, error de DLL pyarrow. Segundo reintento: salida 0, 13 celdas, 113.29 s; total tres intentos, sin más reejecuciones |
| `99 - Recursos/notebooks/verificar_clase01.py` | Salida 0: P01 y P02 con nueve PNG válidos e incorporados cada una; cobertura P02 íntegra, evidencia vinculada a run_id y hashes originales actuales iguales |
| `git diff --check` | Salida 0; avisos LF→CRLF preexistentes de `.gitignore`/`README.md`. El verificador también comprobó whitespace de los seis archivos propios nuevos, que Git aún no incluye en el diff |
| Introspección de imports, sin ejecución de prácticas | ArcPy seguido de pyarrow resolvía paquete externo de usuario y falló; excluyendo user-site se encontró pyarrow de Pro y la importación funcionó |

**Integridad también en fallos nuevos:** `ejecucion_20260915T171228_d0260bbb` (26.74 s) y `ejecucion_20260915T171359_94e151e8` (25.62 s) conservan `integridad_antes.json`/`integridad_despues.json` con coincidencia. No confundirlos con el intento histórico anterior sin baseline. La hipótesis inicial de codificación CSV no resolvió el error; aislar paquetes externos del usuario sí permitió la ejecución. Aviso DeprecationWarning de nbclient no fatal; dos kernels fallidos emitieron error de finalización Python, sin impedir el finally del runner.

### Inspección visual histórica — ejecución 20260915T171532

Se abrieron con herramienta de imagen los tres mapas P02 (`arcgis_mapa_entrada.png`, `arcgis_mapa_dbscan.png`, `arcgis_mapa_hdbscan.png`) y tres gráficos representativos (`arcgis_estaciones.png`, `arcgis_poblacion_dbscan.png`, `arcgis_hist_prob.png`) de aquella ejecución histórica. Mapas de 2520×1800 y gráficos de 1400×850: datos visibles, no vacíos; títulos, ejes y leyendas de grupos legibles. Mismo encuadre: DBSCAN separa más grupos y ruido periférico; HDBSCAN concentra la mayoría en un gran grupo. No inferir riesgo ni límites operativos.

**Limitaciones visuales explícitas:** en los mapas de modelos se trunca el rótulo largo de contexto dentro de la segunda columna de leyenda; el pie completo de ambos conserva «contexto no validado; 1 auto-intersección reportada; no son límites certificados; sin estadísticas poligonales». La línea superior del pie queda próxima al borde del mapa, pero es legible. Las barras de estaciones abrevian nombres largos, aunque conservan códigos B-1 a B-17 y el CSV agregado contiene nombres completos. El gráfico DBSCAN hace visible el predominio del grupo 1; los grupos pequeños no deben interpretarse como vacíos. PROB se concentra cerca de 1 (mediana 1), no es certeza causal. No se inspeccionaron visualmente los otros tres gráficos P02, aunque todos aprobaron formato, dimensiones e incrustación.

Siguiente paso histórico del orquestador (sustituido por el cierre técnico anterior): comprobación visual final de Mermaid/SVG y revisión académica de la [[01 - Clases/2026-09-14 - Clase 01 - Clustering espacial|nota y conceptos escritos]]. Agenda estimada de 120 minutos, no ensayada; no se autoriza publicación. La primera tanda produjo cuatro capturas PPT de referencia exportadas y abiertas, con tres seleccionadas y diagrama inferior truncado de la 18 declarado. La ampliación autorizada añadió 8/9/17, exportadas a 1920×1080 y abiertas: contenido completo y legible, sin recortes observados; PPTX con SHA-256 idéntico antes/después según el registro de fuentes. La selección vigente de seis, 8/9/11/17/19/20, aparece después del encabezado y antes de objetivos/agenda; la 18 sigue archivada, sin exposición. Son ilustraciones del PPTX, no fotogramas ni nuevas salidas de Bomberos. Se preservan las ejecuciones y sus límites históricos sin nuevas corridas; comprobación visual final de Mermaid/SVG y revisión académica aún pendientes.
