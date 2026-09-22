---
tags: [tipo/concepto, tema/teledeteccion, tema/agua]
---
# MNDWI

![[99 - Recursos/grafica-indice-mndwi.svg]]

**Lectura:** compare verde y SWIR1 en la diferencia normalizada; la tarjeta relaciona bandas y posibles confusiones, no umbrales medidos. **Conclusión:** el índice ayuda a reconocer agua superficial y transiciones. **Límite:** sombras y turbidez impiden interpretar su signo como clasificación universal. Fuente: gráfico didáctico original GeoIA; Esri 3.6, «Band Arithmetic», MNDWI, citado al final.

## Resaltar agua abierta con verde y SWIR

El **Modified Normalized Difference Water Index** contrasta verde y SWIR. Modifica el NDWI de agua abierta asociado con McFeeters, sustituyendo NIR por SWIR para reducir algunas confusiones con suelo, construcciones y superficies brillantes. No debe confundirse con el NDWI de humedad de vegetación de Gao. [Esri 3.6, *Band Arithmetic*, MNDWI; atribución fundacional a Xu, 2006.]

$$MNDWI=\frac{Green-SWIR}{Green+SWIR}.$$

En la correspondencia usual Landsat 8/9 se utilizan B3 (verde) y B6 (SWIR1), por lo que resulta $(B3-B6)/(B3+B6)$. Verificar el producto y orden de bandas; «SWIR» no autoriza intercambiar bandas de longitudes de onda distintas. Con reflectancias no negativas y suma no nula, la diferencia normalizada queda entre −1 y 1.

```mermaid
flowchart LR
    A[Reflectancias verde y SWIR] --> B[Diferencia y suma]
    B --> C[MNDWI]
    C --> D[Contraste de agua abierta]
    D --> E[Revisar sombras y mezcla]
    E --> F[Validar interpretación local]
```

El último paso importa: el índice resalta una señal, no genera automáticamente una clasificación correcta de agua.

## Ejemplo manual hipotético

Con Green = 0.08 y SWIR = 0.01:

$$MNDWI=\frac{0.08-0.01}{0.08+0.01}=\frac{0.07}{0.09}\approx0.778.$$

Un valor positivo alto es compatible con agua abierta. El umbral depende de sensor, turbidez, sombras y entorno. Denominadores pequeños amplifican errores; una suma cero hace el índice indefinido.

![[99 - Recursos/grafica-indices-teledeteccion-formulas.svg]]

**Lectura:** localizar verde–SWIR y compararlo con rojo–NIR y con SWIR/NIR. **Conclusión:** MNDWI aborda agua superficial, mientras MSI aporta otra señal hídrica relativa. **Límite:** la fórmula no determina un umbral universal ni distingue por sí sola agua, sombra y píxeles mixtos. Fuente: recurso docente de índices; Esri 3.6, «Band Arithmetic», MNDWI; crédito de Xu (2006).

## Qué aporta al caso Coiba

En un modelo de [[Biomasa aérea sobre el suelo (AGBD)]], MNDWI puede actuar como proxy de agua, humedad ambiental, costa o condiciones de borde. Una [[Importancia de variables|importancia]] alta no significa que el índice cause biomasa ni que mida agua interna de las plantas: puede representar gradientes espaciales asociados con la muestra.

Sombras, sedimentos, nubes y superficies oscuras alteran la señal. SWIR puede tener resolución distinta de verde según sensor, por lo que alineación y remuestreo requieren justificación. No clasificar agua mediante un único umbral sin validación local; tampoco eliminar automáticamente píxeles o muestras por su valor.

[[MSI]] explica otra lectura hídrica; [[Índices de teledetección]] compara las fórmulas; [[Rasters explicativos]] sitúa el índice como entrada al modelo, no como respuesta observada.

## Referencias y contexto

- Esri. *Band Arithmetic function*. ArcGIS Pro 3.6, MNDWI. https://pro.arcgis.com/en/pro-app/3.6/help/analysis/raster-functions/band-arithmetic-function.htm. Consulta documentada: 2026-09-21.
- Créditos académicos conservados, sin nueva consulta: Xu (2006), *Modification of Normalised Difference Water Index to Enhance Open Water Features*, https://doi.org/10.1080/01431160600589179; McFeeters (1996), *The use of the Normalized Difference Water Index in the delineation of open water features*, https://doi.org/10.1080/01431169608948714; Feyisa et al. (2014), *Automated Water Extraction Index*, https://doi.org/10.1016/j.rse.2013.08.029.
- Referencia complementaria conservada, sin nueva consulta: registro de publicación USGS sobre aplicaciones de MNDWI, https://pubs.usgs.gov/publication/70220117. El índice AWEI de Feyisa es una alternativa de extracción de agua, no otro nombre para MNDWI.

Aplicación: [[2026-09-21 - Clase 04 - Aprendizaje supervisado y Random Forest geoespacial|Clase 04]]. Ejemplo hipotético, sin cálculo nuevo sobre imágenes.
