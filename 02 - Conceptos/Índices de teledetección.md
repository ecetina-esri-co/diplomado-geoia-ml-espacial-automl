---
tags: [tipo/concepto, tema/teledeteccion, tema/modelamiento]
---
# Índices de teledetección

## De bandas a señales interpretables

Los índices combinan matemáticamente bandas espectrales para resaltar verdor, vigor vegetal, humedad, suelo visible, agua superficial o diferencias de cobertura. No crean una medición física nueva por sí solos: reorganizan información espectral bajo supuestos.

En Coiba no miden directamente [[Biomasa aérea sobre el suelo (AGBD)]]. Se usan como [[Rasters explicativos]] para que [[Random Forest]] aprenda relaciones predictivas junto con bandas y topografía. [Esri 3.6, «Band Arithmetic», métodos por índice; «How…», predictores raster.]

```mermaid
flowchart LR
    A[Reflectancias y bandas identificadas] --> B[Revisar escala y calidad]
    B --> C[Calcular índices]
    C --> D[Interpretar señal espectral]
    D --> E[Combinar con muestras de biomasa]
    E --> F[Entrenar y validar]
    F --> G[Predicción con límites]
```

Bandas correctamente identificadas y escaladas son condición previa. Una fórmula correcta aplicada a bandas equivocadas produce una señal sin el significado esperado.

## Qué pregunta responde cada índice

| Índice | Fórmula | Señal | Límite |
|---|---|---|---|
| [[NDVI]] | $(NIR-Red)/(NIR+Red)$ | Verdor y vigor vegetal | Saturación en bosque denso |
| [[EVI]] | $2.5(NIR-Red)/(NIR+6Red-7.5Blue+1)$ | Contraste vegetal con ajustes atmosférico y de fondo | Depende de azul y escala confiables |
| [[SAVI]] | $1.5(NIR-Red)/(NIR+Red+0.5)$ | Vegetación con ajuste de suelo para $L=0.5$ | No elimina toda influencia del suelo |
| [[RVI y DVI]] | $NIR/Red$ y $NIR-Red$ | Contraste rojo–NIR | Denominador pequeño en RVI; escala en DVI |
| [[MSI]] | $SWIR/NIR$ | Sequedad o estrés hídrico relativo | No es contenido absoluto de agua |
| [[MNDWI]] | $(Green-SWIR)/(Green+SWIR)$ | Agua superficial y transiciones | Sombras, turbidez y mezcla de coberturas |

La documentación de Esri 3.6 verifica NDVI, EVI, SAVI, MNDWI y el cociente simple SR equivalente a RVI aquí definido. MSI conserva su atribución a ESA SNAP y bibliografía técnica; DVI, a la literatura rojo–NIR. No se supone que todos sean opciones del mismo menú ni se intercambian bandas SWIR sin identificar su intervalo espectral.

![[99 - Recursos/grafica-indices-teledeteccion-formulas.svg]]

**Lectura:** comparar bandas, diferencias y cocientes de cada fórmula; los índices de vegetación enfatizan rojo–NIR mientras los hídricos incorporan SWIR. **Conclusión:** distintos índices responden a contrastes diferentes y pueden ser redundantes. **Límite:** es una síntesis de fórmulas, no una calibración local ni una tabla de umbrales universales. Fuente: recurso docente de fórmulas; Esri 3.6, «Band Arithmetic», y créditos fundacionales listados abajo.

## Ejemplo manual hipotético

Un píxel tiene reflectancias Blue = 0.05, Green = 0.09, Red = 0.06, NIR = 0.52 y SWIR = 0.18.

```text
NDVI  = (0.52 - 0.06) / (0.52 + 0.06) = 0.793
EVI   = 2.5 * (0.52 - 0.06) / (0.52 + 6*0.06 - 7.5*0.05 + 1) = 0.764
SAVI  = 1.5 * (0.52 - 0.06) / (0.52 + 0.06 + 0.5) = 0.639
RVI   = 0.52 / 0.06 = 8.667
DVI   = 0.52 - 0.06 = 0.460
MSI   = 0.18 / 0.52 = 0.346
MNDWI = (0.09 - 0.18) / (0.09 + 0.18) = -0.333
```

Es compatible con una señal vegetal marcada y baja sequedad relativa; MNDWI negativo no sugiere agua abierta en esta lectura ilustrativa. No confirma por sí solo estado fisiológico, ausencia de agua bajo dosel ni biomasa alta: influyen estructura vertical, edad, composición, perturbación y topografía. Los denominadores nulos requieren tratamiento explícito; las constantes de EVI/SAVI exigen la escala de reflectancia pertinente.

## Integración en Coiba

![[99 - Recursos/grafica-biomasa-coiba-indices-modelo.svg]]

**Lectura:** observar cómo índices, bandas y topografía se conectan con muestras y modelo. **Conclusión:** los índices son entradas, no la respuesta de biomasa. **Límite:** el flujo no demuestra exactitud ni ejecución actual. Fuente: recurso docente del ejercicio Coiba; modelamiento con rasters en Esri 3.6.

El ejercicio con `Datos_Coiba.gdb` combina índices, bandas Landsat, DEM, pendiente y aspecto. Su uso exploratorio no constituye por sí solo un producto final: necesita [[Validación de modelos supervisados]], revisión de incertidumbre y coherencia de fechas y escalas. Información estructural GEDI/LiDAR puede complementar el análisis cuando exista autorización y disponibilidad, pero no se incorpora aquí como dato nuevo. [[Importancia de variables]] ayuda a examinar qué señales aprovecha el modelo sin interpretar ranking como causalidad.

## Referencias y créditos

- Esri. *Band Arithmetic function*. ArcGIS Pro 3.6, NDVI, EVI, SAVI, MNDWI y SR. https://pro.arcgis.com/en/pro-app/3.6/help/analysis/raster-functions/band-arithmetic-function.htm. Consulta documentada: 2026-09-21.
- Esri. *How Forest-based and Boosted Classification and Regression works*. ArcGIS Pro 3.6, rasters explicativos. https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-statistics/how-forest-works.htm. Consulta documentada: 2026-09-21.
- Fuentes técnicas conservadas, sin nueva consulta: USGS, *Landsat Normalized Difference Vegetation Index*, https://www.usgs.gov/landsat-missions/landsat-normalized-difference-vegetation-index; *Enhanced Vegetation Index*, https://www.usgs.gov/landsat-missions/landsat-enhanced-vegetation-index; *Soil Adjusted Vegetation Index*, https://www.usgs.gov/landsat-missions/landsat-soil-adjusted-vegetation-index; NASA MODIS, *MOD13 User Guide V6.1*, https://modis-land.gsfc.nasa.gov/pdf/MOD13_User_Guide_V61.pdf; ESA SNAP 13, *Moisture Stress Index Algorithm Specification*, https://step.esa.int/main/wp-content/help/versions/13.0.0/snap-toolboxes/eu.esa.opt.opttbx.radiometric.indices.ui/msi/MsiAlgorithmSpecification.html.
- Créditos académicos conservados, sin nueva consulta: Tucker (1979), *Red and photographic infrared linear combinations for monitoring vegetation*, https://doi.org/10.1016/0034-4257(79)90013-0; Zeng et al. (2022), *Optical vegetation indices for monitoring terrestrial ecosystems globally*, https://doi.org/10.1038/s43017-022-00298-5; Xue y Su (2017), *Significant Remote Sensing Vegetation Indices*, https://doi.org/10.1155/2017/1353691. La atribución de MNDWI a Xu (2006) se desarrolla en su nota específica.

Aplicación: [[2026-09-21 - Clase 04 - Aprendizaje supervisado y Random Forest geoespacial|Clase 04]]. Cálculos didácticos, no ejecución nueva sobre imágenes.
