#! /usr/bin/env python3
# coding: utf-8
#------------------------------------------------------------------------------------------#
# This file is part of Pyccel which is released under MIT License. See the LICENSE file or #
# go to https://github.com/pyccel/pyccel/blob/master/LICENSE for full license details.     #
#------------------------------------------------------------------------------------------#
""" Module providing the code for executing the benchmark suite
"""
from argparse import ArgumentParser
from collections import namedtuple
import json
import os
import re
import resource
import shutil
import subprocess
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

TestInfo = namedtuple('TestInfo', 'name basename imports setup call')

parser = ArgumentParser(description='Run the benchmarks to compare pyccel with pure python, pythran and numba')

parser.add_argument('--pyperf', action='store_true', \
                        help='Runs timing tests with pyperf (more accurate but much slower).')
parser.add_argument('--no_compilation', action='store_false', dest='compilation', \
                        help="Don't time the compilation step")
parser.add_argument('--no_execution', action='store_false', dest='execution', \
                        help="Don't time the execution step")
parser.add_argument('--pypy', action='store_true', help='Run test cases with pypy')
parser.add_argument('--no_numba', action='store_true', help="Don't run numba tests")
parser.add_argument('--pythran-config-files', type=str, nargs='*', help='Provide configuration files for pythran', default = [])
parser.add_argument('--pyccel-config-files', type=str, nargs='*', help='Provide configuration files for pyccel', default = [])
parser.add_argument('--output', choices=('latex', 'markdown'), \
                        help='Format of the output table (default=markdown)',default='markdown')
parser.add_argument('--verbose', action='store_true', help='Enables verbose mode.')

args = parser.parse_args()

verbose = args.verbose
output_format = args.output

pyperf = args.pyperf
time_compilation = args.compilation
time_execution = args.execution
pyccel_configs = [os.path.abspath(f) for f in args.pyccel_config_files]
pythran_configs = [os.path.abspath(f) for f in args.pythran_config_files]


test_cases = ['python']
test_case_names = ['python']
if args.pypy:
    test_cases.append('pypy')
    test_case_names.append('pypy')
for i,f in enumerate(pythran_configs):
    test_cases.append(f'pythran_{i}')
    test_case_names.append(os.path.splitext(os.path.basename(f))[0])
if not args.no_numba:
    test_cases.append('numba')
    test_case_names.append('numba')
n_configs = 0
for i,f in enumerate(pyccel_configs):
    name = os.path.splitext(os.path.basename(f))[0]
    with open(f) as config:
        languages = json.load(config).keys()
    for l in languages:
        test_cases.append(f'pyccel_{i}_{l}')
        test_case_names.append(f'{name}_{l}')
        n_configs += 1

tests = [
    TestInfo('Ackermann',
        'ackermann_mod.py',
        ['ackermann'],
        'import sys; sys.setrecursionlimit(3000);',
        'a = ackermann(3,8)'),
    TestInfo('Bellman Ford',
        'bellman_ford_mod.py',
        ['bellman_ford_test'],
        '',
        'err = bellman_ford_test()'),
    TestInfo('Dijkstra',
        'dijkstra.py',
        ['dijkstra_distance_test'],
        '',
        'd = dijkstra_distance_test()'),
    TestInfo('Euler',
        'euler_mod.py',
        ['euler_humps_test'],
        '',
        'err = euler_humps_test(0., 2000., 1000000)'),
    TestInfo('Midpoint Explicit',
        'midpoint_explicit_mod.py',
        ['midpoint_explicit_humps_test'],
        '',
        'err = midpoint_explicit_humps_test(0., 2000., 1000000)'),
    TestInfo('Midpoint Fixed',
        'midpoint_fixed_mod.py',
        ['midpoint_fixed_humps_test'],
        '',
        'err = midpoint_fixed_humps_test(0., 2000., 1000000)'),
    TestInfo('RK4',
        'rk4_mod.py',
        ['rk4_humps_test'],
        '',
        'err = rk4_humps_test(0., 2000., 1000000)'),
    TestInfo('FD - L Convection',
        'linearconv_1d_mod.py',
        ['linearconv_1d'],
        '',
        'x, u = linearconv_1d(2001, 0.0003, 3000)'),
    TestInfo('FD - NL Convection',
        'nonlinearconv_1d_mod.py',
        ['nonlinearconv_1d'],
        '',
        'x, u = nonlinearconv_1d(2001, 0.00035, 3000)'),
    TestInfo('FD - Poisson',
        'poisson_2d_mod.py',
        ['poisson_2d'],
        '',
        'x, y, phi = poisson_2d(150, 150, 200)'),
    TestInfo('FD - Laplace',
        'laplace_2d_mod.py',
        ['laplace_2d'],
        '',
        'x, y, phi, niter = laplace_2d(150, 150, 5e-5, 5000)'),
    TestInfo('M-D',
        'md_mod.py',
        ['md'],
        '',
        'p, k = md(3, 100, 200, 0.1)'),
    TestInfo('Splines',
        'splines.py',
        ['Spline'],
        'import numpy as np; s = Spline(5, knots = np.linspace(0,1, 1000), coeffs = np.ones(1000)); x = np.random.rand(100000); y = np.empty(100000);',
        's.eval(x, y)'),
]

if verbose:
    log_file = sys.stdout
else:
    log_file = open("bench.log",'w')

timeit_cmd = ['pyperf', 'timeit', '--copy-env', '--fast'] if pyperf else ['timeit']

cell_splitter = {'latex'    : ' & ',
                 'markdown' : ' | '}
row_splitter  = {'latex'    : '\\\\\n\\hline\n',
                 'markdown' : '\n'}

test_cases_row = cell_splitter[output_format].join('{0: <25}'.format(s) for s in ['Algorithm']+test_case_names)
comp_result_table = [test_cases_row]
exec_result_table = [test_cases_row]

out_header = {'latex'    : lambda s : r'\textbf{'+s+'}',
              'markdown' : lambda s : '## '+s
             }

if output_format == 'markdown':
    header_row = cell_splitter[output_format].join('-------------------------' for _ in range(len(test_cases)+1))
    comp_result_table.append(header_row)
    exec_result_table.append(header_row)

possible_units = ['sec','ms','us','ns']
latex_units = ['s','ms','\\textmu s','ns']

start_dir = os.getcwd()

code_folder = os.path.join(os.path.dirname(__file__), 'tests')

def run_process(cmd: "List[str]", time_compilation: "bool"=False, env = None):
    if not time_compilation:
        with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                universal_newlines=True, env=env) as p:
            out, err = p.communicate()
            returncode = p.returncode
        return returncode, out, err, 0.0

    usage_start = resource.getrusage(resource.RUSAGE_CHILDREN)
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            universal_newlines=True, env=env) as p:
        out, err = p.communicate()
        returncode = p.returncode
    usage_end = resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu_time = sum([
        usage_end.ru_utime - usage_start.ru_utime,
        usage_end.ru_stime - usage_start.ru_stime
    ])
    return returncode, out, err, cpu_time


for t in tests:
    print("===========================================", file=log_file, flush=True)
    print("   ",t.name, file=log_file, flush=True)
    print("===========================================", file=log_file, flush=True)
    basename = t.basename

    test_file = os.path.join(code_folder,basename)
    testname  = os.path.splitext(basename)[0]

    numba_basename = 'numba_'+basename
    numba_testname = 'numba_'+testname
    numba_test_file = os.path.join(os.path.dirname(test_file), numba_basename)

    new_folder = os.path.join('tmp',t.imports[0])

    os.makedirs(new_folder, exist_ok=True)
    shutil.copyfile(test_file, os.path.join(new_folder, basename))
    shutil.copyfile(numba_test_file, os.path.join(new_folder, numba_basename))
    os.chdir(new_folder)

    import_funcs = ', '.join(t.imports)
    exec_cmd  = t.call

    comp_times = [t.name]

    run_times = []
    run_units = []

    for case in test_cases:
        setup_cmd = 'from {testname} import {funcs};'.format(
                testname = numba_testname if case == 'numba' else testname,
                funcs = import_funcs)
        setup_cmd += t.setup.replace('\n','')
        print("-------------------", file=log_file, flush=True)
        print("   ",case, file=log_file, flush=True)
        print("-------------------", file=log_file, flush=True)
        env = os.environ.copy()
        create_shared_lib = case.startswith('pyccel') or case.startswith('pythran')
        if create_shared_lib:
            tag, idx_str = case.split('_', 1)
            if tag == 'pyccel':
                idx_str, language = idx_str.split('_')
                idx = int(idx_str)
                my_file = pyccel_configs[idx]
                cmd = ['pyccel', f'--compiler-config={my_file}', f'--language={language}', '--verbose', basename]
            elif tag == 'pythran':
                idx = int(idx_str)
                my_file = pythran_configs[idx]
                cmd = ['pythran', '-v', basename]
                env['PYTHRANRC'] = my_file

            if verbose:
                print(cmd, file=log_file, flush=True)

            returncode, out, err, cpu_time = run_process(cmd, time_compilation, env=env)

            if returncode != 0:
                print("Compilation Error!", file=log_file, flush=True)
                print(out, file=log_file, flush=True)
                print(err, file=log_file, flush=True)
                comp_times.append('-')
                run_times.append(None)
                run_units.append(None)
                continue
            elif verbose:
                print(out, file=log_file, flush=True)
                print(err, file=log_file, flush=True)

            if time_compilation:
                print("Compilation CPU time : ", cpu_time, file=log_file)
                comp_times.append('{:.2f}'.format(float(cpu_time)))

        elif time_compilation and case == "numba":
            cmd = ['pypy'] if case=='pypy' else ['python3']
            run_str = "{setup}import resource; t0 = resource.getrusage(resource.RUSAGE_SELF); {run}; t1 = resource.getrusage(resource.RUSAGE_SELF); {run}; t2 = resource.getrusage(resource.RUSAGE_SELF); print(2*t1.ru_utime-t0.ru_utime-t2.ru_utime + 2*t1.ru_stime-t0.ru_stime-t2.ru_stime)".format(
                    setup=setup_cmd,
                    run=exec_cmd)
            cmd += ['-c', run_str]

            if verbose:
                print(cmd, file=log_file, flush=True)

            # don't use `run_process` time_compilation here
            # because the command executed uses the `time` module
            returncode, out, err, _ = run_process(cmd)

            if returncode != 0:
                print("Execution Error!", file=log_file, flush=True)
                comp_times.append('-')
                run_times.append(None)
                run_units.append(None)
                print(err, file=log_file, flush=True)
            else:
                print("Compilation Process time : ",out, file=log_file, flush=True)
                comp_times.append('{:.2f}'.format(float(out)))
        else:
            comp_times.append('-')

        if time_execution:
            cmd = ['pypy'] if case=='pypy' else ['python3']
            cmd += ['-m'] + timeit_cmd + ['-s', setup_cmd, exec_cmd]

            if verbose:
                print(cmd, file=log_file, flush=True)

            returncode, out, err, _ = run_process(cmd)

            if returncode != 0:
                print("Execution Error!", file=log_file, flush=True)
                run_times.append(None)
                run_units.append(None)
                print(err, file=log_file, flush=True)
            else:
                if verbose:
                    print(out, file=log_file, flush=True)
                if pyperf:
                    regexp = re.compile(r'([0-9.]+) (\w\w\w?) \+- ([0-9.]+) (\w\w\w?)')
                    r = regexp.search(out)
                    assert r.group(2) == r.group(4)
                    mean = float(r.group(1))
                    stddev = float(r.group(3))
                    units = r.group(2)

                    bench_str = '{mean:.2f} $\pm$ {stddev:.2f}'.format(
                            mean=mean,
                            stddev=stddev)
                    run_times.append((mean,stddev))
                else:
                    regexp = re.compile(r'([0-9]+) loops?, best of ([0-9]+): ([0-9.]+) (\w*)')
                    r = regexp.search(out)
                    best = float(r.group(3))
                    units = r.group(4)
                    if units!= 'sec':
                        units = units[:-2]
                    bench_str = best
                    run_times.append(best)

                run_units.append(possible_units.index(units))

        if create_shared_lib:
            subprocess.run([shutil.which('pyccel-clean'), '-s'])

    if time_compilation:
        row = cell_splitter[output_format].join('{0: <25}'.format(s) for s in comp_times)
        if verbose:
            print(row, file=log_file, flush=True)
        comp_result_table.append(row)

    if time_execution:
        used_units = [u for u in run_units if u is not None]
        unit_index = round(sum(used_units)/len(used_units))
        units = latex_units[unit_index]
        row = [t.name + ' ('+units+')']

        mult_fact = [1000**(unit_index-u) if u is not None else None for u in run_units]

        if pyperf:
            for time,f in zip(run_times,mult_fact):
                if time is None:
                    row.append('-')
                else:
                    mean,stddev = time
                    row.append('{mean:.2f} $\pm$ {stddev:.2f}'.format(
                                mean=mean*f,
                                stddev=stddev*f))
        else:
            for time,f in zip(run_times,mult_fact):
                if time is None:
                    row.append('-')
                else:
                    row.append('{:.2f}'.format(time*f))

        row = cell_splitter[output_format].join('{0: <25}'.format(s) for s in row)
        if verbose:
            print(row, file=log_file, flush=True)
        exec_result_table.append(row)
    os.chdir(start_dir)

log_file.close()

result_file = open("bench.out",'w')
if time_compilation:
    print(out_header[output_format]("Compilation time"), file=result_file, flush=True)
    print(row_splitter[output_format].join(comp_result_table), file=result_file, flush=True)

print(file=result_file, flush=True)

if time_execution:
    print(out_header[output_format]("Execution time"), file=result_file, flush=True)
    print(row_splitter[output_format].join(exec_result_table), file=result_file, flush=True)
result_file.close()
