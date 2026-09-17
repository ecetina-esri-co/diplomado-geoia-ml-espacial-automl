---
tags: [tipo/indice, estado/base]
---

# Diplomado GeoIA · Módulos 5 y 6

Clase 01 tiene nota central, cinco conceptos, dos herramientas y ambos notebooks ejecutados; P02 integra el Ejercicio 5A completo y P01 se preservó sin reejecución. Material listo para revisión académica humana tras comprobaciones técnicas y renderizado local aislado; disposición nativa de Obsidian no comprobada. El paquete completo no está aprobado. Calendario definitivo en [[README]]; reglas en [[AGENTS]].

## Accesos

- [Mapa del diplomado](<00 - Mapa del diplomado.canvas>): tablero sencillo de entrada.
- [[Templates/Plantilla - Clase|Plantilla adaptada]]: escribir directamente la nota y conceptos, sin informes previos.
- [[04 - Proyectos/Ideas de aplicación|Proyectos]]: registrar aportes reales cuando existan.
- [[05 - Preguntas/Preguntas abiertas|Preguntas]]: seguimiento de dudas y decisiones.
- [[99 - Recursos/Enlaces y bibliografía|Bibliografía]]: reutilizar referencias verificadas según afirmación y versión.
- [[99 - Recursos/datos/README|Datos]]: procedencia, selección y rutas configurables.

## Sesiones pendientes

Cada sesión dura dos horas en septiembre de 2026. Clase 03 se incorpora como borrador migrado; las demás entradas conservan su seguimiento previo. No hay enlaces a clases inexistentes.

| Fecha | Identidad confirmada | Tema | Estado |
| --- | --- | --- | --- |
| 2026-09-14 | Clase 01 | Clustering espacial | [[01 - Clases/2026-09-14 - Clase 01 - Clustering espacial|Nota y prácticas]] actualizadas; comprobación técnica y renderizado local aislado completos, revisión académica humana pendiente. P1–P7 aprobadas. |
| 2026-09-15 | Por fecha | Clustering espacial | Pendiente |
| 2026-09-16 | Clase 03 | Minería de patrones espacio-temporales | [[01 - Clases/2026-09-16 - Clase 03 - Cubos espacio-temporales y patrones emergentes|Borrador migrado]]; video parcialmente revisado y cierre del kernel fallido. No procesada completa. |
| 2026-09-17 | Por fecha | Minería de patrones espacio-temporales | Pendiente |
| 2026-09-21 | Por fecha | Minería de patrones espacio-temporales | Pendiente |
| 2026-09-22 | Por fecha | Regresión y clasificación basada en bosques | Pendiente |
| 2026-09-23 | Por fecha | Regresión y clasificación basada en bosques | Pendiente |
| 2026-09-24 | Por fecha | Regresión y clasificación basada en bosques | Pendiente |
| 2026-09-28 | Por fecha | Automatización de modelos (AutoML) | Pendiente |

Las grabaciones 13–15 y 16–20 son ocho fuentes: se documentará su correspondencia por contenido, no una relación uno a uno con estas nueve sesiones.

## Conocimiento y prácticas

[[01 - Clases/2026-09-14 - Clase 01 - Clustering espacial|Clase 01: Clustering espacial]] integra conceptos, código comentado, agenda estimada de 120 minutos y resultados sin repetir ejecuciones.

- [[02 - Conceptos/Aprendizaje no supervisado]]: objetivo, etiquetas y decisiones del analista.
- [[02 - Conceptos/Agrupación espacial]]: proximidad, dependencia y límites territoriales.
- [[02 - Conceptos/DBSCAN]]: vecindad, núcleo, frontera y ruido.
- [[02 - Conceptos/HDBSCAN y OPTICS]]: jerarquía frente a orden y alcanzabilidad.
- [[02 - Conceptos/Comparación de métodos de clustering]]: sensibilidad y co-pertenencia sin óptimo automático.
- [[03 - Herramientas/ArcGIS Pro - Density-based Clustering]]: copia, parámetros y campos geográficos.
- [[03 - Herramientas/scikit-learn - Clustering por densidad]]: experimento sintético y diferencias de implementación.

Prácticas ejecutadas:

- [[99 - Recursos/notebooks/Clase 01 - Practica 01 - Comparacion DBSCAN HDBSCAN sintetica.ipynb|P01: comparación sintética DBSCAN/HDBSCAN]]: `make_moons`, sin contraste Bogotá ni mapas geográficos; mantiene gráficos tabulares ArcGIS y conceptuales.
- [[99 - Recursos/notebooks/Clase 01 - Practica 02 - Clustering Bomberos con ArcGIS Pro.ipynb|P02: clustering de bomberos]]: EDA, DBSCAN, centros/Identity/COUNT/unión, HDBSCAN y OPTICS ejecutados; copia jurisdiccional preparada externamente y comprobada, de solo lectura en el notebook. No certifica límites legales ni cobertura operativa.

### Clase 03 · Del mapa acumulado a los patrones temporales

[[01 - Clases/2026-09-16 - Clase 03 - Cubos espacio-temporales y patrones emergentes|Clase 03]] conecta siniestros fechados con concentración y evolución del patrón; conserva los contrastes de colegios y abejas.

- [[02 - Conceptos/Cubo espacio-temporal]]: cómo combinar ubicación e intervalo.
- [[02 - Conceptos/Emerging Hot Spot Analysis]]: distinguir persistencia e intensificación del agrupamiento.
- [[03 - Herramientas/ArcGIS Pro - Space Time Pattern Mining]]: llevar esas preguntas a ArcGIS Pro.
- [P01: cubo y contrastes](99%20-%20Recursos/notebooks/Clase%2003%20-%20Practica%2001%20-%20Cubos%20espacio-temporales%20y%20patrones%20emergentes.ipynb): 21 celdas de código completadas y 16 PNG guardados, con fallo al cerrar el kernel; no ejecución integral limpia. Consulta las [[99 - Recursos/datos/clase_03/README|entradas seleccionadas y su procedencia]].

El video sigue parcialmente revisado y la revisión integrada está pendiente. Este borrador no equivale a clase procesada ni aprobación académica.

## Próximo paso

Revisión académica humana del contenido escrito, usando [[99 - Recursos/Clase 01 - Fuentes y acuerdos|fuentes y acuerdos]] y [[99 - Recursos/Clase 01 - Resultados de prácticas|resultados vigentes y comprobación técnica/visual]]. No reabrir P1–P7 ni repetir notebooks. Seis diapositivas de referencia seleccionadas para exposición; la captura histórica truncada permanece archivada sin exposición.

Revisar Clase 01 y detenerse. Avances internos no son aprobación académica. Publicación y siguiente clase requieren autorización explícita separada.
