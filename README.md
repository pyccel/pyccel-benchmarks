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
### Performance Comparison (as of Tue Apr  7 17:00:21 UTC 2026)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.07                      | 2.23                      | 0.31                      | 1.47                      | 1.52                      | 1.54                      | 1.63                     
Bellman Ford              | -                         | 3.60                      | 3.85                      | 1.13                      | 1.70                      | 1.68                      | 1.69                      | 1.77                     
Dijkstra                  | -                         | 2.57                      | 2.88                      | 1.20                      | 1.82                      | 1.80                      | 1.82                      | 1.93                     
Euler                     | -                         | 2.90                      | 3.25                      | 3.42                      | 1.69                      | 1.76                      | 1.74                      | 1.78                     
Midpoint Explicit         | -                         | 3.15                      | 3.64                      | 3.79                      | 1.90                      | 1.91                      | 1.92                      | 2.08                     
Midpoint Fixed            | -                         | 3.58                      | 3.99                      | 3.81                      | 1.98                      | 1.96                      | 1.96                      | 2.04                     
RK4                       | -                         | 3.69                      | 4.20                      | 3.92                      | 2.35                      | 2.37                      | 2.32                      | 2.46                     
FD - L Convection         | -                         | 2.49                      | 2.83                      | 2.62                      | 1.62                      | 1.63                      | 1.62                      | 1.72                     
FD - NL Convection        | -                         | 3.62                      | 3.82                      | 2.76                      | 1.67                      | 1.63                      | 1.65                      | 1.70                     
FD - Poisson              | -                         | 3.70                      | 3.95                      | 4.30                      | 2.30                      | 1.93                      | 2.76                      | 2.16                     
FD - Laplace              | -                         | 7.56                      | 8.46                      | 5.68                      | 2.14                      | 2.18                      | 2.04                      | 2.27                     
M-D                       | -                         | 6.27                      | 6.70                      | 6.54                      | 2.97                      | 2.74                      | 3.53                      | 2.91                     
Splines                   | -                         | -                         | -                         | 0.77                      | 2.38                      | 1.98                      | 2.84                      | 2.07                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 438.00                    | 2.70                      | 3.67                      | 8.59                      | 1.33                      | 1.32                      | 4.06                      | 9.33                     
Bellman Ford (ms)         | 1990.00                   | 4.60                      | 3.69                      | 4.06                      | 3.29                      | 3.23                      | 5.34                      | 4.20                     
Dijkstra (ms)             | 5750.00                   | 17.30                     | 15.10                     | 19.60                     | 29.40                     | 16.50                     | 29.50                     | 20.70                    
Euler (ms)                | 3770.00                   | 26.10                     | 25.50                     | 36.70                     | 20.50                     | 11.10                     | 25.00                     | 15.60                    
Midpoint Explicit (ms)    | 7590.00                   | 52.60                     | 51.80                     | 68.10                     | 41.50                     | 19.90                     | 42.30                     | 15.70                    
Midpoint Fixed (ms)       | 37600.00                  | 269.00                    | 92.70                     | 311.00                    | 180.00                    | 73.10                     | 201.00                    | 55.50                    
RK4 (ms)                  | 18800.00                  | 152.00                    | 35.40                     | 126.00                    | 85.80                     | 32.70                     | 91.90                     | 27.70                    
FD - L Convection (ms)    | 2340.00                   | 1.44                      | 1.60                      | 2.83                      | 4.28                      | 1.52                      | 4.51                      | 1.36                     
FD - NL Convection (ms)   | 2940.00                   | 1.84                      | 1.70                      | 2.90                      | 4.69                      | 1.62                      | 4.04                      | 1.50                     
FD - Poisson (ms)         | 6410.00                   | 2.90                      | 5.51                      | 6.83                      | 3.74                      | 2.58                      | 6.46                      | 2.51                     
FD - Laplace (ms)         | 642.00                    | 64.50                     | 106.00                    | 190.00                    | 151.00                    | 57.40                     | 193.00                    | 55.20                    
M-D (ms)                  | 8570.00                   | 36.10                     | 50.30                     | 56.90                     | 99.60                     | 62.30                     | 92.20                     | 90.40                    
Splines (ms)              | 1780.00                   | -                         | -                         | 18.30                     | 13.40                     | 17.70                     | 15.10                     | 28.10                    

![Development compilation results](./version_specific_results/devel_performance_312_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_312_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 2.2.3)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.13                      | 2.13                      | 0.34                      | 1.44                      | 1.45                      | 1.47                      | 1.53                     
Bellman Ford              | -                         | 3.46                      | 3.74                      | 1.02                      | 1.61                      | 1.60                      | 1.64                      | 1.70                     
Dijkstra                  | -                         | 2.41                      | 2.71                      | 1.17                      | 1.70                      | 1.71                      | 1.74                      | 1.85                     
Euler                     | -                         | 2.67                      | 3.08                      | 3.39                      | 1.59                      | 1.57                      | 1.62                      | 1.69                     
Midpoint Explicit         | -                         | 3.01                      | 3.48                      | 3.79                      | 1.81                      | 1.80                      | 1.84                      | 1.91                     
Midpoint Fixed            | -                         | 3.42                      | 3.87                      | 3.95                      | 1.88                      | 1.86                      | 1.89                      | 1.97                     
RK4                       | -                         | 3.53                      | 4.03                      | 3.97                      | 2.27                      | 2.28                      | 2.24                      | 2.37                     
FD - L Convection         | -                         | 2.33                      | 2.67                      | 2.62                      | 1.54                      | 1.54                      | 1.56                      | 1.64                     
FD - NL Convection        | -                         | 3.28                      | 3.65                      | 2.75                      | 1.55                      | 1.54                      | 1.56                      | 1.64                     
FD - Poisson              | -                         | 3.50                      | 3.84                      | 4.41                      | 2.18                      | 1.83                      | 2.67                      | 2.07                     
FD - Laplace              | -                         | 6.99                      | 7.78                      | 5.67                      | 1.92                      | 1.98                      | 1.89                      | 2.11                     
M-D                       | -                         | 6.11                      | 6.43                      | 6.47                      | 2.90                      | 2.67                      | 3.44                      | 2.84                     
Splines                   | -                         | -                         | -                         | 0.65                      | 2.20                      | 1.84                      | 2.73                      | 2.01                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 306.00 $\pm$ 5.00         | 3.05 $\pm$ 0.14           | 3.68 $\pm$ 0.05           | 9.42 $\pm$ 0.44           | 1.23 $\pm$ 0.01           | 1.32 $\pm$ 0.00           | 4.37 $\pm$ 0.01           | 7.80 $\pm$ 0.25          
Bellman Ford (ms)         | 1910.00 $\pm$ 20.00       | 4.53 $\pm$ 0.01           | 3.62 $\pm$ 0.07           | 4.06 $\pm$ 0.02           | 3.29 $\pm$ 0.02           | 3.28 $\pm$ 0.03           | 5.39 $\pm$ 0.02           | 3.83 $\pm$ 0.02          
Dijkstra (ms)             | 5230.00 $\pm$ 50.00       | 17.90 $\pm$ 0.20          | 15.60 $\pm$ 0.10          | 18.50 $\pm$ 0.60          | 35.70 $\pm$ 0.40          | 18.60 $\pm$ 0.30          | 40.20 $\pm$ 0.30          | 20.70 $\pm$ 0.30         
Euler (ms)                | 3440.00 $\pm$ 30.00       | 25.60 $\pm$ 0.50          | 27.30 $\pm$ 2.90          | 35.40 $\pm$ 0.50          | 22.20 $\pm$ 4.40          | 10.90 $\pm$ 0.40          | 23.80 $\pm$ 0.40          | 15.30 $\pm$ 0.90         
Midpoint Explicit (ms)    | 7020.00 $\pm$ 50.00       | 51.70 $\pm$ 0.50          | 51.40 $\pm$ 1.10          | 67.40 $\pm$ 1.40          | 41.10 $\pm$ 0.50          | 19.20 $\pm$ 0.50          | 42.30 $\pm$ 0.40          | 16.00 $\pm$ 0.60         
Midpoint Fixed (ms)       | 35200.00 $\pm$ 200.00     | 268.00 $\pm$ 1.00         | 94.00 $\pm$ 0.60          | 325.00 $\pm$ 50.00        | 181.00 $\pm$ 1.00         | 73.10 $\pm$ 1.30          | 202.00 $\pm$ 1.00         | 51.60 $\pm$ 0.70         
RK4 (ms)                  | 17200.00 $\pm$ 200.00     | 155.00 $\pm$ 3.00         | 35.40 $\pm$ 0.80          | 124.00 $\pm$ 1.00         | 85.70 $\pm$ 0.50          | 31.90 $\pm$ 0.50          | 94.20 $\pm$ 0.70          | 28.00 $\pm$ 1.60         
FD - L Convection (ms)    | 2310.00 $\pm$ 20.00       | 1.67 $\pm$ 0.04           | 1.46 $\pm$ 0.06           | 2.84 $\pm$ 0.03           | 4.28 $\pm$ 0.02           | 1.63 $\pm$ 0.06           | 4.52 $\pm$ 0.01           | 1.32 $\pm$ 0.04          
FD - NL Convection (ms)   | 2840.00 $\pm$ 30.00       | 1.93 $\pm$ 0.07           | 1.80 $\pm$ 0.04           | 2.90 $\pm$ 0.02           | 4.71 $\pm$ 0.05           | 1.67 $\pm$ 0.12           | 4.06 $\pm$ 0.05           | 1.39 $\pm$ 0.03          
FD - Poisson (ms)         | 6470.00 $\pm$ 130.00      | 2.91 $\pm$ 0.04           | 5.46 $\pm$ 0.07           | 6.63 $\pm$ 0.07           | 3.67 $\pm$ 0.02           | 2.60 $\pm$ 0.03           | 6.29 $\pm$ 0.06           | 2.55 $\pm$ 0.03          
FD - Laplace (ms)         | 627.00 $\pm$ 6.00         | 63.40 $\pm$ 0.40          | 103.00 $\pm$ 1.00         | 190.00 $\pm$ 1.00         | 151.00 $\pm$ 1.00         | 57.50 $\pm$ 0.90          | 193.00 $\pm$ 0.00         | 55.60 $\pm$ 0.50         
M-D (ms)                  | 15100.00 $\pm$ 100.00     | 36.20 $\pm$ 0.90          | 50.50 $\pm$ 0.40          | 57.20 $\pm$ 0.50          | 106.00 $\pm$ 0.00         | 66.00 $\pm$ 11.50         | 89.30 $\pm$ 0.20          | 90.30 $\pm$ 0.20         
Splines (ms)              | 1930.00 $\pm$ 40.00       | -                         | -                         | 17.60 $\pm$ 0.10          | 13.60 $\pm$ 0.10          | 17.60 $\pm$ 0.00          | 15.20 $\pm$ 0.00          | 27.60 $\pm$ 0.20         

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 2.2.3)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.17                      | 2.14                      | 0.29                      | 1.40                      | 1.42                      | 1.49                      | 1.56                     
Bellman Ford              | -                         | 3.39                      | 3.73                      | 1.04                      | 1.61                      | 1.68                      | 1.64                      | 1.74                     
Dijkstra                  | -                         | 2.34                      | 2.66                      | 1.18                      | 1.71                      | 1.75                      | 1.74                      | 1.85                     
Euler                     | -                         | 2.63                      | 3.05                      | 3.39                      | 1.56                      | 1.56                      | 1.63                      | 1.72                     
Midpoint Explicit         | -                         | 2.90                      | 3.43                      | 3.77                      | 1.80                      | 1.78                      | 1.81                      | 1.88                     
Midpoint Fixed            | -                         | 3.26                      | 3.72                      | 3.88                      | 1.85                      | 1.83                      | 1.88                      | 1.96                     
RK4                       | -                         | 3.44                      | 3.90                      | 3.92                      | 2.21                      | 2.25                      | 2.18                      | 2.32                     
FD - L Convection         | -                         | 2.27                      | 2.60                      | 2.53                      | 1.50                      | 1.52                      | 1.54                      | 1.63                     
FD - NL Convection        | -                         | 3.21                      | 3.57                      | 2.65                      | 1.52                      | 1.52                      | 1.54                      | 1.64                     
FD - Poisson              | -                         | 3.38                      | 3.71                      | 4.17                      | 2.15                      | 1.81                      | 2.65                      | 2.06                     
FD - Laplace              | -                         | 7.09                      | 7.82                      | 5.41                      | 1.90                      | 2.02                      | 1.93                      | 2.17                     
M-D                       | -                         | 5.88                      | 6.44                      | 6.42                      | 2.82                      | 2.55                      | 3.37                      | 2.75                     
Splines                   | -                         | -                         | -                         | 0.67                      | 2.20                      | 1.84                      | 2.73                      | 1.99                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 476.00 $\pm$ 7.00         | 2.93 $\pm$ 0.02           | 3.69 $\pm$ 0.09           | 9.03 $\pm$ 0.50           | 1.23 $\pm$ 0.00           | 1.33 $\pm$ 0.00           | 4.07 $\pm$ 0.04           | 8.14 $\pm$ 0.30          
Bellman Ford (ms)         | 1780.00 $\pm$ 30.00       | 4.53 $\pm$ 0.04           | 3.67 $\pm$ 0.11           | 4.06 $\pm$ 0.02           | 3.31 $\pm$ 0.07           | 3.28 $\pm$ 0.02           | 5.38 $\pm$ 0.04           | 3.88 $\pm$ 0.19          
Dijkstra (ms)             | 4750.00 $\pm$ 40.00       | 18.70 $\pm$ 0.10          | 15.30 $\pm$ 0.10          | 18.80 $\pm$ 0.80          | 35.20 $\pm$ 1.30          | 17.40 $\pm$ 0.30          | 41.50 $\pm$ 0.50          | 19.50 $\pm$ 0.20         
Euler (ms)                | 3350.00 $\pm$ 30.00       | 25.60 $\pm$ 0.50          | 26.50 $\pm$ 0.70          | 35.60 $\pm$ 1.50          | 20.50 $\pm$ 0.40          | 11.00 $\pm$ 0.40          | 23.90 $\pm$ 0.50          | 15.10 $\pm$ 0.60         
Midpoint Explicit (ms)    | 6740.00 $\pm$ 40.00       | 52.20 $\pm$ 1.00          | 50.90 $\pm$ 0.50          | 66.50 $\pm$ 0.60          | 41.10 $\pm$ 0.50          | 19.10 $\pm$ 0.40          | 42.50 $\pm$ 0.40          | 16.30 $\pm$ 0.60         
Midpoint Fixed (ms)       | 33800.00 $\pm$ 400.00     | 268.00 $\pm$ 3.00         | 94.00 $\pm$ 0.50          | 308.00 $\pm$ 5.00         | 183.00 $\pm$ 9.00         | 73.40 $\pm$ 1.20          | 201.00 $\pm$ 1.00         | 54.50 $\pm$ 0.30         
RK4 (ms)                  | 16900.00 $\pm$ 100.00     | 155.00 $\pm$ 3.00         | 41.90 $\pm$ 19.90         | 127.00 $\pm$ 13.00        | 86.00 $\pm$ 1.00          | 32.00 $\pm$ 0.40          | 93.70 $\pm$ 0.40          | 28.00 $\pm$ 0.50         
FD - L Convection (ms)    | 2140.00 $\pm$ 30.00       | 1.45 $\pm$ 0.05           | 1.43 $\pm$ 0.02           | 2.84 $\pm$ 0.03           | 4.94 $\pm$ 0.29           | 1.66 $\pm$ 0.06           | 4.12 $\pm$ 0.20           | 1.37 $\pm$ 0.05          
FD - NL Convection (ms)   | 2700.00 $\pm$ 20.00       | 1.88 $\pm$ 0.06           | 1.79 $\pm$ 0.03           | 2.90 $\pm$ 0.06           | 4.69 $\pm$ 0.01           | 1.57 $\pm$ 0.10           | 4.21 $\pm$ 0.19           | 1.54 $\pm$ 0.04          
FD - Poisson (ms)         | 5770.00 $\pm$ 40.00       | 2.98 $\pm$ 0.03           | 5.57 $\pm$ 0.03           | 6.63 $\pm$ 0.05           | 3.75 $\pm$ 0.03           | 2.62 $\pm$ 0.03           | 6.37 $\pm$ 0.04           | 2.61 $\pm$ 0.11          
FD - Laplace (ms)         | 692.00 $\pm$ 3.00         | 66.10 $\pm$ 2.10          | 104.00 $\pm$ 1.00         | 189.00 $\pm$ 1.00         | 151.00 $\pm$ 1.00         | 59.20 $\pm$ 2.20          | 193.00 $\pm$ 0.00         | 56.00 $\pm$ 1.50         
M-D (ms)                  | 8050.00 $\pm$ 70.00       | 34.30 $\pm$ 0.20          | 50.80 $\pm$ 1.30          | 57.50 $\pm$ 2.00          | 107.00 $\pm$ 0.00         | 62.30 $\pm$ 0.20          | 88.80 $\pm$ 0.20          | 90.70 $\pm$ 0.20         
Splines (ms)              | 1740.00 $\pm$ 120.00      | -                         | -                         | 17.80 $\pm$ 0.10          | 13.60 $\pm$ 0.40          | 17.80 $\pm$ 0.00          | 15.30 $\pm$ 0.10          | 27.90 $\pm$ 0.40         

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
## Python 3.12 results
### Performance Comparison (as of 2.2.3)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.99                      | 2.16                      | 0.31                      | 1.44                      | 1.47                      | 1.48                      | 1.56                     
Bellman Ford              | -                         | 3.44                      | 3.69                      | 1.08                      | 1.62                      | 1.63                      | 1.66                      | 1.77                     
Dijkstra                  | -                         | 2.33                      | 2.67                      | 1.14                      | 1.71                      | 1.72                      | 1.73                      | 1.86                     
Euler                     | -                         | 2.62                      | 3.03                      | 3.22                      | 1.60                      | 1.59                      | 1.63                      | 1.70                     
Midpoint Explicit         | -                         | 3.02                      | 3.48                      | 3.57                      | 1.83                      | 1.83                      | 1.86                      | 1.97                     
Midpoint Fixed            | -                         | 3.33                      | 3.76                      | 3.67                      | 1.93                      | 1.91                      | 1.94                      | 2.04                     
RK4                       | -                         | 3.46                      | 3.95                      | 3.69                      | 2.27                      | 2.30                      | 2.25                      | 2.39                     
FD - L Convection         | -                         | 2.32                      | 2.72                      | 2.49                      | 1.55                      | 1.55                      | 1.58                      | 1.66                     
FD - NL Convection        | -                         | 3.36                      | 3.60                      | 2.63                      | 1.56                      | 1.57                      | 1.58                      | 1.66                     
FD - Poisson              | -                         | 3.43                      | 3.80                      | 4.09                      | 2.21                      | 1.84                      | 2.66                      | 2.08                     
FD - Laplace              | -                         | 6.89                      | 7.68                      | 5.34                      | 1.96                      | 2.00                      | 1.92                      | 2.13                     
M-D                       | -                         | 5.88                      | 6.35                      | 6.17                      | 2.86                      | 2.62                      | 3.40                      | 2.78                     
Splines                   | -                         | -                         | -                         | 0.74                      | 2.21                      | 1.85                      | 2.74                      | 2.01                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 485.00 $\pm$ 5.00         | 2.71 $\pm$ 0.01           | 3.67 $\pm$ 0.02           | 9.02 $\pm$ 0.52           | 1.33 $\pm$ 0.00           | 1.28 $\pm$ 0.00           | 4.06 $\pm$ 0.01           | 9.58 $\pm$ 0.18          
Bellman Ford (ms)         | 2020.00 $\pm$ 50.00       | 4.64 $\pm$ 0.16           | 3.56 $\pm$ 0.10           | 4.08 $\pm$ 0.03           | 3.28 $\pm$ 0.02           | 3.25 $\pm$ 0.04           | 5.38 $\pm$ 0.03           | 4.22 $\pm$ 0.12          
Dijkstra (ms)             | 5600.00 $\pm$ 50.00       | 16.80 $\pm$ 0.10          | 14.50 $\pm$ 0.20          | 18.50 $\pm$ 1.00          | 35.30 $\pm$ 0.30          | 16.00 $\pm$ 0.10          | 38.90 $\pm$ 0.30          | 19.30 $\pm$ 0.20         
Euler (ms)                | 3760.00 $\pm$ 40.00       | 26.00 $\pm$ 0.50          | 25.40 $\pm$ 0.50          | 36.00 $\pm$ 0.40          | 21.00 $\pm$ 0.40          | 10.90 $\pm$ 0.50          | 25.30 $\pm$ 3.60          | 14.60 $\pm$ 0.40         
Midpoint Explicit (ms)    | 7680.00 $\pm$ 60.00       | 52.50 $\pm$ 0.20          | 51.00 $\pm$ 0.50          | 67.90 $\pm$ 0.70          | 42.20 $\pm$ 3.40          | 19.30 $\pm$ 0.40          | 42.70 $\pm$ 1.10          | 16.00 $\pm$ 0.50         
Midpoint Fixed (ms)       | 37700.00 $\pm$ 200.00     | 267.00 $\pm$ 2.00         | 93.10 $\pm$ 1.70          | 310.00 $\pm$ 2.00         | 180.00 $\pm$ 1.00         | 72.60 $\pm$ 0.60          | 201.00 $\pm$ 1.00         | 50.50 $\pm$ 0.50         
RK4 (ms)                  | 19100.00 $\pm$ 300.00     | 155.00 $\pm$ 7.00         | 35.60 $\pm$ 0.50          | 125.00 $\pm$ 2.00         | 87.30 $\pm$ 4.50          | 31.60 $\pm$ 0.40          | 93.40 $\pm$ 0.50          | 27.80 $\pm$ 0.50         
FD - L Convection (ms)    | 2300.00 $\pm$ 30.00       | 1.52 $\pm$ 0.04           | 1.63 $\pm$ 0.03           | 2.84 $\pm$ 0.03           | 4.44 $\pm$ 0.33           | 1.56 $\pm$ 0.08           | 4.32 $\pm$ 0.12           | 1.54 $\pm$ 0.03          
FD - NL Convection (ms)   | 2940.00 $\pm$ 30.00       | 2.00 $\pm$ 0.01           | 1.65 $\pm$ 0.03           | 2.93 $\pm$ 0.09           | 4.69 $\pm$ 0.00           | 1.64 $\pm$ 0.05           | 4.29 $\pm$ 0.16           | 1.53 $\pm$ 0.03          
FD - Poisson (ms)         | 6490.00 $\pm$ 80.00       | 3.04 $\pm$ 0.18           | 5.55 $\pm$ 0.04           | 6.63 $\pm$ 0.06           | 3.75 $\pm$ 0.03           | 2.60 $\pm$ 0.02           | 6.48 $\pm$ 0.20           | 2.55 $\pm$ 0.03          
FD - Laplace (ms)         | 694.00 $\pm$ 3.00         | 64.50 $\pm$ 0.40          | 106.00 $\pm$ 2.00         | 191.00 $\pm$ 1.00         | 151.00 $\pm$ 0.00         | 61.10 $\pm$ 0.50          | 197.00 $\pm$ 0.00         | 56.40 $\pm$ 1.40         
M-D (ms)                  | 8780.00 $\pm$ 280.00      | 35.40 $\pm$ 0.40          | 50.40 $\pm$ 0.20          | 56.90 $\pm$ 0.10          | 106.00 $\pm$ 0.00         | 62.30 $\pm$ 0.30          | 88.80 $\pm$ 0.10          | 90.20 $\pm$ 0.10         
Splines (ms)              | 1820.00 $\pm$ 30.00       | -                         | -                         | 18.30 $\pm$ 0.80          | 13.60 $\pm$ 0.10          | 17.70 $\pm$ 0.00          | 15.20 $\pm$ 0.30          | 27.70 $\pm$ 0.00         

![Python 3.12 compilation results](./version_specific_results/pypi_performance_312_compilation.svg)
![Python 3.12 execution results](./version_specific_results/pypi_performance_312_execution.svg)
## Python 3.13 results
### Performance Comparison (as of 2.2.3)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.04                      | 2.10                      | 0.29                      | 1.45                      | 1.46                      | 1.49                      | 1.55                     
Bellman Ford              | -                         | 3.36                      | 3.65                      | 1.09                      | 1.62                      | 1.61                      | 1.65                      | 1.71                     
Dijkstra                  | -                         | 2.33                      | 2.65                      | 1.14                      | 1.70                      | 1.70                      | 1.73                      | 1.86                     
Euler                     | -                         | 2.61                      | 3.06                      | 3.18                      | 1.62                      | 1.59                      | 1.63                      | 1.70                     
Midpoint Explicit         | -                         | 2.99                      | 3.44                      | 3.55                      | 1.81                      | 1.81                      | 1.85                      | 1.91                     
Midpoint Fixed            | -                         | 3.30                      | 3.75                      | 3.67                      | 1.91                      | 1.91                      | 1.93                      | 2.00                     
RK4                       | -                         | 3.44                      | 3.97                      | 3.68                      | 2.27                      | 2.28                      | 2.22                      | 2.37                     
FD - L Convection         | -                         | 2.29                      | 2.66                      | 2.53                      | 1.54                      | 1.55                      | 1.57                      | 1.66                     
FD - NL Convection        | -                         | 3.35                      | 3.60                      | 2.63                      | 1.56                      | 1.55                      | 1.59                      | 1.66                     
FD - Poisson              | -                         | 3.42                      | 3.76                      | 4.03                      | 2.17                      | 1.84                      | 2.67                      | 2.08                     
FD - Laplace              | -                         | 6.84                      | 7.69                      | 5.24                      | 1.91                      | 1.97                      | 1.89                      | 2.11                     
M-D                       | -                         | 5.81                      | 6.29                      | 6.11                      | 2.85                      | 2.63                      | 3.39                      | 2.78                     
Splines                   | -                         | -                         | -                         | 0.74                      | 2.24                      | 1.88                      | 2.73                      | 2.02                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 496.00 $\pm$ 7.00         | 2.72 $\pm$ 0.03           | 3.68 $\pm$ 0.05           | 9.19 $\pm$ 0.51           | 1.33 $\pm$ 0.01           | 1.32 $\pm$ 0.00           | 4.06 $\pm$ 0.01           | 10.10 $\pm$ 0.40         
Bellman Ford (ms)         | 2250.00 $\pm$ 20.00       | 4.60 $\pm$ 0.02           | 3.51 $\pm$ 0.04           | 4.08 $\pm$ 0.03           | 3.28 $\pm$ 0.02           | 3.25 $\pm$ 0.03           | 5.51 $\pm$ 0.04           | 4.17 $\pm$ 0.01          
Dijkstra (ms)             | 5310.00 $\pm$ 40.00       | 16.80 $\pm$ 0.20          | 14.50 $\pm$ 0.10          | 18.70 $\pm$ 0.50          | 35.10 $\pm$ 0.30          | 17.40 $\pm$ 0.30          | 39.00 $\pm$ 0.30          | 18.90 $\pm$ 0.30         
Euler (ms)                | 3910.00 $\pm$ 40.00       | 26.50 $\pm$ 2.20          | 25.90 $\pm$ 0.70          | 36.20 $\pm$ 0.70          | 21.20 $\pm$ 0.40          | 11.20 $\pm$ 0.40          | 24.10 $\pm$ 0.40          | 14.80 $\pm$ 0.40         
Midpoint Explicit (ms)    | 7950.00 $\pm$ 80.00       | 52.80 $\pm$ 0.60          | 51.10 $\pm$ 1.40          | 68.40 $\pm$ 1.20          | 41.30 $\pm$ 0.50          | 18.90 $\pm$ 0.40          | 42.20 $\pm$ 0.40          | 17.20 $\pm$ 1.40         
Midpoint Fixed (ms)       | 39400.00 $\pm$ 200.00     | 268.00 $\pm$ 2.00         | 92.80 $\pm$ 0.50          | 310.00 $\pm$ 2.00         | 181.00 $\pm$ 1.00         | 73.10 $\pm$ 1.40          | 201.00 $\pm$ 1.00         | 50.80 $\pm$ 0.80         
RK4 (ms)                  | 19700.00 $\pm$ 200.00     | 152.00 $\pm$ 1.00         | 35.50 $\pm$ 0.40          | 128.00 $\pm$ 11.00        | 86.40 $\pm$ 0.70          | 31.70 $\pm$ 0.40          | 94.00 $\pm$ 2.60          | 27.80 $\pm$ 0.60         
FD - L Convection (ms)    | 2750.00 $\pm$ 40.00       | 1.58 $\pm$ 0.07           | 1.62 $\pm$ 0.03           | 2.83 $\pm$ 0.01           | 4.51 $\pm$ 0.37           | 1.69 $\pm$ 0.07           | 4.53 $\pm$ 0.01           | 1.30 $\pm$ 0.02          
FD - NL Convection (ms)   | 3470.00 $\pm$ 50.00       | 1.86 $\pm$ 0.03           | 1.66 $\pm$ 0.04           | 2.89 $\pm$ 0.02           | 4.70 $\pm$ 0.01           | 1.55 $\pm$ 0.06           | 4.50 $\pm$ 0.04           | 1.54 $\pm$ 0.03          
FD - Poisson (ms)         | 6890.00 $\pm$ 80.00       | 2.96 $\pm$ 0.05           | 5.55 $\pm$ 0.10           | 6.59 $\pm$ 0.04           | 3.75 $\pm$ 0.03           | 2.60 $\pm$ 0.03           | 6.46 $\pm$ 0.03           | 2.52 $\pm$ 0.02          
FD - Laplace (ms)         | 697.00 $\pm$ 2.00         | 64.50 $\pm$ 0.40          | 105.00 $\pm$ 1.00         | 189.00 $\pm$ 1.00         | 150.00 $\pm$ 0.00         | 57.20 $\pm$ 0.70          | 193.00 $\pm$ 0.00         | 55.70 $\pm$ 0.30         
M-D (ms)                  | 8970.00 $\pm$ 110.00      | 35.20 $\pm$ 0.20          | 50.40 $\pm$ 0.30          | 57.10 $\pm$ 0.80          | 106.00 $\pm$ 0.00         | 62.20 $\pm$ 0.30          | 89.20 $\pm$ 2.40          | 90.20 $\pm$ 0.10         
Splines (ms)              | 2020.00 $\pm$ 30.00       | -                         | -                         | 17.80 $\pm$ 0.10          | 13.40 $\pm$ 0.00          | 17.70 $\pm$ 0.00          | 15.20 $\pm$ 0.20          | 27.70 $\pm$ 0.00         

![Python 3.13 compilation results](./version_specific_results/pypi_performance_313_compilation.svg)
![Python 3.13 execution results](./version_specific_results/pypi_performance_313_execution.svg)
## Python 3.14 results
### Performance Comparison (as of 2.2.3)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.06                      | 2.17                      | 0.30                      | 1.47                      | 1.51                      | 1.51                      | 1.58                     
Bellman Ford              | -                         | 3.31                      | 3.70                      | 0.98                      | 1.65                      | 1.63                      | 1.68                      | 1.75                     
Dijkstra                  | -                         | 2.35                      | 2.74                      | 1.11                      | 1.74                      | 1.73                      | 1.78                      | 1.88                     
Euler                     | -                         | 2.61                      | 3.05                      | 3.20                      | 1.65                      | 1.60                      | 1.68                      | 1.74                     
Midpoint Explicit         | -                         | 2.96                      | 3.55                      | 3.53                      | 2.07                      | 2.06                      | 2.08                      | 2.14                     
Midpoint Fixed            | -                         | 3.28                      | 3.70                      | 3.69                      | 1.95                      | 1.93                      | 1.97                      | 2.05                     
RK4                       | -                         | 3.39                      | 3.93                      | 3.64                      | 2.30                      | 2.36                      | 2.29                      | 2.42                     
FD - L Convection         | -                         | 2.30                      | 2.67                      | 2.48                      | 1.56                      | 1.57                      | 1.60                      | 1.67                     
FD - NL Convection        | -                         | 3.33                      | 3.56                      | 2.59                      | 1.57                      | 1.56                      | 1.60                      | 1.67                     
FD - Poisson              | -                         | 3.41                      | 3.71                      | 4.11                      | 2.20                      | 1.85                      | 2.69                      | 2.10                     
FD - Laplace              | -                         | 6.89                      | 7.70                      | 5.31                      | 2.00                      | 2.04                      | 1.96                      | 2.17                     
M-D                       | -                         | 5.79                      | 6.28                      | 6.16                      | 2.87                      | 2.63                      | 3.41                      | 2.79                     
Splines                   | -                         | -                         | -                         | 0.73                      | 2.25                      | 1.87                      | 2.76                      | 2.03                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 509.00 $\pm$ 3.00         | 2.70 $\pm$ 0.00           | 3.67 $\pm$ 0.01           | 9.00 $\pm$ 0.50           | 1.23 $\pm$ 0.00           | 1.28 $\pm$ 0.00           | 4.06 $\pm$ 0.01           | 10.20 $\pm$ 0.30         
Bellman Ford (ms)         | 2120.00 $\pm$ 30.00       | 4.51 $\pm$ 0.01           | 3.61 $\pm$ 0.27           | 4.05 $\pm$ 0.02           | 3.28 $\pm$ 0.02           | 3.26 $\pm$ 0.02           | 5.38 $\pm$ 0.03           | 4.17 $\pm$ 0.02          
Dijkstra (ms)             | 5060.00 $\pm$ 60.00       | 17.70 $\pm$ 0.20          | 15.20 $\pm$ 0.20          | 19.20 $\pm$ 1.00          | 35.80 $\pm$ 0.80          | 16.70 $\pm$ 0.30          | 39.40 $\pm$ 0.20          | 19.90 $\pm$ 0.20         
Euler (ms)                | 3710.00 $\pm$ 30.00       | 25.70 $\pm$ 0.40          | 25.60 $\pm$ 0.20          | 35.80 $\pm$ 0.30          | 20.50 $\pm$ 0.40          | 10.90 $\pm$ 0.50          | 24.00 $\pm$ 0.40          | 15.30 $\pm$ 0.50         
Midpoint Explicit (ms)    | 7640.00 $\pm$ 60.00       | 52.80 $\pm$ 0.60          | 51.40 $\pm$ 2.00          | 68.30 $\pm$ 0.60          | 41.30 $\pm$ 0.40          | 20.10 $\pm$ 0.50          | 42.80 $\pm$ 0.40          | 16.90 $\pm$ 0.50         
Midpoint Fixed (ms)       | 37800.00 $\pm$ 500.00     | 267.00 $\pm$ 1.00         | 93.10 $\pm$ 2.70          | 315.00 $\pm$ 15.00        | 182.00 $\pm$ 1.00         | 72.70 $\pm$ 0.50          | 201.00 $\pm$ 1.00         | 50.80 $\pm$ 0.50         
RK4 (ms)                  | 18900.00 $\pm$ 200.00     | 156.00 $\pm$ 2.00         | 35.20 $\pm$ 0.40          | 132.00 $\pm$ 3.00         | 85.70 $\pm$ 0.70          | 31.40 $\pm$ 0.20          | 93.40 $\pm$ 0.70          | 28.30 $\pm$ 0.40         
FD - L Convection (ms)    | 2570.00 $\pm$ 30.00       | 1.68 $\pm$ 0.04           | 1.62 $\pm$ 0.03           | 2.85 $\pm$ 0.03           | 4.77 $\pm$ 0.41           | 1.67 $\pm$ 0.04           | 4.31 $\pm$ 0.10           | 1.33 $\pm$ 0.06          
FD - NL Convection (ms)   | 3260.00 $\pm$ 60.00       | 2.00 $\pm$ 0.02           | 1.65 $\pm$ 0.02           | 2.91 $\pm$ 0.07           | 4.70 $\pm$ 0.01           | 1.67 $\pm$ 0.05           | 4.33 $\pm$ 0.13           | 1.51 $\pm$ 0.01          
FD - Poisson (ms)         | 6970.00 $\pm$ 120.00      | 3.03 $\pm$ 0.20           | 5.54 $\pm$ 0.10           | 6.58 $\pm$ 0.05           | 3.75 $\pm$ 0.03           | 2.59 $\pm$ 0.03           | 6.33 $\pm$ 0.02           | 2.53 $\pm$ 0.03          
FD - Laplace (ms)         | 711.00 $\pm$ 3.00         | 66.70 $\pm$ 1.10          | 104.00 $\pm$ 1.00         | 189.00 $\pm$ 2.00         | 151.00 $\pm$ 0.00         | 60.70 $\pm$ 0.40          | 196.00 $\pm$ 0.00         | 55.20 $\pm$ 0.40         
M-D (ms)                  | 8950.00 $\pm$ 150.00      | 34.50 $\pm$ 0.30          | 50.20 $\pm$ 0.50          | 57.00 $\pm$ 0.20          | 107.00 $\pm$ 1.00         | 62.40 $\pm$ 0.10          | 88.80 $\pm$ 0.10          | 90.40 $\pm$ 0.30         
Splines (ms)              | 1920.00 $\pm$ 20.00       | -                         | -                         | 16.40 $\pm$ 0.10          | 13.60 $\pm$ 0.00          | 17.70 $\pm$ 0.10          | 15.10 $\pm$ 0.10          | 27.80 $\pm$ 0.10         

![Python 3.14 compilation results](./version_specific_results/pypi_performance_314_compilation.svg)
![Python 3.14 execution results](./version_specific_results/pypi_performance_314_execution.svg)
