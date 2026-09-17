---
tags: [tipo/guia, estado/en-uso]
---

# Datos de las prácticas

Reutilizar insumos disponibles para la práctica autorizada e inspeccionar solo lo necesario. `99 - Recursos/datos/` es la ubicación predeterminada para nuevas entradas seleccionadas, no una ruta obligatoria. La preparación externa de jurisdicciones P02 se registra abajo; no implica ejecución de la práctica.

## Procedencia y selección proporcional

- Fuente original, solo lectura: `C:\Users\[USER]\OneDrive - Esri NOSA\diplomado_geoia\99 - Recursos\datos`.
- Ruta relativa desde este vault: `../diplomado_geoia/99 - Recursos/datos`.
- Copia heredada local: `Datos/`, intacta; incluye las carpetas previamente identificadas `Datos/Datos Ejercicio5A.gdb/` y `Datos/Datos Ejercicio5C.gdb/`. Existencia de una GDB no prueba contenido ni validez de cada capa; reutilizar comprobaciones registradas de la práctica, no extrapolarlas.

1. Partir de la práctica ya autorizada y su fuente. Comprobar disponibilidad local antes de copiar, evitando duplicados; no reautorizar entradas/acuerdos conocidos.
2. Inspeccionar campos usados, tipos/significado, nulos frente a ceros y claves duplicadas pertinentes; geometrías, distancias, SR/unidades y cobertura temporal cuando el método dependa de ellos. Verificar versión, licencia y dependencias de las operaciones necesarias, no campos o capacidades ajenos al ejercicio.
3. Registrar brevemente procedencia, entradas/salidas, requisitos y estado en nota/notebook o enlazar evidencia vigente. No exigir expediente exhaustivo de permisos para uso local ya autorizado. Datos nuevos no autorizados, acceso privado o dudas que exijan decisión humana sí se consultan.
4. La autorización de copia cubre **solo insumos necesarios seleccionados por clase** desde la fuente original. Registrar origen, destino y motivo; nunca sobrescribir/modificar originales ni inventar sustitutos ante faltantes.
5. Crear copias de trabajo separadas. Calculate Field y otras operaciones mutantes solo sobre copias; no deduplicar, imputar, eliminar ni transformar automáticamente; no reparar geometrías sin autorización. La excepción P02 siguiente está explícitamente autorizada. Comparar antes/después cuando corresponda; no forzar limpieza.

Evaluar EDA e ingeniería ArcGIS primero según campos/pregunta reales. Consultar únicamente secciones pertinentes de [[99 - Recursos/Matriz - Análisis exploratorio y ArcGIS|Matriz documental]] ante la operación o incertidumbre; diferenciar UI, API documentada y ejecución. La matriz no verifica la licencia/versión local ni convierte resultados históricos en evidencia actual. Conservar bibliotecas Python justificadas de la fuente sin duplicar todo el análisis.

## Rutas y autonomía

**Una práctica real, un notebook**, `99 - Recursos/notebooks/Clase NN - Practica PP - Tema.ipynb`, no uno por algoritmo. Registrar PP → notebook → entradas → salidas → estado brevemente en la nota. No reabrir los dos notebooks ni acuerdos P1–P7 aprobados de Clase 01.

Objetivos primero en Markdown; primera celda de código única y corta con `DATA_DIR` y `OUTPUT_DIR`, explicada y comentada; el resto reutiliza esas variables. Reiniciar y ejecutar completo sin estado oculto de otro notebook. Declarar/verificar auxiliares compartidos sin duplicar entradas de solo lectura; no crear runners o sistemas de hashes como prerrequisito. Conservar los auxiliares y evidencia existentes.

| Variable | Convención |
| --- | --- |
| `DATA_DIR` | Entradas seleccionadas: `99 - Recursos/datos/`, `Datos/` existente o ubicación externa verificada. |
| `OUTPUT_DIR` | Copias/resultados separados: `99 - Recursos/salidas_clase_NN/practica_PP/` o equivalente externo. Nunca dentro de originales ni igual a `DATA_DIR`. |

Explicar resolución de rutas desde el notebook; no depender silenciosamente del directorio de trabajo ni dispersar rutas personales. Cada celda de código lleva comentarios educativos y cada salida interpretación; evidencia esperada y ejecutada se distinguen. No repetir ejecuciones no modificadas sin incertidumbre creíble.

## Límites de Clase 01 y salidas

Notebooks geográficos requieren vistas/mapas y gráficos ArcGIS pertinentes e interpretados. Solo **P01 Clase 01 `make_moons`** es sintética sin contraste Bogotá, mapas geográficos ni EPSG/georreferenciación ficticia; conserva gráficos tabulares ArcGIS y conceptuales. No generalizar la excepción.

**P02 — preparación geométrica autorizada, fuera de la práctica:** preparar por separado una copia nueva jurisdiccional en `99 - Recursos/datos/` y aplicar CheckGeometry. Si persisten errores, RepairGeometry exclusivamente sobre esa copia con `KEEP_NULL`, sin eliminación implícita; preservar identificadores, conteo y atributos, informar geometrías cambiadas y CheckGeometry posterior. Si ya es válida, no reparar. El notebook no contiene ni ejecuta RepairGeometry ni un script de preparación: consume el insumo preparado de solo lectura, puede comprobar su calidad y se detiene si no es válido para Identity de centros MeanCenter sin ruido por `CLUSTER_ID`. Configurar su ruta en la primera celda de código junto a `DATA_DIR`/`OUTPUT_DIR`; no duplicar incidentes para reunir entradas en una carpeta. Errores puntuales/desconocidos siguen fatales, pendientes de otra decisión; sin deduplicación ni imputación automática. Reportar frontera, coincidencias múltiples y ausencia de jurisdicción sin asignación forzada; reparar la copia no certifica límites legales. Originales, DOCX/TXT fuente y skill del otro diplomado permanecen intactos.

P02 debe completar `DiplomadoGeoIA Ejercicio 5A.docx` en Python autosuficiente, sin ModelBuilder manual ni auxiliar personalizado compartido: EDA visible (diccionario de campos, nulos/ceros, claves, XY, tiempo, CRS y gráficos/mapas ArcGIS) antes de DBSCAN 100/350 m → MeanCenter → Identity válida → Statistics COUNT/AddJoin/CopyFeatures → HDBSCAN 100 → OPTICS 100/350 m con sensibilidad automática predeterminada y mapa/barras/perfil de alcanzabilidad nativos. P01 no cambia. La evidencia existente corresponde a la versión anterior; no acredita ejecución del nuevo alcance. Un fallo bloquea solo lo dependiente; no declarar ejecución/renderizado sin pruebas.

## Preparación externa P02: intento interrumpido

Se creó la copia de `Datos/Datos Ejercicio5A.gdb/Jurisdicciones_Bomberos` en `99 - Recursos/datos/p02_jurisdicciones_preparadas/jurisdicciones.gdb/Jurisdicciones_Bomberos`. CheckGeometry ESRI inicial detectó una auto-intersección (`self intersections`, OBJECTID 5) en 17 polígonos; los atributos de la copia coincidían con el original antes de reparar. Al invocar RepairGeometry con `KEEP_NULL`/`ESRI` sobre la selección afectada, Python terminó con `Fatal Python error: InitDatetime: Could not import datetime C API` e `ImportError: PyCapsule_Import could not import module "datetime"` (salida 127). No hubo reintento.

La copia y la tabla `geometria_antes` se conservan, pero **no constituyen un insumo validado**: no se alcanzaron CheckGeometry posterior, conteo/IDs/atributos finales, identificación de geometrías cambiadas ni comprobación final de integridad de la GDB original. La llamada de reparación se inició; su terminación y efectos no están verificados. No se ejecutó ningún notebook ni operación sobre los puntos. La recuperación y validación quedan pendientes de seguimiento acotado; no usar esta copia para Identity todavía. Una futura validación geométrica no certifica límites legales.

### Recuperación posterior validada — 2026-09-15

Estado vigente: **copia geométricamente válida para continuar la preparación de Identity**, sin certificar límites legales. En proceso Pro 3.6.2/ArcInfo nuevo, aislado (`PYTHONNOUSERSITE=1`, `-X utf8 -B -s`, importación datetime → NumPy 2.2.0 → ArcPy), CheckGeometry confirmó primero la misma auto-intersección de OID 5. Una sola llamada RepairGeometry `KEEP_NULL`/`ESRI` terminó correctamente (0.71 s según GP); CheckGeometry posterior: cero errores. Se mantienen 17 entidades, todos los IDs, CRS y atributos temáticos. Únicamente cambió la geometría de OID 5 y sus medidas automáticas: `Shape_Length` 31947.20460860704 → 31947.204425947064; `Shape_Area` 24920728.137778986 → 24920728.12893815. No se forzaron los valores antiguos de estas medidas derivadas.

La primera validación conservada (`validacion_20260915T163945_530643.json`, 7.792 s desde imports) se detuvo por tratar esas medidas como atributos inmutables; no fue otra caída de Python. La comprobación ajustada distingue medidas de atributos temáticos y terminó válida (`validacion_20260915T164105_730402.json`, 7.089 s), **sin repetir RepairGeometry**: CheckGeometry inicial/final cero, copia sin cambios adicionales. Ambas comparaciones del original contra su baseline actual comprobaron conteo, IDs, todos los atributos y WKB sin cambios; no acreditan retroactivamente la integridad de ejecuciones anteriores ni de toda la GDB. La causa del fallo InitDatetime previo continúa sin determinarse. GP notificó un listado temporal nativo de entidades no simples fuera del directorio preparado; no se leyó ni se conservó aquí ese archivo.

Evidencia y script externo acotado: `99 - Recursos/datos/p02_jurisdicciones_preparadas/`; tablas nuevas `check_antes_*`/`check_despues_*` en `jurisdicciones.gdb`, conservando `geometria_antes`. `recuperar_jurisdicciones.py` no es dependencia del notebook. Comando ejecutado dos veces, primero recuperación y después validación sin reparación:

```bash
PYTHONNOUSERSITE=1 "C:/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe" -X utf8 -B -s "99 - Recursos/datos/p02_jurisdicciones_preparadas/recuperar_jurisdicciones.py"
```

No se editaron ni ejecutaron notebooks, ni se procesaron incidentes. La actualización/ejecución del nuevo alcance P02 sigue pendiente.

## Clase 03 · Entradas para cubos y contrastes

La [[01 - Clases/2026-09-16 - Clase 03 - Cubos espacio-temporales y patrones emergentes|Clase 03, borrador migrado]] usa `99 - Recursos/datos/clase_03/`: `entradas.gdb` contiene `SiniestrosViales`, `UPZ`, `Colegios_Colombia_CollectEvents` e `Incidentes_Control_Abejas_CollectEvents`; la carpeta también contiene `cubo_espacio_temporal_accidentes.nc`.

La [procedencia de estas entradas](clase_03/README.md) explica su selección desde el vault original y sus comprobaciones. Colegios y abejas son preparados históricos con pesos `ICOUNT`, no eventos individuales ni salidas de Clase 02 de este vault. No se repite su preparación.

Configura esa carpeta como `DATA_DIR` en el notebook y conserva las entradas en solo lectura. Las copias y resultados van a `99 - Recursos/salidas_clase_03/practica_01/`, en una subcarpeta nueva por ejecución. **Emerging Hot Spot Analysis modifica el NetCDF que recibe:** usa solo la copia de salida, nunca el cubo de entrada, que ya contiene análisis históricos.

## Antes de compartir

Datos crudos, GDB y resultados generados permanecen ignorados por Git hasta autorización humana. Revisar privacidad y derechos de redistribución **antes de staging o publicación**: disponibilidad local y uso docente no conceden esos derechos. No forzar incorporación ni publicar originales; conservar solo derivados académicos reutilizables, sin credenciales o metadatos privados de extracción. Sin instalaciones, créditos, commit/push o publicación no autorizados.

Volver a [[00 - Índice|Índice]] o [[Templates/Plantilla - Clase|Plantilla de clase]].
