# Coiba · Entradas públicas de Clase 04

**Docente:** Fabian Cetina. La [práctica autónoma](../../notebooks/Clase%2004%20-%20Practica%2001%20-%20Random%20Forest%20geoespacial.ipynb) usa `99 - Recursos/datos/clase_04/Datos_Coiba.gdb` como entrada de solo lectura. La guía independiente de ArcGIS Pro, dentro del notebook, explica cómo conectarla desde Catalog. No requiere descargar insumos adicionales ni acceder a otro vault.

## Contenido y significado

La geodatabase contiene **19 datasets**: `AGBD_Observaciones_2023_Coiba` (4.946 puntos), `Coiba` (una entidad) y 17 rasters. La práctica utiliza **18 entradas activas**: los puntos AGBD y los 17 rasters enumerados en `RASTER_SPECS`; conservar `Coiba` no añade una operación al ejercicio.

Los puntos tienen CRS `GCS_WGS_1984`; campos `OBJECTID`, `Shape`, `lon`/`lat` (Double), `Time` (Date), `AGBD` (Double) y `Trajectory` (Integer). El significado de `Trajectory` no está documentado: no se atribuye órbita ni haz. Las coordenadas geográficas no son distancias en metros.

AGBD se interpreta en **Mg/ha por confirmación del usuario**, sin conversión de valores: 1 Mg/ha = 1 tonelada métrica por hectárea. Los metadatos disponibles no acreditan esa unidad ni el producto de origen; no se atribuye procedencia GEDI. La autorización expresa de redistribución de Coiba no constituye una certificación científica de sus datos.

La ejecución histórica conserva las 4.946 observaciones y utiliza 4.840 casos completos; 106 quedan fuera del modelo, sin eliminación. Copiar esa selección a una entidad persistente permite abrir los gráficos nativos; no es imputación ni deduplicación. Las salidas nuevas deben escribirse en una subcarpeta nueva de `salidas_clase_04/practica_01`, identificada por ejecución, nunca sobre esta entrada.

## Procedencia y comprobación

Esta es una **copia pública nueva**, construida mediante operaciones ArcGIS sobre la copia local histórica Coiba. La fuente histórica `datos/clase_06` permanece intacta, privada y fuera de la distribución; no es una dependencia del estudiante.

En ArcGIS Pro **3.6.2 / ArcInfo**, kernel nuevo, se compararon las dos entidades vectoriales: esquema, todos los atributos, geometrías WKB, número de filas y CRS. Para los 17 rasters se compararon todos los píxeles, dimensiones, bandas, tipo, NoData, tamaño de celda, extensión y CRS. Las comparaciones fueron exactas. No se proyectó, reparó, imputó, deduplicó ni entrenó.

Se filtraron únicamente los metadatos sensibles de la copia, preservando títulos, créditos y restricciones de uso presentes. Se eliminaron el historial de geoprocesamiento y archivos adjuntos de metadatos; la fuente no fue modificada. Referencia técnica: Esri, *Metadata*, ArcGIS Pro 3.6, `saveAsXML` (`REMOVE_ALL_SENSITIVE_INFO`), `deleteContent` y `save`: https://pro.arcgis.com/en/pro-app/3.6/arcpy/metadata/metadata-class.htm. Pasajes verificados por el orquestador durante la preparación pública.

La [selección de resultados](../../salidas_clase_04/publicados/README.md) distingue la ejecución histórica 17/17 —incluida la rama raster— de la corrección cartográfica residual focal posterior, sin nuevo modelo. La publicación de esta copia no acredita otro Run All: el notebook solo cambia su carpeta de entrada para utilizar los mismos valores. El video sigue parcial y excluido de esta preparación; la disposición completa de Notebook/Obsidian no se verificó. Clase en borrador para revisión humana, no aprobada académicamente.

Volver a [[2026-09-21 - Clase 04 - Aprendizaje supervisado y Random Forest geoespacial|Clase 04]].
