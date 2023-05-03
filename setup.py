# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from setuptools import setup

if __name__ == '__main__':
    setup(
        name='pyccel-benchmarks',
        version='0.0.0',
        install_requires=[
            'pyccel',
            'pythran',
            'numba',
            'pyperf',
            'numpy',
            'matplotlib',
        ],
    )
