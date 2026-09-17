# Escribir una clase que se pueda comprender

Guía opcional para resolver problemas concretos de redacción. Las políticas y autorizaciones están en [AGENTS](../../../../AGENTS.md); el flujo de trabajo está en la [skill](../SKILL.md). No usar esta guía como lista de encabezados que deba aparecer en cada concepto.

## Del problema a la explicación

Una explicación puede comenzar con una pregunta que el estudiante reconozca: «¿Estos puntos forman grupos o solo parecen cercanos en el mapa?». Un ejemplo concreto permite decir qué queremos distinguir antes de introducir términos. Después, el método da precisión a esa intuición; una demostración permite contrastarla y el resultado devuelve la conversación a la pregunta inicial.

Ese recorrido es flexible. Un concepto breve puede integrarse en el relato sin subdivisiones; un método difícil puede necesitar varias subsecciones, fórmulas y demostraciones. En ambos casos se mantienen los recursos visuales obligatorios de AGENTS. El tamaño depende de lo que haya que comprender, no de un mínimo de líneas. Elegir títulos que expresen dudas o ideas del tema, no repetir «problema / analogía / definición / ejemplo / relaciones / visuales / respaldo» como formulario.

Una analogía ayuda si se explican sus correspondencias y dónde falla. Por ejemplo, comparar agrupaciones con personas que se reúnen en una plaza ayuda a imaginar proximidad, pero no define por sí sola una distancia, densidad mínima o regla de pertenencia. La explicación técnica debe resolver justamente lo que la analogía deja abierto.

## Precisar sin convertir el texto en inventario

Introducir una fórmula cuando permita razonar sobre una decisión. Definir símbolos, unidades y condiciones de aplicación junto a ella, y mostrar cómo cambia la lectura al variar un parámetro. Evitar tanto la fórmula ornamental como suprimirla cuando es necesaria.

Separar preguntas que parecen iguales: describir agrupaciones no demuestra significancia estadística ni identifica una causa. Una explicación rigurosa conecta cada conclusión con lo que el método realmente evalúa y con los datos disponibles. Los ejemplos editoriales de esta guía no sustituyen la documentación técnica verificada.

Para relacionar conceptos, explicar la dependencia: «La elección de distancia cambia qué observaciones consideramos vecinas; por eso conviene revisar el sistema de referencia antes de interpretar el agrupamiento». Después enlazar la nota existente que desarrolla esa idea. Un conjunto de enlaces sin esa relación no enseña.

## Hacer trabajar a las imágenes

Colocar el visual donde resuelve una dificultad: un diagrama para seguir decisiones, una gráfica para comparar comportamientos, un mapa para interpretar distribución espacial. La política de recursos obligatorios está en [AGENTS: Visuales y código que enseñan](../../../../AGENTS.md#visuales-y-código-que-enseñan); esta guía orienta su integración, no reduce sus requisitos.

Una interpretación puede integrar lectura y límite sin repetir un formulario: «El eje horizontal representa la distancia; el vertical, el indicador definido arriba. El cambio entre los dos escenarios muestra sensibilidad a esa elección, pero no prueba causalidad». Ajustar siempre este texto a la figura real: no atribuir tendencias a resultados aún no observados.

Interpretar cada recurso una vez donde enseña. Las diapositivas iniciales sitúan las ideas de la fuente; el desarrollo puede remitir a ellas sin volver a incrustarlas. Las gráficas y diagramas propios tienen su función explicativa independiente, con procedencia de ideas/datos y distinción entre ilustración conceptual y resultado real.

## Del código a una decisión comprensible

Antes de un bloque, explicar qué pregunta resuelve y qué recibe. Dentro, comentar las decisiones que el estudiante necesita entender, no narrar cada carácter. Después, leer la salida y explicar qué permite concluir o por qué todavía no basta. La nota conserva fragmentos importantes; el notebook contiene el recorrido autónomo completo conforme a [AGENTS: Prácticas, datos y ArcGIS](../../../../AGENTS.md#prácticas-datos-y-arcgis).

En vez de «el orquestador comprobó la etapa y guardó el run ID», escribir lo que interesa al estudiante: «Comparamos el número de registros antes y después del filtro para saber qué población analizaremos». Si la comparación no se ejecutó, presentarla como tarea o resultado esperado, nunca como observación.

No ocultar un problema para hacer fluida la narración. «No se obtuvo este mapa por una restricción de licencia» es un límite comprensible; los detalles del entorno y el enlace al error pertenecen al registro final. Una tabla no reemplaza un mapa obligatorio pendiente.

## Citas cercanas, evidencia al final

Usar una cita compacta al lado de la afirmación —por ejemplo, autor/institución y sección enlazados— y conservar los datos completos de la referencia en el registro final. Para un pasaje de video, incluir su identidad y tiempo. Así se puede verificar el respaldo sin interrumpir cada párrafo con la misma ficha bibliográfica.

El registro final puede reunir:

- Fuentes y correspondencia entre grabación y clase destino; adaptaciones o correcciones respaldadas.
- Cobertura real del video y pendientes, sin confundir apertura, revisión parcial y cobertura pertinente completa.
- Práctica → notebook → entrada de solo lectura → salida → estado, enlazando archivos físicos existentes.
- Entorno y parámetros usados, tiempo de ejecución medido y comprobaciones realmente observadas; límites que siguen abiertos.

No duplicar ese registro en cada explicación ni crear un informe nuevo por costumbre. Los resultados se interpretan cerca de sus salidas y las citas permanecen junto a sus afirmaciones. Los registros históricos se conservan como históricos; no prueban una ejecución nueva.

## Lectura final desde el lugar del estudiante

Leer una sección preguntándose si se entiende qué buscamos, por qué elegimos el método y qué podemos concluir. Si una lista interrumpe el razonamiento, convertirla en explicación; si el párrafo oculta una secuencia operativa, una lista breve puede ayudar. No es una prohibición de tablas, listas o subtítulos, sino una elección según su función.

La [plantilla](<../../../../Templates/Plantilla - Clase.md>) propone puntos de entrada, no títulos obligatorios para cada concepto. Quitar sus marcadores al finalizar y conservar las dudas reales. Revisar el rigor técnico contra fuentes verificadas, no copiar interpretaciones del vault original solo por su estilo.

## Procedencia editorial

Adaptación del original `../diplomado_geoia/.opencode/skills/geoia-class-recording/SKILL.md`, versión 1.1, autor `gentleman-programming`, licencia Apache-2.0. El original permanece de solo lectura; esa licencia no concede derechos sobre grabaciones, diapositivas ni datos.

La revisión 2.3 separa políticas, flujo y ayuda de escritura para recuperar una explicación natural sin reducir profundidad ni requisitos. No modifica ejercicios ni constituye revisión del video o ejecución de prácticas.
