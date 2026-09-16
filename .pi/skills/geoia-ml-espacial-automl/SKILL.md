---
name: geoia-ml-espacial-automl
description: "GeoIA, clase, grabación, Obsidian: prepara una sola clase completa de Machine Learning Espacial y AutoML para revisión humana."
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "2.2"
---

## Activation Contract

Activa para una sesión seleccionada y autorizada de los módulos 5–6. Ajustar instrucciones no autoriza producir material. Lee una vez el contrato necesario de AGENTS y calendario; reutiliza contexto cargado y consulta la referencia solo según necesidad. Clase 01 y sus dos prácticas ya están autorizadas: no reabrir acuerdos P1–P7.

## Hard Rules

- Muestra siempre **Docente:** Fabian Cetina, con esa escritura exacta, en cada nota de clase destino; conserva por separado autores y docentes reales de las fuentes en procedencia y citas.

- Conserva profundidad docente y todos los ejercicios/secuencia: problema, importancia, analogía limitada, definición formal, supuestos, método, parámetros, evaluación, límites, ejemplo real atribuible y relaciones explicadas. Español profesional; menos informes, no menos contenido.
- Cada clase y concepto exige Mermaid y gráficas independientes incrustadas, interpretadas y respaldadas. En cada nota de clase, incorpora obligatoriamente seis diapositivas fuente limpias, completas, legibles, pertinentes y distintas en `## Diapositivas de referencia`, al inicio tras el encabezado y antes de objetivos/agenda, incrustadas sin bloques colapsados. Cada una lleva título, fuente/tiempo o archivo de presentación verificado/número de diapositiva, pie/interpretación y propósito de selección. Solo admite menos tras revisión directa que confirme insuficientes diapositivas aptas; explica brevemente, sin relleno: fallo de acceso/extracción no demuestra insuficiencia. Demos, interfaz, participantes, controles y duplicados no cuentan; tampoco SVG propios, gráficas ni mapas sustituyen las seis. Conserva Mermaid y gráficas independientes, sin ese límite. Declara renderizado no comprobado.
- Incluye código importante comentado dentro de la nota, con lenguaje, imports, configuración, llamadas, explicación, procedencia y estado; no basta enlazar notebooks.
- Una práctica real, un notebook autónomo: objetivos primero en Markdown y primera celda de código corta DATA_DIR/OUTPUT_DIR, celdas educativas comentadas, interpretación de cada salida y evidencia real. ArcGIS primero, complementos justificados, originales intactos; no inventes APIs ni sustituyas gráficos ArcGIS bloqueados.
- Exige mapas/vistas geoespaciales y gráficos ArcGIS pertinentes. Solo P01 Clase 01 `make_moons` está exceptuada de mapas: sintética, sin Bogotá ni EPSG ficticio; mantiene gráficos tabulares ArcGIS y conceptuales. P02: Ejercicio 5A DOCX completo en Python autónomo, sin ModelBuilder manual ni auxiliar personalizado compartido; EDA visible antes de modelos, DBSCAN → MeanCenter sin ruido → Identity con copia válida → Statistics COUNT/AddJoin/CopyFeatures → HDBSCAN → OPTICS, con visuales nativos y parámetros de AGENTS. La preparación geométrica se realiza por separado, fuera de la práctica, sobre una copia nueva jurisdiccional en `99 - Recursos/datos/`: CheckGeometry antes/después y RepairGeometry solo si persisten errores, con `KEEP_NULL` y preservación de IDs/conteo/atributos. El notebook no contiene ni ejecuta RepairGeometry ni un script de preparación; consume el insumo preparado de solo lectura, puede comprobar su calidad y se detiene si no es válido para Identity. Configura su ruta en la primera celda de código junto a DATA_DIR/OUTPUT_DIR, sin duplicar incidentes. No reparar si ya es válida ni extender el permiso; errores puntuales/desconocidos fatales. Informar cambios y coincidencias fronterizas/múltiples/ausentes sin forzar asignación ni certificar límites legales.
- Reutiliza fuentes verificadas; cita cerca y distingue fuente, corrección respaldada y ejecución. Excepción obligatoria en cada procesamiento: abre y revisa el video fuente correcto con Chrome DevTools MCP en Stream/SharePoint visible autorizado; comprueba reproductor/contenido multimedia real, no solo URL/título. Revisa contenido docente, demos, ejercicios y orden con reproducción/línea de tiempo visibles; transcripción visible solo como apoyo. Notas, notebooks, transcripciones guardadas, documentos fuente, acceso histórico y evidencia previa nunca sustituyen revisar el video en esta sesión; no repitas segmentos ya verificados en ella. Registra identidad, tiempos/cobertura y pendientes en procedencia existente, distinguiendo apertura, revisión parcial y cobertura docente pertinente completa; abrir o muestrear diapositivas no basta. Captura solo imágenes académicas limpias; sin vías alternativas, API privada, elusión, descargas prohibidas, transcripciones crudas, credenciales ni metadatos privados retenidos.
- Registra acuerdos/resultados brevemente en nota/notebook; reutiliza evidencia existente, no exijas informes, inventarios exhaustivos, runners, hashes ni ensayos como prerrequisitos. No elimines los existentes.
- No instales, consumas créditos, alteres originales, crees PPTX, hagas commit/push, publiques ni avances de clase sin autorización específica.

## Decision Gates

| Situación | Acción |
| --- | --- |
| Alcance/frontera ambiguos, recorte o cambio de secuencia, nuevos datos/accesos o acción restringida | Consulta la decisión concreta |
| Chrome DevTools MCP o acceso al video no disponibles | Bloquea cobertura dependiente y declaración de clase procesada/completa; material independiente solo como borrador |
| Fuente, entrada/modelo, licencia, ejecución o visual obligatorio faltante | Bloquea solo lo dependiente; informa pendiente, continúa escritura independiente |
| Corrección técnica respaldada o elección editorial reversible autorizada | Resuelve y anota sin aprobación por frase |
| Evidencia vigente sin cambios | Reutiliza salvo revisión directa obligatoria del video en esta sesión; verifica otros cambios o incertidumbre creíble |

## Execution Steps

1. Abre y revisa obligatoriamente el video seleccionado mediante Chrome DevTools MCP según la regla de fuentes; registra cobertura real y pendientes. Lee fuentes necesarias de la única sesión; reutiliza acuerdos y pasajes como apoyo. No mapees las nueve clases para actuar en una.
2. Escribe pronto desde la plantilla: objetivos, agenda estimada de 120 minutos, contenido, código, conceptos y visuales. Marca borrador/resultados pendientes sin esperar notebooks.
3. Trabaja directamente en un notebook por práctica; inspecciona datos/entorno y secciones EDA pertinentes, ejecuta e interpreta. Reutiliza auxiliares salvo en P02, que debe ser autosuficiente sin auxiliar personalizado compartido; crea automatización solo por necesidad concreta.
4. Integra resultados y revisa una vez coherencia, enlaces, referencias, visuales y salidas; revalida solo piezas afectadas. Separa duración medida de estimación, sin ensayo obligatorio.
5. Entrega la clase completa a revisión humana y detente. Avances internos no equivalen a aprobación; publicación y otra clase requieren permiso separado.

## Output Contract

Devuelve archivos reales, resultados/comprobaciones observados, límites y pendientes concisos. No declares completo lo obligatorio faltante ni produzcas un informe separado por defecto.

## References

- [Reglas compartidas](../../../AGENTS.md).
- [Calendario](../../../README.md).
- [Plantilla](<../../../Templates/Plantilla - Clase.md>).
- [Ayuda por necesidad y atribución](references/procesamiento-clase.md).
- [Matriz EDA: secciones pertinentes](<../../../99 - Recursos/Matriz - Análisis exploratorio y ArcGIS.md>).
