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
### Performance Comparison (as of Tue Feb 13 08:39:26 UTC 2024)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.57                      | 2.37                      | 0.33                      | 1.32                      | 1.26                      | -                         | 1.36                     
Bellman Ford              | -                         | 3.68                      | 4.14                      | 1.14                      | -                         | -                         | -                         | -                        
Dijkstra                  | -                         | 2.58                      | 3.05                      | 1.68                      | 2.53                      | 2.68                      | -                         | 3.64                     
Euler                     | -                         | 2.93                      | 3.36                      | 2.09                      | 2.38                      | 2.60                      | -                         | 3.45                     
Midpoint Explicit         | -                         | 3.30                      | 3.95                      | 3.17                      | 2.69                      | 2.91                      | -                         | 3.70                     
Midpoint Fixed            | -                         | 3.77                      | 4.62                      | 3.35                      | 2.78                      | 2.98                      | -                         | 3.72                     
RK4                       | -                         | 3.95                      | 4.57                      | 3.81                      | 3.19                      | 3.27                      | -                         | 4.09                     
FD - L Convection         | -                         | 2.50                      | 2.95                      | 0.90                      | 2.33                      | 2.53                      | -                         | 3.31                     
FD - NL Convection        | -                         | 3.43                      | 3.89                      | 0.92                      | 2.30                      | 2.53                      | -                         | 3.31                     
FD - Poisson              | -                         | 3.53                      | 4.08                      | 1.36                      | 2.47                      | 2.62                      | -                         | 3.37                     
FD - Laplace              | -                         | 6.73                      | 9.04                      | 3.09                      | 2.85                      | 3.06                      | -                         | 3.92                     
M-D                       | -                         | 6.37                      | 7.36                      | 4.00                      | 3.11                      | 3.12                      | -                         | 4.31                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 307.00                    | 2.95                      | 3.46                      | 9.74                      | 1.50                      | 1.50                      | -                         | 3.93                     
Bellman Ford (ms)         | 1800.00                   | 4.16                      | 3.17                      | 3.87                      | -                         | -                         | -                         | -                        
Dijkstra (ms)             | 5030.00                   | 23.60                     | 17.30                     | 21.20                     | 19.10                     | 31.40                     | -                         | 23.40                    
Euler (ms)                | 3890.00                   | 28.80                     | 28.60                     | 39.70                     | 15.00                     | 145.00                    | -                         | 128.00                   
Midpoint Explicit (ms)    | 7930.00                   | 60.50                     | 57.40                     | 82.30                     | 22.90                     | 280.00                    | -                         | 251.00                   
Midpoint Fixed (ms)       | 40400.00                  | 255.00                    | 63.20                     | 372.00                    | 75.00                     | 1380.00                   | -                         | 1260.00                  
RK4 (ms)                  | 19800.00                  | 163.00                    | 38.50                     | 149.00                    | 34.70                     | 486.00                    | -                         | 412.00                   
FD - L Convection (ms)    | 2320.00                   | 1.67                      | 1.57                      | 2.66                      | 1.45                      | 1.62                      | -                         | 3.69                     
FD - NL Convection (ms)   | 2840.00                   | 1.91                      | 1.80                      | 2.82                      | 1.66                      | 2.20                      | -                         | 3.74                     
FD - Poisson (ms)         | 6330.00                   | 2.95                      | 2.65                      | 7.16                      | 2.76                      | 3.78                      | -                         | 8.97                     
FD - Laplace (ms)         | 577.00                    | 64.30                     | 151.00                    | 245.00                    | 58.20                     | 280.00                    | -                         | 305.00                   
M-D (ms)                  | 14900.00                  | 15.20                     | 52.10                     | 59.10                     | 53.90                     | 59.40                     | -                         | 60.10                    

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.8 results
## Python 3.9 results
## Python 3.10 results
## Python 3.11 results
## Python 3.12 results
