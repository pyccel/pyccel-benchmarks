"""
Functions for plotting results
"""

import matplotlib.pyplot as plt
from matplotlib import rcParams as rc
import numpy as np

rc['font.size'] = 8
rc['font.family'] = 'serif'
rc['font.serif'] = 'Times New Roman'

def plot_bar_chart(results, result_keys, normalise_key = -1):

    unpacked_results = [np.array([v.values[i] * v.factor for v in results]) for i in result_keys.values()]
    if normalise_key != -1:
        python_results = np.array([v.values[normalise_key] * v.factor for v in results])
        unpacked_results = [python_results / r for r in unpacked_results]

    labels = [v.test for v in results]

    x = np.arange(len(results))
    width = 0.75/len(result_keys)

    fig, ax = plt.subplots(figsize=(7,2))
    start = x-width/2
    for i, (lab, c) in enumerate(result_keys.items()):
        if lab == 'Python':
            continue
        ax.bar(start + i*width, unpacked_results[i], width, label=lab, color='C'+str(c))

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=30, ha='right', rotation_mode="anchor")
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    return fig, ax
