"""
Functions for collecting tables from markdown
"""
from collections import namedtuple
import re

import numpy as np

Entry = namedtuple('Entry', ['test', 'values', 'factor'])

def collect_tables(filename):
    """
    Collect all tables in a markdown file
    """
    tables = []
    with open(filename, encoding='utf8') as f:
        lines = f.readlines()

    in_table = False
    for i in range(len(lines)):
        if '|' in lines[i]:
            if not in_table:
                table_start = i
            in_table = True
        elif in_table:
            tables.append(lines[table_start:i])
            in_table = False

    if in_table:
        tables.append(lines[table_start:])
        in_table = False

    return [unpack_table(tab) for tab in tables]

def unpack_table(lines):
    """
    Unpacks a list of strings describing lines of a markdown array into the lists describing the cells

    Parameters
    -----------
    lines : list of str
         A list of each of the lines in the table

    Results
    --------
    table_header : list of str
        A list containing each of the headers of the table
    table_body : list of list of str
        A 2d object containing the contents of the cells
    """
    table_header = [s.strip() for s in lines[0].split('|')]
    table_body = [[s.strip() for s in l.split('|')] for l in lines[2:]]
    return neaten_header(table_header), table_body

def build_compilation_entries(table_body):
    """
    From a list describing the cells of a table of compilation times, extract the entries
    """
    name = [n[0].strip() for n in table_body]
    time_str = [[t.strip() for t in l[1:]] for l in table_body]
    times = [[np.nan if t == '-' else float(t) for t in l] for l in time_str]
    return [Entry(n, v, 1) for n,v in zip(name, times)]


def build_execution_entries(table_body):
    """
    From a list describing the cells of a table of execution times, extract the entries
    """
    units = {'s':1, 'ms' : 1e-3, r'\textmu s' : 1e-6, 'ns' : 1e-9}
    name_with_units = [re.split(r'\(|\)', b[0]) for b in table_body]
    name = [n[0].strip() for n in name_with_units]
    time_factor = [units[n[1]] for n in name_with_units]
    time_str = [[t.split(r'$\pm$') for t in l[1:]] for l in table_body]
    times = [[np.nan if t[0] == '-' else float(t[0].strip()) for t in l] for l in time_str]
    errors = [[np.nan if len(t) == 1 else float(t[1].strip()) for t in l] for l in time_str]
    return [Entry(n, v, f) for n,v,f in zip(name, times, time_factor)]

header_neat_names = {
        'python' : 'Python',
        'numba' : 'Numba',
        'pythran_gnu' : 'Pythran (g++)',
        'pythran_intel' : 'Pythran (icx)',
        'pyccel_fortran_gnu' : 'Pyccel (Fortran, gfortran)',
        'pyccel_c_gnu' : 'Pyccel (C, gcc)',
        'pyccel_fortran_intel' : 'Pyccel (Fortran, ifort)',
        'pyccel_c_intel' : 'Pyccel (C, icc)',
        }

def neaten_header(header):
    return [header_neat_names.get(h,h) for h in header]

