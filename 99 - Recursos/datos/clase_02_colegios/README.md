# Colegios: entrada local de Clase 02, práctica 02

Copia seleccionada para estudiar la distribución y la escala espacial de los colegios. Consumir `colegios.gdb/Colegios_Colombia` como entrada de solo lectura; generar resultados en otra carpeta.

## Procedencia y copia

- **Origen encontrado:** `../diplomado_geoia/99 - Recursos/salidas_clase_14/clase_14_colegios_work.gdb/Colegios_Colombia`, relativo a la raíz de este vault. Es la entrada conservada en una geodatabase de trabajo del vault original, no una capa encontrada en `datos/5C` ni en `Datos Ejercicio5C.gdb`.
- **Destino:** `99 - Recursos/datos/clase_02_colegios/colegios.gdb/Colegios_Colombia`.
- **Copia observada:** 16 de septiembre de 2026, 18:12:45, UTC−05:00. Esta es la fecha de copia, no la fecha de actualización de los datos.
- **Entorno:** ArcGIS Pro 3.6.2, licencia ArcInfo (Advanced), proceso Python nuevo; finalización natural con código **0**.
- **Operación:** CreateFileGDB en destino inexistente y una llamada CopyFeatures a la ruta completa de la feature class, sin selección de capa, extensión de recorte ni reproyección. El origen se utilizó exclusivamente para lectura.
- No se copiaron la geodatabase completa, `_Integrados` ni `_CollectEvents`. No se aplicaron filtros, imputación, deduplicación, Integrate, RepairGeometry ni cambios de CRS.

## Comprobaciones observadas

| Comprobación | Resultado |
| --- | --- |
| Entidades | 10.617 puntos en origen y destino |
| XY únicos | 10.262 |
| Filas adicionales con XY repetidos | 355; conservadas, no eliminadas |
| XY nulos | 0 |
| `Tipo` y `Ciudad` | Sin valores nulos ni vacíos en el origen; atributos copiados idénticos |
| CRS | EPSG:3857, `WGS_1984_Web_Mercator_Auxiliary_Sphere`, unidad `Meter` |
| Esquema | Los siete campos, tipos, alias, longitudes, precisión, escala, nulabilidad y obligatoriedad coinciden |
| Atributos y geometrías | Igualdad exacta de multiconjuntos de todas las tuplas de atributos temáticos + bytes `SHAPE@WKB`, incluidos repetidos |
| Identificadores | También coincide cada OID asociado a sus atributos y WKB entre origen y copia |
| Integridad del origen | Comparación antes/después: mismos OID, atributos y bytes WKB |
| Referencia espacial | Definición completa exportada idéntica entre origen y destino |

Esquema conservado: `OBJECTID` (OID), `Shape` (Geometry), `Nombre` (String, 100), `Dirección` (String, 100), `Tipo` (String, 50; alias **Marca**), `Descripción` (String, 100) y `Ciudad` (String, 50). La igualdad de OID se observó en esta copia; no debe suponerse para toda exportación futura.

## Uso y límites

La entrada representa puntos de interés públicos utilizados en el ejercicio; **no es un censo exhaustivo ni certifica la vigencia o cobertura de todos los establecimientos educativos**. No se infiere fecha de actualización de los registros. Los XY coincidentes requieren interpretación, no eliminación automática. Que el CRS use metros no elimina la distorsión de distancias de Web Mercator.

El notebook conserva su configuración externa anterior: en su copia de estudiante, cambie `DATA_DIR` por la geodatabase local indicada en la [guía principal](../../../README.md). Su código ya añade `Colegios_Colombia`. Esta copia no ejecuta modelos ni resuelve por sí sola los errores de licencia guardados en la última ejecución del [notebook de colegios](../../notebooks/Clase%2002%20-%20Practica%2002%20-%20Colegios%20y%20escala%20espacial.ipynb).

## Referencias de la operación

Documentación oficial Esri, ArcGIS Pro **3.6**, pasajes de sintaxis, uso y licencias verificados el 16 de septiembre de 2026:

- [Create File Geodatabase](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/data-management/create-file-gdb.htm): `arcpy.management.CreateFileGDB(out_folder_path, out_name, {out_version})`; la carpeta debe existir. Disponible con Basic, Standard y Advanced.
- [Copy Features](https://pro.arcgis.com/en/pro-app/3.6/tool-reference/data-management/copy-features.htm): copia geometría y atributos; una selección de capa limitaría los registros, por eso aquí se usó la ruta completa. Disponible con Basic, Standard y Advanced.
