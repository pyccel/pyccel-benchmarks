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
### Performance Comparison (as of Fri Jun 27 09:07:43 UTC 2025)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.36                      | 2.04                      | 0.27                      | 1.33                      | 1.35                      | 1.33                      | 1.39                     
Bellman Ford              | -                         | 3.37                      | 3.65                      | 0.94                      | 1.62                      | 1.50                      | 1.56                      | 1.55                     
Dijkstra                  | -                         | 2.35                      | 2.62                      | 1.20                      | 1.72                      | 1.60                      | 1.67                      | 1.69                     
Euler                     | -                         | 2.59                      | 2.95                      | 3.30                      | 1.57                      | 1.46                      | 1.55                      | 1.52                     
Midpoint Explicit         | -                         | 2.93                      | 3.32                      | 3.63                      | 1.83                      | 1.70                      | 1.75                      | 1.76                     
Midpoint Fixed            | -                         | 3.27                      | 3.63                      | 3.71                      | 1.88                      | 1.75                      | 1.80                      | 1.81                     
RK4                       | -                         | 3.43                      | 3.88                      | 3.71                      | 2.21                      | 2.14                      | 2.11                      | 2.16                     
FD - L Convection         | -                         | 2.28                      | 2.61                      | 2.43                      | 1.54                      | 1.44                      | 1.48                      | 1.48                     
FD - NL Convection        | -                         | 3.23                      | 3.54                      | 2.43                      | 1.53                      | 1.43                      | 1.50                      | 1.48                     
FD - Poisson              | -                         | 3.41                      | 3.67                      | 5.59                      | 1.66                      | 1.70                      | 1.63                      | 1.87                     
FD - Laplace              | -                         | 6.79                      | 7.50                      | 6.94                      | 1.90                      | 1.85                      | 1.80                      | 1.96                     
M-D                       | -                         | 6.16                      | 6.10                      | 8.36                      | 2.33                      | 2.46                      | 2.22                      | 2.53                     
Splines                   | -                         | -                         | -                         | 0.58                      | -                         | -                         | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 409.00                    | 2.92                      | 3.05                      | 9.82                      | 1.23                      | 1.32                      | 4.00                      | 9.63                     
Bellman Ford (ms)         | 1680.00                   | 5.25                      | 3.49                      | 3.83                      | 3.74                      | 3.26                      | 6.44                      | 4.42                     
Dijkstra (ms)             | 4750.00                   | 21.00                     | 17.10                     | 19.30                     | 67.00                     | 19.00                     | 69.20                     | 22.20                    
Euler (ms)                | 3380.00                   | 25.30                     | 25.20                     | 36.40                     | 26.40                     | 10.60                     | 26.80                     | 15.10                    
Midpoint Explicit (ms)    | 6860.00                   | 50.90                     | 50.80                     | 69.00                     | 45.20                     | 18.90                     | 45.90                     | 16.00                    
Midpoint Fixed (ms)       | 34500.00                  | 268.00                    | 91.90                     | 323.00                    | 190.00                    | 71.90                     | 354.00                    | 51.30                    
RK4 (ms)                  | 17100.00                  | 153.00                    | 36.00                     | 127.00                    | 95.80                     | 32.30                     | 90.40                     | 28.00                    
FD - L Convection (ms)    | 2130.00                   | 1.55                      | 1.60                      | 5.63                      | 6.63                      | 1.51                      | 7.74                      | 1.56                     
FD - NL Convection (ms)   | 2640.00                   | 2.02                      | 1.65                      | 5.65                      | 6.66                      | 1.59                      | 8.02                      | 1.40                     
FD - Poisson (ms)         | 5460.00                   | 2.97                      | 5.33                      | 6.74                      | 16.10                     | 2.63                      | 24.00                     | 2.60                     
FD - Laplace (ms)         | 623.00                    | 66.80                     | 127.00                    | 274.00                    | 484.00                    | 61.30                     | 656.00                    | 59.50                    
M-D (ms)                  | 14300.00                  | 36.10                     | 52.50                     | 60.60                     | 114.00                    | 62.40                     | 62.00                     | 89.40                    
Splines (s)               | 1.66                      | -                         | -                         | 0.02                      | -                         | -                         | -                         | -                        

![Development compilation results](./version_specific_results/devel_performance_311_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_311_execution.svg)
## Python 3.8 results
## Python 3.9 results
### Performance Comparison (as of 2.0.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.90                      | 1.78                      | 0.34                      | 1.40                      | 1.44                      | 1.39                      | 1.44                     
Bellman Ford              | -                         | 3.27                      | 3.49                      | 1.07                      | 1.68                      | 1.56                      | 1.64                      | 1.61                     
Dijkstra                  | -                         | 2.28                      | 2.53                      | 1.58                      | 1.78                      | 1.67                      | 1.70                      | 1.72                     
Euler                     | -                         | 2.53                      | 2.86                      | 2.03                      | 1.65                      | 1.54                      | 1.60                      | 1.59                     
Midpoint Explicit         | -                         | 2.93                      | 3.22                      | 3.01                      | 1.87                      | 1.77                      | 1.81                      | 1.80                     
Midpoint Fixed            | -                         | 3.25                      | 3.61                      | 3.22                      | 1.96                      | 1.82                      | 1.87                      | 1.87                     
RK4                       | -                         | 3.38                      | 3.78                      | 3.73                      | 2.35                      | 2.27                      | 2.25                      | 2.29                     
FD - L Convection         | -                         | 2.19                      | 2.45                      | 0.86                      | 1.61                      | 1.50                      | 1.55                      | 1.54                     
FD - NL Convection        | -                         | 3.11                      | 3.40                      | 0.87                      | 1.61                      | 1.52                      | 1.54                      | 1.54                     
FD - Poisson              | -                         | 3.34                      | 3.56                      | 1.33                      | 1.74                      | 1.78                      | 1.66                      | 1.91                     
FD - Laplace              | -                         | 6.63                      | 7.23                      | 3.00                      | 1.99                      | 1.93                      | 1.88                      | 2.00                     
M-D                       | -                         | 6.05                      | 5.97                      | 4.02                      | 2.44                      | 2.60                      | 2.33                      | 2.69                     
Splines                   | -                         | -                         | -                         | 0.60                      | -                         | -                         | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 300.00 $\pm$ 3.00         | 2.81 $\pm$ 0.03           | 3.06 $\pm$ 0.03           | 10.60 $\pm$ 0.40          | 1.23 $\pm$ 0.01           | 1.27 $\pm$ 0.01           | 4.36 $\pm$ 0.03           | 10.30 $\pm$ 0.70         
Bellman Ford (ms)         | 1860.00 $\pm$ 20.00       | 4.56 $\pm$ 0.04           | 3.53 $\pm$ 0.04           | 3.85 $\pm$ 0.06           | 3.72 $\pm$ 0.03           | 3.24 $\pm$ 0.04           | 5.82 $\pm$ 0.03           | 4.32 $\pm$ 0.06          
Dijkstra (ms)             | 4970.00 $\pm$ 50.00       | 18.10 $\pm$ 0.10          | 16.40 $\pm$ 0.00          | 18.90 $\pm$ 0.50          | 69.40 $\pm$ 1.00          | 17.80 $\pm$ 0.10          | 63.80 $\pm$ 1.00          | 20.60 $\pm$ 0.10         
Euler (ms)                | 3900.00 $\pm$ 30.00       | 25.40 $\pm$ 0.40          | 25.60 $\pm$ 0.40          | 36.50 $\pm$ 0.60          | 26.80 $\pm$ 0.40          | 10.80 $\pm$ 0.30          | 27.80 $\pm$ 0.50          | 15.30 $\pm$ 0.40         
Midpoint Explicit (ms)    | 7990.00 $\pm$ 70.00       | 56.50 $\pm$ 15.40         | 50.20 $\pm$ 0.30          | 69.30 $\pm$ 0.50          | 46.30 $\pm$ 3.80          | 18.90 $\pm$ 0.30          | 45.90 $\pm$ 0.40          | 16.20 $\pm$ 0.40         
Midpoint Fixed (ms)       | 40100.00 $\pm$ 300.00     | 267.00 $\pm$ 1.00         | 93.40 $\pm$ 3.60          | 356.00 $\pm$ 4.00         | 188.00 $\pm$ 2.00         | 73.20 $\pm$ 1.50          | 198.00 $\pm$ 1.00         | 52.30 $\pm$ 0.40         
RK4 (ms)                  | 19900.00 $\pm$ 100.00     | 155.00 $\pm$ 3.00         | 35.30 $\pm$ 0.50          | 149.00 $\pm$ 37.00        | 95.40 $\pm$ 1.50          | 31.90 $\pm$ 0.30          | 92.20 $\pm$ 2.30          | 27.90 $\pm$ 1.00         
FD - L Convection (ms)    | 2380.00 $\pm$ 20.00       | 1.51 $\pm$ 0.12           | 1.49 $\pm$ 0.04           | 2.70 $\pm$ 0.03           | 7.44 $\pm$ 0.05           | 1.49 $\pm$ 0.09           | 7.69 $\pm$ 0.10           | 1.31 $\pm$ 0.05          
FD - NL Convection (ms)   | 2910.00 $\pm$ 20.00       | 1.94 $\pm$ 0.06           | 1.61 $\pm$ 0.08           | 2.84 $\pm$ 0.05           | 6.75 $\pm$ 0.05           | 1.48 $\pm$ 0.07           | 8.13 $\pm$ 0.16           | 1.41 $\pm$ 0.05          
FD - Poisson (ms)         | 6470.00 $\pm$ 80.00       | 2.83 $\pm$ 0.04           | 5.34 $\pm$ 0.06           | 7.22 $\pm$ 0.05           | 15.30 $\pm$ 0.10          | 2.68 $\pm$ 0.04           | 23.70 $\pm$ 0.40          | 2.61 $\pm$ 0.05          
FD - Laplace (ms)         | 586.00 $\pm$ 9.00         | 66.50 $\pm$ 0.80          | 130.00 $\pm$ 1.00         | 250.00 $\pm$ 3.00         | 490.00 $\pm$ 3.00         | 60.60 $\pm$ 0.80          | 676.00 $\pm$ 6.00         | 59.30 $\pm$ 1.00         
M-D (ms)                  | 15400.00 $\pm$ 200.00     | 34.00 $\pm$ 0.40          | 52.70 $\pm$ 0.30          | 58.30 $\pm$ 0.60          | 113.00 $\pm$ 1.00         | 61.90 $\pm$ 0.20          | 61.20 $\pm$ 0.20          | 89.20 $\pm$ 0.50         
Splines (s)               | 2.03 $\pm$ 0.03           | -                         | -                         | 0.02 $\pm$ 0.00           | -                         | -                         | -                         | -                        

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 2.0.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.43                      | 2.11                      | 0.31                      | 1.34                      | 1.41                      | 1.34                      | 1.42                     
Bellman Ford              | -                         | 3.43                      | 3.68                      | 0.93                      | 1.63                      | 1.51                      | 1.59                      | 1.60                     
Dijkstra                  | -                         | 2.42                      | 2.69                      | 1.24                      | 1.72                      | 1.61                      | 1.65                      | 1.68                     
Euler                     | -                         | 2.66                      | 3.00                      | 3.31                      | 1.60                      | 1.49                      | 1.54                      | 1.54                     
Midpoint Explicit         | -                         | 3.01                      | 3.37                      | 3.62                      | 1.82                      | 1.73                      | 1.76                      | 1.75                     
Midpoint Fixed            | -                         | 3.43                      | 3.75                      | 3.77                      | 1.90                      | 1.77                      | 1.81                      | 1.81                     
RK4                       | -                         | 3.51                      | 3.94                      | 3.78                      | 2.27                      | 2.20                      | 2.19                      | 2.22                     
FD - L Convection         | -                         | 2.34                      | 2.59                      | 2.50                      | 1.55                      | 1.45                      | 1.49                      | 1.50                     
FD - NL Convection        | -                         | 3.27                      | 3.53                      | 2.54                      | 1.55                      | 1.46                      | 1.50                      | 1.50                     
FD - Poisson              | -                         | 3.49                      | 3.72                      | 5.80                      | 1.68                      | 1.72                      | 1.62                      | 1.88                     
FD - Laplace              | -                         | 6.86                      | 7.40                      | 7.24                      | 1.93                      | 1.88                      | 1.82                      | 1.95                     
M-D                       | -                         | 6.29                      | 6.14                      | 8.43                      | 2.38                      | 2.52                      | 2.28                      | 2.62                     
Splines                   | -                         | -                         | -                         | 0.57                      | -                         | -                         | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 305.00 $\pm$ 4.00         | 2.92 $\pm$ 0.00           | 3.06 $\pm$ 0.00           | 10.70 $\pm$ 0.30          | 1.23 $\pm$ 0.01           | 1.33 $\pm$ 0.00           | 3.71 $\pm$ 0.00           | 10.40 $\pm$ 0.20         
Bellman Ford (ms)         | 1870.00 $\pm$ 20.00       | 5.27 $\pm$ 0.05           | 3.52 $\pm$ 0.06           | 3.86 $\pm$ 0.05           | 3.75 $\pm$ 0.03           | 3.25 $\pm$ 0.03           | 6.47 $\pm$ 0.02           | 4.45 $\pm$ 0.02          
Dijkstra (ms)             | 5150.00 $\pm$ 60.00       | 20.50 $\pm$ 0.10          | 17.00 $\pm$ 0.10          | 19.10 $\pm$ 0.10          | 67.80 $\pm$ 0.20          | 18.70 $\pm$ 0.10          | 65.30 $\pm$ 0.10          | 22.00 $\pm$ 0.80         
Euler (ms)                | 3500.00 $\pm$ 40.00       | 25.50 $\pm$ 0.40          | 26.20 $\pm$ 1.60          | 36.90 $\pm$ 2.20          | 27.10 $\pm$ 0.40          | 10.90 $\pm$ 0.30          | 27.00 $\pm$ 0.40          | 15.20 $\pm$ 0.40         
Midpoint Explicit (ms)    | 7090.00 $\pm$ 70.00       | 51.40 $\pm$ 1.50          | 54.40 $\pm$ 13.00         | 69.70 $\pm$ 0.60          | 44.60 $\pm$ 0.30          | 19.00 $\pm$ 0.30          | 46.10 $\pm$ 0.50          | 16.30 $\pm$ 0.40         
Midpoint Fixed (ms)       | 35400.00 $\pm$ 200.00     | 267.00 $\pm$ 5.00         | 92.30 $\pm$ 0.50          | 320.00 $\pm$ 1.00         | 190.00 $\pm$ 1.00         | 72.20 $\pm$ 0.40          | 198.00 $\pm$ 1.00         | 50.70 $\pm$ 0.30         
RK4 (ms)                  | 17400.00 $\pm$ 100.00     | 153.00 $\pm$ 3.00         | 35.30 $\pm$ 0.50          | 126.00 $\pm$ 3.00         | 95.50 $\pm$ 0.40          | 31.30 $\pm$ 0.30          | 101.00 $\pm$ 8.00         | 29.50 $\pm$ 0.50         
FD - L Convection (ms)    | 2310.00 $\pm$ 50.00       | 1.53 $\pm$ 0.07           | 1.64 $\pm$ 0.02           | 5.66 $\pm$ 0.05           | 7.49 $\pm$ 0.05           | 1.57 $\pm$ 0.08           | 7.73 $\pm$ 0.10           | 1.33 $\pm$ 0.05          
FD - NL Convection (ms)   | 2780.00 $\pm$ 10.00       | 1.90 $\pm$ 0.06           | 1.80 $\pm$ 0.03           | 5.68 $\pm$ 0.01           | 6.76 $\pm$ 0.07           | 1.62 $\pm$ 0.07           | 8.20 $\pm$ 0.21           | 1.40 $\pm$ 0.03          
FD - Poisson (ms)         | 6730.00 $\pm$ 160.00      | 2.86 $\pm$ 0.07           | 5.40 $\pm$ 0.13           | 6.90 $\pm$ 0.15           | 16.00 $\pm$ 0.00          | 2.58 $\pm$ 0.02           | 24.00 $\pm$ 0.20          | 2.56 $\pm$ 0.02          
FD - Laplace (ms)         | 580.00 $\pm$ 19.00        | 66.70 $\pm$ 0.40          | 127.00 $\pm$ 1.00         | 281.00 $\pm$ 9.00         | 477.00 $\pm$ 3.00         | 60.90 $\pm$ 0.40          | 663.00 $\pm$ 2.00         | 55.40 $\pm$ 1.20         
M-D (ms)                  | 15100.00 $\pm$ 100.00     | 35.60 $\pm$ 1.70          | 52.50 $\pm$ 0.20          | 60.20 $\pm$ 0.20          | 117.00 $\pm$ 0.00         | 62.40 $\pm$ 0.30          | 61.20 $\pm$ 0.20          | 89.50 $\pm$ 0.20         
Splines (s)               | 1.91 $\pm$ 0.02           | -                         | -                         | 0.02 $\pm$ 0.00           | -                         | -                         | -                         | -                        

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 2.0.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.35                      | 2.10                      | 0.28                      | 1.34                      | 1.39                      | 1.33                      | 1.38                     
Bellman Ford              | -                         | 3.33                      | 3.61                      | 0.95                      | 1.63                      | 1.52                      | 1.56                      | 1.54                     
Dijkstra                  | -                         | 2.39                      | 2.59                      | 1.20                      | 1.74                      | 1.61                      | 1.66                      | 1.68                     
Euler                     | -                         | 2.58                      | 2.97                      | 3.33                      | 1.59                      | 1.48                      | 1.54                      | 1.59                     
Midpoint Explicit         | -                         | 2.92                      | 3.34                      | 3.58                      | 1.84                      | 1.69                      | 1.75                      | 1.73                     
Midpoint Fixed            | -                         | 3.33                      | 3.72                      | 3.72                      | 1.90                      | 1.77                      | 1.83                      | 1.82                     
RK4                       | -                         | 3.47                      | 3.94                      | 3.75                      | 2.21                      | 2.17                      | 2.12                      | 2.17                     
FD - L Convection         | -                         | 2.29                      | 2.57                      | 2.45                      | 1.54                      | 1.44                      | 1.48                      | 1.48                     
FD - NL Convection        | -                         | 3.24                      | 3.61                      | 2.45                      | 1.54                      | 1.44                      | 1.49                      | 1.48                     
FD - Poisson              | -                         | 3.40                      | 3.67                      | 5.60                      | 1.67                      | 1.71                      | 1.62                      | 1.87                     
FD - Laplace              | -                         | 6.77                      | 7.53                      | 7.03                      | 1.91                      | 1.85                      | 1.81                      | 1.94                     
M-D                       | -                         | 6.14                      | 6.16                      | 8.40                      | 2.35                      | 2.46                      | 2.24                      | 2.56                     
Splines                   | -                         | -                         | -                         | 0.59                      | -                         | -                         | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 425.00 $\pm$ 8.00         | 2.94 $\pm$ 0.09           | 3.06 $\pm$ 0.01           | 10.80 $\pm$ 0.10          | 1.23 $\pm$ 0.00           | 1.33 $\pm$ 0.01           | 4.06 $\pm$ 0.02           | 9.51 $\pm$ 0.51          
Bellman Ford (ms)         | 1690.00 $\pm$ 10.00       | 5.25 $\pm$ 0.01           | 3.55 $\pm$ 0.06           | 3.87 $\pm$ 0.06           | 3.86 $\pm$ 0.02           | 3.24 $\pm$ 0.02           | 6.46 $\pm$ 0.02           | 4.32 $\pm$ 0.06          
Dijkstra (ms)             | 4770.00 $\pm$ 30.00       | 21.00 $\pm$ 0.50          | 17.10 $\pm$ 0.30          | 20.00 $\pm$ 0.50          | 68.00 $\pm$ 0.40          | 19.10 $\pm$ 0.30          | 65.60 $\pm$ 0.30          | 21.90 $\pm$ 0.20         
Euler (ms)                | 3360.00 $\pm$ 30.00       | 25.40 $\pm$ 0.30          | 25.50 $\pm$ 0.30          | 36.40 $\pm$ 0.40          | 27.60 $\pm$ 2.90          | 11.10 $\pm$ 0.40          | 27.00 $\pm$ 0.30          | 15.70 $\pm$ 0.40         
Midpoint Explicit (ms)    | 6890.00 $\pm$ 50.00       | 51.30 $\pm$ 0.40          | 50.80 $\pm$ 1.30          | 69.60 $\pm$ 0.80          | 46.00 $\pm$ 3.60          | 18.90 $\pm$ 0.30          | 46.10 $\pm$ 1.10          | 16.70 $\pm$ 1.10         
Midpoint Fixed (ms)       | 34700.00 $\pm$ 200.00     | 268.00 $\pm$ 2.00         | 93.40 $\pm$ 1.60          | 322.00 $\pm$ 1.00         | 190.00 $\pm$ 1.00         | 72.40 $\pm$ 0.30          | 199.00 $\pm$ 1.00         | 51.10 $\pm$ 0.50         
RK4 (ms)                  | 17100.00 $\pm$ 100.00     | 154.00 $\pm$ 3.00         | 35.60 $\pm$ 0.60          | 127.00 $\pm$ 1.00         | 96.20 $\pm$ 3.10          | 31.70 $\pm$ 0.30          | 90.90 $\pm$ 0.90          | 28.30 $\pm$ 0.40         
FD - L Convection (ms)    | 2120.00 $\pm$ 30.00       | 1.53 $\pm$ 0.04           | 1.62 $\pm$ 0.02           | 5.64 $\pm$ 0.01           | 7.49 $\pm$ 0.09           | 1.52 $\pm$ 0.05           | 7.72 $\pm$ 0.08           | 1.52 $\pm$ 0.02          
FD - NL Convection (ms)   | 2640.00 $\pm$ 20.00       | 2.02 $\pm$ 0.02           | 1.79 $\pm$ 0.02           | 5.69 $\pm$ 0.06           | 6.73 $\pm$ 0.06           | 1.56 $\pm$ 0.06           | 8.07 $\pm$ 0.15           | 1.52 $\pm$ 0.02          
FD - Poisson (ms)         | 5990.00 $\pm$ 350.00      | 3.00 $\pm$ 0.14           | 5.42 $\pm$ 0.07           | 6.95 $\pm$ 0.10           | 16.10 $\pm$ 0.00          | 2.60 $\pm$ 0.02           | 23.70 $\pm$ 0.10          | 2.55 $\pm$ 0.03          
FD - Laplace (ms)         | 632.00 $\pm$ 3.00         | 66.90 $\pm$ 0.50          | 127.00 $\pm$ 1.00         | 276.00 $\pm$ 5.00         | 478.00 $\pm$ 6.00         | 56.70 $\pm$ 0.20          | 663.00 $\pm$ 1.00         | 59.30 $\pm$ 0.60         
M-D (ms)                  | 14500.00 $\pm$ 100.00     | 35.70 $\pm$ 0.30          | 52.40 $\pm$ 0.20          | 60.20 $\pm$ 0.30          | 117.00 $\pm$ 0.00         | 62.20 $\pm$ 0.20          | 62.00 $\pm$ 0.30          | 89.20 $\pm$ 0.30         
Splines (s)               | 1.70 $\pm$ 0.03           | -                         | -                         | 0.02 $\pm$ 0.00           | -                         | -                         | -                         | -                        

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
## Python 3.12 results
### Performance Comparison (as of 2.0.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.01                      | 2.10                      | 0.30                      | 1.41                      | 1.47                      | 1.42                      | 1.48                     
Bellman Ford              | -                         | 3.36                      | 3.66                      | 1.01                      | 1.71                      | 1.59                      | 1.63                      | 1.63                     
Dijkstra                  | -                         | 2.38                      | 2.69                      | 1.28                      | 1.86                      | 1.68                      | 1.71                      | 1.77                     
Euler                     | -                         | 2.62                      | 3.02                      | 3.25                      | 1.68                      | 1.60                      | 1.62                      | 1.62                     
Midpoint Explicit         | -                         | 2.97                      | 3.42                      | 3.53                      | 1.90                      | 1.79                      | 1.85                      | 1.82                     
Midpoint Fixed            | -                         | 3.34                      | 3.71                      | 3.62                      | 2.02                      | 1.84                      | 1.91                      | 1.91                     
RK4                       | -                         | 3.50                      | 4.08                      | 3.69                      | 2.41                      | 2.38                      | 2.33                      | 2.37                     
FD - L Convection         | -                         | 2.35                      | 2.70                      | 2.51                      | 1.66                      | 1.56                      | 1.58                      | 1.59                     
FD - NL Convection        | -                         | 3.31                      | 3.75                      | 2.58                      | 1.68                      | 1.59                      | 1.61                      | 1.62                     
FD - Poisson              | -                         | 3.57                      | 3.87                      | 6.07                      | 1.83                      | 1.89                      | 1.79                      | 2.07                     
FD - Laplace              | -                         | 7.37                      | 8.21                      | 7.50                      | 2.12                      | 2.09                      | 2.00                      | 2.17                     
M-D                       | -                         | 6.23                      | 6.28                      | 8.41                      | 2.47                      | 2.67                      | 2.38                      | 2.72                     
Splines                   | -                         | -                         | -                         | 0.64                      | -                         | -                         | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 434.00 $\pm$ 9.00         | 2.73 $\pm$ 0.08           | 3.96 $\pm$ 0.01           | 10.60 $\pm$ 0.40          | 1.28 $\pm$ 0.01           | 1.28 $\pm$ 0.00           | 4.36 $\pm$ 0.01           | 10.60 $\pm$ 0.10         
Bellman Ford (ms)         | 2290.00 $\pm$ 50.00       | 4.53 $\pm$ 0.01           | 3.52 $\pm$ 0.08           | 3.88 $\pm$ 0.08           | 3.88 $\pm$ 0.03           | 3.25 $\pm$ 0.02           | 5.91 $\pm$ 0.06           | 4.21 $\pm$ 0.02          
Dijkstra (ms)             | 5990.00 $\pm$ 70.00       | 21.50 $\pm$ 0.20          | 18.30 $\pm$ 0.20          | 21.00 $\pm$ 0.70          | 71.30 $\pm$ 0.40          | 20.00 $\pm$ 0.30          | 68.00 $\pm$ 0.40          | 22.80 $\pm$ 0.40         
Euler (ms)                | 3930.00 $\pm$ 80.00       | 25.60 $\pm$ 0.40          | 26.10 $\pm$ 0.50          | 37.00 $\pm$ 0.40          | 27.00 $\pm$ 0.40          | 11.20 $\pm$ 0.40          | 27.60 $\pm$ 1.90          | 15.50 $\pm$ 0.40         
Midpoint Explicit (ms)    | 7970.00 $\pm$ 50.00       | 51.80 $\pm$ 0.40          | 51.60 $\pm$ 2.20          | 70.10 $\pm$ 0.60          | 45.30 $\pm$ 1.30          | 19.00 $\pm$ 0.30          | 45.80 $\pm$ 0.20          | 16.30 $\pm$ 0.40         
Midpoint Fixed (ms)       | 39000.00 $\pm$ 200.00     | 269.00 $\pm$ 5.00         | 92.90 $\pm$ 0.40          | 327.00 $\pm$ 2.00         | 189.00 $\pm$ 0.00         | 73.30 $\pm$ 1.50          | 198.00 $\pm$ 1.00         | 53.80 $\pm$ 1.90         
RK4 (ms)                  | 19900.00 $\pm$ 100.00     | 155.00 $\pm$ 3.00         | 36.00 $\pm$ 0.60          | 127.00 $\pm$ 1.00         | 103.00 $\pm$ 21.00        | 32.70 $\pm$ 0.40          | 92.20 $\pm$ 0.90          | 28.10 $\pm$ 0.30         
FD - L Convection (ms)    | 2520.00 $\pm$ 40.00       | 1.48 $\pm$ 0.08           | 1.63 $\pm$ 0.02           | 5.64 $\pm$ 0.00           | 7.48 $\pm$ 0.08           | 1.52 $\pm$ 0.02           | 7.49 $\pm$ 0.08           | 1.52 $\pm$ 0.03          
FD - NL Convection (ms)   | 3160.00 $\pm$ 40.00       | 1.85 $\pm$ 0.00           | 1.71 $\pm$ 0.07           | 5.67 $\pm$ 0.02           | 6.74 $\pm$ 0.08           | 1.55 $\pm$ 0.05           | 8.11 $\pm$ 0.13           | 1.54 $\pm$ 0.04          
FD - Poisson (ms)         | 6950.00 $\pm$ 120.00      | 2.89 $\pm$ 0.03           | 5.47 $\pm$ 0.05           | 6.96 $\pm$ 0.13           | 16.10 $\pm$ 0.00          | 2.64 $\pm$ 0.04           | 24.00 $\pm$ 0.00          | 2.56 $\pm$ 0.04          
FD - Laplace (ms)         | 633.00 $\pm$ 9.00         | 63.80 $\pm$ 1.20          | 104.00 $\pm$ 1.00         | 279.00 $\pm$ 7.00         | 487.00 $\pm$ 2.00         | 62.20 $\pm$ 0.70          | 659.00 $\pm$ 1.00         | 55.50 $\pm$ 0.50         
M-D (ms)                  | 16700.00 $\pm$ 100.00     | 34.30 $\pm$ 0.20          | 49.90 $\pm$ 0.20          | 60.60 $\pm$ 0.70          | 115.00 $\pm$ 0.00         | 62.50 $\pm$ 0.40          | 62.00 $\pm$ 0.40          | 95.70 $\pm$ 19.20        
Splines (s)               | 2.03 $\pm$ 0.04           | -                         | -                         | 0.02 $\pm$ 0.00           | -                         | -                         | -                         | -                        

![Python 3.12 compilation results](./version_specific_results/pypi_performance_312_compilation.svg)
![Python 3.12 execution results](./version_specific_results/pypi_performance_312_execution.svg)
