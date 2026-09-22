# Clase 04 · Resultados seleccionados

Estas copias acompañan la [clase](../../../01%20-%20Clases/2026-09-21%20-%20Clase%2004%20-%20Aprendizaje%20supervisado%20y%20Random%20Forest%20geoespacial.md) y el [notebook autónomo](../../notebooks/Clase%2004%20-%20Practica%2001%20-%20Random%20Forest%20geoespacial.ipynb). No son una nueva ejecución ni un producto de biomasa certificado. **Docente:** Fabian Cetina. Estado: borrador para revisión humana, sin aprobación académica.

## Qué muestran

| Archivo | Lectura y alcance |
|---|---|
| [Mapa raster](arcgis_raster_agbd.png) | Predicción exploratoria en grises; los huecos son NoData, no biomasa cero. |
| [Histograma raster](arcgis_raster_histograma.png) | 50.000 píxeles finitos seleccionados sistemáticamente; no validación retenida. |
| [Reporte TRAIN](clase_04_rf_diagnostico_arcgis.html) | Diagnósticos del modelo con campos extraídos. |
| [Reporte raster](clase_04_raster_diagnostico_arcgis.html) | Diagnósticos de otro ajuste con rasters, no reutilización del SSM anterior. |
| [Métricas de la capa TRAIN](clase_04_metricas_entrenamiento.csv) | MAE 52,374470; RMSE 74,247486; error medio −1,948037; R² 0,766611. No corresponden al subconjunto retenido. |
| [Residuales corregidos](arcgis_residuales.png) y [comprobación focal](residuales_resultado.json) | Representación corregida de resultados existentes, sin entrenar otra vez. |
| [Mapa AGBD histórico](historico_arcgis_agbd.png) | Observaciones anteriores a la ampliación raster; conserva el rótulo genérico original. |
| [Dispersión histórica AGBD–NDVI](historico_arcgis_agbd_ndvi.png) | Relación observada, no causalidad; misma ejecución histórica que el mapa anterior. |

AGBD, residuales, MAE y RMSE se interpretan en **Mg/ha por confirmación del usuario**, no por metadatos ni como prueba de procedencia GEDI. No se convirtieron los valores.

## Evidencia y límites

- **Ejecución histórica integral:** 17/17 celdas exitosas, kernel nuevo, ArcGIS Pro 3.6.2 / ArcInfo, aproximadamente 320 segundos. Incluye TRAIN y PREDICT_RASTER. Las salidas y contadores están integrados en el notebook autoral; esta publicación no reejecuta modelos.
- **Entradas y selección:** 4.946 observaciones; 4.840 casos completos y 106 fuera del modelo, conservados sin eliminación. La [copia pública de datos](../../datos/clase_04/README.md) mantiene valores, geometrías y rasters, con metadatos privados filtrados.
- **Evaluación:** R² entrenamiento/retenido de TRAIN: 0,890/0,196; de raster: 0,891/0,219. Hay extrapolación en los 17 predictores y validación no espacial: el ajuste alto no demuestra generalización.
- **Raster observado:** F64, 1.099 × 1.222 celdas de 30 × 30 m; 542.006 píxeles finitos y 800.972 NoData, sin ceros válidos. Rango 0,934559–687,265558; media 227,702455. Mapa e histograma inspeccionados históricamente.
- **Corrección residual posterior:** tres celdas de arranque y diagnóstico focal, no otro Run All. Copia de 4.840 entidades con valores y XY preservados; RESIDUAL = AGBD − PREDICTED en todas las filas. Negativos: 2.859; positivos: 1.981; ceros: 0. Rango −340,868 a 560,933 Mg/ha. PNG y mapa abierto en ArcGIS Pro verificados; azul significa sobrepredicción y rojo subpredicción, no magnitud del error.
- **Interfaz y diagramas:** cinco Mermaid del notebook comprobados previamente con parser y renderizado; no se verificó íntegramente la disposición nativa de Notebook/Obsidian ni se renderizaron nuevamente los conceptos. La comprobación del mapa en Pro no acredita toda la guía manual.
- **Video:** cobertura previa parcial; excluido de esta preparación, sin nueva revisión. No se declara la clase procesada completa.

La ejecución anterior de 13/13 y dos intentos raster fallidos (14 éxitos y un error cada uno) permanecen como antecedentes locales, no como resultado vigente. Los diagnósticos, logs, proyectos APRX, modelos SSM y árboles históricos completos no forman parte del paquete público ni son dependencias del notebook.

Las imágenes se conservan sin cambios de píxeles. El JSON residual conserva comprobaciones y valores; sus cuatro rutas personales se sustituyen por la imagen pública y localizadores históricos relativos, expresamente no distribuidos. La autorización de redistribución de los datos Coiba y las capturas de diapositivas fue confirmada por el usuario; no acredita origen científico adicional ni calidad del modelo. Diapositivas: **Francisco Javier Anzola**, `RandomForest_FA.pptx`; grabación fuente: José Sebastián Gómez Romero. Los PPTX no se redistribuyen.
