from collections import namedtuple

import matplotlib.pyplot as plt
from matplotlib import rcParams as rc
import numpy as np


#methods = ('Python', 'Pythran', 'Numba', 'Pyccel (GCC)', 'Pyccel (Intel)')
Entry = namedtuple('Entry', ['test', 'values', 'factor'])


results = [
        Entry('Ackermann (ms)           ', [    (698, 13),  (5.32, 0.08),  (15.1, 0.0),  (1.77, 0.02),  (6.72, 0.07)], 10**-3),
        Entry('Bellman Ford (ns)        ', [(95200, 1700),      (506, 6),     (588, 2),      (283, 4),      (180, 1)], 10**-9),
        Entry('Dijkstra (ns)            ', [ (51500, 800),      (416, 8),     (417, 6),      (339, 5),      (411, 5)], 10**-9),

        Entry('FD - L Convection (ms)   ', [(3410, 10),  (1.54, 0.03),  (7.84, 0.07),  (1.82, 0.07),  (1.26, 0.03)], 10**-3),
        Entry('FD - NL Convection (ms)  ', [(4490, 10),  (1.73, 0.04),  (7.75, 0.06),  (1.83, 0.05),  (1.25, 0.01)], 10**-3),
        Entry('FD - Laplace (\textmu s) ', [ (57.6, 0.6),  (9.98, 0.14),  (7.5, 0.06),  (2.1, 0.05),  (2.26, 0.02)], 10**-6),
#        Entry('FD - Poisson (ms)        ', [(6630, 10),  (1.75, 0.04),  (8.77, 0.08),  (3.28, 0.04),  (1.93, 0.05)], 10**-3),

        Entry('Euler (\textmu s)        ', [(70500, 800),      (976, 9),    (1100, 10),        (116, 3),     (55.9, 0.7)], 10**-6),
        Entry('Midpoint Explicit (ms)   ', [(141.0, 2.0),  (2.17, 0.03),  (2.73, 0.04),  (0.194, 0.004),  (0.161, 0.003)], 10**-3),
        Entry('Midpoint Fixed (ms)      ', [(692.0, 3.0),   (13.9, 0.2),   (14.5, 0.1),  (0.781, 0.013),  (0.592, 0.006)], 10**-3),
        Entry('RK4 (ms)                 ', [(311.0, 3.0),  (2.38, 0.03),  (5.29, 0.02),  (0.819, 0.013),  (0.353, 0.004)], 10**-3),

        Entry('M-D (s)                  ', [(70.2, 1.5),  (0.117, 0.003),  (1.78, 0.0),  (0.119, 0.003),  (1.72, 0.0)], 1)
]

python_results       = np.array([v.values[0][0] * v.factor for v in results])
python_err           = np.array([v.values[0][1] * v.factor for v in results])

pythran_results      = np.array([v.values[1][0] * v.factor for v in results])
pythran_err          = np.array([v.values[1][1] * v.factor for v in results])

numba_results        = np.array([v.values[2][0] * v.factor for v in results])
numba_err            = np.array([v.values[2][1] * v.factor for v in results])

pyccel_gcc_results   = np.array([v.values[3][0] * v.factor for v in results])
pyccel_gcc_err       = np.array([v.values[3][1] * v.factor for v in results])

pyccel_intel_results = np.array([v.values[4][0] * v.factor for v in results])
pyccel_intel_err     = np.array([v.values[4][1] * v.factor for v in results])

pythran_results      = python_results / pythran_results
numba_results        = python_results / numba_results
pyccel_gcc_results   = python_results / pyccel_gcc_results
pyccel_intel_results = python_results / pyccel_intel_results
python_results       = python_results / python_results


labels = [v.test.split('(')[0].strip() for v in results]

x = np.arange(len(results))
width = 0.15

rc['font.size'] = 8
rc['font.family'] = 'serif'
rc['font.serif'] = 'Times New Roman'

#plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(7,2))
rects1 = ax.bar(x-2*width, python_results, width, label='Python')
rects2 = ax.bar(x-  width, numba_results, width, label='Numba')
rects3 = ax.bar(x        , pythran_results, width, label='Pythran')
rects4 = ax.bar(x+  width, pyccel_gcc_results, width, label='Pyccel (GCC)')
rects5 = ax.bar(x+2*width, pyccel_intel_results, width, label='Pyccel (Intel)')

ax.set_ylabel('Speedup')
ax.set_yscale('log')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=30, ha='right', rotation_mode="anchor")
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)
#ax.bar_label(rects3, padding=3)
#ax.bar_label(rects4, padding=3)
#ax.bar_label(rects5, padding=3)

fig.tight_layout()

plt.savefig('speedup.pdf')
plt.show()
