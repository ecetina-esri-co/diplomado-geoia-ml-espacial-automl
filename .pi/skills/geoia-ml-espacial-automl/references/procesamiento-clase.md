# Procesamiento directo de una clase GeoIA

Consulta las secciones necesarias, no como preflight completo. El contrato compartido está en [AGENTS](../../../../AGENTS.md); reutiliza lo ya leído y verificado.

## Procedencia y cambios 2.2

Adaptación del original `../diplomado_geoia/.opencode/skills/geoia-class-recording/SKILL.md`, versión 1.1, autor `gentleman-programming`, licencia Apache-2.0. El original es de solo lectura; esta licencia no concede derechos sobre grabaciones, diapositivas ni datos.

La versión 2.2 elimina preparación exhaustiva, aprobaciones internas y revalidaciones rituales; conserva profundidad, ejercicios, visuales, código y ejecución real. El acuerdo vigente exige seis diapositivas fuente en cada nota de clase, visibles después del encabezado y antes de objetivos/agenda, con la única excepción de insuficiencia real comprobada mediante revisión directa, no por fallos de acceso/extracción (criterios en §2). SVG propios, gráficas y mapas no cuentan entre las seis. Se conservan Mermaid y gráficas independientes obligatorios; ArcGIS primero; sin guardar transcripciones crudas; una sesión destino integrada, no equivalencia grabación-clase.

## 1. Partir del alcance conocido

- Consulta el [calendario](../../../../README.md) solo para la sesión activa: módulos 5–6, nueve sesiones de septiembre de 2026. Solo Clase 01 tiene autorización actual; acuerdos P1–P7 y dos notebooks no se reabren.
- Abre y revisa obligatoriamente el video seleccionado mediante Chrome DevTools MCP según la regla siguiente. Lee fuentes necesarias de grabaciones 13–20: ocho fuentes para nueve destinos. No mapees todas para escribir una clase.
- Reutiliza acuerdos, localizadores, pasajes verificados y resultados registrados como apoyo, nunca como sustituto de la revisión directa obligatoria del video en esta sesión. Para las demás fuentes, solo nuevas afirmaciones, versiones/datos cambiados o contradicciones requieren nueva comprobación.
- Distingue título, fecha y número fuente de destino; registra brevemente qué contenido/ejercicio respalda cada fuente, sin inventar equivalencia uno a uno.
- Conserva ejercicios y secuencia. Consulta antes de omitir, reordenar o trasladar contenido, también por falta de tiempo.

### Revisión directa obligatoria del video

En cada procesamiento de clase, usa Chrome DevTools MCP sobre la interfaz visible autorizada de Stream/SharePoint: abre la fuente correcta y comprueba acceso real al reproductor/contenido multimedia, no solo URL/título. Revisa contenido docente, demos, ejercicios y secuencia mediante reproducción/línea de tiempo visibles; el panel visible de transcripción es solo apoyo. Notas, notebooks, transcripciones guardadas, documentos fuente, indicadores históricos de acceso y evidencia previa nunca sustituyen esta revisión en la sesión actual. Es la excepción a no repetir consultas: no exige reproducir de nuevo segmentos ya verificados dentro de esta misma sesión.

Registra brevemente identidad fuente, tiempos revisados, cobertura y pendientes en la procedencia existente de la nota, sin informe nuevo. Distingue apertura, revisión parcial y cobertura docente pertinente completa: abrir la URL o muestrear diapositivas no prueba procesamiento completo. Captura solo imágenes académicas limpias; no persistas transcripciones crudas, credenciales ni metadatos privados. Sin vías alternativas, API privada, elusión de login/MFA ni descargas prohibidas. Si falta herramienta o acceso, bloquea cobertura dependiente y declaración de clase procesada/completa; material independiente solo como borrador. Solicita la acción mínima, nunca credenciales.

## 2. Escribir primero el material docente

Crea pronto la nota desde la [plantilla](<../../../../Templates/Plantilla - Clase.md>): objetivos observables, agenda **estimada** de 120 minutos, contenido, código, conceptos y visuales. No esperes ejecución, inventario o informe previo. Marca resultados pendientes sin rellenar notas finales con marcadores vacíos.

Para cada concepto desarrolla problema e importancia, analogía con límites, definición formal, supuestos, método/pasos, parámetros, evaluación y límites. Añade ejemplo real atribuible y explica relaciones con otros conceptos, herramientas y práctica. La profundidad depende del concepto, no de una cuota de líneas.

Crea notas reutilizables de conceptos/herramientas cuando aporten conocimiento, no para llenar carpetas. Cada clase y concepto necesita Mermaid válido y legible **y** gráficas explicativas independientes, incrustadas y suficientemente variadas para cubrir procesos/etapas. Explica lectura, escalas, conclusión y límites; identifica elaboración propia y fuentes. Declara renderizado no comprobado.

Capturas fuente: incorpora obligatoriamente seis diapositivas fuente en `## Diapositivas de referencia`, al inicio de cada nota de clase, después del encabezado y antes de objetivos/agenda, incrustadas y visibles sin desplegar bloques. Deben ser limpias, completas, legibles, pertinentes y distintas; cada una con título, fuente/tiempo o archivo de presentación verificado/número de diapositiva, pie/interpretación y propósito de selección. Solo admite menos si la revisión directa confirma que la fuente realmente no ofrece suficientes diapositivas aptas; explica brevemente esa excepción, sin relleno. Fallos técnicos de acceso/extracción no prueban insuficiencia de la fuente. Demos, interfaz, participantes, controles y duplicados no cuentan. SVG propios, gráficas y mapas tampoco cuentan entre las seis ni sustituyen capturas; siguen siendo necesarios junto con Mermaid, sin ese límite para recursos propios.

Cita junto a la afirmación título, autor/institución, URL, versión, sección y fecha de consulta; grabación/tiempo o archivo/diapositiva cuando corresponda. Reutiliza pasajes ya verificados, no URLs recordadas ni fragmentos de búsqueda. Prefiere Esri para sus productos y fuentes oficiales/primarias pertinentes. Separa fuente, explicación/corrección respaldada y resultado ejecutado. Corrige errores técnicos documentados sin pedir aprobación por frase; consulta ambigüedad que cambie contenido o significado.

Incluye en la nota bloques con lenguaje para imports, configuración y operaciones importantes: propósito/requisitos/entradas antes, comentarios dentro, parámetros/salida/interpretación después. Indica procedencia, adaptación, documentación pertinente y ejecución real; no sustituyas por enlaces ni copies todo el notebook.

## 3. Resolver cada práctica directamente

- Una práctica por pregunta, datos y secuencia metodológica, no por algoritmo. Un notebook autónomo por práctica; consulta solo fronteras realmente ambiguas.
- Usa `99 - Recursos/notebooks/Clase NN - Practica PP - Tema.ipynb`; entradas compartidas de solo lectura y salidas `99 - Recursos/salidas_clase_NN/practica_PP/` o equivalente externo.
- Objetivos primero en Markdown; primera celda de código única y corta: `DATA_DIR` y `OUTPUT_DIR`, comentada y explicando cómo cambiar rutas. Sin estado oculto de otro notebook; declara/verifica auxiliares compartidos.
- Enseña propósito, pregunta, datos, método, requisitos, pasos, parámetros y evaluación antes de ejecutar. Cada celda de código lleva comentarios educativos; cada salida, lectura, conclusión y límites.
- Prefiere ejecución directa en ArcGIS Pro. Reutiliza auxiliares existentes; crea automatización solo para problemas concretos o repetición. Ningún runner, test genérico, hash o informe separado es prerrequisito. Conserva los existentes y su evidencia.

### Datos y capacidades pertinentes

Consulta la [guía de datos](<../../../../99 - Recursos/datos/README.md>) para nuevas entradas y únicamente las secciones aplicables de la [matriz EDA](<../../../../99 - Recursos/Matriz - Análisis exploratorio y ArcGIS.md>) ante operaciones o dudas. Reutiliza disponibilidad local; no dupliques datos ni exijas expedientes de uso local ya autorizado.

Verifica campos usados, tipos/significado, nulos/ceros, claves duplicadas, geometrías, distancias, SR/unidades y tiempo pertinentes. No heredes EPSG ni resultados históricos. Trabaja sobre copias; no dedupliques, imputes, elimines ni transformes automáticamente; no repares sin autorización, salvo la excepción P02 explícita siguiente. Calculate Field puede modificar entradas: nunca originales.

Evalúa ingeniería de datos/EDA y visualización ArcGIS primero según la pregunta. Comprueba documentación oficial, firma, versión/licencia y dependencias de las operaciones usadas, no un catálogo. Distingue UI, API documentada y ejecución: Data Engineering es una vista, no `arcpy.DataEngineering`. Prefiere subclases `arcpy.charts` documentadas a `Chart` heredado.

Conserva y explica NumPy/pandas/scikit-learn de la fuente; justifica complementos con fuentes oficiales sin reemplazarlos indiscriminadamente por ArcPy ni duplicar análisis. Inferencia espacial, diagnóstico supervisado y reducción dimensional no son EDA universal.

### Salidas y límites aprobados

Notebooks geográficos requieren mapas/escenas/vistas ArcGIS y gráficos ArcGIS interpretados en etapas relevantes; tablas/métricas no sustituyen mapas ni Matplotlib sustituye gráficos ArcGIS bloqueados.

**Solo P01 Clase 01 `make_moons`:** sintética, sin contraste Bogotá, EPSG ficticio, georreferenciación ni mapas geográficos; sí gráficos tabulares ArcGIS y conceptuales. No extender esta excepción sin decisión.

**P02 Clase 01:** completar `DiplomadoGeoIA Ejercicio 5A.docx` en un notebook Python autosuficiente, sin ModelBuilder manual ni auxiliar personalizado compartido. EDA visible antes de modelos: diccionario de campos, nulos/ceros, claves, XY, tiempo y CRS, gráficos y mapas ArcGIS. DBSCAN 100/350 m → MeanCenter sin ruido por `CLUSTER_ID` → Identity de centros con copia jurisdiccional válida → Statistics COUNT/AddJoin/CopyFeatures → HDBSCAN 100 → OPTICS 100/350 m y sensibilidad automática predeterminada, con mapa, barras y perfil de alcanzabilidad nativos.

**Preparación geométrica P02 autorizada, fuera de la práctica:** preparar por separado una copia nueva jurisdiccional en `99 - Recursos/datos/` y comprobarla con CheckGeometry. Si persisten errores, RepairGeometry solo en esa copia con `KEEP_NULL`, preservando IDs/conteo/atributos; informar geometrías cambiadas y CheckGeometry posterior. No reparar si ya es válida. El notebook no contiene ni ejecuta RepairGeometry ni un script de preparación: consume el insumo preparado de solo lectura, puede comprobar su calidad y se detiene si no es válido para Identity. Su ruta se configura en la primera celda de código junto a `DATA_DIR`/`OUTPUT_DIR`, sin duplicar incidentes. Errores puntuales/desconocidos siguen fatales hasta otra decisión. Reportar fronteras, coincidencias múltiples y ausencia de jurisdicción sin asignación forzada; no certificar límites legales. No extender el permiso ni alterar originales, DOCX/TXT o la skill original. Conservar evidencia anterior sin presentarla como resultados del nuevo alcance; P01 intacta. Un bloqueo dependiente no detiene escritura independiente.

## 4. Integrar y cerrar una vez

Bastan secciones breves de nota/notebook con fuentes, PP → entradas/notebook/salidas/estado, acuerdos y evidencia enlazada. No crear informes o matrices como preinsumos; reutilizar registros existentes. Integrar resultados realmente observados con entorno y parámetros; distinguir esperado de ejecutado.

Revisar de forma enfocada coherencia, profundidad, cobertura fuente, enlaces existentes, visuales, código comentado y salidas. No repetir consultas o notebooks completos sin cambios o incertidumbre creíble, salvo la revisión directa obligatoria del video en cada sesión de procesamiento descrita en §1. Agenda de 120 minutos estimada; duración de ejecución medida aparte, sin ensayo obligatorio ni ficticio.

Actualizar navegación solo donde aporte: enlaces explicados, notas no huérfanas, Canvas ligero. Retirar instrucciones/marcadores de notas finales; la plantilla los conserva. Un obligatorio faltante bloquea completar su pieza y, por tanto, el paquete, no el trabajo independiente.

Informar archivos, evidencia, comprobaciones reales y pendientes de forma concisa. Consultar decisiones humanas genuinas, no formatos rutinarios o arreglos simples. Sin instalaciones, créditos, cambios de originales, PPTX, commit/push o publicación no autorizados; revisar privacidad y redistribución antes de staging/publicación. Entregar una clase completa para revisión humana y detenerse: otra clase y publicación requieren permiso separado.
