# Entradas seleccionadas de Clase 03

Migración local para los ejercicios de cubos espacio-temporales y los contrastes de siniestros, colegios y abejas de la Clase 15 original. Estas entradas se consumen **solo en lectura**; las copias de trabajo y resultados corresponden a `99 - Recursos/salidas_clase_03/`, fuera de esta carpeta. El usuario confirmó expresamente los derechos de redistribución pública de estas cuatro entidades, incluidas direcciones, coordenadas e identificadores de incidentes, y del NetCDF. Esta confirmación no se extiende a otros insumos del vault. Volver a [[99 - Recursos/datos/README|Datos de las prácticas]].

## Copia pública y uso

El notebook consume `publicados/entradas.gdb` y `cubo_espacio_temporal_accidentes.nc`. La GDB local `entradas.gdb` se conserva intacta e ignorada por Git; no forma parte del paquete público. Las rutas de destino de la tabla siguiente describen esa migración local histórica, no la ruta pública actual.

La copia pública se creó como una GDB nueva con ArcPy 3.6.2, sin registrar historial ni metadatos de geoprocesamiento. Se retiraron únicamente nodos `Process` y `linkage` con rutas privadas mediante `arcpy.metadata.Metadata`; se conservaron atribuciones y restricciones académicas. La compactación se aplicó solo a la GDB nueva para no conservar páginas obsoletas con metadatos privados. No se anonimizaron atributos ni se modificaron entidades: la autorización incluye esos datos.

## Procedencia y contenido

Las rutas de origen siguientes son relativas a la raíz del vault actual y pertenecen al vault original, conservado sin edición. No se utilizó la copia heredada `Datos/` ni salidas de Clase 02 del vault actual.

| Origen | Destino en esta carpeta | Entidades observadas | Referencia espacial observada |
| --- | --- | ---: | --- |
| `../diplomado_geoia/99 - Recursos/datos/Datos Ejercicio5C.gdb/SiniestrosViales` | `entradas.gdb/SiniestrosViales` | 199146 | MAGNA_Ciudad_Bogota, WKID Esri 102233; metros |
| `../diplomado_geoia/99 - Recursos/datos/Datos Ejercicio5C.gdb/UPZ` | `entradas.gdb/UPZ` | 112 | MAGNA_Ciudad_Bogota, WKID Esri 102233; metros |
| `../diplomado_geoia/99 - Recursos/salidas_clase_14/clase_14_colegios_work.gdb/Colegios_Colombia_CollectEvents` | `entradas.gdb/Colegios_Colombia_CollectEvents` | 9911 | WGS_1984_Web_Mercator_Auxiliary_Sphere, EPSG:3857; metros |
| `../diplomado_geoia/99 - Recursos/salidas_clase_14/clase_14_bomberos_work.gdb/Incidentes_Control_Abejas_CollectEvents` | `entradas.gdb/Incidentes_Control_Abejas_CollectEvents` | 1918 | MAGNA-SIRGAS_2018_Origen-Nacional, EPSG:9377; metros |
| `../diplomado_geoia/99 - Recursos/datos/cubo_espacio_temporal_accidentes.nc` | `cubo_espacio_temporal_accidentes.nc` | No aplica | WKT Esri MAGNA_Ciudad_Bogota; metros |

Solo se copiaron estas cuatro clases de entidad mediante `arcpy.management.CopyFeatures` y el archivo NetCDF mediante copia binaria. No se copió ninguna GDB completa, archivo de bloqueo ni directorio de resultados. No se ejecutaron Integrate, CollectEvents, RepairGeometry, modelos, transformaciones, imputación ni deduplicación.

### Qué representan los campos

- **Siniestros:** `OBJECTID_1` es el OID del almacenamiento y `OBJECTID` es un identificador entero adicional conservado, no intercambiable por su nombre. Se mantienen `FORMULARIO`, `CODIGO_ACC`, `DIRECCION`, `GRAVEDAD`, `CLASE_ACC`, `LOCALIDAD`, `CIV`, `PK_CALZADA`, coordenadas `LATITUD`/`LONGITUD` (Double) y `ANO_OCURRE` (SmallInteger). `FECHA_OCUR` y `FECHA_HORA` son Date: ambos tienen cero nulos y rango observado 2015-01-01 a 2021-09-10. Esto no demuestra cobertura completa, precisión horaria ni ausencia de duplicados.
- **UPZ:** se preservan los identificadores `OBJECTID_1` (OID), `OBJECTID` (Integer), `CODIGO_UPZ` y `UPZ` (String); nombres, zonificación y actos administrativos; `AREA_HECTA`, `SHAPE_Leng`, `Shape_Length` y `Shape_Area` (Double). No se corrigieron límites ni se certificó vigencia jurídica.
- **Preparados históricos:** sus únicos campos son `OBJECTID` (OID), `Shape` (Geometry) e `ICOUNT` (Integer). No contienen fechas ni identificadores individuales de cada evento agregado. Colegios: ICOUNT sin nulos, mínimo 1, máximo 13, suma 10617; abejas: sin nulos, mínimo 1, máximo 5, suma 2173. La cantidad de puntos ponderados no es la cantidad de eventos representados.

Los notebooks fuente `Clase 14 - Practica colegios Moran incremental.ipynb` y `Clase 14 - OPTICS y autocorrelacion espacial incremental.ipynb`, bajo `../diplomado_geoia/99 - Recursos/notebooks/`, documentan **Integrate con 10 Meters seguido de CollectEvents**. Se migraron sus resultados existentes como entradas preparadas históricas, sin repetir esa preparación. Las geometrías recibidas ya reflejan esa historia; la igualdad de la copia no verifica retroactivamente sus desplazamientos ni recupera los puntos originales. EPSG:3857 tiene distorsión de escala: unidades métricas no garantizan distancias de terreno exactas.

### Cubo histórico: lectura y precauciones

El NetCDF tiene 5498890 bytes y dimensiones `time=14`, `x=57`, `y=166`. La coordenada temporal usa `seconds since 2014-09-10 00:00:00`, calendario gregoriano, con etiquetas desde 2014-09-10 hasta 2021-03-10: son etiquetas de intervalos, no el rango de fechas individuales de siniestros. Sus pasos de coordenadas iniciales son x≈433.0127 m e y=−500 m; no se deduce de ellos por sí solos una resolución cuadrada.

Contiene `COUNT`, máscaras, variables de tendencia y variables `EMERGING_COUNT_*`: **ya incorpora análisis históricos**, no es un cubo virgen ni una ejecución nueva de Clase 03. La metadata de proyección no es totalmente uniforme: el WKT Esri indica latitud de origen 4.680486111111112 mientras el atributo NetCDF `latitude_of_projection_origin` indica 0.0. Se conserva sin corrección; no interpretar esa discrepancia como reproyección validada.

**EmergingHotSpotAnalysis modifica su cubo de entrada. Antes de cada ejecución, el notebook debe copiar este NetCDF a un directorio de salida aislado y pasar únicamente esa copia a `arcpy.stpm.EmergingHotSpotAnalysis`. Nunca pasar el archivo de esta carpeta ni el original.** La misma separación protege las entidades frente a operaciones mutantes posteriores.

## Comprobación de la migración

Ejecutada en proceso de primer plano con `PYTHONNOUSERSITE=1`, Python Pro 3.13.7, ArcGIS Pro 3.6.2, licencia observada ArcInfo. Kernel: `C:/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe`, opciones `-X utf8 -B -s`, código Python inline; salida 0.

`Exists`, `GetCount`, `ListFields`, `Describe` y cursores de lectura comprobaron, para cada entrada, igualdad completa entre origen y destino de OID, atributos, geometría WKB, esquema (nombre/tipo/longitud/precisión/escala) y referencia espacial serializada. Los OID originales coincidieron: no se descartaron ni se generó un identificador sustituto. Una segunda lectura del origen coincidió con la primera en OID, atributos y WKB. Las cuatro entradas presentaron cero geometrías nulas; esto no sustituye CheckGeometry ni certifica validez topológica.

El NetCDF copiado coincidió byte a byte con el original (`filecmp.cmp(..., shallow=False)`) y se inspeccionó con `netCDF4.Dataset(..., 'r')`. No se creó un sistema de hashes. La comprobación se limita a estas entradas: no certifica toda la GDB de origen, dominios externos ni relaciones no utilizadas. No se ejecutó ningún notebook, mapa o análisis de Clase 03. La revisión del video y la completitud docente corresponden al seguimiento de la clase, no a esta migración de datos.

**Comprobación del paquete público:** 74 componentes de GDB, 30.217.754 bytes; cuatro entidades con los conteos de la tabla. Comparación completa de OID, atributos, WKB, campos/tipos, propiedades geométricas, índices, subtipos y CRS frente a la GDB local; sin dominios en ambas. Atribuciones conservadas y sin rutas privadas en los metadatos públicos. Escaneo binario preservando bytes en Latin-1 y UTF-16 LE, sin coincidencias de los patrones de rutas personales, enlaces SharePoint/OneDrive o correos ASCII; este escaneo acotado no es garantía universal de ausencia de información sensible. Se descartaron coincidencias aleatorias no ASCII de un patrón inicial de correo sobre bytes binarios. Los atributos decodificados del NetCDF no presentaron coincidencias.

La comprobación posterior a la salida del proceso ArcPy encontró cero locks; hashes antes/después confirmaron intactos todos los componentes de la GDB fuente y el NetCDF. Ningún componente supera 100 MB. Solo cambiaron referencias de entrada del notebook: fuentes restantes, salidas y contadores de ejecución preservados; JSON y sintaxis Python comprobados, sin ejecutar celdas ni modelos. La revisión independiente y la entrega Git son pasos separados; esta preparación no equivale a aprobación académica.
