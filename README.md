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

Pyccel configurations valid for your machine can be generated using the following command (which may be adapted for another compiler family, see the [pyccel documentation](https://pyccel.github.io/pyccel/docs/compiler.html)):
```
pyccel --compiler-family intel --export-compiler-config pyccel_intel.json
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
### Performance Comparison (as of Tue Dec 16 09:57:30 UTC 2025)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.18                      | 2.13                      | 0.28                      | 1.36                      | 1.39                      | 1.37                      | 1.45                     
Bellman Ford              | -                         | 3.27                      | 3.65                      | 0.95                      | 25.86                     | 1.62                      | 28.82                     | 1.64                     
Dijkstra                  | -                         | 2.42                      | 2.67                      | 1.06                      | 26.06                     | 1.70                      | 28.83                     | 1.83                     
Euler                     | -                         | 2.63                      | 2.99                      | 3.39                      | 25.95                     | 1.58                      | 28.97                     | 1.63                     
Midpoint Explicit         | -                         | 3.00                      | 3.44                      | 3.72                      | 26.20                     | 1.76                      | 28.93                     | 1.82                     
Midpoint Fixed            | -                         | 3.36                      | 3.80                      | 3.77                      | 26.55                     | 1.84                      | 29.01                     | 1.88                     
RK4                       | -                         | 3.56                      | 4.00                      | 3.87                      | 26.72                     | 2.19                      | 29.48                     | 2.31                     
FD - L Convection         | -                         | 2.34                      | 2.61                      | 2.53                      | 26.16                     | 1.51                      | 28.82                     | 1.54                     
FD - NL Convection        | -                         | 3.41                      | 3.58                      | 2.71                      | 25.92                     | 1.46                      | 28.75                     | 1.58                     
FD - Poisson              | -                         | 3.42                      | 3.77                      | 4.37                      | 26.35                     | 1.85                      | 29.07                     | 2.00                     
FD - Laplace              | -                         | 7.50                      | 7.94                      | 5.66                      | 26.32                     | 1.91                      | 29.25                     | 2.02                     
M-D                       | -                         | 6.24                      | 6.20                      | 6.22                      | 26.71                     | 2.54                      | 29.64                     | 2.57                     
Splines                   | -                         | -                         | -                         | 0.64                      | 26.29                     | 1.78                      | 28.88                     | 1.89                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 305.00                    | 7.09                      | 13.00                     | 18.90                     | 2.10                      | 2.25                      | 12.10                     | 15.50                    
Bellman Ford (ms)         | 1730.00                   | 4.61                      | 3.80                      | 4.57                      | 3.90                      | 3.23                      | 5.88                      | 3.53                     
Dijkstra (ms)             | 4540.00                   | 37.00                     | 31.50                     | 40.00                     | 55.60                     | 33.90                     | 64.00                     | 43.30                    
Euler (ms)                | 3110.00                   | 24.20                     | 25.80                     | 88.00                     | 21.50                     | 10.90                     | 24.80                     | 11.50                    
Midpoint Explicit (ms)    | 6330.00                   | 47.90                     | 46.80                     | 176.00                    | 39.40                     | 17.30                     | 42.90                     | 15.30                    
Midpoint Fixed (ms)       | 31600.00                  | 237.00                    | 84.00                     | 592.00                    | 173.00                    | 77.50                     | 178.00                    | 45.50                    
RK4 (ms)                  | 15800.00                  | 130.00                    | 34.40                     | 310.00                    | 80.30                     | 27.60                     | 87.10                     | 31.90                    
FD - L Convection (ms)    | 1990.00                   | 1.33                      | 1.78                      | 1.98                      | 6.42                      | 1.52                      | 8.49                      | 1.40                     
FD - NL Convection (ms)   | 2500.00                   | 1.42                      | 1.34                      | 2.84                      | 6.06                      | 1.42                      | 8.55                      | 1.41                     
FD - Poisson (ms)         | 5740.00                   | 3.08                      | 6.22                      | 6.63                      | 8.54                      | 2.79                      | 13.30                     | 2.75                     
FD - Laplace (ms)         | 551.00                    | 63.20                     | 233.00                    | 211.00                    | 203.00                    | 54.20                     | 396.00                    | 61.40                    
M-D (ms)                  | 14200.00                  | 25.00                     | 45.80                     | 53.10                     | 89.20                     | 55.40                     | 56.70                     | 54.20                    
Splines (ms)              | 1720.00                   | -                         | -                         | 18.20                     | 12.00                     | 17.00                     | 13.10                     | 26.50                    

![Development compilation results](./version_specific_results/devel_performance_311_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_311_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 2.1.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | -                         | -                         | 0.32                      | 1.40                      | 1.46                      | 1.44                      | 1.48                     
Bellman Ford              | -                         | -                         | -                         | 1.08                      | 1.70                      | 1.58                      | 1.66                      | 1.66                     
Dijkstra                  | -                         | -                         | -                         | 1.59                      | 1.79                      | 1.68                      | 1.75                      | 1.78                     
Euler                     | -                         | -                         | -                         | 2.05                      | 1.66                      | 1.56                      | 1.64                      | 1.64                     
Midpoint Explicit         | -                         | -                         | -                         | 3.06                      | 1.88                      | 1.78                      | 1.86                      | 1.85                     
Midpoint Fixed            | -                         | -                         | -                         | 3.27                      | 1.97                      | 1.83                      | 1.91                      | 1.91                     
RK4                       | -                         | -                         | -                         | 3.84                      | 2.35                      | 2.26                      | 2.27                      | 2.31                     
FD - L Convection         | -                         | -                         | -                         | 0.87                      | 1.62                      | 1.53                      | 1.59                      | 1.60                     
FD - NL Convection        | -                         | -                         | -                         | 0.87                      | 1.62                      | 1.53                      | 1.60                      | 1.60                     
FD - Poisson              | -                         | -                         | -                         | 1.32                      | 1.76                      | 1.80                      | 1.74                      | 2.00                     
FD - Laplace              | -                         | -                         | -                         | 3.04                      | 1.99                      | 1.94                      | 1.91                      | 2.05                     
M-D                       | -                         | -                         | -                         | 4.11                      | 2.47                      | 2.62                      | 2.40                      | 2.75                     
Splines                   | -                         | -                         | -                         | 0.60                      | 1.85                      | 1.81                      | 1.80                      | 1.92                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 312.00 $\pm$ 3.00         | -                         | -                         | 13.50 $\pm$ 0.00          | 1.39 $\pm$ 0.01           | 1.50 $\pm$ 0.00           | 4.46 $\pm$ 0.02           | 8.36 $\pm$ 0.24          
Bellman Ford (ms)         | 1870.00 $\pm$ 20.00       | -                         | -                         | 3.91 $\pm$ 0.04           | 4.16 $\pm$ 0.02           | 3.20 $\pm$ 0.02           | 6.04 $\pm$ 0.32           | 4.29 $\pm$ 0.01          
Dijkstra (ms)             | 4850.00 $\pm$ 70.00       | -                         | -                         | 18.60 $\pm$ 0.40          | 69.80 $\pm$ 1.00          | 18.10 $\pm$ 0.00          | 67.30 $\pm$ 0.30          | 19.80 $\pm$ 0.10         
Euler (ms)                | 3710.00 $\pm$ 30.00       | -                         | -                         | 37.80 $\pm$ 0.30          | 29.10 $\pm$ 0.40          | 11.80 $\pm$ 0.40          | 30.40 $\pm$ 0.40          | 13.40 $\pm$ 3.00         
Midpoint Explicit (ms)    | 7520.00 $\pm$ 60.00       | -                         | -                         | 72.00 $\pm$ 0.50          | 50.20 $\pm$ 0.40          | 19.90 $\pm$ 0.40          | 51.80 $\pm$ 0.30          | 14.80 $\pm$ 0.20         
Midpoint Fixed (ms)       | 38800.00 $\pm$ 500.00     | -                         | -                         | 370.00 $\pm$ 3.00         | 211.00 $\pm$ 0.00         | 80.10 $\pm$ 1.50          | 228.00 $\pm$ 1.00         | 47.30 $\pm$ 0.20         
RK4 (ms)                  | 19200.00 $\pm$ 100.00     | -                         | -                         | 141.00 $\pm$ 20.00        | 94.60 $\pm$ 0.80          | 29.50 $\pm$ 0.40          | 91.20 $\pm$ 0.70          | 25.30 $\pm$ 0.10         
FD - L Convection (ms)    | 2390.00 $\pm$ 40.00       | -                         | -                         | 3.05 $\pm$ 0.04           | 7.26 $\pm$ 0.20           | 1.66 $\pm$ 0.08           | 8.84 $\pm$ 0.12           | 1.50 $\pm$ 0.05          
FD - NL Convection (ms)   | 3000.00 $\pm$ 30.00       | -                         | -                         | 3.18 $\pm$ 0.07           | 7.66 $\pm$ 0.27           | 1.53 $\pm$ 0.07           | 8.90 $\pm$ 0.19           | 1.67 $\pm$ 0.02          
FD - Poisson (ms)         | 6370.00 $\pm$ 50.00       | -                         | -                         | 6.86 $\pm$ 0.06           | 14.00 $\pm$ 0.00          | 2.82 $\pm$ 0.03           | 21.60 $\pm$ 0.30          | 2.76 $\pm$ 0.02          
FD - Laplace (ms)         | 617.00 $\pm$ 2.00         | -                         | -                         | 273.00 $\pm$ 1.00         | 509.00 $\pm$ 1.00         | 57.00 $\pm$ 0.70          | 672.00 $\pm$ 1.00         | 54.30 $\pm$ 0.60         
M-D (ms)                  | 14900.00 $\pm$ 200.00     | -                         | -                         | 61.30 $\pm$ 0.60          | 101.00 $\pm$ 0.00         | 61.80 $\pm$ 0.20          | 63.30 $\pm$ 0.30          | 63.90 $\pm$ 2.20         
Splines (ms)              | 2070.00 $\pm$ 30.00       | -                         | -                         | 18.10 $\pm$ 0.30          | 15.10 $\pm$ 0.00          | 19.30 $\pm$ 0.50          | 17.10 $\pm$ 1.00          | 29.60 $\pm$ 0.10         

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 2.1.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | -                         | -                         | 0.35                      | 1.46                      | 1.48                      | 1.54                      | 1.61                     
Bellman Ford              | -                         | -                         | -                         | 1.02                      | 26.42                     | 1.58                      | 29.92                     | 1.69                     
Dijkstra                  | -                         | -                         | -                         | 1.17                      | 26.12                     | 1.66                      | 29.83                     | 1.81                     
Euler                     | -                         | -                         | -                         | 3.34                      | 25.90                     | 1.54                      | 29.77                     | 1.64                     
Midpoint Explicit         | -                         | -                         | -                         | 3.89                      | 26.31                     | 1.79                      | 30.27                     | 1.91                     
Midpoint Fixed            | -                         | -                         | -                         | 3.90                      | 26.15                     | 1.83                      | 30.00                     | 1.95                     
RK4                       | -                         | -                         | -                         | 3.98                      | 26.57                     | 2.27                      | 30.23                     | 2.33                     
FD - L Convection         | -                         | -                         | -                         | 2.59                      | 26.20                     | 1.50                      | 29.87                     | 1.61                     
FD - NL Convection        | -                         | -                         | -                         | 2.80                      | 26.60                     | 1.56                      | 30.39                     | 1.66                     
FD - Poisson              | -                         | -                         | -                         | 4.39                      | 26.03                     | 1.77                      | 29.67                     | 1.99                     
FD - Laplace              | -                         | -                         | -                         | 5.67                      | 27.09                     | 1.93                      | 30.10                     | 2.07                     
M-D                       | -                         | -                         | -                         | 6.54                      | 26.69                     | 2.61                      | 30.56                     | 2.77                     
Splines                   | -                         | -                         | -                         | 0.66                      | 26.10                     | 1.79                      | 29.85                     | 1.93                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 312.00 $\pm$ 3.00         | -                         | -                         | 9.02 $\pm$ 0.47           | 1.23 $\pm$ 0.01           | 1.32 $\pm$ 0.01           | 4.06 $\pm$ 0.02           | 8.76 $\pm$ 0.27          
Bellman Ford (ms)         | 1830.00 $\pm$ 30.00       | -                         | -                         | 4.05 $\pm$ 0.02           | 4.06 $\pm$ 0.02           | 3.25 $\pm$ 0.02           | 5.19 $\pm$ 0.01           | 3.83 $\pm$ 0.01          
Dijkstra (ms)             | 4980.00 $\pm$ 60.00       | -                         | -                         | 20.70 $\pm$ 0.70          | 38.00 $\pm$ 0.60          | 19.90 $\pm$ 0.20          | 47.80 $\pm$ 0.30          | 22.10 $\pm$ 0.30         
Euler (ms)                | 3420.00 $\pm$ 10.00       | -                         | -                         | 35.30 $\pm$ 0.60          | 22.20 $\pm$ 0.30          | 10.90 $\pm$ 0.30          | 24.20 $\pm$ 0.50          | 15.50 $\pm$ 0.40         
Midpoint Explicit (ms)    | 7000.00 $\pm$ 40.00       | -                         | -                         | 69.20 $\pm$ 4.90          | 39.90 $\pm$ 0.30          | 19.40 $\pm$ 0.50          | 43.90 $\pm$ 0.50          | 16.50 $\pm$ 1.10         
Midpoint Fixed (ms)       | 35400.00 $\pm$ 200.00     | -                         | -                         | 308.00 $\pm$ 3.00         | 183.00 $\pm$ 1.00         | 73.60 $\pm$ 2.90          | 195.00 $\pm$ 0.00         | 55.00 $\pm$ 0.40         
RK4 (ms)                  | 17300.00 $\pm$ 100.00     | -                         | -                         | 123.00 $\pm$ 2.00         | 90.40 $\pm$ 0.60          | 31.90 $\pm$ 0.40          | 94.30 $\pm$ 1.10          | 27.90 $\pm$ 0.30         
FD - L Convection (ms)    | 2300.00 $\pm$ 20.00       | -                         | -                         | 2.84 $\pm$ 0.02           | 5.80 $\pm$ 0.03           | 1.58 $\pm$ 0.11           | 8.25 $\pm$ 0.30           | 1.33 $\pm$ 0.04          
FD - NL Convection (ms)   | 2900.00 $\pm$ 30.00       | -                         | -                         | 2.89 $\pm$ 0.04           | 5.09 $\pm$ 0.01           | 1.62 $\pm$ 0.01           | 8.15 $\pm$ 0.13           | 1.40 $\pm$ 0.03          
FD - Poisson (ms)         | 6200.00 $\pm$ 40.00       | -                         | -                         | 6.58 $\pm$ 0.07           | 10.20 $\pm$ 0.00          | 2.59 $\pm$ 0.03           | 18.20 $\pm$ 0.10          | 2.54 $\pm$ 0.02          
FD - Laplace (ms)         | 580.00 $\pm$ 8.00         | -                         | -                         | 190.00 $\pm$ 2.00         | 204.00 $\pm$ 1.00         | 56.60 $\pm$ 0.40          | 355.00 $\pm$ 1.00         | 55.00 $\pm$ 0.30         
M-D (ms)                  | 15100.00 $\pm$ 100.00     | -                         | -                         | 56.90 $\pm$ 0.10          | 105.00 $\pm$ 0.00         | 62.80 $\pm$ 1.20          | 91.90 $\pm$ 0.50          | 90.40 $\pm$ 0.50         
Splines (ms)              | 1950.00 $\pm$ 40.00       | -                         | -                         | 17.60 $\pm$ 0.10          | 14.20 $\pm$ 0.00          | 17.60 $\pm$ 0.00          | 15.20 $\pm$ 0.10          | 27.80 $\pm$ 0.30         

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 2.1.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | -                         | -                         | 0.30                      | 1.39                      | 1.42                      | 1.46                      | 1.55                     
Bellman Ford              | -                         | -                         | -                         | 1.01                      | 26.15                     | 1.59                      | 30.04                     | 1.71                     
Dijkstra                  | -                         | -                         | -                         | 1.10                      | 26.21                     | 1.67                      | 30.02                     | 1.81                     
Euler                     | -                         | -                         | -                         | 3.30                      | 26.06                     | 1.53                      | 29.67                     | 1.66                     
Midpoint Explicit         | -                         | -                         | -                         | 3.70                      | 26.35                     | 1.76                      | 30.16                     | 1.86                     
Midpoint Fixed            | -                         | -                         | -                         | 3.87                      | 26.29                     | 1.80                      | 29.99                     | 1.93                     
RK4                       | -                         | -                         | -                         | 3.91                      | 26.98                     | 2.23                      | 30.83                     | 2.34                     
FD - L Convection         | -                         | -                         | -                         | 2.48                      | 26.06                     | 1.48                      | 29.86                     | 1.65                     
FD - NL Convection        | -                         | -                         | -                         | 2.62                      | 26.32                     | 1.51                      | 30.27                     | 1.62                     
FD - Poisson              | -                         | -                         | -                         | 4.14                      | 26.30                     | 1.86                      | 30.92                     | 2.05                     
FD - Laplace              | -                         | -                         | -                         | 5.44                      | 26.57                     | 1.95                      | 30.31                     | 2.09                     
M-D                       | -                         | -                         | -                         | 6.41                      | 26.90                     | 2.53                      | 30.66                     | 2.71                     
Splines                   | -                         | -                         | -                         | 0.66                      | 26.20                     | 1.80                      | 30.01                     | 1.95                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 448.00 $\pm$ 22.00        | -                         | -                         | 9.53 $\pm$ 0.40           | 1.30 $\pm$ 0.02           | 1.37 $\pm$ 0.02           | 4.07 $\pm$ 0.04           | 7.43 $\pm$ 0.04          
Bellman Ford (ms)         | 1710.00 $\pm$ 10.00       | -                         | -                         | 4.06 $\pm$ 0.03           | 4.20 $\pm$ 0.10           | 3.24 $\pm$ 0.02           | 5.29 $\pm$ 0.11           | 4.19 $\pm$ 0.02          
Dijkstra (ms)             | 4920.00 $\pm$ 30.00       | -                         | -                         | 22.70 $\pm$ 1.40          | 40.50 $\pm$ 0.80          | 20.50 $\pm$ 0.50          | 49.20 $\pm$ 0.60          | 22.50 $\pm$ 0.70         
Euler (ms)                | 3320.00 $\pm$ 30.00       | -                         | -                         | 35.30 $\pm$ 0.40          | 22.30 $\pm$ 0.40          | 10.90 $\pm$ 0.30          | 24.40 $\pm$ 0.50          | 15.40 $\pm$ 0.40         
Midpoint Explicit (ms)    | 6770.00 $\pm$ 60.00       | -                         | -                         | 70.30 $\pm$ 11.50         | 41.30 $\pm$ 4.50          | 19.00 $\pm$ 0.40          | 43.90 $\pm$ 0.50          | 16.40 $\pm$ 0.70         
Midpoint Fixed (ms)       | 34400.00 $\pm$ 600.00     | -                         | -                         | 308.00 $\pm$ 3.00         | 183.00 $\pm$ 1.00         | 73.00 $\pm$ 1.40          | 195.00 $\pm$ 1.00         | 55.10 $\pm$ 0.50         
RK4 (ms)                  | 16700.00 $\pm$ 100.00     | -                         | -                         | 123.00 $\pm$ 1.00         | 91.40 $\pm$ 1.20          | 32.10 $\pm$ 0.40          | 97.00 $\pm$ 1.80          | 27.90 $\pm$ 0.60         
FD - L Convection (ms)    | 2130.00 $\pm$ 20.00       | -                         | -                         | 2.85 $\pm$ 0.02           | 6.00 $\pm$ 0.11           | 1.64 $\pm$ 0.01           | 8.27 $\pm$ 0.19           | 1.52 $\pm$ 0.03          
FD - NL Convection (ms)   | 2670.00 $\pm$ 30.00       | -                         | -                         | 2.94 $\pm$ 0.05           | 5.27 $\pm$ 0.09           | 1.58 $\pm$ 0.06           | 8.37 $\pm$ 0.23           | 1.52 $\pm$ 0.01          
FD - Poisson (ms)         | 5910.00 $\pm$ 110.00      | -                         | -                         | 6.62 $\pm$ 0.05           | 10.30 $\pm$ 0.10          | 2.62 $\pm$ 0.04           | 18.80 $\pm$ 0.10          | 2.55 $\pm$ 0.02          
FD - Laplace (ms)         | 628.00 $\pm$ 9.00         | -                         | -                         | 190.00 $\pm$ 1.00         | 205.00 $\pm$ 1.00         | 61.80 $\pm$ 0.70          | 374.00 $\pm$ 5.00         | 59.80 $\pm$ 0.50         
M-D (ms)                  | 14500.00 $\pm$ 100.00     | -                         | -                         | 56.90 $\pm$ 0.20          | 105.00 $\pm$ 0.00         | 62.40 $\pm$ 0.30          | 91.20 $\pm$ 0.10          | 90.40 $\pm$ 0.40         
Splines (ms)              | 1690.00 $\pm$ 30.00       | -                         | -                         | 18.10 $\pm$ 0.10          | 14.30 $\pm$ 0.50          | 17.70 $\pm$ 0.00          | 15.20 $\pm$ 0.10          | 27.90 $\pm$ 0.20         

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
## Python 3.12 results
### Performance Comparison (as of 2.1.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | -                         | -                         | 0.32                      | 1.47                      | 1.50                      | 1.49                      | 1.56                     
Bellman Ford              | -                         | -                         | -                         | 1.09                      | 26.28                     | 1.60                      | 29.98                     | 1.71                     
Dijkstra                  | -                         | -                         | -                         | 1.15                      | 26.46                     | 1.71                      | 29.96                     | 1.84                     
Euler                     | -                         | -                         | -                         | 3.29                      | 26.24                     | 1.57                      | 29.90                     | 1.69                     
Midpoint Explicit         | -                         | -                         | -                         | 3.71                      | 26.51                     | 1.83                      | 30.05                     | 1.93                     
Midpoint Fixed            | -                         | -                         | -                         | 3.74                      | 26.59                     | 1.92                      | 30.25                     | 2.01                     
RK4                       | -                         | -                         | -                         | 3.78                      | 26.99                     | 2.31                      | 30.64                     | 2.40                     
FD - L Convection         | -                         | -                         | -                         | 2.53                      | 26.40                     | 1.54                      | 29.73                     | 1.64                     
FD - NL Convection        | -                         | -                         | -                         | 2.63                      | 26.18                     | 1.55                      | 29.77                     | 1.65                     
FD - Poisson              | -                         | -                         | -                         | 4.18                      | 26.40                     | 1.81                      | 29.90                     | 2.06                     
FD - Laplace              | -                         | -                         | -                         | 5.45                      | 26.67                     | 2.01                      | 30.08                     | 2.11                     
M-D                       | -                         | -                         | -                         | 6.48                      | 27.30                     | 2.73                      | 31.27                     | 2.80                     
Splines                   | -                         | -                         | -                         | 0.72                      | 26.55                     | 1.84                      | 30.05                     | 1.98                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 444.00 $\pm$ 10.00        | -                         | -                         | 9.22 $\pm$ 0.44           | 1.34 $\pm$ 0.02           | 1.28 $\pm$ 0.02           | 3.71 $\pm$ 0.02           | 9.78 $\pm$ 0.46          
Bellman Ford (ms)         | 2130.00 $\pm$ 20.00       | -                         | -                         | 4.10 $\pm$ 0.18           | 4.67 $\pm$ 0.02           | 3.24 $\pm$ 0.02           | 5.15 $\pm$ 0.02           | 3.83 $\pm$ 0.02          
Dijkstra (ms)             | 5870.00 $\pm$ 70.00       | -                         | -                         | 20.60 $\pm$ 1.00          | 37.80 $\pm$ 0.60          | 18.20 $\pm$ 0.20          | 47.10 $\pm$ 0.40          | 21.50 $\pm$ 0.40         
Euler (ms)                | 3880.00 $\pm$ 40.00       | -                         | -                         | 35.90 $\pm$ 0.20          | 22.50 $\pm$ 0.40          | 11.20 $\pm$ 0.60          | 24.20 $\pm$ 0.40          | 14.80 $\pm$ 0.20         
Midpoint Explicit (ms)    | 7870.00 $\pm$ 60.00       | -                         | -                         | 68.50 $\pm$ 0.60          | 39.80 $\pm$ 0.40          | 19.30 $\pm$ 0.30          | 44.20 $\pm$ 0.50          | 16.10 $\pm$ 0.40         
Midpoint Fixed (ms)       | 38900.00 $\pm$ 300.00     | -                         | -                         | 311.00 $\pm$ 2.00         | 183.00 $\pm$ 0.00         | 73.20 $\pm$ 1.20          | 203.00 $\pm$ 26.00        | 51.00 $\pm$ 0.30         
RK4 (ms)                  | 19800.00 $\pm$ 400.00     | -                         | -                         | 124.00 $\pm$ 2.00         | 89.60 $\pm$ 0.90          | 32.40 $\pm$ 0.30          | 96.00 $\pm$ 5.00          | 27.90 $\pm$ 0.60         
FD - L Convection (ms)    | 2390.00 $\pm$ 60.00       | -                         | -                         | 2.86 $\pm$ 0.06           | 5.83 $\pm$ 0.10           | 1.65 $\pm$ 0.06           | 8.09 $\pm$ 0.11           | 1.33 $\pm$ 0.06          
FD - NL Convection (ms)   | 2980.00 $\pm$ 20.00       | -                         | -                         | 2.96 $\pm$ 0.16           | 5.10 $\pm$ 0.01           | 1.70 $\pm$ 0.11           | 8.21 $\pm$ 0.17           | 1.43 $\pm$ 0.06          
FD - Poisson (ms)         | 6630.00 $\pm$ 320.00      | -                         | -                         | 6.66 $\pm$ 0.06           | 10.60 $\pm$ 0.30          | 2.60 $\pm$ 0.03           | 18.70 $\pm$ 0.10          | 2.56 $\pm$ 0.04          
FD - Laplace (ms)         | 655.00 $\pm$ 15.00        | -                         | -                         | 191.00 $\pm$ 1.00         | 205.00 $\pm$ 1.00         | 61.20 $\pm$ 0.70          | 348.00 $\pm$ 1.00         | 60.40 $\pm$ 0.80         
M-D (ms)                  | 16500.00 $\pm$ 200.00     | -                         | -                         | 57.10 $\pm$ 0.30          | 106.00 $\pm$ 0.00         | 62.00 $\pm$ 0.10          | 91.60 $\pm$ 1.20          | 90.20 $\pm$ 0.20         
Splines (ms)              | 1970.00 $\pm$ 40.00       | -                         | -                         | 17.80 $\pm$ 0.10          | 14.20 $\pm$ 0.10          | 17.70 $\pm$ 0.00          | 15.50 $\pm$ 0.60          | 27.70 $\pm$ 0.20         

![Python 3.12 compilation results](./version_specific_results/pypi_performance_312_compilation.svg)
![Python 3.12 execution results](./version_specific_results/pypi_performance_312_execution.svg)
## Python 3.13 results
### Performance Comparison (as of 2.1.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | -                         | -                         | 0.29                      | 1.39                      | 1.41                      | 1.45                      | 1.50                     
Bellman Ford              | -                         | -                         | -                         | 1.03                      | 25.86                     | 1.55                      | 29.43                     | 1.66                     
Dijkstra                  | -                         | -                         | -                         | 1.09                      | 26.00                     | 1.66                      | 29.58                     | 1.79                     
Euler                     | -                         | -                         | -                         | 3.07                      | 25.82                     | 1.54                      | 29.38                     | 1.65                     
Midpoint Explicit         | -                         | -                         | -                         | 3.42                      | 26.05                     | 1.75                      | 29.60                     | 1.84                     
Midpoint Fixed            | -                         | -                         | -                         | 3.57                      | 26.16                     | 1.82                      | 29.72                     | 1.94                     
RK4                       | -                         | -                         | -                         | 3.57                      | 26.47                     | 2.22                      | 30.04                     | 2.30                     
FD - L Convection         | -                         | -                         | -                         | 2.43                      | 25.76                     | 1.50                      | 29.44                     | 1.61                     
FD - NL Convection        | -                         | -                         | -                         | 2.52                      | 25.78                     | 1.50                      | 29.37                     | 1.60                     
FD - Poisson              | -                         | -                         | -                         | 3.94                      | 25.94                     | 1.77                      | 29.54                     | 2.00                     
FD - Laplace              | -                         | -                         | -                         | 5.10                      | 26.17                     | 1.91                      | 29.69                     | 2.03                     
M-D                       | -                         | -                         | -                         | 5.99                      | 26.59                     | 2.51                      | 30.21                     | 2.69                     
Splines                   | -                         | -                         | -                         | 0.70                      | 26.01                     | 1.78                      | 29.61                     | 1.93                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 446.00 $\pm$ 6.00         | -                         | -                         | 9.19 $\pm$ 0.53           | 1.33 $\pm$ 0.00           | 1.32 $\pm$ 0.01           | 3.70 $\pm$ 0.01           | 9.50 $\pm$ 0.28          
Bellman Ford (ms)         | 2120.00 $\pm$ 40.00       | -                         | -                         | 4.05 $\pm$ 0.02           | 4.69 $\pm$ 0.03           | 3.26 $\pm$ 0.03           | 5.19 $\pm$ 0.01           | 4.17 $\pm$ 0.01          
Dijkstra (ms)             | 5320.00 $\pm$ 30.00       | -                         | -                         | 19.90 $\pm$ 0.40          | 36.60 $\pm$ 0.50          | 17.60 $\pm$ 0.30          | 46.20 $\pm$ 0.30          | 20.20 $\pm$ 0.10         
Euler (ms)                | 3860.00 $\pm$ 80.00       | -                         | -                         | 35.90 $\pm$ 0.30          | 22.20 $\pm$ 0.30          | 10.90 $\pm$ 0.40          | 24.00 $\pm$ 0.50          | 14.80 $\pm$ 0.40         
Midpoint Explicit (ms)    | 7840.00 $\pm$ 80.00       | -                         | -                         | 67.70 $\pm$ 0.40          | 39.60 $\pm$ 0.40          | 18.80 $\pm$ 0.30          | 43.80 $\pm$ 0.50          | 15.80 $\pm$ 0.40         
Midpoint Fixed (ms)       | 39000.00 $\pm$ 300.00     | -                         | -                         | 315.00 $\pm$ 15.00        | 183.00 $\pm$ 0.00         | 72.50 $\pm$ 1.20          | 195.00 $\pm$ 1.00         | 50.60 $\pm$ 0.60         
RK4 (ms)                  | 19500.00 $\pm$ 100.00     | -                         | -                         | 125.00 $\pm$ 1.00         | 88.70 $\pm$ 0.60          | 31.80 $\pm$ 0.40          | 93.20 $\pm$ 0.40          | 28.60 $\pm$ 1.40         
FD - L Convection (ms)    | 2690.00 $\pm$ 20.00       | -                         | -                         | 2.85 $\pm$ 0.06           | 5.79 $\pm$ 0.01           | 1.56 $\pm$ 0.06           | 8.17 $\pm$ 0.15           | 1.35 $\pm$ 0.05          
FD - NL Convection (ms)   | 3380.00 $\pm$ 70.00       | -                         | -                         | 2.92 $\pm$ 0.10           | 5.09 $\pm$ 0.02           | 1.67 $\pm$ 0.06           | 8.18 $\pm$ 0.16           | 1.37 $\pm$ 0.02          
FD - Poisson (ms)         | 6730.00 $\pm$ 100.00      | -                         | -                         | 6.59 $\pm$ 0.03           | 10.60 $\pm$ 0.00          | 2.59 $\pm$ 0.04           | 23.50 $\pm$ 0.50          | 2.50 $\pm$ 0.02          
FD - Laplace (ms)         | 639.00 $\pm$ 7.00         | -                         | -                         | 189.00 $\pm$ 1.00         | 205.00 $\pm$ 1.00         | 56.30 $\pm$ 0.40          | 350.00 $\pm$ 1.00         | 54.90 $\pm$ 0.20         
M-D (ms)                  | 16000.00 $\pm$ 100.00     | -                         | -                         | 59.20 $\pm$ 7.00          | 106.00 $\pm$ 0.00         | 62.20 $\pm$ 0.20          | 94.50 $\pm$ 9.40          | 90.50 $\pm$ 0.10         
Splines (ms)              | 2030.00 $\pm$ 30.00       | -                         | -                         | 18.10 $\pm$ 0.20          | 14.10 $\pm$ 0.10          | 17.70 $\pm$ 0.00          | 15.30 $\pm$ 0.10          | 27.70 $\pm$ 0.10         

![Python 3.13 compilation results](./version_specific_results/pypi_performance_313_compilation.svg)
![Python 3.13 execution results](./version_specific_results/pypi_performance_313_execution.svg)
