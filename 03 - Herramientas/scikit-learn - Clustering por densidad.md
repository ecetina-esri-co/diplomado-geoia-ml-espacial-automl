---
tags: [tipo/herramienta, tema/geoia, herramienta/scikit-learn, estado/revision]
---

# scikit-learn - Clustering por densidad

En Clase 01 se conserva scikit-learn para el generador y los experimentos sintéticos de la fuente. Es complemento metodológico de ArcGIS, no sustituto de mapas o gráficos nativos bloqueados.

## Versiones y entrada

**Observada:** scikit-learn 1.6.1 en Python 3.13.7 del entorno ArcGIS Pro 3.6.2. **Documentación:** scikit-learn 1.6, consultada el 2026-09-15 y registrada en [[99 - Recursos/Clase 01 - Fuentes y acuerdos]]; no recuperada de nuevo. Las bibliotecas ya estaban disponibles, no se requiere una instalación de deep learning para estos imports.

Entrada P01: matriz n×2 de make_moons, 200 observaciones base, `noise=0.9999`, `random_state=10`. Los atributos no son coordenadas geográficas. StandardScaler aplica z=(x−u)/s por variable, es sensible a atípicos y no impone normalidad. [make_moons, API](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_moons.html) y [StandardScaler, definición](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.StandardScaler.html), versión 1.6, consulta 2026-09-15 (E12–E13).

## Llamadas y parámetros

```python
# Fragmento P01: los imports no añaden instalaciones ni geografía a los sintéticos.
from sklearn.cluster import DBSCAN, HDBSCAN
from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
X, y_true = make_moons(n_samples=200, noise=0.9999, random_state=10)
X_scaled = StandardScaler().fit_transform(X)
# Las etiquetas del generador no se entregan a fit_predict.
dbscan = DBSCAN(eps=0.3, min_samples=5)
labels_db = dbscan.fit_predict(X_scaled)
hdbscan = HDBSCAN(min_cluster_size=5, min_samples=5, cluster_selection_epsilon=0.0)
labels_hd = hdbscan.fit_predict(X_scaled)
```

Adaptación abreviada del [[99 - Recursos/notebooks/Clase 01 - Practica 01 - Comparacion DBSCAN HDBSCAN sintetica.ipynb|notebook P01 ejecutado]]: aquí se pasa X directamente al escalador en vez de las dos columnas del DataFrame. No se ha ejecutado este fragmento aislado. El notebook completo mantiene configuración inicial, perfil ArcGIS, comentarios, gráficos y salidas propias.

| API | Salida/control importante | Límite |
| --- | --- | --- |
| DBSCAN | `eps`, `min_samples`, `labels_`, `core_sample_indices_` | Incluye el propio punto; ε no limita diámetro del grupo |
| HDBSCAN | `min_cluster_size`, `min_samples`, `cluster_selection_epsilon`, `probabilities_` | None en mínimo adopta tamaño; fuerza no equivale a valor p |
| OPTICS | `max_eps`, `ordering_`, `reachability_` | Capacidad documental; no se importó ni ejecutó en la práctica |

Fuentes: [DBSCAN, Parameters/Notes](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.DBSCAN.html), [HDBSCAN, Parameters/Attributes/Notes](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.HDBSCAN.html), [OPTICS, Attributes/Notes](https://scikit-learn.org/1.6/modules/generated/sklearn.cluster.OPTICS.html), scikit-learn 1.6, consulta 2026-09-15 (E3/E4/E9).

## Precauciones que evitan comparaciones falsas

- `min_samples` HDBSCAN incluye el propio punto en sklearn; contrib difiere. No portar valores sin revisar semántica.
- `cluster_selection_epsilon` fusiona bajo una distancia de selección; no es automáticamente ε DBSCAN.
- `probabilities_` expresa fuerza proporcional a persistencia, no certeza causal ni equivalencia automática con PROB Esri.
- Etiquetas −1 son no asignados, distintas del ruido gaussiano de make_moons.
- DBSCAN documenta memoria de peor caso O(n²) en sklearn; OPTICS documenta O(n²). No inferir tiempos locales a partir de esas notas.

## Resultados y uso docente

Base ejecutada: DBSCAN 5 grupos/58 ruidos, HDBSCAN 8/108; DBSCAN 108 núcleos y 34 fronteras. Se conservan seis configuraciones por método y 14 resultados de controles de muestra/perturbación. EDA y barras son ArcGIS; Matplotlib complementa paneles sintéticos. No se asigna EPSG ni se añade contraste Bogotá.

[[99 - Recursos/Clase 01 - Resultados de prácticas]] proporciona rutas y evidencia, no una nueva ejecución. [[02 - Conceptos/DBSCAN]] explica los roles; [[02 - Conceptos/HDBSCAN y OPTICS]] distingue estructuras; [[02 - Conceptos/Comparación de métodos de clustering]] enseña a comparar parámetros. [[03 - Herramientas/ArcGIS Pro - Density-based Clustering]] corresponde a la práctica geográfica distinta. Volver a [[01 - Clases/2026-09-14 - Clase 01 - Clustering espacial]].
