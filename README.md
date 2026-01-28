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
### Performance Comparison (as of Wed Jan 28 13:13:26 UTC 2026)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.07                      | 2.22                      | 0.31                      | 1.44                      | 1.47                      | 1.49                      | 1.59                     
Bellman Ford              | -                         | 3.48                      | 3.74                      | 1.07                      | 1.63                      | 1.62                      | 1.65                      | 1.75                     
Dijkstra                  | -                         | 2.38                      | 2.75                      | 1.15                      | 1.70                      | 1.71                      | 1.78                      | 1.87                     
Euler                     | -                         | 2.66                      | 3.09                      | 3.24                      | 1.58                      | 1.58                      | 1.64                      | 1.70                     
Midpoint Explicit         | -                         | 2.99                      | 3.46                      | 3.59                      | 1.82                      | 1.82                      | 1.83                      | 1.93                     
Midpoint Fixed            | -                         | 3.39                      | 3.81                      | 3.73                      | 1.93                      | 1.92                      | 1.96                      | 2.01                     
RK4                       | -                         | 3.53                      | 4.07                      | 3.83                      | 2.27                      | 2.32                      | 2.26                      | 2.39                     
FD - L Convection         | -                         | 2.34                      | 2.72                      | 2.50                      | 1.54                      | 1.58                      | 1.60                      | 1.70                     
FD - NL Convection        | -                         | 3.44                      | 3.68                      | 2.64                      | 1.56                      | 1.56                      | 1.59                      | 1.67                     
FD - Poisson              | -                         | 3.54                      | 3.80                      | 4.18                      | 1.72                      | 1.85                      | 1.71                      | 2.07                     
FD - Laplace              | -                         | 7.07                      | 7.85                      | 5.44                      | 1.96                      | 2.00                      | 1.95                      | 2.15                     
M-D                       | -                         | 6.00                      | 6.43                      | 6.24                      | 2.45                      | 2.68                      | 2.54                      | 2.81                     
Splines                   | -                         | -                         | -                         | 0.73                      | 1.76                      | 1.86                      | 1.79                      | 2.02                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 425.00                    | 2.69                      | 3.66                      | 8.55                      | 1.33                      | 1.32                      | 3.70                      | 9.00                     
Bellman Ford (ms)         | 2140.00                   | 4.62                      | 3.51                      | 4.03                      | 3.31                      | 3.26                      | 5.36                      | 4.18                     
Dijkstra (ms)             | 5760.00                   | 19.10                     | 16.70                     | 19.90                     | 38.10                     | 19.70                     | 42.10                     | 21.50                    
Euler (ms)                | 3780.00                   | 25.70                     | 25.40                     | 36.10                     | 24.00                     | 11.50                     | 23.50                     | 14.90                    
Midpoint Explicit (ms)    | 7720.00                   | 52.30                     | 50.50                     | 68.00                     | 40.10                     | 19.40                     | 43.00                     | 16.90                    
Midpoint Fixed (ms)       | 38800.00                  | 266.00                    | 92.30                     | 309.00                    | 178.00                    | 72.40                     | 201.00                    | 50.50                    
RK4 (ms)                  | 19200.00                  | 154.00                    | 35.70                     | 125.00                    | 86.00                     | 31.70                     | 90.10                     | 27.70                    
FD - L Convection (ms)    | 2450.00                   | 1.56                      | 1.60                      | 2.82                      | 4.28                      | 1.52                      | 4.54                      | 1.56                     
FD - NL Convection (ms)   | 3000.00                   | 1.85                      | 1.70                      | 2.85                      | 4.69                      | 1.61                      | 4.07                      | 1.37                     
FD - Poisson (ms)         | 6420.00                   | 2.98                      | 5.54                      | 6.82                      | 3.74                      | 2.61                      | 6.32                      | 2.56                     
FD - Laplace (ms)         | 642.00                    | 68.00                     | 106.00                    | 191.00                    | 151.00                    | 61.20                     | 197.00                    | 59.50                    
M-D (ms)                  | 16300.00                  | 35.20                     | 50.20                     | 56.80                     | 106.00                    | 62.00                     | 88.70                     | 90.90                    
Splines (ms)              | 1800.00                   | -                         | -                         | 18.00                     | 13.50                     | 18.40                     | 15.10                     | 27.70                    

![Development compilation results](./version_specific_results/devel_performance_312_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_312_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 2.1.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.93                      | 1.98                      | 0.30                      | 1.28                      | 1.30                      | 1.31                      | 1.37                     
Bellman Ford              | -                         | 3.13                      | 3.42                      | 0.90                      | 24.44                     | 1.43                      | 27.01                     | 1.51                     
Dijkstra                  | -                         | 2.20                      | 2.46                      | 1.01                      | 24.44                     | 1.52                      | 26.88                     | 1.63                     
Euler                     | -                         | 2.43                      | 2.74                      | 3.18                      | 24.29                     | 1.42                      | 26.73                     | 1.47                     
Midpoint Explicit         | -                         | 2.81                      | 3.12                      | 3.83                      | 25.89                     | 1.72                      | 28.46                     | 1.82                     
Midpoint Fixed            | -                         | 3.20                      | 3.47                      | 3.67                      | 24.60                     | 1.67                      | 26.93                     | 1.75                     
RK4                       | -                         | 3.38                      | 3.74                      | 3.77                      | 25.19                     | 2.09                      | 27.62                     | 2.13                     
FD - L Convection         | -                         | 2.20                      | 2.43                      | 2.53                      | 24.60                     | 1.40                      | 26.85                     | 1.47                     
FD - NL Convection        | -                         | 3.11                      | 3.31                      | 2.67                      | 24.34                     | 1.37                      | 26.58                     | 1.45                     
FD - Poisson              | -                         | 3.17                      | 3.36                      | 4.35                      | 24.56                     | 1.64                      | 26.66                     | 1.81                     
FD - Laplace              | -                         | 6.59                      | 7.15                      | 5.62                      | 24.63                     | 1.78                      | 26.86                     | 1.86                     
M-D                       | -                         | 5.69                      | 5.74                      | 6.08                      | 25.30                     | 2.45                      | 27.70                     | 2.53                     
Splines                   | -                         | -                         | -                         | 0.59                      | 24.56                     | 1.64                      | 26.81                     | 1.74                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 282.00 $\pm$ 3.00         | 7.10 $\pm$ 0.06           | 13.00 $\pm$ 0.00          | 19.10 $\pm$ 0.10          | 2.23 $\pm$ 0.01           | 2.27 $\pm$ 0.00           | 11.70 $\pm$ 0.10          | 15.30 $\pm$ 0.10         
Bellman Ford (ms)         | 1740.00 $\pm$ 20.00       | 4.59 $\pm$ 0.01           | 3.78 $\pm$ 0.08           | 4.57 $\pm$ 0.02           | 3.94 $\pm$ 0.10           | 3.21 $\pm$ 0.00           | 5.87 $\pm$ 0.02           | 3.53 $\pm$ 0.02          
Dijkstra (ms)             | 5020.00 $\pm$ 60.00       | 28.40 $\pm$ 0.70          | 23.10 $\pm$ 2.30          | 27.00 $\pm$ 0.40          | 43.90 $\pm$ 0.50          | 24.50 $\pm$ 0.50          | 58.50 $\pm$ 7.70          | 33.30 $\pm$ 2.80         
Euler (ms)                | 3210.00 $\pm$ 20.00       | 22.40 $\pm$ 0.40          | 22.80 $\pm$ 0.50          | 86.10 $\pm$ 2.90          | 19.50 $\pm$ 0.10          | 10.30 $\pm$ 0.30          | 22.80 $\pm$ 0.40          | 9.84 $\pm$ 0.36          
Midpoint Explicit (ms)    | 6440.00 $\pm$ 20.00       | 46.40 $\pm$ 0.90          | 45.20 $\pm$ 0.50          | 166.00 $\pm$ 1.00         | 38.70 $\pm$ 0.20          | 17.80 $\pm$ 0.20          | 41.70 $\pm$ 0.30          | 15.20 $\pm$ 0.40         
Midpoint Fixed (ms)       | 32700.00 $\pm$ 200.00     | 233.00 $\pm$ 3.00         | 82.30 $\pm$ 1.00          | 595.00 $\pm$ 11.00        | 171.00 $\pm$ 0.00         | 70.30 $\pm$ 4.60          | 180.00 $\pm$ 3.00         | 42.80 $\pm$ 0.40         
RK4 (ms)                  | 16100.00 $\pm$ 100.00     | 131.00 $\pm$ 3.00         | 33.70 $\pm$ 0.50          | 309.00 $\pm$ 4.00         | 80.60 $\pm$ 1.40          | 26.60 $\pm$ 0.80          | 85.80 $\pm$ 3.50          | 29.90 $\pm$ 0.30         
FD - L Convection (ms)    | 2000.00 $\pm$ 10.00       | 1.31 $\pm$ 0.02           | 1.40 $\pm$ 0.00           | 2.14 $\pm$ 0.18           | 6.38 $\pm$ 0.04           | 1.49 $\pm$ 0.03           | 8.51 $\pm$ 0.06           | 1.40 $\pm$ 0.00          
FD - NL Convection (ms)   | 2530.00 $\pm$ 20.00       | 1.41 $\pm$ 0.01           | 1.33 $\pm$ 0.00           | 2.56 $\pm$ 0.12           | 6.07 $\pm$ 0.04           | 1.39 $\pm$ 0.02           | 8.58 $\pm$ 0.06           | 1.41 $\pm$ 0.00          
FD - Poisson (ms)         | 6170.00 $\pm$ 120.00      | 3.05 $\pm$ 0.01           | 6.17 $\pm$ 0.02           | 6.75 $\pm$ 0.06           | 8.62 $\pm$ 0.05           | 2.71 $\pm$ 0.01           | 13.30 $\pm$ 0.10          | 2.70 $\pm$ 0.01          
FD - Laplace (ms)         | 491.00 $\pm$ 5.00         | 64.60 $\pm$ 0.80          | 226.00 $\pm$ 2.00         | 214.00 $\pm$ 3.00         | 202.00 $\pm$ 1.00         | 55.40 $\pm$ 0.30          | 396.00 $\pm$ 5.00         | 60.70 $\pm$ 0.50         
M-D (ms)                  | 14300.00 $\pm$ 0.00       | 25.10 $\pm$ 0.60          | 46.10 $\pm$ 0.60          | 53.40 $\pm$ 0.30          | 89.10 $\pm$ 0.10          | 55.50 $\pm$ 0.90          | 56.60 $\pm$ 0.20          | 54.70 $\pm$ 0.70         
Splines (ms)              | 1910.00 $\pm$ 20.00       | -                         | -                         | 17.70 $\pm$ 0.10          | 12.00 $\pm$ 0.10          | 17.00 $\pm$ 0.10          | 13.20 $\pm$ 0.10          | 26.50 $\pm$ 0.10         

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 2.1.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.14                      | 2.20                      | 0.30                      | 1.37                      | 1.42                      | 1.42                      | 1.50                     
Bellman Ford              | -                         | 3.31                      | 3.66                      | 0.98                      | 26.13                     | 1.56                      | 29.68                     | 1.66                     
Dijkstra                  | -                         | 2.27                      | 2.60                      | 1.10                      | 26.69                     | 1.71                      | 30.31                     | 1.82                     
Euler                     | -                         | 2.68                      | 3.16                      | 3.43                      | 26.76                     | 1.54                      | 29.89                     | 1.66                     
Midpoint Explicit         | -                         | 2.95                      | 3.40                      | 3.73                      | 26.66                     | 1.79                      | 30.51                     | 1.90                     
Midpoint Fixed            | -                         | 3.26                      | 3.73                      | 3.89                      | 26.34                     | 1.81                      | 30.12                     | 1.92                     
RK4                       | -                         | 3.35                      | 3.81                      | 3.75                      | 26.53                     | 2.18                      | 29.92                     | 2.27                     
FD - L Convection         | -                         | 2.26                      | 2.68                      | 2.41                      | 25.85                     | 1.47                      | 29.48                     | 1.57                     
FD - NL Convection        | -                         | 3.21                      | 3.55                      | 2.59                      | 25.72                     | 1.47                      | 29.27                     | 1.56                     
FD - Poisson              | -                         | 3.39                      | 3.78                      | 4.08                      | 25.99                     | 1.75                      | 29.56                     | 2.00                     
FD - Laplace              | -                         | 7.00                      | 7.77                      | 5.33                      | 26.41                     | 1.89                      | 29.77                     | 2.05                     
M-D                       | -                         | 6.27                      | 6.70                      | 6.59                      | 26.62                     | 2.50                      | 30.29                     | 2.65                     
Splines                   | -                         | -                         | -                         | 0.65                      | 25.91                     | 1.75                      | 29.93                     | 1.94                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 430.00 $\pm$ 8.00         | 2.95 $\pm$ 0.16           | 3.67 $\pm$ 0.01           | 9.26 $\pm$ 0.47           | 1.25 $\pm$ 0.02           | 1.33 $\pm$ 0.01           | 4.06 $\pm$ 0.03           | 10.00 $\pm$ 0.50         
Bellman Ford (ms)         | 1740.00 $\pm$ 20.00       | 4.51 $\pm$ 0.01           | 3.65 $\pm$ 0.13           | 4.05 $\pm$ 0.02           | 4.06 $\pm$ 0.02           | 3.28 $\pm$ 0.03           | 5.19 $\pm$ 0.02           | 3.84 $\pm$ 0.01          
Dijkstra (ms)             | 4890.00 $\pm$ 40.00       | 20.00 $\pm$ 0.20          | 16.50 $\pm$ 0.40          | 20.80 $\pm$ 0.80          | 38.70 $\pm$ 0.50          | 19.80 $\pm$ 0.40          | 51.70 $\pm$ 0.60          | 22.70 $\pm$ 0.30         
Euler (ms)                | 3350.00 $\pm$ 90.00       | 25.80 $\pm$ 0.40          | 26.30 $\pm$ 0.30          | 35.80 $\pm$ 0.30          | 24.00 $\pm$ 4.20          | 11.40 $\pm$ 0.60          | 24.50 $\pm$ 0.40          | 14.90 $\pm$ 0.30         
Midpoint Explicit (ms)    | 6830.00 $\pm$ 70.00       | 52.90 $\pm$ 1.90          | 51.50 $\pm$ 2.40          | 67.50 $\pm$ 0.50          | 41.80 $\pm$ 4.50          | 19.70 $\pm$ 0.50          | 45.50 $\pm$ 4.20          | 16.30 $\pm$ 0.60         
Midpoint Fixed (ms)       | 34400.00 $\pm$ 200.00     | 269.00 $\pm$ 1.00         | 94.50 $\pm$ 0.90          | 308.00 $\pm$ 5.00         | 183.00 $\pm$ 1.00         | 73.20 $\pm$ 1.30          | 196.00 $\pm$ 3.00         | 55.70 $\pm$ 0.50         
RK4 (ms)                  | 16900.00 $\pm$ 100.00     | 154.00 $\pm$ 3.00         | 34.80 $\pm$ 0.30          | 123.00 $\pm$ 2.00         | 89.40 $\pm$ 0.70          | 32.10 $\pm$ 0.40          | 93.70 $\pm$ 0.50          | 28.30 $\pm$ 0.40         
FD - L Convection (ms)    | 2130.00 $\pm$ 20.00       | 1.57 $\pm$ 0.07           | 1.51 $\pm$ 0.04           | 2.84 $\pm$ 0.04           | 5.80 $\pm$ 0.02           | 1.59 $\pm$ 0.11           | 8.20 $\pm$ 0.19           | 1.51 $\pm$ 0.01          
FD - NL Convection (ms)   | 2660.00 $\pm$ 20.00       | 2.04 $\pm$ 0.03           | 1.78 $\pm$ 0.01           | 2.88 $\pm$ 0.02           | 5.09 $\pm$ 0.03           | 1.53 $\pm$ 0.04           | 8.28 $\pm$ 0.18           | 1.40 $\pm$ 0.03          
FD - Poisson (ms)         | 5880.00 $\pm$ 100.00      | 2.95 $\pm$ 0.04           | 5.51 $\pm$ 0.06           | 6.57 $\pm$ 0.07           | 10.40 $\pm$ 0.30          | 2.57 $\pm$ 0.04           | 18.30 $\pm$ 0.10          | 2.54 $\pm$ 0.02          
FD - Laplace (ms)         | 628.00 $\pm$ 6.00         | 63.50 $\pm$ 0.50          | 103.00 $\pm$ 0.00         | 189.00 $\pm$ 1.00         | 204.00 $\pm$ 1.00         | 56.80 $\pm$ 0.80          | 355.00 $\pm$ 4.00         | 55.10 $\pm$ 0.30         
M-D (ms)                  | 14300.00 $\pm$ 100.00     | 34.10 $\pm$ 0.20          | 50.30 $\pm$ 0.20          | 57.40 $\pm$ 1.60          | 105.00 $\pm$ 0.00         | 62.30 $\pm$ 0.20          | 91.90 $\pm$ 0.10          | 90.70 $\pm$ 0.10         
Splines (ms)              | 1680.00 $\pm$ 40.00       | -                         | -                         | 18.10 $\pm$ 0.10          | 14.10 $\pm$ 0.10          | 17.70 $\pm$ 0.00          | 15.10 $\pm$ 0.00          | 27.70 $\pm$ 0.20         

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
## Python 3.12 results
### Performance Comparison (as of 2.1.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.00                      | 2.20                      | 0.31                      | 1.43                      | 1.45                      | 1.49                      | 1.54                     
Bellman Ford              | -                         | 3.42                      | 3.71                      | 1.06                      | 26.37                     | 1.59                      | 29.78                     | 1.69                     
Dijkstra                  | -                         | 2.34                      | 2.70                      | 1.14                      | 26.38                     | 1.70                      | 29.74                     | 1.83                     
Euler                     | -                         | 2.59                      | 3.05                      | 3.25                      | 26.02                     | 1.57                      | 29.70                     | 1.67                     
Midpoint Explicit         | -                         | 2.93                      | 3.44                      | 3.57                      | 26.28                     | 1.81                      | 29.93                     | 1.90                     
Midpoint Fixed            | -                         | 3.35                      | 3.82                      | 3.73                      | 26.39                     | 1.89                      | 29.93                     | 2.02                     
RK4                       | -                         | 3.49                      | 4.06                      | 3.75                      | 26.76                     | 2.28                      | 30.48                     | 2.36                     
FD - L Convection         | -                         | 2.35                      | 2.71                      | 2.50                      | 26.02                     | 1.49                      | 29.74                     | 1.63                     
FD - NL Convection        | -                         | 3.40                      | 3.59                      | 2.62                      | 25.98                     | 1.53                      | 29.67                     | 1.63                     
FD - Poisson              | -                         | 3.50                      | 3.83                      | 4.16                      | 26.14                     | 1.79                      | 29.76                     | 2.03                     
FD - Laplace              | -                         | 6.94                      | 7.77                      | 5.38                      | 26.41                     | 1.97                      | 29.98                     | 2.12                     
M-D                       | -                         | 5.90                      | 6.46                      | 6.20                      | 26.82                     | 2.59                      | 30.42                     | 2.77                     
Splines                   | -                         | -                         | -                         | 0.71                      | 26.23                     | 1.81                      | 29.92                     | 1.96                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 439.00 $\pm$ 7.00         | 2.73 $\pm$ 0.08           | 3.66 $\pm$ 0.01           | 9.50 $\pm$ 0.37           | 1.33 $\pm$ 0.01           | 1.28 $\pm$ 0.00           | 4.06 $\pm$ 0.02           | 10.00 $\pm$ 0.40         
Bellman Ford (ms)         | 2150.00 $\pm$ 40.00       | 4.59 $\pm$ 0.02           | 3.55 $\pm$ 0.09           | 4.06 $\pm$ 0.03           | 4.68 $\pm$ 0.02           | 3.25 $\pm$ 0.02           | 5.19 $\pm$ 0.14           | 4.17 $\pm$ 0.02          
Dijkstra (ms)             | 5850.00 $\pm$ 50.00       | 19.20 $\pm$ 0.10          | 16.60 $\pm$ 0.20          | 20.90 $\pm$ 0.40          | 37.80 $\pm$ 0.50          | 18.70 $\pm$ 0.20          | 50.70 $\pm$ 0.60          | 21.30 $\pm$ 0.20         
Euler (ms)                | 3840.00 $\pm$ 50.00       | 26.20 $\pm$ 0.40          | 26.20 $\pm$ 1.00          | 36.20 $\pm$ 0.40          | 22.30 $\pm$ 0.30          | 11.00 $\pm$ 0.40          | 24.00 $\pm$ 0.60          | 15.30 $\pm$ 0.40         
Midpoint Explicit (ms)    | 7800.00 $\pm$ 100.00      | 52.20 $\pm$ 0.30          | 51.80 $\pm$ 2.00          | 68.40 $\pm$ 1.50          | 39.90 $\pm$ 0.40          | 19.20 $\pm$ 0.40          | 44.00 $\pm$ 0.50          | 16.00 $\pm$ 0.40         
Midpoint Fixed (ms)       | 38400.00 $\pm$ 100.00     | 267.00 $\pm$ 1.00         | 92.90 $\pm$ 0.60          | 345.00 $\pm$ 102.00       | 183.00 $\pm$ 0.00         | 72.80 $\pm$ 0.80          | 196.00 $\pm$ 2.00         | 50.50 $\pm$ 0.30         
RK4 (ms)                  | 19300.00 $\pm$ 100.00     | 153.00 $\pm$ 2.00         | 36.00 $\pm$ 0.80          | 124.00 $\pm$ 2.00         | 89.80 $\pm$ 2.60          | 32.40 $\pm$ 0.40          | 94.30 $\pm$ 0.70          | 29.80 $\pm$ 0.30         
FD - L Convection (ms)    | 2370.00 $\pm$ 20.00       | 1.54 $\pm$ 0.03           | 1.62 $\pm$ 0.02           | 2.83 $\pm$ 0.01           | 5.80 $\pm$ 0.02           | 1.66 $\pm$ 0.05           | 8.26 $\pm$ 0.20           | 1.33 $\pm$ 0.05          
FD - NL Convection (ms)   | 3030.00 $\pm$ 90.00       | 1.85 $\pm$ 0.03           | 1.65 $\pm$ 0.03           | 2.90 $\pm$ 0.06           | 5.10 $\pm$ 0.02           | 1.51 $\pm$ 0.01           | 8.24 $\pm$ 0.24           | 1.38 $\pm$ 0.04          
FD - Poisson (ms)         | 6630.00 $\pm$ 130.00      | 3.03 $\pm$ 0.16           | 5.35 $\pm$ 0.07           | 6.63 $\pm$ 0.04           | 10.50 $\pm$ 0.00          | 2.62 $\pm$ 0.04           | 18.70 $\pm$ 0.10          | 2.57 $\pm$ 0.04          
FD - Laplace (ms)         | 651.00 $\pm$ 19.00        | 67.70 $\pm$ 0.50          | 106.00 $\pm$ 1.00         | 190.00 $\pm$ 1.00         | 205.00 $\pm$ 1.00         | 58.80 $\pm$ 2.40          | 348.00 $\pm$ 1.00         | 56.90 $\pm$ 1.90         
M-D (ms)                  | 16500.00 $\pm$ 300.00     | 35.20 $\pm$ 0.20          | 50.40 $\pm$ 0.20          | 57.00 $\pm$ 0.40          | 106.00 $\pm$ 0.00         | 62.40 $\pm$ 0.20          | 91.10 $\pm$ 0.10          | 90.70 $\pm$ 0.10         
Splines (ms)              | 1950.00 $\pm$ 40.00       | -                         | -                         | 17.80 $\pm$ 0.20          | 14.20 $\pm$ 0.10          | 17.80 $\pm$ 0.20          | 15.30 $\pm$ 0.00          | 27.90 $\pm$ 0.00         

![Python 3.12 compilation results](./version_specific_results/pypi_performance_312_compilation.svg)
![Python 3.12 execution results](./version_specific_results/pypi_performance_312_execution.svg)
## Python 3.13 results
### Performance Comparison (as of 2.1.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.01                      | 2.29                      | 0.28                      | 1.44                      | 1.49                      | 1.50                      | 1.54                     
Bellman Ford              | -                         | 3.36                      | 3.69                      | 0.97                      | 25.97                     | 1.52                      | 27.76                     | 1.64                     
Dijkstra                  | -                         | 2.37                      | 2.66                      | 1.02                      | 25.98                     | 1.64                      | 29.50                     | 1.84                     
Euler                     | -                         | 2.63                      | 2.99                      | 3.18                      | 25.03                     | 1.48                      | 27.46                     | 1.54                     
Midpoint Explicit         | -                         | 2.83                      | 3.17                      | 3.35                      | 25.61                     | 1.67                      | 28.03                     | 1.73                     
Midpoint Fixed            | -                         | 3.14                      | 3.51                      | 3.47                      | 25.50                     | 1.76                      | 28.09                     | 1.82                     
RK4                       | -                         | 3.51                      | 3.88                      | 3.59                      | 26.31                     | 2.17                      | 29.18                     | 2.24                     
FD - L Convection         | -                         | 2.26                      | 2.52                      | 2.42                      | 25.41                     | 1.47                      | 28.10                     | 1.54                     
FD - NL Convection        | -                         | 3.26                      | 3.42                      | 2.52                      | 25.40                     | 1.44                      | 28.14                     | 1.53                     
FD - Poisson              | -                         | 3.32                      | 3.52                      | 4.08                      | 25.53                     | 1.82                      | 28.13                     | 1.93                     
FD - Laplace              | -                         | 7.00                      | 7.52                      | 5.30                      | 25.74                     | 1.87                      | 28.34                     | 1.96                     
M-D                       | -                         | 5.80                      | 6.01                      | 5.80                      | 25.79                     | 2.42                      | 28.42                     | 2.51                     
Splines                   | -                         | -                         | -                         | 0.62                      | 25.82                     | 1.73                      | 27.87                     | 1.83                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 335.00 $\pm$ 7.00         | 6.90 $\pm$ 0.04           | 13.00 $\pm$ 0.00          | 19.20 $\pm$ 0.10          | 2.15 $\pm$ 0.02           | 2.26 $\pm$ 0.01           | 11.70 $\pm$ 0.10          | 15.30 $\pm$ 0.10         
Bellman Ford (ms)         | 2020.00 $\pm$ 60.00       | 4.63 $\pm$ 0.01           | 3.71 $\pm$ 0.06           | 4.62 $\pm$ 0.05           | 4.07 $\pm$ 0.19           | 3.24 $\pm$ 0.01           | 5.89 $\pm$ 0.01           | 3.56 $\pm$ 0.01          
Dijkstra (ms)             | 5180.00 $\pm$ 40.00       | 35.20 $\pm$ 0.40          | 29.40 $\pm$ 1.40          | 36.00 $\pm$ 0.70          | 53.80 $\pm$ 0.90          | 31.10 $\pm$ 1.40          | 61.00 $\pm$ 0.50          | 40.20 $\pm$ 0.60         
Euler (ms)                | 3530.00 $\pm$ 40.00       | 24.80 $\pm$ 0.70          | 24.80 $\pm$ 0.30          | 87.80 $\pm$ 3.70          | 21.40 $\pm$ 0.20          | 11.10 $\pm$ 0.20          | 23.80 $\pm$ 0.30          | 11.10 $\pm$ 0.20         
Midpoint Explicit (ms)    | 7150.00 $\pm$ 70.00       | 46.60 $\pm$ 0.30          | 46.50 $\pm$ 0.70          | 166.00 $\pm$ 1.00         | 39.00 $\pm$ 0.30          | 17.90 $\pm$ 0.60          | 41.20 $\pm$ 0.50          | 14.80 $\pm$ 0.40         
Midpoint Fixed (ms)       | 35200.00 $\pm$ 200.00     | 232.00 $\pm$ 3.00         | 82.40 $\pm$ 0.50          | 597.00 $\pm$ 9.00         | 172.00 $\pm$ 0.00         | 68.70 $\pm$ 0.50          | 183.00 $\pm$ 2.00         | 44.60 $\pm$ 1.40         
RK4 (ms)                  | 17500.00 $\pm$ 200.00     | 131.00 $\pm$ 2.00         | 35.20 $\pm$ 1.40          | 311.00 $\pm$ 5.00         | 80.80 $\pm$ 0.60          | 28.20 $\pm$ 0.90          | 85.60 $\pm$ 1.80          | 30.90 $\pm$ 0.30         
FD - L Convection (ms)    | 2240.00 $\pm$ 30.00       | 1.37 $\pm$ 0.01           | 1.46 $\pm$ 0.00           | 2.11 $\pm$ 0.20           | 6.32 $\pm$ 0.02           | 1.42 $\pm$ 0.01           | 8.51 $\pm$ 0.07           | 1.41 $\pm$ 0.00          
FD - NL Convection (ms)   | 2900.00 $\pm$ 70.00       | 1.40 $\pm$ 0.00           | 1.40 $\pm$ 0.00           | 2.49 $\pm$ 0.06           | 6.07 $\pm$ 0.04           | 1.39 $\pm$ 0.00           | 8.51 $\pm$ 0.06           | 1.42 $\pm$ 0.00          
FD - Poisson (ms)         | 6070.00 $\pm$ 110.00      | 3.10 $\pm$ 0.02           | 6.22 $\pm$ 0.02           | 6.78 $\pm$ 0.05           | 8.57 $\pm$ 0.03           | 2.72 $\pm$ 0.02           | 13.30 $\pm$ 0.10          | 2.70 $\pm$ 0.01          
FD - Laplace (ms)         | 559.00 $\pm$ 5.00         | 64.40 $\pm$ 0.70          | 229.00 $\pm$ 3.00         | 213.00 $\pm$ 2.00         | 203.00 $\pm$ 1.00         | 55.50 $\pm$ 0.50          | 398.00 $\pm$ 2.00         | 61.10 $\pm$ 0.80         
M-D (ms)                  | 15100.00 $\pm$ 200.00     | 25.00 $\pm$ 0.70          | 46.00 $\pm$ 0.20          | 53.60 $\pm$ 0.30          | 89.40 $\pm$ 0.00          | 56.10 $\pm$ 0.40          | 57.00 $\pm$ 0.60          | 54.40 $\pm$ 0.30         
Splines (ms)              | 1880.00 $\pm$ 10.00       | -                         | -                         | 18.20 $\pm$ 0.70          | 12.00 $\pm$ 0.10          | 17.10 $\pm$ 0.20          | 13.40 $\pm$ 0.20          | 26.70 $\pm$ 0.10         

![Python 3.13 compilation results](./version_specific_results/pypi_performance_313_compilation.svg)
![Python 3.13 execution results](./version_specific_results/pypi_performance_313_execution.svg)
## Python 3.14 results
### Performance Comparison (as of 2.1.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.10                      | 2.37                      | 0.31                      | 1.47                      | 1.48                      | 1.51                      | 1.61                     
Bellman Ford              | -                         | 3.41                      | 3.72                      | 0.98                      | 26.69                     | 1.65                      | 30.18                     | 1.74                     
Dijkstra                  | -                         | 2.34                      | 2.74                      | 1.11                      | 26.98                     | 1.73                      | 30.16                     | 1.87                     
Euler                     | -                         | 2.64                      | 3.05                      | 3.18                      | 26.30                     | 1.60                      | 29.98                     | 1.71                     
Midpoint Explicit         | -                         | 2.95                      | 3.45                      | 3.54                      | 26.57                     | 1.84                      | 30.42                     | 1.93                     
Midpoint Fixed            | -                         | 3.43                      | 3.80                      | 3.70                      | 26.84                     | 1.93                      | 30.51                     | 2.08                     
RK4                       | -                         | 3.55                      | 3.99                      | 3.64                      | 26.85                     | 2.33                      | 30.66                     | 2.38                     
FD - L Convection         | -                         | 2.38                      | 2.69                      | 2.46                      | 26.29                     | 1.55                      | 29.90                     | 1.67                     
FD - NL Convection        | -                         | 3.59                      | 3.66                      | 2.62                      | 26.22                     | 1.56                      | 30.05                     | 1.69                     
FD - Poisson              | -                         | 3.52                      | 3.76                      | 4.15                      | 26.51                     | 1.85                      | 30.26                     | 2.08                     
FD - Laplace              | -                         | 7.16                      | 7.87                      | 5.35                      | 26.74                     | 2.04                      | 30.38                     | 2.18                     
M-D                       | -                         | 5.95                      | 6.47                      | 6.16                      | 27.00                     | 2.60                      | 30.86                     | 2.77                     
Splines                   | -                         | -                         | -                         | 0.71                      | 26.45                     | 1.86                      | 30.20                     | 2.00                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 466.00 $\pm$ 6.00         | 2.71 $\pm$ 0.03           | 3.67 $\pm$ 0.01           | 9.32 $\pm$ 0.48           | 1.23 $\pm$ 0.00           | 1.28 $\pm$ 0.00           | 3.78 $\pm$ 0.10           | 10.50 $\pm$ 0.10         
Bellman Ford (ms)         | 2060.00 $\pm$ 40.00       | 4.52 $\pm$ 0.01           | 3.59 $\pm$ 0.09           | 4.06 $\pm$ 0.03           | 4.06 $\pm$ 0.02           | 3.27 $\pm$ 0.02           | 5.16 $\pm$ 0.03           | 4.17 $\pm$ 0.01          
Dijkstra (ms)             | 5070.00 $\pm$ 60.00       | 18.90 $\pm$ 0.20          | 16.70 $\pm$ 0.30          | 21.70 $\pm$ 0.50          | 44.70 $\pm$ 0.70          | 18.30 $\pm$ 0.40          | 47.20 $\pm$ 0.30          | 21.80 $\pm$ 0.50         
Euler (ms)                | 3800.00 $\pm$ 50.00       | 25.50 $\pm$ 0.30          | 25.70 $\pm$ 0.40          | 36.30 $\pm$ 0.60          | 24.00 $\pm$ 4.10          | 10.90 $\pm$ 0.30          | 24.30 $\pm$ 0.50          | 15.00 $\pm$ 0.40         
Midpoint Explicit (ms)    | 7880.00 $\pm$ 400.00      | 52.30 $\pm$ 0.60          | 51.00 $\pm$ 0.60          | 68.30 $\pm$ 0.60          | 40.10 $\pm$ 0.40          | 19.00 $\pm$ 0.30          | 43.90 $\pm$ 0.50          | 16.00 $\pm$ 0.50         
Midpoint Fixed (ms)       | 38500.00 $\pm$ 200.00     | 267.00 $\pm$ 1.00         | 93.10 $\pm$ 0.90          | 310.00 $\pm$ 2.00         | 184.00 $\pm$ 1.00         | 72.90 $\pm$ 0.40          | 198.00 $\pm$ 5.00         | 51.50 $\pm$ 0.60         
RK4 (ms)                  | 19600.00 $\pm$ 200.00     | 158.00 $\pm$ 3.00         | 35.80 $\pm$ 0.60          | 132.00 $\pm$ 1.00         | 90.90 $\pm$ 0.40          | 31.70 $\pm$ 0.40          | 94.10 $\pm$ 0.90          | 27.90 $\pm$ 0.20         
FD - L Convection (ms)    | 2640.00 $\pm$ 20.00       | 1.66 $\pm$ 0.03           | 1.63 $\pm$ 0.03           | 2.85 $\pm$ 0.04           | 6.08 $\pm$ 0.05           | 1.53 $\pm$ 0.00           | 8.21 $\pm$ 0.27           | 1.35 $\pm$ 0.06          
FD - NL Convection (ms)   | 3300.00 $\pm$ 40.00       | 2.00 $\pm$ 0.02           | 1.67 $\pm$ 0.04           | 2.89 $\pm$ 0.06           | 5.11 $\pm$ 0.02           | 1.54 $\pm$ 0.05           | 8.23 $\pm$ 0.22           | 1.39 $\pm$ 0.02          
FD - Poisson (ms)         | 6760.00 $\pm$ 90.00       | 2.96 $\pm$ 0.07           | 5.51 $\pm$ 0.03           | 6.61 $\pm$ 0.05           | 10.60 $\pm$ 0.00          | 2.61 $\pm$ 0.02           | 18.80 $\pm$ 0.00          | 2.53 $\pm$ 0.02          
FD - Laplace (ms)         | 639.00 $\pm$ 14.00        | 63.80 $\pm$ 0.40          | 104.00 $\pm$ 0.00         | 191.00 $\pm$ 1.00         | 206.00 $\pm$ 1.00         | 59.00 $\pm$ 2.40          | 350.00 $\pm$ 1.00         | 55.70 $\pm$ 0.50         
M-D (ms)                  | 16300.00 $\pm$ 200.00     | 34.50 $\pm$ 0.20          | 50.00 $\pm$ 0.10          | 56.90 $\pm$ 0.10          | 106.00 $\pm$ 0.00         | 62.40 $\pm$ 0.20          | 91.40 $\pm$ 0.10          | 90.60 $\pm$ 0.10         
Splines (ms)              | 1970.00 $\pm$ 30.00       | -                         | -                         | 16.50 $\pm$ 0.10          | 14.10 $\pm$ 0.00          | 17.70 $\pm$ 0.00          | 15.30 $\pm$ 0.10          | 27.80 $\pm$ 0.10         

![Python 3.14 compilation results](./version_specific_results/pypi_performance_314_compilation.svg)
![Python 3.14 execution results](./version_specific_results/pypi_performance_314_execution.svg)
