"""Apoyo docente local: aislamiento, perfiles agregados y visuales ArcGIS Pro 3.6.

Dependencia compartida declarada por ambas prácticas; no ejecuta modelos al importar.
Las llamadas de clustering permanecen visibles en los notebooks. Sin servicios ni CURRENT.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import math
import uuid


def validate_paths(data_dir, output_dir, protected=()):
    """Rechaza igualdad, ancestros, descendientes y rutas dentro de geodatabases."""
    data, output = Path(data_dir).resolve(), Path(output_dir).resolve()
    # Resolver enlaces antes de comparar evita que un alias eluda el aislamiento.
    for original in (data, *(Path(p).resolve() for p in protected)):
        if output == original or output in original.parents or original in output.parents:
            raise ValueError('Entrada y salida deben estar completamente separadas.')
    if any(p.suffix.lower() == '.gdb' for p in (output, *output.parents)):
        raise ValueError('La raíz de resultados no puede estar dentro de una GDB.')
    return data, output


def new_run(data_dir, output_dir, protected=()):
    """Crea exclusivamente un directorio nuevo, sin sobrescribir ejecuciones anteriores."""
    _, output = validate_paths(data_dir, output_dir, protected)
    import os
    selected = os.environ.get('GEOIA_P01_RUN')
    if selected:
        run = Path(selected).resolve()
        if run.parent != output or not run.is_dir():
            raise RuntimeError('Ejecución seleccionada fuera de la salida configurada.')
        return run
    run = output / ('ejecucion_'  + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')
                    + '_' + uuid.uuid4().hex[:8])
    run.mkdir(parents=True, exist_ok=False)
    return run


def fingerprint(path):
    """SHA-256 compuesto: contenido y nombres relativos, excluyendo solo archivos .lock."""
    path = Path(path)
    digest = hashlib.sha256()
    files = [path] if path.is_file() else sorted(p for p in path.rglob('*')
                                               if p.is_file() and p.suffix.lower() != '.lock')
    if not files:
        raise ValueError('No hay archivos para comprobar integridad.')
    for file in files:
        digest.update((file.name if path.is_file() else file.relative_to(path).as_posix()).encode())
        with file.open('rb') as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b''):
                digest.update(block)
    return {'sha256': digest.hexdigest(), 'archivos': len(files)}


def assess_geometry(rows, points, jurisdictions):
    """Clasifica CLASS por ruta completa; solo contexto conocido admite advertencias."""
    import ntpath
    normalize = lambda value: ntpath.normcase(ntpath.normpath(str(value)))
    point_path, context_path = normalize(points), normalize(jurisdictions)
    if point_path == context_path:
        raise ValueError('Las clases de puntos y contexto deben ser distintas.')
    result = {'points_errors': 0, 'context_errors': 0, 'unknown_errors': 0,
              'context_problems': {}, 'context_only_approved': True}
    for feature_class, problem in rows:
        key = normalize(feature_class)
        if key == point_path:
            result['points_errors'] += 1
        elif key == context_path:
            result['context_errors'] += 1
            text = str(problem)
            result['context_problems'][text] = result['context_problems'].get(text, 0) + 1
        else:
            result['unknown_errors'] += 1
    return result


def require_geometry(result, nonfinite=0):
    """Los puntos y clases desconocidas siguen bloqueando; no reparar ni filtrar."""
    if result['points_errors'] or result['unknown_errors'] or nonfinite:
        raise RuntimeError('Geometría de puntos o clase desconocida: modelado detenido.')
    if result['context_errors'] and not result['context_only_approved']:
        raise RuntimeError('Contexto sin autorización para continuar.')
    return ('ADVERTENCIA: jurisdicciones solo como contexto no validado; '
            + str(result['context_problems']) + '. Sin análisis poligonal ni reparación.'
            if result['context_errors'] else '')


def input_hashes(identities):
    """Las identidades estables viven en el proceso padre, nunca se publican sus rutas."""
    return {key: fingerprint(path) for key, path in identities.items()}


def require_hash_match(before, after):
    """Ausencia de baseline, claves incompletas o cambios nunca equivalen a éxito."""
    if not before or set(before) != {'gdb', 'plantilla'} or before != after:
        raise RuntimeError('Integridad original no demostrada.')
    for value in before.values():
        if not value.get('sha256') or value.get('archivos', 0) < 1:
            raise RuntimeError('Baseline de integridad incompleta.')


def start_integrity(run, identities):
    """Persistir antes de CopyFeatures; no depende de variables del kernel."""
    baseline = {'run_id': run.name, 'hashes': input_hashes(identities)}
    (run / 'integridad_antes.json').write_text(json.dumps(baseline, indent=2), encoding='utf-8')
    return baseline['hashes']


def finish_integrity(run, identities):
    """Finaliza también tras error del kernel y deja evidencia explícita si falla."""
    result = {'run_id': run.name, 'coinciden': False}
    try:
        result['hashes'] = input_hashes(identities)
        baseline = json.loads((run / 'integridad_antes.json').read_text(encoding='utf-8'))
        if baseline.get('run_id') != run.name:
            raise RuntimeError('Baseline pertenece a otra ejecución.')
        require_hash_match(baseline.get('hashes'), result['hashes'])
        result['coinciden'] = True
    except Exception as exc:
        result['error_tipo'] = type(exc).__name__
        raise
    finally:
        (run / 'integridad_despues.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    return result


def prepared_run(data_dir, output_dir, template):
    """Reutiliza solo la ejecución explícita del runner o prepara una autónoma."""
    import os
    selected = os.environ.get('GEOIA_P02_RUN')
    identities = {'gdb': Path(data_dir) / 'Datos Ejercicio5A.gdb', 'plantilla': template}
    if selected:
        run = Path(selected).resolve()
        validate_paths(data_dir, output_dir, [template])
        if run.parent != Path(output_dir).resolve() or not run.is_dir():
            raise RuntimeError('Ejecución seleccionada fuera de la salida configurada.')
        baseline = json.loads((run / 'integridad_antes.json').read_text(encoding='utf-8'))
        if baseline.get('run_id') != run.name:
            raise RuntimeError('Identidad de ejecución incompatible.')
        require_hash_match(baseline.get('hashes'), input_hashes(identities))
        return run, baseline['hashes']
    run = new_run(data_dir, output_dir, [template])
    return run, start_integrity(run, identities)


def blank_template():
    """Única plantilla admitida: recurso instalado de Esri, nunca un proyecto privado."""
    import arcpy
    path = Path(arcpy.GetInstallInfo()['InstallDir']) / 'Resources/ArcToolBox/Services/routingservices/data/Blank.aprx'
    if not path.is_file():
        raise RuntimeError('No está disponible la plantilla instalada autorizada.')
    return path


def configure_arcpy(run):
    """Todos los destinos GP y temporales ArcPy quedan en la ejecución nueva."""
    import arcpy
    arcpy.env.overwriteOutput = False
    arcpy.env.parallelProcessingFactor = '0'
    arcpy.env.workspace = str(run)
    arcpy.env.scratchWorkspace = str(run)
    arcpy.SetLogHistory(False)
    arcpy.SetLogMetadata(False)
    arcpy.management.CreateFileGDB(str(run), 'trabajo.gdb', 'CURRENT')
    return run / 'trabajo.gdb'


def runtime():
    """Solo versiones y licencia, nunca identidad del usuario ni rutas personales."""
    import arcpy
    import platform
    from importlib.metadata import version
    return {'python': platform.python_version(), 'arcgis_pro': arcpy.GetInstallInfo()['Version'],
            'licencia': arcpy.ProductInfo(),
            'paquetes': {p: version(p) for p in ('numpy', 'pandas', 'scikit-learn',
                                                 'matplotlib', 'nbclient', 'ipykernel')}}


def write_evidence(run, evidence):
    """Guarda únicamente métricas agregadas y nombres de artefactos docentes."""
    evidence['runtime'] = runtime()
    evidence['png'] = sorted(p.name for p in run.glob('*.png'))
    (run / 'evidencia.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding='utf-8')


def summary(labels):
    """Cuenta grupos excluyendo ruido; el mayor grupo tampoco incluye ruido."""
    counts = Counter(int(v) for v in labels)
    total = sum(counts.values())
    assigned = {k: n for k, n in counts.items() if k != -1}
    return {'filas': total, 'clusters': len(assigned), 'ruido': counts.get(-1, 0),
            'porcentaje_ruido': 100 * counts.get(-1, 0) / total if total else 0,
            'mayor_cluster': max(assigned.values(), default=0)}


def native_profile(table, fields, gdb, name):
    """ArcGIS primero: descriptivos elegidos por semántica, sin medias de identificadores."""
    import arcpy
    arcpy.management.FieldStatisticsToTable(
        str(table), fields, str(gdb), [['ALL', name]],
        out_statistics=[['FIELDNAME', 'campo'], ['FIELDTYPE', 'tipo'],
                        ['COUNT', 'conteo'], ['NULLS', 'nulos'],
                        ['NUMBEROFUNIQUEVALUES', 'unicos'],
                        ['MINIMUM', 'minimo'], ['MAXIMUM', 'maximo']])
    return str(gdb / name)


def chart_png(chart, run, name):
    """Exportación PNG nativa; una excepción detiene la práctica, sin sustitución."""
    path = run / (name + '.png')
    chart.theme = 'Light'
    chart.displaySize = [1100, 680]
    chart.exportToPNG(str(path), 1800, 1100)
    return path


def bar_csv(frame, run, name, x, y, title):
    """Tabla agregada local: etiquetas nominales de texto, valores numéricos."""
    import arcpy
    csv = run / (name + '.csv')
    # BOM identifica UTF-8 al controlador de tablas de Pro para categorías con tildes.
    frame.to_csv(csv, index=False, encoding='utf-8-sig')
    return chart_png(arcpy.charts.Bar(x=x, y=y, aggregation='SUM',
                     dataSource=str(csv), title=title, xTitle='Categoría',
                     yTitle='Cantidad', rotated=True), run, name)


def scatter_csv(frame, run, name, title):
    """Dispersión de atributos sintéticos: no mapa, sin referencia espacial."""
    import arcpy
    csv = run / (name + '.csv')
    frame.to_csv(csv, index=False, encoding='utf-8')
    return chart_png(arcpy.charts.Scatter('Variable1', 'Variable2',
                     splitCategory='Grupo', showTrendLine=False,
                     dataSource=str(csv), title=title,
                     xTitle='Variable 1 (sin unidades territoriales)',
                     yTitle='Variable 2 (sin unidades territoriales)'), run, name)


def plot_labels(ax, values, labels, title, core=None):
    """Panel sintético: colores nominales, ruido gris y núcleos mayores."""
    import numpy as np
    import matplotlib.pyplot as plt
    labels = np.asarray(labels)
    for label in sorted(set(labels)):
        mask = labels == label
        palette = ['#0f766e', '#d97732', '#665191', '#4477aa', '#aa4499', '#80802b']
        color = '#737b83' if label == -1 else palette[int(label) % len(palette)]
        sizes = 22 if core is None else np.where(core[mask], 65, 20)
        ax.scatter(values[mask, 0], values[mask, 1], c=[color], s=sizes,
                   marker='x' if label == -1 else 'o', alpha=.8)
    ax.set(title=title, xlabel='Variable 1 estandarizada', ylabel='Variable 2 estandarizada')
    ax.set_facecolor('#f7f9fa')
    ax.title.set_color('#142b40')
    ax.tick_params(colors='#142b40', labelsize=10)
    ax.grid(color='#cbd5df', alpha=.45)
    ax.text(.02, .02, 'Gris: ruido · colores: grupos, sin orden', transform=ax.transAxes,
            fontsize=8, color='#142b40', bbox=dict(facecolor='white', alpha=.85, edgecolor='none'))


def profile_incidents(fc):
    """Lee campos mínimos; devuelve agregados, no registros ni coordenadas en logs."""
    import arcpy
    fields = ['IncidentesBomberos_FECHA', 'IncidentesBomberos_NUMERO_INC',
              'IncidentesBomberos_ESTACION', 'SHAPE@XY']
    ids, xy, stations, years = Counter(), Counter(), Counter(), Counter()
    nulls = dict.fromkeys(fields[:3], 0)
    dates, nonfinite, rows, zero_ids = [], 0, 0, 0
    with arcpy.da.SearchCursor(str(fc), fields) as cursor:
        for date, identifier, station, point in cursor:
            rows += 1
            for field, value in zip(fields[:3], (date, identifier, station)):
                nulls[field] += value is None or value == ''
            if date is not None:
                dates.append(date)
                years[str(date.year)] += 1
            if identifier is not None:
                ids[identifier] += 1
                zero_ids += identifier == 0
            stations[station] += 1
            if point is None or not all(math.isfinite(v) for v in point):
                nonfinite += 1
            else:
                xy[point] += 1
    def repeated(counter):
        return {'distintas': len(counter), 'claves_repetidas': sum(v > 1 for v in counter.values()),
                'filas_excedentes': sum(v - 1 for v in counter.values())}
    sr = arcpy.Describe(str(fc)).spatialReference
    return {'filas': rows, 'nulos': nulls, 'id_cero': zero_ids,
            'ids_no_nulos': repeated(ids), 'xy': repeated(xy), 'xy_no_finitas': nonfinite,
            'fecha_min': min(dates).isoformat(), 'fecha_max': max(dates).isoformat(),
            'estaciones': dict(sorted(stations.items())), 'anios': dict(sorted(years.items())),
            'wkid': sr.factoryCode, 'unidades': sr.linearUnitName}


def output_labels(fc, expected, hdb=False):
    """SOURCE_ID enlaza OID de la copia; exige esquema y cobertura íntegra de registros."""
    import arcpy
    import pandas as pd
    fields = ['SOURCE_ID', 'CLUSTER_ID', 'COLOR_ID']
    if hdb:
        fields += ['PROB', 'OUTLIER', 'EXEMPLAR']
    available = {f.name for f in arcpy.ListFields(str(fc))}
    if not set(fields) <= available:
        raise RuntimeError('Faltan campos esperados en la salida de clustering.')
    with arcpy.da.SearchCursor(str(fc), fields) as cursor:
        frame = pd.DataFrame(list(cursor), columns=fields)
    if len(frame) != expected or frame.SOURCE_ID.isna().any() or not frame.SOURCE_ID.is_unique:
        raise RuntimeError('La salida no preserva la cobertura y clave técnica esperadas.')
    if frame.CLUSTER_ID.isna().any():
        raise RuntimeError('Hay etiquetas nulas que requieren inspección.')
    return frame


def pair_comparison(db, hdb):
    """Co-pertenencia entre pares asignados: invariante a renumerar los grupos."""
    joined = db[['SOURCE_ID', 'CLUSTER_ID']].merge(hdb[['SOURCE_ID', 'CLUSTER_ID']],
                on='SOURCE_ID', validate='one_to_one', suffixes=('_db', '_hdb'))
    if len(joined) != len(db) or len(joined) != len(hdb):
        raise RuntimeError('Las claves técnicas no cubren las mismas observaciones.')
    # El ruido no se trata como un gran grupo para contar pares.
    choose2 = lambda n: int(n) * (int(n) - 1) // 2
    both = joined[(joined.CLUSTER_ID_db != -1) & (joined.CLUSTER_ID_hdb != -1)]
    intersection = sum(choose2(n) for n in both.groupby(['CLUSTER_ID_db', 'CLUSTER_ID_hdb']).size())
    dbpairs = sum(choose2(n) for n in db.loc[db.CLUSTER_ID != -1].groupby('CLUSTER_ID').size())
    hdpairs = sum(choose2(n) for n in hdb.loc[hdb.CLUSTER_ID != -1].groupby('CLUSTER_ID').size())
    union = dbpairs + hdpairs - intersection
    return {'filas_enlazadas': len(joined), 'pares_compartidos': intersection,
            'pares_dbscan': dbpairs, 'pares_hdbscan': hdpairs,
            'jaccard_copertenencia': intersection / union if union else None}


def _rect(x0, y0, x1, y1):
    """Geometría de página en pulgadas, no una referencia inventada para datos."""
    import arcpy
    return arcpy.Polygon(arcpy.Array([arcpy.Point(x0, y0), arcpy.Point(x1, y0),
                                     arcpy.Point(x1, y1), arcpy.Point(x0, y1)]))


def export_map(template, points, jurisdictions, run, name, title, extent, clusters=False):
    """Mapa local desde Blank autorizado; misma extensión de entrada en comparaciones.

    Esri Pro 3.6: ArcGISProject/Map/Layout/PNGFormat/UniqueValueRenderer/Symbol.
    No guarda la plantilla, no abre vistas y retira capas predeterminadas antes de dibujar.
    """
    import arcpy
    import colorsys
    project = arcpy.mp.ArcGISProject(str(template))
    # Eliminar mapas de plantilla en memoria evita conservar conexiones ajenas.
    for previous in project.listMaps():
        project.deleteItem(previous)
    map_obj = project.createMap(name, 'MAP')
    for layer in map_obj.listLayers():
        map_obj.removeLayer(layer)
    map_obj.spatialReference = arcpy.Describe(str(points)).spatialReference
    polygons = map_obj.addDataFromPath(str(jurisdictions))
    polygons.name = 'Contexto no validado (auto-intersección)'
    sym = polygons.symbology
    sym.updateRenderer('SimpleRenderer')
    sym.renderer.symbol.color = {'RGB': [255, 255, 255, 0]}
    sym.renderer.symbol.outlineColor = {'RGB': [110, 110, 110, 100]}
    sym.renderer.symbol.outlineWidth = .7
    polygons.symbology = sym
    layer = map_obj.addDataFromPath(str(points))
    layer.name = 'Grupos nominales y ruido' if clusters else 'Registros 2022–2024'
    sym = layer.symbology
    if clusters:
        sym.updateRenderer('UniqueValueRenderer')
        sym.renderer.fields = ['CLUSTER_ID']
        for group in sym.renderer.groups:
            for item in group.items:
                value = int(item.values[0][0])
                rgb = [110, 110, 110] if value == -1 else [round(v * 255) for v in
                      colorsys.hsv_to_rgb((value * .61803398875) % 1, .75, .8)]
                item.label = 'Ruido (-1)' if value == -1 else f'Grupo {value}'
                item.symbol.color = {'RGB': rgb + [80]}
                item.symbol.outlineColor = {'RGB': [255, 255, 255, 0]}
                item.symbol.size = 2.0 if value == -1 else 2.8
    else:
        sym.updateRenderer('SimpleRenderer')
        sym.renderer.symbol.color = {'RGB': [30, 100, 160, 65]}
        sym.renderer.symbol.outlineColor = {'RGB': [255, 255, 255, 0]}
        sym.renderer.symbol.size = 2.1
    layer.symbology = sym
    layout = project.createLayout(14, 10, 'INCH', name)
    frame = layout.createMapFrame(_rect(.3, .9, 10.5, 9.2), map_obj, 'Mapa local')
    frame.camera.setExtent(extent)
    frame.camera.scale *= 1.08
    frame.camera.heading = 0
    project.createTextElement(layout, arcpy.Point(.35, 9.6), 'POINT', title, 16,
                              'Arial', 'Regular')
    legend = layout.createMapSurroundElement(_rect(10.7, 1.1, 13.8, 9.1), 'LEGEND', frame,
                                             None, 'Leyenda')
    legend.title = 'Categorías nominales'
    legend.fittingStrategy = 'AdjustFontSize'
    legend.columnCount = 2 if clusters else 1
    note = ('N ↑ (norte de cuadrícula) | WKID 9377 | metros | '
            f'Escala 1:{round(frame.camera.scale):,}\n'
            '2022–2024 acumulados; no espacio-tiempo. Colores ≠ riesgo. '
            '350 m delimita vecindad, no radio del grupo.\n'
            'Jurisdicciones: contexto no validado; 1 auto-intersección reportada. '
            'No son límites certificados; sin estadísticas poligonales.')
    project.createTextElement(layout, arcpy.Point(.35, .5), 'POINT', note, 9, 'Arial', 'Regular')
    png = run / (name + '.png')
    fmt = arcpy.mp.CreateExportFormat('PNG', str(png))
    fmt.resolution = 180
    layout.export(fmt)
    # Solo copia local de trabajo: jamás project.save() sobre la plantilla instalada.
    project.saveACopy(str(run / (name + '.aprx')))
    return png
