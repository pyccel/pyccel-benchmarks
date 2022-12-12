import os
import sys

import matplotlib.pyplot as plt

from tables import collect_tables, build_compilation_entries, build_execution_entries
from plotting import plot_bar_chart

if __name__ == '__main__':
    filenames = sys.argv[1:]

    for f in filenames:
        compilation_table, execution_table = collect_tables(f)

        compilation_header, compilation_body = compilation_table
        execution_header, execution_body = execution_table

        n_accelerators = len(compilation_header) - 1

        compilation_keys = {compilation_header[1+i]: i for i in range(1, n_accelerators)}
        execution_keys = {execution_header[1+i]: i for i in range(n_accelerators)}

        dirname = os.path.dirname(f)
        basename = os.path.splitext(os.path.basename(f))[0]

        name_parts = basename.split('_')

        basename_without_version = '_'.join(name_parts[:-1])

        compilation_filename = os.path.join(dirname, basename_without_version + '_compilation.svg')
        execution_filename   = os.path.join(dirname, basename_without_version + '_execution.svg')

        fig, ax = plot_bar_chart(build_compilation_entries(compilation_body), compilation_keys)
        ax.set_ylabel('Compilation time [s]')
        ax.set_yscale('linear')
        ax.grid(True, which='major', axis='y', alpha=0.5, linewidth=0.50)
        ax.set_axisbelow(True)
        fig.tight_layout()

        plt.savefig(compilation_filename, dpi=150)

        fig, ax = plot_bar_chart(build_execution_entries(execution_body), execution_keys, 0)
        ax.set_ylabel('Speedup')
        ax.set_yscale('log')
        ylim = ax.get_ylim()
        ax.set_ylim(1,ylim[1])
        ax.grid(True, which='major', axis='y', alpha=0.5, linewidth=0.50)
        ax.grid(True, which='minor', axis='y', alpha=0.5, linewidth=0.25)
        ax.set_axisbelow(True)
        fig.tight_layout()

        plt.savefig(execution_filename, dpi=150)
