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
### Performance Comparison (as of Tue Feb 13 09:17:56 UTC 2024)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.37                      | 2.31                      | 0.33                      | 1.25                      | 1.21                      | -                         | 1.33                     
Bellman Ford              | -                         | 3.47                      | 3.91                      | 1.09                      | -                         | -                         | -                         | -                        
Dijkstra                  | -                         | 2.42                      | 2.88                      | 1.60                      | 2.48                      | 2.61                      | -                         | 3.43                     
Euler                     | -                         | 2.85                      | 3.34                      | 2.07                      | 2.34                      | 2.58                      | -                         | 3.38                     
Midpoint Explicit         | -                         | 3.19                      | 3.79                      | 3.09                      | 2.65                      | 2.87                      | -                         | 3.66                     
Midpoint Fixed            | -                         | 3.62                      | 4.32                      | 3.21                      | 2.65                      | 2.85                      | -                         | 3.65                     
RK4                       | -                         | 3.82                      | 4.47                      | 3.74                      | 3.08                      | 3.25                      | -                         | 4.07                     
FD - L Convection         | -                         | 2.47                      | 2.89                      | 0.88                      | 2.33                      | 2.53                      | -                         | 3.35                     
FD - NL Convection        | -                         | 3.40                      | 3.81                      | 0.88                      | 2.31                      | 2.53                      | -                         | 3.31                     
FD - Poisson              | -                         | 3.50                      | 3.98                      | 1.34                      | 2.42                      | 2.62                      | -                         | 3.38                     
FD - Laplace              | -                         | 6.66                      | 8.83                      | 3.04                      | 2.76                      | 2.97                      | -                         | 3.85                     
M-D                       | -                         | 6.45                      | 7.51                      | 4.03                      | 3.13                      | 3.13                      | -                         | 4.27                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 313.00                    | 2.95                      | 3.47                      | 9.62                      | 1.55                      | 1.54                      | -                         | 3.93                     
Bellman Ford (ms)         | 1780.00                   | 4.18                      | 3.19                      | 3.88                      | -                         | -                         | -                         | -                        
Dijkstra (ms)             | 5070.00                   | 23.40                     | 16.90                     | 19.40                     | 18.40                     | 30.90                     | -                         | 22.20                    
Euler (ms)                | 3940.00                   | 28.20                     | 28.20                     | 39.70                     | 15.60                     | 141.00                    | -                         | 127.00                   
Midpoint Explicit (ms)    | 8010.00                   | 59.80                     | 56.30                     | 77.70                     | 22.30                     | 278.00                    | -                         | 250.00                   
Midpoint Fixed (ms)       | 40500.00                  | 329.00                    | 62.60                     | 374.00                    | 75.20                     | 1390.00                   | -                         | 1240.00                  
RK4 (ms)                  | 20000.00                  | 162.00                    | 38.00                     | 200.00                    | 32.50                     | 484.00                    | -                         | 405.00                   
FD - L Convection (ms)    | 2320.00                   | 1.69                      | 1.60                      | 2.67                      | 1.45                      | 1.62                      | -                         | 3.70                     
FD - NL Convection (ms)   | 2830.00                   | 1.83                      | 1.80                      | 2.82                      | 1.69                      | 2.19                      | -                         | 3.74                     
FD - Poisson (ms)         | 6250.00                   | 2.96                      | 2.62                      | 7.11                      | 2.78                      | 3.83                      | -                         | 8.92                     
FD - Laplace (ms)         | 589.00                    | 63.60                     | 151.00                    | 246.00                    | 58.20                     | 256.00                    | -                         | 304.00                   
M-D (ms)                  | 15000.00                  | 15.20                     | 51.80                     | 59.10                     | 52.80                     | 59.50                     | -                         | 60.10                    

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.8 results
## Python 3.9 results
## Python 3.10 results
## Python 3.11 results
## Python 3.12 results
