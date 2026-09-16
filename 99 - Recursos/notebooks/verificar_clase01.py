"""Verificación de solo lectura: estructura, contratos y evidencia real de Clase 01."""
from pathlib import Path
import ast
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
NAMES = ['Clase 01 - Practica 01 - Comparacion DBSCAN HDBSCAN sintetica.ipynb',
         'Clase 01 - Practica 02 - Clustering Bomberos con ArcGIS Pro.ipynb']


def require(condition, message):
    """No usar asserts desactivables para puertas de entrega."""
    if not condition:
        raise ValueError(message)


def structural():
    """Validar schema, sintaxis, docencia y parámetros sin geoprocesamiento."""
    import nbformat
    import clase01_arcgis as apoyo
    for number, name in enumerate(NAMES, 1):
        nb = nbformat.read(Path(__file__).parent / name, as_version=4)
        nbformat.validate(nb)
        first_code = next(c for c in nb.cells if c.cell_type == 'code')
        if number == 1:
            require(nb.cells[0].cell_type == 'code', 'Primera celda P01 debe configurar rutas.')
        else:
            require(nb.cells[0].cell_type == 'markdown' and 'Objetivos' in nb.cells[0].source, 'P02 debe empezar con objetivos.')
            require('PREPARED_JURIS' in first_code.source and len(first_code.source.splitlines()) <= 10, 'Configuración P02 no es corta/completa.')
            # Simular notebook fuera del vault: solo configurar rutas, sin acceder a datos ni escribir.
            from unittest.mock import patch
            config = {}
            with patch.object(Path, 'is_dir', return_value=False):
                exec(compile(first_code.source, '<configuracion P02>', 'exec'), config)
            require(config['ROOT'] == Path.cwd(), 'Configuración externa exige un vault implícito.')
        require(all(v in first_code.source for v in ['DATA_DIR', 'OUTPUT_DIR']), 'Configuración incompleta.')
        sources = []
        for i, cell in enumerate(nb.cells):
            if cell.cell_type != 'code':
                continue
            ast.parse(cell.source)
            require(any(line.lstrip().startswith('#') for line in cell.source.splitlines()), f'P{number} celda {i} sin comentarios.')
            require(len(cell.source.splitlines()) <= 35, f'P{number} celda {i} demasiado larga.')
            if i:
                require(nb.cells[i - 1].cell_type == 'markdown', f'P{number} celda {i} sin explicación previa.')
            sources.append(cell.source)
        text = '\n'.join(sources)
        if number == 1:
            require('clase01_arcgis' in text and 'new_run' in text, 'Dependencia/aislamiento no declarados.')
        else:
            require('clase01_arcgis' not in text and "ArcGISProject('CURRENT')" not in text, 'P02 depende de auxiliar/proyecto abierto.')
            require('RUN.mkdir' in text and 'fingerprint' in text, 'Aislamiento/integridad P02 incompletos.')
        require('overwriteOutput = True' not in text and 'RepairGeometry' not in text, 'Operación no autorizada.')
        if number == 1:
            require(not any(x in text for x in ['Bomberos', 'SpatialReference', '9377', 'export_map', 'DensityBasedClustering']), 'P01 no es exclusivamente sintética.')
            for parameter in ['n_samples=200', 'noise=0.9999', 'random_state=10', 'fit_transform', 'core_sample_indices_',
                              'eps=0.3', 'min_samples=5', 'min_cluster_size=5', 'cluster_selection_epsilon=0.0',
                              '[0.0, 0.2, 0.8, 0.9999]', '[200, 500, 1000]', 'native_profile', 'scatter_csv', 'bar_csv']:
                require(parameter in text, 'Falta contrato P01: ' + parameter)
            tree = ast.parse(text)
            assigned = {node.targets[0].id: ast.literal_eval(node.value) for node in tree.body
                        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name)
                        and node.targets[0].id in ['parametros_dbscan', 'parametros_hdbscan']}
            require(assigned['parametros_dbscan'] == [(0.10, 5), (0.20, 5), (0.30, 5), (0.30, 10), (0.45, 5), (0.45, 10)], 'Sensibilidades DBSCAN cambiadas.')
            require(assigned['parametros_hdbscan'] == [(5, 5, 0.), (10, 5, 0.), (15, 5, 0.), (5, 10, 0.), (10, 10, 0.), (10, 5, .15)], 'Sensibilidades HDBSCAN cambiadas.')
        else:
            for parameter in ['9377', 'CheckGeometry', 'CopyFeatures', "'DBSCAN', 100, '350 Meters'", "'HDBSCAN', 100)",
                              "'OPTICS', 100, '350 Meters'", 'MeanCenter', "'CLUSTER_ID <> -1'", "'NO_FID'",
                              "[['CLUSTER_ID','COUNT']]", 'AddJoin', 'IncidentesBomberosCentrosGruposDB',
                              'extension_comun', 'Histogram', 'arcpy.charts.Line', 'FieldStatisticsToTable', 'DIAGNOSTICO_CENTROS']:
                require(parameter in text, 'Falta contrato P02: ' + parameter)
            require(text.index("medir('FieldStatisticsToTable'") < text.index("medir('DBSCAN'"), 'EDA posterior al modelo.')
            require(text.index("medir('MeanCenter'") < text.index("medir('Identity'") < text.index("medir('Statistics_COUNT'") < text.index("medir('HDBSCAN'") < text.index("medir('OPTICS'"), 'Secuencia DOCX alterada.')
            calls = [n for n in ast.walk(ast.parse(text)) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'medir' and n.args and isinstance(n.args[0], ast.Constant) and n.args[0].value == 'OPTICS']
            require(len(calls) == 1 and len(calls[0].args) == 7 and not calls[0].keywords, 'OPTICS no omite sensibilidad.')
        print(f'P{number:02}: schema, sintaxis, comentarios, secuencia docente y parámetros correctos.')
    for filename in ['clase01_arcgis.py', 'ejecutar_clase01.py', 'verificar_clase01.py']:
        ast.parse((Path(__file__).parent / filename).read_text(encoding='utf-8'))
    # Los archivos nuevos no están cubiertos por git diff --check: revisar superficies propias.
    owned = [Path(__file__).parent / filename for filename in
             ['clase01_arcgis.py', 'ejecutar_clase01.py', 'verificar_clase01.py', NAMES[1]]]
    owned += [ROOT / '99 - Recursos' / name for name in
              ['Clase 01 - Fuentes y acuerdos.md', 'Clase 01 - Resultados de prácticas.md']]
    for path in owned:
        require(all(line == line.rstrip() for line in path.read_text(encoding='utf-8').splitlines()),
                'Whitespace final en superficie propia: ' + path.name)
    # Casos negativos: mismos directorios, descendientes, ancestros, GDB y plantilla.
    data = ROOT / 'Datos'
    for unsafe in [data, data / 'salidas', ROOT, ROOT / 'otra.gdb' / 'salidas']:
        try:
            apoyo.validate_paths(data, unsafe)
        except ValueError:
            pass
        else:
            raise ValueError('El aislamiento aceptó una ruta peligrosa.')
    try:
        apoyo.validate_paths(data, ROOT / 'plantilla' / 'salidas', [ROOT / 'plantilla'])
    except ValueError:
        pass
    else:
        raise ValueError('No se protege la plantilla.')
    apoyo.validate_paths(data, ROOT / '99 - Recursos/salidas_clase_01/practica_01')
    # Ruido no forma grupo; la co-pertenencia no depende del número de la etiqueta.
    require(apoyo.summary([-1, -1, 3, 3])['clusters'] == 1, 'Ruido contado como grupo.')
    require(apoyo.summary([-1, -1])['mayor_cluster'] == 0, 'Ruido contado como grupo mayor.')
    import pandas as pd
    db = pd.DataFrame({'SOURCE_ID': [1, 2, 3], 'CLUSTER_ID': [0, 0, -1]})
    hd = pd.DataFrame({'SOURCE_ID': [3, 2, 1], 'CLUSTER_ID': [-1, 7, 7]})
    require(apoyo.pair_comparison(db, hd)['jaccard_copertenencia'] == 1, 'Comparación no invariante a etiquetas.')
    print('Apoyo: casos negativos de aislamiento y semántica de grupos/co-pertenencia correctos.')


def policy_tests():
    """Contratos puros y finally simulado, sin escrituras ni kernels reales."""
    import clase01_arcgis as apoyo
    import ejecutar_clase01 as runner
    from unittest.mock import patch, Mock
    points, context = 'c:/prueba/trabajo.gdb/puntos', 'c:/prueba/trabajo.gdb/contexto'
    approved = apoyo.assess_geometry([(context, 'self intersections')], points, context)
    require('ADVERTENCIA' in apoyo.require_geometry(approved), 'Contexto no advertido.')
    require(approved['points_errors'] == 0 and approved['context_errors'] == 1, 'Clases mezcladas.')
    for rows, nonfinite in [([(points, 'null geometry')], 0),
                            ([('otra.gdb/contexto', 'self intersections')], 0),
                            ([('contexto', 'self intersections')], 0), ([], 1)]:
        try:
            apoyo.require_geometry(apoyo.assess_geometry(rows, points, context), nonfinite)
        except RuntimeError:
            pass
        else:
            raise ValueError('Geometría bloqueante aceptada.')
    require(runner.selected_notebooks(['--practica', '02']) == [(2, NAMES[1])], 'Selector ejecuta P01.')
    require(len(runner.selected_notebooks([])) == 2, 'Predeterminado no conserva dos prácticas.')
    with patch('sys.stderr'):
        try:
            runner.selected_notebooks(['--practica', '03'])
        except SystemExit as exc:
            require(exc.code == 2, 'Selector no cerrado.')
        else:
            raise ValueError('Selector acepta práctica desconocida.')
    hashes = {k: {'sha256': 'a' * 64, 'archivos': 1} for k in ['gdb', 'plantilla']}
    apoyo.require_hash_match(hashes, hashes)
    for before, after in [(None, hashes), ({}, {}), (hashes, {}),
                           (hashes, dict(hashes, gdb={'sha256': 'b' * 64, 'archivos': 1}))]:
        try:
            apoyo.require_hash_match(before, after)
        except RuntimeError:
            pass
        else:
            raise ValueError('Integridad ausente/diferente aceptada.')
    run = Path('ejecucion_prueba')
    # Las escrituras se interceptan: comprobar evidencia final sin crear archivos.
    for baseline, valid in [({'run_id': run.name, 'hashes': hashes}, True),
                            ({'run_id': run.name, 'hashes': {}}, False),
                            ({'run_id': 'otra', 'hashes': hashes}, False)]:
        with patch.object(apoyo, 'input_hashes', return_value=hashes), patch.object(Path, 'read_text', return_value=json.dumps(baseline)), patch.object(Path, 'write_text') as written:
            try:
                apoyo.finish_integrity(run, {})
            except RuntimeError:
                require(not valid, 'Comparación válida falló.')
            else:
                require(valid, 'Baseline inválida aceptada.')
            result = json.loads(written.call_args.args[0])
            require(result['coinciden'] == valid and result['run_id'] == run.name, 'Evidencia final incorrecta.')
    with patch.object(apoyo, 'input_hashes', return_value=hashes), patch.object(Path, 'read_text', side_effect=FileNotFoundError), patch.object(Path, 'write_text') as written:
        try:
            apoyo.finish_integrity(run, {})
        except FileNotFoundError:
            require(not json.loads(written.call_args.args[0])['coinciden'], 'Baseline ausente aprobada.')
        else:
            raise ValueError('Baseline ausente no bloqueó.')
    client = Mock()
    client.execute.side_effect = RuntimeError('kernel cerrado')
    with patch.object(apoyo, 'finish_integrity') as final:
        try:
            runner.execute_kernel(client, run, {'estables': True}, {})
        except RuntimeError:
            pass
        final.assert_called_once_with(run, {'estables': True})
    client.execute.side_effect = None
    with patch.object(apoyo, 'finish_integrity', side_effect=RuntimeError('hash diferente')):
        try:
            runner.execute_kernel(client, run, {}, {})
        except RuntimeError:
            pass
        else:
            raise ValueError('Kernel correcto ocultó fallo de integridad.')
    print('Política: puntos/desconocidos fatales, contexto advertido, selector P02 y finally/hash correctos.')


def execution():
    """Comprobar salidas actuales, cobertura visual e integridad original de solo lectura."""
    import nbformat
    from PIL import Image
    import clase01_arcgis as apoyo
    report = (ROOT / '99 - Recursos/Clase 01 - Resultados de prácticas.md').read_text(encoding='utf-8')
    for number, name in enumerate(NAMES, 1):
        nb = nbformat.read(Path(__file__).parent / name, as_version=4)
        require(nb.metadata.geoia.estado == 'ejecutado', f'P{number:02} no ejecutado completamente.')
        code = [c for c in nb.cells if c.cell_type == 'code']
        require(all(c.execution_count is not None for c in code), 'Hay celdas sin ejecutar.')
        require(not any(o.output_type == 'error' for c in code for o in c.outputs), 'Hay error de ejecución.')
        embedded = sum('image/png' in o.get('data', {}) for c in code for o in c.outputs)
        directory = ROOT / f'99 - Recursos/salidas_clase_01/practica_{number:02}'
        states = json.loads((directory / 'estado_ejecucion.json').read_text(encoding='utf-8'))
        require(states == dict(nb.metadata.geoia), 'Estado externo y notebook no coinciden.')
        from ejecutar_clase01 import evidence_path
        path = evidence_path(number, states, report)
        require(path.is_file(), 'Falta evidencia agregada enlazada.')
        evidence = json.loads(path.read_text(encoding='utf-8'))
        run = path.parent
        required = (['arcgis_original.png', 'arcgis_escalado.png', 'arcgis_sensibilidad_clusters.png',
                     'arcgis_sensibilidad_ruido.png', 'matplotlib_base.png', 'matplotlib_sensibilidad_dbscan.png',
                     'matplotlib_sensibilidad_hdbscan.png', 'matplotlib_control_ruido.png', 'matplotlib_control_muestra.png']
                    if number == 1 else ['arcgis_estaciones.png', 'arcgis_anios.png', 'arcgis_mapa_entrada.png',
                     'arcgis_mapa_dbscan.png', 'arcgis_mapa_hdbscan.png', 'arcgis_poblacion_dbscan.png',
                     'arcgis_poblacion_hdbscan.png', 'arcgis_hist_prob.png', 'arcgis_hist_outlier.png',
                     'arcgis_jurisdicciones.png', 'arcgis_mapa_optics.png', 'arcgis_poblacion_optics.png', 'arcgis_alcanzabilidad.png'])
        require(embedded >= len(required), 'Faltan PNG incorporados al notebook.')
        for png in required:
            require(png in evidence['png'] and (run / png).is_file(), 'Falta visual: ' + png)
            with Image.open(run / png) as image:
                require(image.format == 'PNG' and image.width >= 800 and image.height >= 500, 'PNG insuficiente.')
                image.verify()
            require((run / png).relative_to(ROOT).as_posix() in report, 'Visual no referenciado en informe.')
        if number == 1:
            require(evidence['sintetica_exclusiva'] and evidence['n_samples'] == 200, 'P01 cambió muestra/base.')
            require(len(evidence['sensibilidades']) == 12 and len(evidence['controlados']) == 14, 'Experimentos incompletos.')
        else:
            require(evidence['perfil_antes'] == evidence['perfil_despues'], 'Perfil cambió tras copia.')
            require(evidence['perfil_despues']['filas'] == 90443 and evidence['jurisdicciones'] == 17, 'Cobertura alterada.')
            geometry = evidence['geometria']
            require(geometry == {'puntos': 0, 'jurisdicciones_preparadas': 0}, 'Geometría nueva no válida para Identity.')
            require(evidence['autonomo'] and evidence['perfil_despues']['xy_no_finitas'] == 0, 'Autonomía/XY no válidas.')
            before = json.loads((run / 'integridad_antes.json').read_text(encoding='utf-8'))
            after = json.loads((run / 'integridad_despues.json').read_text(encoding='utf-8'))
            require(before['run_id'] == after['run_id'] == states['run_id'] == evidence['run_id'] == run.name, 'Identidades no coinciden.')
            require(after['coinciden'] is True, 'Integridad finally no aprobada.')
            apoyo.require_hash_match(before.get('hashes'), after.get('hashes'))
            require(before['hashes'] == {k:evidence['hashes_antes'][k] for k in ['gdb','plantilla']} and after['hashes'] == {k:evidence['hashes_despues'][k] for k in ['gdb','plantilla']}, 'Hashes notebook/runner diferentes.')
            protected_before = json.loads((run / 'protegidos_antes.json').read_text(encoding='utf-8'))
            protected_after = json.loads((run / 'protegidos_despues.json').read_text(encoding='utf-8'))
            require(protected_after['coinciden'] and protected_before['hashes'] == protected_after['hashes'], 'P01/preparada alteradas.')
            from ejecutar_clase01 import protected_hashes
            require(protected_hashes(apoyo) == protected_after['hashes'], 'P01/preparada cambiaron después del kernel.')
            require(evidence['hashes_antes'] == evidence['hashes_despues'], 'Integridad interna incompleta.')
            current = {'gdb': apoyo.fingerprint(ROOT / 'Datos/Datos Ejercicio5A.gdb'),
                       'plantilla': apoyo.fingerprint(apoyo.blank_template())}
            require(current == {k:evidence['hashes_despues'][k] for k in current}, 'Original cambió después de la ejecución.')
            require(all(evidence[k]['filas'] == 90443 for k in ['DBSCAN', 'HDBSCAN', 'OPTICS']), 'Modelos no cubren todos los registros.')
            require(all(c['filas_enlazadas'] == 90443 for c in evidence['comparacion'].values()), 'Comparación perdió registros.')
            require(evidence['centros']['centros'] == evidence['DBSCAN']['clusters'], 'Centros incompletos.')
            require(sum(evidence['conteos_centros'].values()) == 90443 - evidence['DBSCAN']['ruido'], 'COUNT incorrecto.')
            require(evidence['alcanzabilidad']['filas'] == 90443 and len(evidence['aprx']) == 4, 'Perfil/mapas incompletos.')
        print(f'P{number:02}: ejecución, {len(required)} PNG válidos e incorporados, evidencia y referencias correctas.')
    print('Validación final correcta; legibilidad visual requiere inspección humana separada.')


if __name__ == '__main__':
    try:
        structural()
        policy_tests()
        if '--estructura' not in sys.argv:
            execution()
    except Exception as exc:
        print('VALIDACIÓN FALLIDA:', type(exc).__name__, str(exc))
        sys.exit(1)
