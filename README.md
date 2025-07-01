# Benchmarks

Several tests are available for the user to benchmark Pyccel against other common accelerators, notably [pythran](https://pythran.readthedocs.io/en/latest/) and [numba](https://numba.pydata.org/).
The same code is used for all tests, only the decorators change.

The dependencies can be installed using the command `python3 -m pip install .`

The code can be executed by running the script `benchmarks/run_benchmarks.py`.

In order to test pyccel and/or pythran, configuration files must be provided. An example configuration for pythran is found in [`benchmarks/config.pythranrc`](./benchmarks/config.pythranrc). This configuration is the default pythran configuration with the following additional flags:
- `-O3`
- `-march=native`
- `-mtune=native`
- `-mavx`
- `-ffast-math`
Pyccel configurations valid for your machine can be generated using the following command (which may be adapted for c generation or other compiler languages, see the [pyccel documentation](https://github.com/pyccel/pyccel/blob/master/tutorial/compiler.md)):
```
pyccel --language=fortran --export-compile-info pyccel_fortran.json
```
This configuration can then be modified to include additional flags or use different compilers. The tests shown below add the following additional flags (which match the flags added to pythran):
- `-O3`
- `-march=native`
- `-mtune=native`
- `-mavx`
- `-ffast-math`

Additional options can be used with this script to add further comparisons, change the output format, or change what is generated.

Run `python3 benchmarks/run_benchmarks.py --help` for more details.

The results below are presented for the current state of the development branch of pyccel, as well as the most recent version of pyccel available on pypi.

A requirements.txt file providing the necessary packages to reproduce the tests run can be found in the `version_specific_results` folder.
The environment can be reproduced using the following commands:
```
python3 -m venv my_virtual_environment
source my_virtual_environment/bin/activate
pip3 install -r requirements.txt
```
## Tests used

The tests used can be found in the [benchmarks/tests](./benchmarks/tests) directory.

### Ackermann

A basic implementation of the Ackermann function which is one of the simplest and oldest examples of a total computable function that is not primitive recursive.

### Bellman Ford

An algorithm for solving the shortest path problem. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)

### Djikstra

An algorithm for solving the shortest path problem. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)

### Euler

Solves an ordinary differential equation using Euler's method. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)

### Midpoint Explicit

Solves an ordinary differential equation using the explicit midpoint method. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)

### Midpoint Fixed

Solves an ordinary differential equation using the implicit midpoint method with a fixed number of iterations. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)

### RK4

Solves an ordinary differential equation using a fourth order Runge-Kutta method. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)

### FD - Linear Convection

Solves a 1D linear convection problem using Finite Differences methods. The code is adapted from examples written by [L. A. Barba](https://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/)

### FD - Non-Linear Convection

Solves a 1D non-linear convection problem using Finite Differences methods. The code is adapted from examples written by [L. A. Barba](https://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/)

### FD - Poisson

Solves a 2D Poisson problem using Finite Differences methods. The code is adapted from examples written by [L. A. Barba](https://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/)

### FD - Laplace

Solves a 2D Laplace problem using Finite Differences methods. The code is adapted from examples written by [L. A. Barba](https://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/)

### MD

Runs a molecular dynamics simulation. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)

### Splines

Evaluates a non-uniform spline saved as a class instance at a large number of test points. The code uses Algorithm A2.2 from the NURBS book (Piegl, Les, and Wayne Tiller. The NURBS book. Springer Science & Business Media, 2012.).
## Development branch results
### Performance Comparison (as of Tue Jul  1 16:18:07 UTC 2025)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.49                      | 2.16                      | 0.28                      | 1.37                      | 1.39                      | 1.37                      | 1.42                     
Bellman Ford              | -                         | 3.52                      | 3.91                      | 0.98                      | 1.70                      | 1.57                      | 1.62                      | 1.65                     
Dijkstra                  | -                         | 2.46                      | 2.85                      | 1.26                      | 1.79                      | 1.67                      | 1.72                      | 1.73                     
Euler                     | -                         | 2.76                      | 3.15                      | 3.51                      | 1.63                      | 1.53                      | 1.58                      | 1.57                     
Midpoint Explicit         | -                         | 3.15                      | 3.52                      | 3.75                      | 1.90                      | 1.80                      | 1.86                      | 1.82                     
Midpoint Fixed            | -                         | 3.59                      | 4.03                      | 3.94                      | 2.01                      | 1.90                      | 1.92                      | 1.89                     
RK4                       | -                         | 3.77                      | 4.23                      | 4.01                      | 2.31                      | 2.31                      | 2.22                      | 2.28                     
FD - L Convection         | -                         | 2.47                      | 2.76                      | 2.64                      | 1.61                      | 1.51                      | 1.56                      | 1.56                     
FD - NL Convection        | -                         | 3.54                      | 3.83                      | 2.64                      | 1.61                      | 1.54                      | 1.55                      | 1.54                     
FD - Poisson              | -                         | 3.69                      | 3.92                      | 5.89                      | 1.76                      | 1.79                      | 1.72                      | 1.99                     
FD - Laplace              | -                         | 7.50                      | 8.24                      | 7.62                      | 2.02                      | 1.99                      | 1.91                      | 2.06                     
M-D                       | -                         | 6.79                      | 6.81                      | 9.08                      | 2.50                      | 2.66                      | 2.42                      | 2.68                     
Splines                   | -                         | -                         | -                         | 0.62                      | 1.86                      | 1.83                      | 1.81                      | 1.90                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 433.00                    | 2.92                      | 3.06                      | 9.69                      | 1.33                      | 1.32                      | 4.05                      | 9.43                     
Bellman Ford (ms)         | 1720.00                   | 5.27                      | 3.48                      | 4.01                      | 3.72                      | 3.25                      | 6.45                      | 4.41                     
Dijkstra (ms)             | 4800.00                   | 21.20                     | 17.90                     | 21.20                     | 69.70                     | 19.50                     | 67.10                     | 24.40                    
Euler (ms)                | 3410.00                   | 25.70                     | 26.00                     | 36.40                     | 27.20                     | 11.70                     | 27.00                     | 15.40                    
Midpoint Explicit (ms)    | 6950.00                   | 51.50                     | 50.80                     | 148.00                    | 44.70                     | 20.00                     | 46.10                     | 16.40                    
Midpoint Fixed (ms)       | 34800.00                  | 266.00                    | 92.60                     | 322.00                    | 190.00                    | 73.50                     | 199.00                    | 55.50                    
RK4 (ms)                  | 17200.00                  | 158.00                    | 35.60                     | 134.00                    | 96.10                     | 32.40                     | 91.00                     | 29.10                    
FD - L Convection (ms)    | 2120.00                   | 1.59                      | 1.60                      | 5.63                      | 7.52                      | 1.50                      | 8.00                      | 1.37                     
FD - NL Convection (ms)   | 2640.00                   | 1.84                      | 1.69                      | 5.66                      | 6.69                      | 1.59                      | 8.06                      | 1.38                     
FD - Poisson (ms)         | 5660.00                   | 2.88                      | 5.44                      | 7.14                      | 14.50                     | 2.65                      | 24.00                     | 2.53                     
FD - Laplace (ms)         | 645.00                    | 62.80                     | 128.00                    | 278.00                    | 485.00                    | 56.60                     | 665.00                    | 60.00                    
M-D (ms)                  | 14500.00                  | 35.90                     | 64.60                     | 60.10                     | 117.00                    | 62.40                     | 61.10                     | 89.40                    
Splines (ms)              | 1730.00                   | -                         | -                         | 18.80                     | 14.40                     | 17.70                     | 15.20                     | 27.70                    

![Development compilation results](./version_specific_results/devel_performance_311_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_311_execution.svg)
## Python 3.8 results
## Python 3.9 results
## Python 3.10 results
## Python 3.11 results
## Python 3.12 results
