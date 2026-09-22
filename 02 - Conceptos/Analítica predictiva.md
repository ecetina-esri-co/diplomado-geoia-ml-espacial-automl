---
tags: [tipo/concepto, tema/analitica-geoespacial, tema/machine-learning]
---
# Analítica predictiva

## Estimar lo no observado, no prometer el futuro

La analítica predictiva usa datos, patrones y modelos para estimar valores desconocidos. Puede responder qué podría pasar en el futuro, pero también cuánto podría valer una variable **hoy en una ubicación no medida**. Estimar biomasa en Coiba es este segundo caso; no es necesariamente un pronóstico temporal.

Predecir no es adivinar: es modelar bajo supuestos y reconocer incertidumbre. La pregunta profesional es si el error es aceptable para la decisión y según qué [[Métricas de evaluación de modelos]]. [Esri 3.6, *Forest-based and Boosted Classification and Regression*, propósito y tipos de predicción.]

Si las muertes se concentran cerca de una bomba, aumentan en cierta semana y afectan a determinados perfiles, esas señales pueden ayudar a estimar zonas expuestas. No prueban por sí solas causalidad ni garantizan continuidad del patrón. Diagnosticar causas y recomendar intervenciones son preguntas adicionales, no consecuencias automáticas del pronóstico.

## Métodos y evaluación

- Series temporales y forecasting para evolución temporal.
- Regresión para respuestas continuas.
- [[Aprendizaje supervisado]] para clasificación y regresión con etiquetas.
- Scoring para ordenar riesgo según una regla o modelo.
- Métodos no supervisados como apoyo para explorar, segmentar o construir variables; por sí solos no aprenden una respuesta etiquetada.
- Validación, métricas y estimación de incertidumbre acordes con el modelo y la decisión.

Un intervalo de confianza sobre una media no es lo mismo que un intervalo de predicción para una observación nueva. Si no se estimaron intervalos, declarar esa limitación; no inventar un margen a partir de la apariencia del mapa.

```mermaid
flowchart LR
    A[Datos y pregunta] --> B[Variables disponibles]
    B --> C[Modelo predictivo]
    C --> D[Predicción]
    D --> E[Evaluación fuera de entrenamiento]
    E --> F[Error y límites territoriales]
    F --> G[Decisión informada]
```

La evaluación es parte de la decisión: no basta con obtener una superficie de valores.

## Ejemplo hipotético calculado

Con $e_i=y_i-\hat y_i$, un error positivo indica subestimación.

$$MAE=\frac{1}{n}\sum_i|y_i-\hat y_i|,\qquad RMSE=\sqrt{\frac{1}{n}\sum_i(y_i-\hat y_i)^2}.$$

| Ubicación | Muertes observadas | Predichas | Error |
|---|---:|---:|---:|
| A | 8 | 6 | 2 |
| B | 3 | 4 | −1 |
| C | 5 | 5 | 0 |

$$MAE=\frac{2+1+0}{3}=1,\qquad RMSE=\sqrt{\frac{4+1+0}{3}}\approx1.29.$$

El error absoluto promedio es una muerte; RMSE es aproximadamente 1.29 muertes y penaliza más el error grande de A. Ninguno dice dónde se agrupan los errores ni representa por sí solo un intervalo de predicción.

![[99 - Recursos/clase-06-errores-prediccion.svg]]

**Lectura:** comparar las barras verdes (observados) y naranjas (predichos), medidas en unidades de respuesta sobre el eje horizontal. Su diferencia muestra dirección y magnitud del error. **Conclusión:** el desacuerdo debe cuantificarse y localizarse. **Límite:** recurso hipotético docente, independiente de la tabla anterior y sin una ejecución nueva del modelo. Fuente: elaboración docente; marco de evaluación forest-based de Esri 3.6.

![[99 - Recursos/grafica-aprendizaje-supervisado-geoespacial.svg]]

**Lectura:** siga respuesta conocida → predictores → nuevas entidades o píxeles. Las cajas no representan superficies ni magnitudes y la franja inferior exige validación. **Conclusión:** predecir necesita información disponible en el lugar de aplicación. **Límite:** el esquema no acredita causalidad, exactitud ni ejecución. Fuente: gráfico didáctico original GeoIA; Esri 3.6, tipos de predicción, citado al final.

## La dimensión territorial

Una predicción geoespacial necesita considerar escala, vecindad, dependencia entre muestras y posible autocorrelación residual. Un error promedio favorable puede ocultar fallas regionales. [[Random Forest]] puede usar atributos y [[Rasters explicativos]], pero no incorpora automáticamente una estructura de dependencia espacial.

[[Validación de modelos supervisados]] debe representar el uso futuro o territorial esperado. La predicción sobre condiciones o combinaciones ausentes de la muestra es especialmente riesgosa; los bosques no extrapolan bien fuera de los valores observados. [Esri 3.6, «How…», límites de predicción.]

Evitar presentar estimaciones como certezas, omitir el margen de error disponible, entrenar con muestras sesgadas, mezclar variables no comparables entre territorios o ignorar residuales. La utilidad del mapa depende tanto de sus límites comunicados como de su detalle visual.

## Referencias y contexto

- Esri. *Forest-based and Boosted Classification and Regression*. ArcGIS Pro 3.6, propósito y parámetros. https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-statistics/forestbasedclassificationregression.htm. Consulta documentada: 2026-09-21.
- Esri. *How Forest-based and Boosted Classification and Regression works*. ArcGIS Pro 3.6, entrenamiento y límites. https://pro.arcgis.com/en/pro-app/3.6/tool-reference/spatial-statistics/how-forest-works.htm. Consulta documentada: 2026-09-21.
- Ampliaciones conservadas, sin nueva consulta: Esri, *Ordinary Least Squares*, https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/ordinary-least-squares.htm; James, Witten, Hastie y Tibshirani, *An Introduction to Statistical Learning*, https://www.statlearning.com/.

Aplicación: [[2026-09-21 - Clase 04 - Aprendizaje supervisado y Random Forest geoespacial|Clase 04]]. Los ejemplos son didácticos; no son resultados de una ejecución nueva.
