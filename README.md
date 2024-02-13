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
## Development branch results
### Performance Comparison (as of Tue Feb 13 07:48:09 UTC 2024)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.26                      | -                         | 0.32                      | 1.21                      | 1.16                      | -                         | -                        
Bellman Ford              | -                         | 3.35                      | -                         | 1.08                      | -                         | -                         | -                         | -                        
Dijkstra                  | -                         | 2.36                      | -                         | 1.56                      | 2.36                      | 2.48                      | -                         | -                        
Euler                     | -                         | 2.69                      | -                         | 2.00                      | 2.25                      | 2.48                      | -                         | -                        
Midpoint Explicit         | -                         | 3.07                      | -                         | 2.96                      | 2.52                      | 2.78                      | -                         | -                        
Midpoint Fixed            | -                         | 3.45                      | -                         | 3.16                      | 2.56                      | 2.79                      | -                         | -                        
RK4                       | -                         | 3.74                      | -                         | 3.70                      | 3.02                      | 3.19                      | -                         | -                        
FD - L Convection         | -                         | 2.31                      | -                         | 0.85                      | 2.22                      | 2.45                      | -                         | -                        
FD - NL Convection        | -                         | 3.29                      | -                         | 0.87                      | 2.24                      | 2.41                      | -                         | -                        
FD - Poisson              | -                         | 3.36                      | -                         | 1.32                      | 2.37                      | 2.56                      | -                         | -                        
FD - Laplace              | -                         | 6.54                      | -                         | 3.02                      | 2.68                      | 2.91                      | -                         | -                        
M-D                       | -                         | 6.23                      | -                         | 4.01                      | 3.05                      | 3.06                      | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 304.00                    | 2.95                      | -                         | 9.59                      | 1.54                      | 1.53                      | -                         | -                        
Bellman Ford (ms)         | 1800.00                   | 4.18                      | -                         | 4.09                      | -                         | -                         | -                         | -                        
Dijkstra (ms)             | 4990.00                   | 22.30                     | -                         | 18.70                     | 17.90                     | 30.50                     | -                         | -                        
Euler (ms)                | 3890.00                   | 28.00                     | -                         | 39.00                     | 15.30                     | 142.00                    | -                         | -                        
Midpoint Explicit (ms)    | 8050.00                   | 58.80                     | -                         | 82.70                     | 23.10                     | 280.00                    | -                         | -                        
Midpoint Fixed (ms)       | 40200.00                  | 254.00                    | -                         | 395.00                    | 74.10                     | 1420.00                   | -                         | -                        
RK4 (ms)                  | 20300.00                  | 161.00                    | -                         | 142.00                    | 34.90                     | 485.00                    | -                         | -                        
FD - L Convection (ms)    | 2320.00                   | 1.63                      | -                         | 2.69                      | 1.46                      | 1.62                      | -                         | -                        
FD - NL Convection (ms)   | 2840.00                   | 1.97                      | -                         | 2.82                      | 1.69                      | 2.22                      | -                         | -                        
FD - Poisson (ms)         | 6320.00                   | 2.90                      | -                         | 7.09                      | 2.76                      | 3.82                      | -                         | -                        
FD - Laplace (ms)         | 578.00                    | 67.20                     | -                         | 244.00                    | 62.10                     | 308.00                    | -                         | -                        
M-D (ms)                  | 14700.00                  | 15.20                     | -                         | 58.90                     | 53.60                     | 59.40                     | -                         | -                        

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.8 results
## Python 3.9 results
## Python 3.10 results
## Python 3.11 results
## Python 3.12 results
