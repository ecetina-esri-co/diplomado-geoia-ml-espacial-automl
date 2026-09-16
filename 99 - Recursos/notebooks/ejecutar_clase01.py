"""Kernels nuevos y selección cerrada; integridad P02 también después de un fallo."""
from pathlib import Path
import argparse
import json
import os
import re
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parents[2]
NOTEBOOKS = [
    'Clase 01 - Practica 01 - Comparacion DBSCAN HDBSCAN sintetica.ipynb',
    'Clase 01 - Practica 02 - Clustering Bomberos con ArcGIS Pro.ipynb',
]
REPORT = ROOT / '99 - Recursos/Clase 01 - Resultados de prácticas.md'


def selected_notebooks(argv=None):
    """Enumerar antes de filtrar evita convertir P02 en P01."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--practica', choices=['01', '02'])
    choice = parser.parse_args(argv).practica
    return [(n, name) for n, name in enumerate(NOTEBOOKS, 1)
            if choice is None or choice == f'{n:02}']


def evidence_path(number, state, report):
    """Enlace explícito, nunca el último glob; P01 heredada se vincula al informe."""
    directory = ROOT / f'99 - Recursos/salidas_clase_01/practica_{number:02}'
    if state.get('run_id'):
        run_id = state['run_id']
        if Path(run_id).name != run_id or not run_id.startswith('ejecucion_'):
            raise ValueError('Identidad de ejecución inválida.')
        return directory / run_id / 'evidencia.json'
    if number != 1:
        raise ValueError('P02 requiere identidad de ejecución explícita.')
    section = report.split('### P01', 1)[1].split('### P02', 1)[0]
    refs = re.findall(r'Evidencia agregada: `([^`]+)`', section)
    if len(refs) != 1:
        raise ValueError('P01 requiere una única referencia histórica explícita.')
    path = ROOT / refs[0]
    if path.resolve().parent.parent != directory.resolve() or path.name != 'evidencia.json':
        raise ValueError('Referencia P01 fuera de su salida.')
    import nbformat
    nb = nbformat.read(Path(__file__).parent / NOTEBOOKS[0], as_version=4)
    evidence = json.loads(path.read_text(encoding='utf-8'))
    if dict(nb.metadata.geoia) != state or state['estado'] != 'ejecutado' or evidence['estado'] != 'ejecutado':
        raise ValueError('Estado histórico P01 no coincide con evidencia/notebook.')
    if not all((path.parent / png).is_file() for png in evidence['png']):
        raise ValueError('Faltan visuales de la evidencia P01.')
    return path


def execute_kernel(client, run, identities, env):
    """finally no utiliza memoria del kernel; el error de integridad también es fatal."""
    import clase01_arcgis as apoyo
    try:
        client.execute(cwd=str(ROOT), env=env, cleanup_kc=True)
    finally:
        if run is not None:
            try:
                apoyo.finish_integrity(run, identities)
            finally:
                protected_path = run / 'protegidos_antes.json'
                if protected_path.is_file():
                    before = json.loads(protected_path.read_text(encoding='utf-8'))
                    after = protected_hashes(apoyo)
                    result = {'run_id': run.name, 'hashes': after, 'coinciden': before['hashes'] == after}
                    (run / 'protegidos_despues.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
                    if not result['coinciden']:
                        raise RuntimeError('Cambió la jurisdicción preparada o P01.')


def protected_hashes(apoyo):
    """Solo lectura: incluye P01 y la GDB preparada también cuando falla el kernel."""
    return {'preparada': apoyo.fingerprint(ROOT / '99 - Recursos/datos/p02_jurisdicciones_preparadas/jurisdicciones.gdb'),
            'P01': apoyo.fingerprint(Path(__file__).parent / NOTEBOOKS[0])}


def main():
    """Solo el intérprete Pro explícito; sin instalar ni descubrir kernels privados."""
    selected = selected_notebooks()
    if Path(sys.executable).name.lower() != 'python.exe' or 'arcgispro-py3' not in sys.executable.lower():
        raise RuntimeError('Ejecute exclusivamente con el intérprete ArcGIS Pro autorizado.')
    # Excluir paquetes del usuario: el intérprete Pro no basta para aislar DLL externas.
    import site
    sys.path[:] = [p for p in sys.path if p != site.getusersitepackages()]
    import nbformat
    from nbclient import NotebookClient
    from jupyter_client import KernelManager
    from jupyter_client.kernelspec import KernelSpec
    import clase01_arcgis as apoyo

    # Validar P01 existente antes de empezar P02, sin ejecutarla ni escribirla.
    if [n for n, _ in selected] == [2]:
        state = json.loads((ROOT / '99 - Recursos/salidas_clase_01/practica_01/estado_ejecucion.json').read_text(encoding='utf-8'))
        evidence_path(1, state, REPORT.read_text(encoding='utf-8'))
    outcomes = []
    for number, name in selected:
        output = ROOT / f'99 - Recursos/salidas_clase_01/practica_{number:02}'
        apoyo.validate_paths(ROOT / 'Datos', output)
        run = apoyo.new_run(ROOT / 'Datos', output)
        identities = ({'gdb': ROOT / 'Datos/Datos Ejercicio5A.gdb',
                       'plantilla': apoyo.blank_template()} if number == 2 else None)
        if number == 2:
            apoyo.start_integrity(run, identities)
            (run / 'protegidos_antes.json').write_text(
                json.dumps({'run_id': run.name, 'hashes': protected_hashes(apoyo)}, indent=2), encoding='utf-8')
        support = (run or output) / ('kernel_' + uuid.uuid4().hex[:8])
        support.mkdir(parents=True, exist_ok=False)
        env = os.environ.copy()
        env.pop('GEOIA_P02_RUN', None)
        env.pop('GEOIA_P01_RUN', None)
        env[f'GEOIA_P{number:02}_RUN'] = str(run)
        # Todos los perfiles y temporales nuevos quedan dentro de la salida seleccionada.
        for variable, folder in [('IPYTHONDIR', 'ipython'), ('JUPYTER_CONFIG_DIR', 'jupyter'),
                                 ('JUPYTER_DATA_DIR', 'jupyter_data'), ('JUPYTER_RUNTIME_DIR', 'runtime'),
                                 ('MPLCONFIGDIR', 'matplotlib'), ('TEMP', 'temp'), ('TMP', 'temp')]:
            target = support / folder
            target.mkdir(exist_ok=True)
            env[variable] = str(target)
        env.update(PYTHONNOUSERSITE='1', PYTHONDONTWRITEBYTECODE='1', JUPYTER_PLATFORM_DIRS='1', PYTHONUTF8='1',
                   PYDEVD_DISABLE_FILE_VALIDATION='1', OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1')
        path = Path(__file__).parent / name
        notebook = nbformat.read(path, as_version=4)
        for cell in notebook.cells:
            if cell.cell_type == 'code':
                cell.outputs = []
                cell.execution_count = None
        manager = KernelManager(kernel_name='')
        manager._kernel_spec = KernelSpec(argv=[sys.executable, '-X', 'utf8', '-B',
                    '-m', 'ipykernel_launcher', '-f', '{connection_file}',
                    '--HistoryManager.enabled=False'], display_name='ArcGIS Pro local', language='python')
        manager.connection_file = str(support / 'runtime' / 'kernel.json')
        client = NotebookClient(notebook, km=manager, timeout=1800, allow_errors=False,
                                resources={'metadata': {'path': str(ROOT)}})
        start = time.perf_counter()
        status, error = 'ejecutado', None
        try:
            execute_kernel(client, run if number == 2 else None, identities, env)
        except Exception as exc:
            status, error = 'fallido', type(exc).__name__
            failing = next((i for i, c in enumerate(notebook.cells)
                            if any(o.output_type == 'error' for o in c.get('outputs', []))), None)
            print(f'P{number:02}: {error}; celda {failing}.')
            for cell in notebook.cells:
                for result in cell.get('outputs', []):
                    if result.output_type == 'error':
                        message = result.get('evalue', '')
                        if ':\\' not in message and ':/Users/' not in message:
                            print(result.get('ename', 'Error') + ': ' + message[:1200])
                        # Diagnóstico acotado en consola: solo líneas sin rutas personales.
                        for line in result.get('traceback', []):
                            clean = re.sub(r'\x1b\[[0-9;]*m', '', line)
                            if not any(token in clean for token in ['Users', 'File ', 'Cell In', '---->']):
                                print(clean[-1800:])
                        result['traceback'] = []
                        result['evalue'] = 'Ejecución detenida; consultar estado y celda en el informe.'
        elapsed = time.perf_counter() - start
        executed = sum(c.cell_type == 'code' and c.execution_count is not None for c in notebook.cells)
        metadata = {'practica': f'{number:02}', 'estado': status, 'segundos_kernel': elapsed,
                    'celdas_ejecutadas': executed, 'kernel_nuevo': True,
                    'interprete': 'ArcGIS Pro arcgispro-py3; sys.executable; -X utf8 -B', 'error_tipo': error}
        metadata['run_id'] = run.name
        notebook.metadata['geoia'] = metadata
        nbformat.write(notebook, path)
        if number == 2:
            # Conservar cada intento, completo o fallido, antes de cualquier corrección posterior.
            nbformat.write(notebook, run / 'notebook_ejecutado.ipynb')
        (output / 'estado_ejecucion.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8')
        outcomes.append(metadata)
        print(f'P{number:02}: {status}; {executed} celdas; {elapsed:.2f} s.', flush=True)
        if status != 'ejecutado':
            break
    write_report(outcomes)
    return 0 if len(outcomes) == len(selected) and all(x['estado'] == 'ejecutado' for x in outcomes) else 1


def write_report(outcomes):
    """Sustituir únicamente secciones de ejecución seleccionadas; conservar notas manuales."""
    report = REPORT.read_text(encoding='utf-8')
    for status in outcomes:
        number = int(status['practica'])
        lines = [f'### P{number:02}', '', f'[[99 - Recursos/notebooks/{NOTEBOOKS[number - 1]}|Notebook P{number:02}]]', '',
                 f"Estado: **{status['estado']}**. Celdas: {status['celdas_ejecutadas']}; kernel nuevo: {status['segundos_kernel']:.2f} s.", '']
        if number == 2:
            lines += ['P02 autónoma: EDA → DBSCAN → selección sin ruido → MeanCenter → Identity NO_FID → Statistics COUNT → AddJoin → CopyFeatures → HDBSCAN → OPTICS con sensibilidad automática. Jurisdicciones preparadas y comprobadas, entrada de solo lectura; sin reparación dentro del notebook.', '',
                      'Historia preservada: [[99 - Recursos/salidas_clase_01/practica_02/Resultados_historicos_antes_autonomia.md|informe anterior]] y [[99 - Recursos/salidas_clase_01/practica_02/Notebook_historico_20260915_171532.ipynb|notebook anterior]]. Los resultados nuevos no se atribuyen a ejecuciones históricas.', '']
        path = evidence_path(number, status, report)
        if status['estado'] != 'ejecutado':
            lines += [f"Fallo actual: {status['error_tipo']}; ejecución `{status.get('run_id', 'sin evidencia')}`. No se presentan métricas anteriores como actuales.", '']
        else:
            evidence = json.loads(path.read_text(encoding='utf-8'))
            lines += [f'Evidencia agregada: `{path.relative_to(ROOT).as_posix()}`.', '',
                      'Entorno observado: `' + json.dumps(evidence['runtime'], ensure_ascii=False) + '`.', '',
                      f"Operaciones del notebook: {evidence['segundos']:.2f} s; no es ensayo docente de 120 minutos.", '']
            keys = (['parametros', 'perfil_antes', 'perfil_despues', 'geometria', 'DBSCAN', 'centros',
                     'conteos_centros', 'HDBSCAN', 'OPTICS', 'comparacion', 'tiempos_herramientas',
                     'histogramas_asignados', 'alcanzabilidad']
                    if number == 2 else ['base', 'tipos_dbscan', 'sensibilidades', 'controlados'])
            for key in keys:
                lines += [f'**{key}:** `' + json.dumps(evidence[key], ensure_ascii=False) + '`.', '']
            if number == 2:
                lines += [f"Integridad: `{path.parent.relative_to(ROOT).as_posix()}/integridad_antes.json` y `integridad_despues.json`; original/plantilla comprobados después del cierre del kernel. `protegidos_antes.json`/`protegidos_despues.json` incluyen jurisdicción preparada y P01; `integridad_notebook_antes.json`/`integridad_notebook_despues.json` comprueban las tres entradas desde el notebook.", '']
            lines += ['#### Visuales producidos', '']
            for png in evidence['png']:
                lines.append(f'- [[{(path.parent / png).relative_to(ROOT).as_posix()}|{png}]]')
            lines += ['']
        start = report.index(f'### P{number:02}')
        end = report.index('### P02', start + 1) if number == 1 else report.index('## Límites y comprobación pendiente', start)
        report = report[:start] + '\n'.join(lines) + '\n' + report[end:]
    REPORT.write_text(report, encoding='utf-8')


if __name__ == '__main__':
    sys.exit(main())
