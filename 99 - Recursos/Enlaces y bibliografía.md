---
tags: [tipo/recursos, estado/base]
---

# Enlaces y bibliografía

Bibliografía de trabajo para preparar el flujo de prácticas, no una nota de concepto ni una clase terminada. Las tres referencias siguientes fueron consultadas durante la preparación de esta base por el orquestador; el escritor utilizó esa evidencia, sin afirmar una nueva consulta web ni ejecución.

**Institución:** Esri. **Versión documentada:** ArcGIS Pro 3.6. **Fecha de consulta:** 2026-09-15. Antes de implementar un ejercicio, comprobar su versión instalada y leer la documentación exacta del método elegido.

## Data Engineering

[Get started with Data Engineering — Esri, ArcGIS Pro 3.6](https://pro.arcgis.com/en/pro-app/3.6/help/analysis/geoprocessing/data-engineering/quick-tour-of-data-engineering.htm).

**Secciones consultadas:** Open the Data Engineering view; Explore fields; Interact with statistics; Prepare data.

La vista permite explorar campos y estadísticas y acceder a selecciones, gráficos y herramientas desde las celdas de la tabla. Evidencia: “Right-click a cell in the table to view functionality related to each cell, including making selections, creating charts, and running tools.” Sirve para planificar exploración guiada antes del modelado.

La preparación puede modificar la capa: “Run the Calculate Field tool to add a new field or modify an existing field in the layer.” Por ello, el flujo docente debe usar copias de trabajo y preservar originales. Esta documentación describe una interfaz de ArcGIS Pro; **no demuestra que exista una API llamada `arcpy.DataEngineering`**.

## Gráficos ArcGIS para exploración

[What is the Charts module — Esri, ArcGIS Pro 3.6](https://pro.arcgis.com/en/pro-app/3.6/arcpy/charts/what-is-the-charts-module.htm).

**Contenido consultado:** descripción del módulo y subclases para explorar datos, entre ellas `arcpy.charts.Bar`, `Box`, `Histogram` y `Scatter`.

Respalda seleccionar gráficos ArcGIS según la pregunta y los campos reales de cada ejercicio. No exige usar todos los tipos en todas las clases. Antes de programar, consultar la página de la subclase exacta y sus parámetros, versión y requisitos. Estos gráficos complementan los mapas, no los sustituyen.

## Clase Chart heredada y notebooks

[Chart — Esri, ArcGIS Pro 3.6](https://pro.arcgis.com/en/pro-app/3.6/arcpy/classes/chart.htm).

**Secciones consultadas:** Summary; Legacy; Discussion; dataSource.

La advertencia Legacy indica: “As of ArcGIS Pro 2.9, the Chart class is deprecated and will not be updated for new functionality. It is recommended that you use the subclasses in the arcpy.charts module instead.” Para trabajo nuevo se prefieren esas subclases, no la clase heredada.

La documentación también señala: “Chart objects support rich representation in Notebooks and can be visualized graphically.” Esto respalda la posibilidad documentada de visualización, **no prueba que un notebook de este proyecto ya se haya ejecutado**. La fuente de datos y el comportamiento concreto deben verificarse para la subclase elegida.

## Contraste documental de prácticas anteriores

La [[99 - Recursos/Matriz - Análisis exploratorio y ArcGIS|Matriz EDA y ArcGIS]] conecta antecedentes de notas/notebooks de clases 7–12 con capacidades nativas y complementos justificados. Contiene fuentes oficiales Esri ArcGIS Pro 3.6, pandas 2.3.3 y SciPy 1.18.0 consultadas por el orquestador el 2026-09-15, con secciones y límites junto a cada capacidad. Es referencia de selección por práctica, no clase terminada ni ejecución; conserva discrepancias documentales que requieren comprobar la versión instalada. Las tres referencias originales de esta página se mantienen como E0 en la matriz.

Aplicar un subconjunto pertinente por práctica; no imponer inferencia espacial, diagnósticos supervisados o reducción dimensional como EDA básica. Verificar datos reales y distinguir interfaz manual, ArcPy documentado y ejecución comprobada. Una práctica requiere un notebook autónomo con salidas aisladas; la matriz no autoriza ejecutarlo.

## Cómo ampliar esta bibliografía

**Prioridad de investigación e implementación: ArcGIS primero.** Evaluar y registrar capacidades nativas de Data Engineering, gráficos/mapas y herramientas de geoprocesamiento contra la necesidad real, consultando documentación oficial Esri de la versión instalada. Separar interfaz manual de API documentada. Solo después justificar complementos Python por capacidad o método, leer su documentación oficial y comprobar dependencias; no borrar bibliotecas usadas en la fuente ni repetir todo automáticamente en Python. Una visualización ArcGIS bloqueada se consulta, no se sustituye silenciosamente.

Consultas de búsqueda orientativas, no referencias verificadas ni nuevas consultas realizadas; ajustar la versión al entorno:

- `site:pro.arcgis.com/en/pro-app/3.6/ "Data Engineering" "statistics"`
- `site:pro.arcgis.com/en/pro-app/3.6/arcpy/charts/ Histogram notebook`
- `site:pro.arcgis.com/en/pro-app/3.6/tool-reference/ "herramienta seleccionada"`
- Solo ante complemento justificado: `site:pandas.pydata.org/docs/ "operación seleccionada"`, `site:numpy.org/doc/ "operación seleccionada"` o `site:scikit-learn.org/stable/ "método seleccionado"`.

Verificar editor oficial, versión y pertinencia; abrir y leer la sección que respalda la afirmación antes de citar. Un fragmento de buscador no constituye evidencia. Registrar título, institución, enlace, sección, versión y fecha, y colocar la cita junto a la afirmación en la clase o concepto. Si una fuente es inaccesible o insuficiente, documentarlo y consultar; no inventar respaldo.

Las futuras referencias a grabaciones incluirán título, identidad y tiempo; las de PowerPoint, archivo y diapositiva. No publicar fuentes de terceros sin revisar permisos y recibir autorización.

## Clase 01 — fuentes reutilizadas en el material docente

[[01 - Clases/2026-09-14 - Clase 01 - Clustering espacial]] reúne citas próximas, cinco conceptos y dos herramientas. El catálogo canónico **E1–E14** está en [[99 - Recursos/Clase 01 - Fuentes y acuerdos#8. Referencias verificadas por el orquestador|referencias verificadas]]; las firmas, gráficos y cartografía están en su [[99 - Recursos/Clase 01 - Fuentes y acuerdos#10. Revisión vigente y referencias de implementación|sección API]]. Se reutilizan pasajes leídos el **2026-09-15**, sin nueva consulta web ni reproducción del listado completo aquí.

- E1–E5/E9/E10: DBSCAN, HDBSCAN, OPTICS, campos y origen espacial; distinguir implementación Esri Pro 3.6, sklearn 1.6 y explicación HDBSCAN 0.8.1.
- E6/E11: autocorrelación y límites de validación espacial; Roberts et al. (2017), pp. 913–919 y caso de alces de Alberta, no nueva práctica predictiva.
- E7/E8: refuerzo y entorno Pro; correcciones docentes P3/P5, sin instalaciones.
- E12–E14: escalado, generador sintético y contraste K-means; no ejecución K-means ni georreferenciación de lunas.

V13 conserva identidad y tiempos mediante localizador interno, no URL privada. Se exportaron cuatro diapositivas del PPT de referencia en modo solo lectura: 11/18/19/20. Tres se seleccionan para exposición; la 18 tiene diagrama inferior truncado y se conserva sin presentarla como completa. La nota identifica cada captura como referencia, no fotograma de video; correcciones P1/P2/P7 acompañan la interpretación. Acceso y exportación local no conceden derechos de redistribución.

[[99 - Recursos/Clase 01 - Resultados de prácticas]] es autoridad de cifras observadas; no atribuir a artículos o video métricas de los notebooks locales.

## Clase 03 — cubos espacio-temporales y patrones emergentes

**Fuente:** Clase 15 — *Cubos espacio-temporales y patrones emergentes*, 2026-06-25; docente fuente **José Sebastián Gómez Romero**, Diplomado GeoIA - Esri. Grabación identificada mediante localizador interno `20260625_225553UTC`, duración **1:53:36**, sin URL privada. Su consulta requiere acceso autorizado y no concede derechos de redistribución.

**Destino:** [[01 - Clases/2026-09-16 - Clase 03 - Cubos espacio-temporales y patrones emergentes|Clase 03]], 2026-09-16. **Docente:** Fabian Cetina. Borrador migrado, no clase procesada completa. La [[01 - Clases/2026-09-16 - Clase 03 - Cubos espacio-temporales y patrones emergentes#Procedencia, práctica y pendientes|procedencia de la nota]] registra acceso real al reproductor y revisión **parcial**: EDA 40:30–40:39, creación 45:00–45:10 y 46:50–47:00, escena COUNT 52:20–52:30, entre otros segmentos. No equivalen a cobertura docente completa.

Para construir e interpretar el cubo, consulta las [[01 - Clases/2026-09-16 - Clase 03 - Cubos espacio-temporales y patrones emergentes#Referencias|referencias junto a la clase]]: E1, E2, E4 y E5 reutilizan documentación Esri **ArcGIS Pro 3.6** sobre agregación, Emerging, Gi* y OHA, con secciones y consultas registradas el 2026-09-17. E3 conserva una referencia `latest`, sin atribuirle verificación de versión 3.6. Las seis diapositivas son exportaciones de la presentación de referencia, no fotogramas del video. Los resultados históricos y los actuales con fallo de cierre del kernel se distinguen en la nota y el notebook.

## Clase 04 · Aprendizaje supervisado y Random Forest

[[2026-09-21 - Clase 04 - Aprendizaje supervisado y Random Forest geoespacial|Clase 04, 21/09/2026]] conecta estas referencias con la práctica Coiba. Material para revisión, sin aprobación académica; ejecución histórica 17/17 con raster y corrección residual focal posterior; video parcial y excluido de esta preparación. La disposición completa de Notebook/Obsidian sigue parcialmente comprobada. Las nuevas entradas bibliográficas siguientes corresponden a documentación web ArcGIS y estadística; se reutiliza la consulta del **2026-09-21**, sin nueva investigación.

- **Esri — Forest-based and Boosted Classification and Regression.** ArcGIS Pro **3.6**, Usage, Parameters y Syntax; tipos de predicción, parámetros y porcentaje retenido para validación. https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-statistics/forestbasedclassificationregression.htm.
- **Esri — How Forest-based and Boosted Classification and Regression works.** ArcGIS Pro **3.6**, funcionamiento, validación e importancia de variables. https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-statistics/how-forest-works.htm.
- **Esri — Band Arithmetic function.** ArcGIS Pro **3.6**, fórmulas y bandas de NDVI, EVI, SAVI, MNDWI y SR. https://pro.arcgis.com/en/pro-app/3.6/help/analysis/raster-functions/band-arithmetic-function.htm.
- **Esri — Extract Multi Values to Points.** ArcGIS Pro **3.6**, Usage y Parameters; referencia espacial por raster, interpolación bilineal y modificación de puntos de entrada. https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-analyst/extract-multi-values-to-points.htm.
- **Leo Breiman y Adele Cutler — Random Forests.** University of California, Berkeley; introducción, combinación de árboles, OOB e importancia; recurso web sin versión declarada. https://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm.

Los créditos de grabación y diapositivas, con sus localizadores exactos, están junto a los recursos en la nota; el usuario confirmó expresamente la redistribución de Coiba y las capturas fuente de Francisco Javier Anzola. No se redistribuyen los PPTX ni se acredita procedencia GEDI. Consulte también [[03 - Herramientas/ArcGIS Pro - Forest-based and Boosted Classification and Regression|la herramienta aplicada]] y la [procedencia de Coiba](datos/clase_04/README.md).

## Conexiones

- [[00 - Índice|Índice]]: entrada al bloque.
- [[Templates/Plantilla - Clase|Plantilla]]: aplica estas referencias al diseño de cada práctica.
- [[99 - Recursos/datos/README|Guía de datos]]: protege originales y documenta procedencia.
