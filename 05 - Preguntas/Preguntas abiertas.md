---
tags: [tipo/preguntas, estado/pendiente, tema/geoia]
---

# Preguntas abiertas

## Clase 01: de grupos a decisiones de Bomberos

**Pregunta fuente:** ¿qué decisión operacional puede tomar Bomberos a partir de estas agrupaciones? Contexto: V13, José Gómez Romero, 2026-06-23, comparación Bomberos 01:45:44–02:01:02 y continuidad anunciada 02:01:05–02:02:40; [[99 - Recursos/Clase 01 - Fuentes y acuerdos|registro V13]].

**Respuesta acotada:** describen concentraciones de registros y permiten formular preguntas para investigación. Por sí solas no localizan estaciones, certifican cobertura ni recomiendan despacho. Hace falta capacidad, red vial, tiempos de respuesta, demanda y restricciones; ninguna optimización se ejecutó aquí. El campo de estación reportada no valida asignación operativa y las jurisdicciones son solo contexto no validado con una auto-intersección, sin estadísticas poligonales.

**Estado:** abierta la decisión operativa; no falta una nueva aprobación del alcance de prácticas. **Responsable de resolver su uso futuro:** equipo docente con especialistas operativos de Bomberos; no se presupone acceso a nuevos datos. [[04 - Proyectos/Ideas de aplicación]] conserva la propuesta, no un ejercicio añadido.

### Preguntas para comprobar comprensión

| Pregunta | Criterio de respuesta respaldado | Estado |
| --- | --- | --- |
| ¿350 m limita todo un grupo? | No: vecindad local y encadenamiento de núcleos; E2–E3 | Explicada en [[02 - Conceptos/DBSCAN]] |
| ¿Menos ruido significa mejor modelo? | No sin criterio de utilidad; cambiar granularidad afecta asignación | Explicada en [[02 - Conceptos/Comparación de métodos de clustering]] |
| ¿PROB=0.9 es significancia? | No: diagnóstico de pertenencia, no valor p; E1/E2/E4 | Explicada en [[02 - Conceptos/HDBSCAN y OPTICS]] |
| ¿Coincidencia XY prueba evento duplicado? | No; las filas se preservan y enlazan por clave técnica | Documentada en [[99 - Recursos/Clase 01 - Resultados de prácticas]] |
| ¿Se ejecutó OPTICS o ubicación de centroides? | No; solo anuncio de continuidad de la siguiente clase fuente | Delimitada en la nota de clase |

La revisión visual final y aprobación académica pertenecen al cierre de [[01 - Clases/2026-09-14 - Clase 01 - Clustering espacial]], no modifican las respuestas técnicas aprobadas P1–P7. Volver a [[00 - Índice|Índice]].
