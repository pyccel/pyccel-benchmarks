from collections import namedtuple

import matplotlib.pyplot as plt
from matplotlib import rcParams as rc
import numpy as np


#methods = ('Numba', 'Pythran', 'Pyccel (GCC)')
Entry = namedtuple('Entry', ['test', 'values', 'factor'])


results = [
        Entry('Ackermann (s)           ', [3.762610443, 10.01, 5.53], 1),
        Entry('Bellman Ford (s)        ', [4.250476972, 11.87, 5.65], 1),
        Entry('Dijkstra (s)            ', [4.490422568, 14.31, 5.96], 1),

        Entry('FD - L Convection (s)   ', [3.624814303, 59.07, 8.91], 1),
        Entry('FD - NL Convection (s)  ', [3.630342166, 59.08, 9.04], 1),
        Entry('FD - Laplace (s)        ', [5.263653243, 59.12, 9.12], 1),
#        Entry('FD - Poisson (s)        ', [4.193497739, 58.97, 9.03], 1),

        Entry('Euler (s)               ', [1.337058864, 36.87, 8.37], 1),
        Entry('Midpoint Explicit (s)   ', [1.938374651, 36.96, 8.37], 1),
        Entry('Midpoint Fixed (s)      ', [2.196985954, 36.80, 8.47], 1),
        Entry('RK4 (s)                 ', [2.321180113, 36.77, 8.48], 1),

        Entry('M-D (s)                  ', [8.186452462, 22.02, 7.51], 1)
]

numba_results        = np.array([v.values[0] * v.factor for v in results])
pythran_results      = np.array([v.values[1] * v.factor for v in results])
pyccel_gcc_results   = np.array([v.values[2] * v.factor for v in results])

labels = [v.test.split('(')[0].strip() for v in results]

x = np.arange(len(results))
width = 0.2

rc['font.size'] = 8
rc['font.family'] = 'serif'
rc['font.serif'] = 'Times New Roman'

#plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(7,2))
rects2 = ax.bar(x-  width, numba_results, width, label='Numba', color='tab:orange')
rects3 = ax.bar(x        , pythran_results, width, label='Pythran', color='tab:green')
rects4 = ax.bar(x+  width, pyccel_gcc_results, width, label='Pyccel (GCC)', color='tab:red')

ax.set_ylabel('Compilation time [s]')
ax.set_yscale('linear')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=30, ha='right', rotation_mode="anchor")
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)
#ax.bar_label(rects3, padding=3)
#ax.bar_label(rects4, padding=3)
#ax.bar_label(rects5, padding=3)

fig.tight_layout()

plt.savefig('compilation_timings.pdf')
plt.show()
