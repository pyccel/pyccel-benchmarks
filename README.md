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
### Performance Comparison (as of Thu Feb 26 14:43:18 UTC 2026)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.03                      | 2.12                      | 0.31                      | 1.45                      | 1.46                      | 1.49                      | 1.56                     
Bellman Ford              | -                         | 3.39                      | 3.71                      | 1.09                      | 1.63                      | 1.63                      | 1.69                      | 1.73                     
Dijkstra                  | -                         | 2.34                      | 2.68                      | 1.16                      | 1.70                      | 1.71                      | 1.74                      | 1.85                     
Euler                     | -                         | 2.64                      | 3.04                      | 3.20                      | 1.59                      | 1.59                      | 1.64                      | 1.71                     
Midpoint Explicit         | -                         | 2.97                      | 3.44                      | 3.57                      | 1.83                      | 1.84                      | 1.87                      | 1.94                     
Midpoint Fixed            | -                         | 3.32                      | 3.77                      | 3.70                      | 1.93                      | 1.93                      | 1.96                      | 2.03                     
RK4                       | -                         | 3.47                      | 3.99                      | 3.71                      | 2.28                      | 2.31                      | 2.27                      | 2.39                     
FD - L Convection         | -                         | 2.32                      | 2.73                      | 2.50                      | 1.55                      | 1.55                      | 1.59                      | 1.67                     
FD - NL Convection        | -                         | 3.39                      | 3.59                      | 2.62                      | 1.57                      | 1.55                      | 1.58                      | 1.67                     
FD - Poisson              | -                         | 3.47                      | 3.77                      | 4.11                      | 2.18                      | 1.85                      | 2.68                      | 2.09                     
FD - Laplace              | -                         | 6.98                      | 7.61                      | 5.35                      | 1.96                      | 2.00                      | 1.92                      | 2.14                     
M-D                       | -                         | 5.84                      | 6.48                      | 6.19                      | 2.87                      | 2.62                      | 3.42                      | 2.80                     
Splines                   | -                         | -                         | -                         | 0.75                      | 2.24                      | 1.85                      | 2.74                      | 2.01                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 481.00                    | 2.70                      | 3.68                      | 8.45                      | 1.33                      | 1.32                      | 3.70                      | 9.40                     
Bellman Ford (ms)         | 2080.00                   | 4.57                      | 3.47                      | 4.07                      | 3.30                      | 3.23                      | 5.49                      | 4.18                     
Dijkstra (ms)             | 5660.00                   | 16.80                     | 14.50                     | 17.60                     | 35.50                     | 17.20                     | 38.70                     | 19.30                    
Euler (ms)                | 3790.00                   | 25.60                     | 25.10                     | 35.60                     | 23.10                     | 11.40                     | 23.20                     | 14.40                    
Midpoint Explicit (ms)    | 7630.00                   | 52.10                     | 55.60                     | 67.50                     | 39.90                     | 19.20                     | 42.60                     | 15.50                    
Midpoint Fixed (ms)       | 37700.00                  | 266.00                    | 92.20                     | 309.00                    | 178.00                    | 71.90                     | 201.00                    | 55.40                    
RK4 (ms)                  | 19300.00                  | 156.00                    | 34.80                     | 136.00                    | 85.40                     | 32.30                     | 91.10                     | 27.80                    
FD - L Convection (ms)    | 2320.00                   | 1.51                      | 1.60                      | 2.82                      | 4.28                      | 1.77                      | 4.54                      | 1.49                     
FD - NL Convection (ms)   | 2900.00                   | 1.99                      | 1.69                      | 2.93                      | 4.69                      | 1.67                      | 4.43                      | 1.54                     
FD - Poisson (ms)         | 6190.00                   | 2.94                      | 5.55                      | 6.44                      | 3.76                      | 2.59                      | 6.48                      | 2.44                     
FD - Laplace (ms)         | 706.00                    | 67.20                     | 105.00                    | 189.00                    | 150.00                    | 60.40                     | 192.00                    | 59.10                    
M-D (ms)                  | 8560.00                   | 35.30                     | 50.20                     | 56.70                     | 106.00                    | 62.00                     | 88.70                     | 90.60                    
Splines (ms)              | 1740.00                   | -                         | -                         | 18.10                     | 13.60                     | 17.70                     | 15.10                     | 27.90                    

![Development compilation results](./version_specific_results/devel_performance_312_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_312_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 2.2.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.11                      | 2.08                      | 0.33                      | 1.43                      | 1.46                      | 1.46                      | 1.54                     
Bellman Ford              | -                         | 3.62                      | 3.81                      | 1.01                      | 1.62                      | 1.60                      | 1.66                      | 1.74                     
Dijkstra                  | -                         | 2.50                      | 2.80                      | 1.24                      | 1.82                      | 1.76                      | 1.76                      | 1.86                     
Euler                     | -                         | 2.66                      | 3.06                      | 3.40                      | 1.57                      | 1.57                      | 1.60                      | 1.70                     
Midpoint Explicit         | -                         | 3.09                      | 3.50                      | 4.01                      | 1.81                      | 1.82                      | 1.82                      | 1.92                     
Midpoint Fixed            | -                         | 3.51                      | 3.94                      | 4.11                      | 1.93                      | 1.85                      | 1.90                      | 2.01                     
RK4                       | -                         | 3.84                      | 4.25                      | 4.22                      | 2.33                      | 2.36                      | 2.28                      | 2.48                     
FD - L Convection         | -                         | 2.46                      | 2.79                      | 2.77                      | 1.59                      | 1.57                      | 1.61                      | 1.70                     
FD - NL Convection        | -                         | 3.37                      | 3.59                      | 2.78                      | 1.58                      | 1.59                      | 1.59                      | 1.70                     
FD - Poisson              | -                         | 3.67                      | 3.86                      | 4.55                      | 2.23                      | 1.93                      | 2.75                      | 2.15                     
FD - Laplace              | -                         | 7.62                      | 8.16                      | 5.94                      | 1.97                      | 2.01                      | 1.90                      | 2.12                     
M-D                       | -                         | 6.23                      | 6.38                      | 6.53                      | 2.90                      | 2.64                      | 3.44                      | 2.84                     
Splines                   | -                         | -                         | -                         | 0.65                      | 2.27                      | 1.91                      | 2.76                      | 2.03                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 321.00 $\pm$ 5.00         | 3.02 $\pm$ 0.01           | 3.55 $\pm$ 0.01           | 12.40 $\pm$ 0.10          | 1.40 $\pm$ 0.02           | 1.51 $\pm$ 0.02           | 4.51 $\pm$ 0.15           | 8.22 $\pm$ 0.37          
Bellman Ford (ms)         | 1820.00 $\pm$ 20.00       | 4.84 $\pm$ 0.01           | 3.78 $\pm$ 0.09           | 4.51 $\pm$ 0.07           | 3.25 $\pm$ 0.02           | 3.20 $\pm$ 0.01           | 6.02 $\pm$ 0.02           | 4.31 $\pm$ 0.05          
Dijkstra (ms)             | 4910.00 $\pm$ 70.00       | 19.90 $\pm$ 0.10          | 16.80 $\pm$ 1.10          | 19.50 $\pm$ 0.90          | 37.10 $\pm$ 0.50          | 20.40 $\pm$ 0.50          | 45.60 $\pm$ 0.60          | 20.90 $\pm$ 0.40         
Euler (ms)                | 3370.00 $\pm$ 50.00       | 25.40 $\pm$ 0.60          | 25.40 $\pm$ 0.50          | 36.70 $\pm$ 0.60          | 29.00 $\pm$ 6.80          | 11.80 $\pm$ 0.50          | 27.10 $\pm$ 0.40          | 12.60 $\pm$ 0.50         
Midpoint Explicit (ms)    | 6920.00 $\pm$ 50.00       | 50.60 $\pm$ 0.50          | 50.20 $\pm$ 1.10          | 71.70 $\pm$ 1.10          | 45.80 $\pm$ 0.50          | 19.80 $\pm$ 0.60          | 49.10 $\pm$ 0.50          | 15.10 $\pm$ 0.50         
Midpoint Fixed (ms)       | 34900.00 $\pm$ 200.00     | 298.00 $\pm$ 4.00         | 95.90 $\pm$ 1.40          | 301.00 $\pm$ 3.00         | 201.00 $\pm$ 0.00         | 80.70 $\pm$ 1.20          | 230.00 $\pm$ 1.00         | 48.20 $\pm$ 0.80         
RK4 (ms)                  | 16800.00 $\pm$ 200.00     | 168.00 $\pm$ 4.00         | 32.50 $\pm$ 0.60          | 132.00 $\pm$ 2.00         | 88.60 $\pm$ 2.20          | 30.00 $\pm$ 0.50          | 91.20 $\pm$ 1.90          | 26.10 $\pm$ 0.60         
FD - L Convection (ms)    | 2210.00 $\pm$ 40.00       | 1.71 $\pm$ 0.03           | 1.60 $\pm$ 0.06           | 3.08 $\pm$ 0.04           | 4.74 $\pm$ 0.01           | 1.58 $\pm$ 0.09           | 4.40 $\pm$ 0.04           | 1.70 $\pm$ 0.05          
FD - NL Convection (ms)   | 2730.00 $\pm$ 30.00       | 1.86 $\pm$ 0.06           | 1.68 $\pm$ 0.09           | 3.22 $\pm$ 0.08           | 4.96 $\pm$ 0.05           | 1.64 $\pm$ 0.10           | 4.38 $\pm$ 0.02           | 1.70 $\pm$ 0.03          
FD - Poisson (ms)         | 6050.00 $\pm$ 100.00      | 2.93 $\pm$ 0.03           | 5.29 $\pm$ 0.03           | 6.56 $\pm$ 0.07           | 3.89 $\pm$ 0.03           | 2.69 $\pm$ 0.03           | 6.74 $\pm$ 0.04           | 2.63 $\pm$ 0.03          
FD - Laplace (ms)         | 698.00 $\pm$ 6.00         | 64.80 $\pm$ 1.20          | 96.20 $\pm$ 0.60          | 210.00 $\pm$ 2.00         | 166.00 $\pm$ 0.00         | 57.60 $\pm$ 0.70          | 209.00 $\pm$ 2.00         | 54.60 $\pm$ 1.10         
M-D (ms)                  | 14400.00 $\pm$ 100.00     | 40.90 $\pm$ 0.40          | 50.20 $\pm$ 0.20          | 58.00 $\pm$ 1.20          | 113.00 $\pm$ 0.00         | 61.70 $\pm$ 0.20          | 70.60 $\pm$ 2.40          | 69.60 $\pm$ 1.50         
Splines (ms)              | 1840.00 $\pm$ 20.00       | -                         | -                         | 18.40 $\pm$ 0.10          | 13.90 $\pm$ 0.00          | 19.50 $\pm$ 0.40          | 16.40 $\pm$ 0.60          | 29.70 $\pm$ 0.10         

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 2.2.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.21                      | 2.18                      | 0.31                      | 1.45                      | 1.51                      | 1.50                      | 1.58                     
Bellman Ford              | -                         | 3.54                      | 3.85                      | 1.08                      | 1.69                      | 1.67                      | 1.69                      | 1.71                     
Dijkstra                  | -                         | 2.29                      | 2.60                      | 1.12                      | 1.67                      | 1.69                      | 1.71                      | 1.83                     
Euler                     | -                         | 2.61                      | 3.03                      | 3.42                      | 1.59                      | 1.57                      | 1.61                      | 1.68                     
Midpoint Explicit         | -                         | 3.11                      | 3.55                      | 3.90                      | 1.84                      | 1.84                      | 1.89                      | 1.96                     
Midpoint Fixed            | -                         | 3.29                      | 3.71                      | 3.90                      | 1.85                      | 1.84                      | 1.88                      | 1.95                     
RK4                       | -                         | 3.49                      | 3.98                      | 4.00                      | 2.22                      | 2.26                      | 2.18                      | 2.33                     
FD - L Convection         | -                         | 2.31                      | 2.66                      | 2.64                      | 1.53                      | 1.54                      | 1.56                      | 1.64                     
FD - NL Convection        | -                         | 3.29                      | 3.64                      | 2.69                      | 1.53                      | 1.54                      | 1.55                      | 1.68                     
FD - Poisson              | -                         | 3.40                      | 3.72                      | 4.15                      | 2.15                      | 1.83                      | 2.66                      | 2.06                     
FD - Laplace              | -                         | 6.87                      | 7.75                      | 5.47                      | 1.90                      | 1.96                      | 1.91                      | 2.09                     
M-D                       | -                         | 5.90                      | 6.40                      | 6.48                      | 2.85                      | 2.56                      | 3.42                      | 2.81                     
Splines                   | -                         | -                         | -                         | 0.69                      | 2.23                      | 1.84                      | 2.72                      | 1.98                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 482.00 $\pm$ 4.00         | 2.92 $\pm$ 0.01           | 3.67 $\pm$ 0.01           | 8.99 $\pm$ 0.50           | 1.23 $\pm$ 0.00           | 1.33 $\pm$ 0.00           | 4.06 $\pm$ 0.01           | 9.54 $\pm$ 0.09          
Bellman Ford (ms)         | 1770.00 $\pm$ 20.00       | 4.52 $\pm$ 0.01           | 3.60 $\pm$ 0.03           | 4.11 $\pm$ 0.15           | 3.30 $\pm$ 0.03           | 3.28 $\pm$ 0.02           | 5.45 $\pm$ 0.13           | 3.83 $\pm$ 0.01          
Dijkstra (ms)             | 4860.00 $\pm$ 40.00       | 18.50 $\pm$ 0.20          | 14.70 $\pm$ 0.50          | 18.40 $\pm$ 0.50          | 34.40 $\pm$ 0.30          | 16.60 $\pm$ 0.50          | 40.70 $\pm$ 0.40          | 19.60 $\pm$ 0.20         
Euler (ms)                | 3320.00 $\pm$ 30.00       | 25.90 $\pm$ 0.90          | 26.40 $\pm$ 0.40          | 35.10 $\pm$ 0.30          | 23.10 $\pm$ 0.90          | 10.90 $\pm$ 0.50          | 23.50 $\pm$ 0.40          | 14.90 $\pm$ 0.50         
Midpoint Explicit (ms)    | 6710.00 $\pm$ 60.00       | 52.00 $\pm$ 0.40          | 51.90 $\pm$ 1.80          | 67.10 $\pm$ 0.60          | 42.30 $\pm$ 4.20          | 19.50 $\pm$ 0.50          | 42.90 $\pm$ 0.50          | 16.20 $\pm$ 0.50         
Midpoint Fixed (ms)       | 33700.00 $\pm$ 200.00     | 268.00 $\pm$ 3.00         | 94.00 $\pm$ 0.70          | 311.00 $\pm$ 11.00        | 178.00 $\pm$ 0.00         | 73.80 $\pm$ 1.30          | 201.00 $\pm$ 1.00         | 55.20 $\pm$ 0.70         
RK4 (ms)                  | 16900.00 $\pm$ 100.00     | 154.00 $\pm$ 2.00         | 35.20 $\pm$ 0.50          | 125.00 $\pm$ 4.00         | 86.50 $\pm$ 0.50          | 33.10 $\pm$ 2.20          | 91.90 $\pm$ 0.80          | 28.10 $\pm$ 1.00         
FD - L Convection (ms)    | 2090.00 $\pm$ 10.00       | 1.46 $\pm$ 0.04           | 1.52 $\pm$ 0.05           | 2.88 $\pm$ 0.09           | 4.42 $\pm$ 0.27           | 1.66 $\pm$ 0.05           | 4.23 $\pm$ 0.35           | 1.51 $\pm$ 0.02          
FD - NL Convection (ms)   | 2630.00 $\pm$ 20.00       | 2.01 $\pm$ 0.05           | 1.82 $\pm$ 0.05           | 2.92 $\pm$ 0.04           | 4.70 $\pm$ 0.00           | 1.62 $\pm$ 0.04           | 4.24 $\pm$ 0.19           | 1.53 $\pm$ 0.02          
FD - Poisson (ms)         | 5810.00 $\pm$ 100.00      | 3.18 $\pm$ 0.23           | 5.63 $\pm$ 0.12           | 6.64 $\pm$ 0.08           | 3.75 $\pm$ 0.03           | 2.71 $\pm$ 0.03           | 6.37 $\pm$ 0.03           | 2.63 $\pm$ 0.07          
FD - Laplace (ms)         | 712.00 $\pm$ 18.00        | 67.60 $\pm$ 0.60          | 105.00 $\pm$ 1.00         | 190.00 $\pm$ 1.00         | 151.00 $\pm$ 1.00         | 61.50 $\pm$ 0.50          | 195.00 $\pm$ 4.00         | 60.00 $\pm$ 0.40         
M-D (ms)                  | 8020.00 $\pm$ 90.00       | 34.30 $\pm$ 0.20          | 50.90 $\pm$ 1.60          | 57.10 $\pm$ 0.40          | 106.00 $\pm$ 1.00         | 62.40 $\pm$ 0.50          | 88.80 $\pm$ 0.20          | 90.30 $\pm$ 0.10         
Splines (ms)              | 1670.00 $\pm$ 30.00       | -                         | -                         | 18.20 $\pm$ 0.40          | 13.50 $\pm$ 0.10          | 17.70 $\pm$ 0.10          | 15.20 $\pm$ 0.10          | 27.50 $\pm$ 0.00         

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
## Python 3.12 results
### Performance Comparison (as of 2.2.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.17                      | 2.22                      | 0.33                      | 1.51                      | 1.51                      | 1.53                      | 1.61                     
Bellman Ford              | -                         | 3.56                      | 3.84                      | 1.09                      | 1.71                      | 1.68                      | 1.70                      | 1.78                     
Dijkstra                  | -                         | 2.42                      | 2.81                      | 1.22                      | 1.75                      | 1.76                      | 1.80                      | 1.93                     
Euler                     | -                         | 2.75                      | 3.11                      | 3.29                      | 1.66                      | 1.61                      | 1.68                      | 1.74                     
Midpoint Explicit         | -                         | 3.01                      | 3.54                      | 3.68                      | 1.91                      | 1.91                      | 1.94                      | 2.04                     
Midpoint Fixed            | -                         | 3.48                      | 3.93                      | 3.88                      | 1.99                      | 2.01                      | 2.06                      | 2.12                     
RK4                       | -                         | 3.45                      | 4.04                      | 3.75                      | 2.35                      | 2.36                      | 2.31                      | 2.45                     
FD - L Convection         | -                         | 2.33                      | 2.70                      | 2.50                      | 1.57                      | 1.56                      | 1.61                      | 1.67                     
FD - NL Convection        | -                         | 3.38                      | 3.57                      | 2.61                      | 1.58                      | 1.57                      | 1.61                      | 1.68                     
FD - Poisson              | -                         | 3.47                      | 3.87                      | 4.20                      | 2.21                      | 1.87                      | 2.67                      | 2.10                     
FD - Laplace              | -                         | 6.79                      | 7.62                      | 5.35                      | 1.99                      | 2.06                      | 2.00                      | 2.20                     
M-D                       | -                         | 5.93                      | 6.47                      | 6.18                      | 2.91                      | 2.73                      | 3.47                      | 2.85                     
Splines                   | -                         | -                         | -                         | 0.75                      | 2.25                      | 1.88                      | 2.77                      | 2.05                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 482.00 $\pm$ 4.00         | 2.70 $\pm$ 0.01           | 3.67 $\pm$ 0.02           | 9.20 $\pm$ 0.45           | 1.33 $\pm$ 0.00           | 1.28 $\pm$ 0.00           | 3.72 $\pm$ 0.06           | 9.98 $\pm$ 0.34          
Bellman Ford (ms)         | 2110.00 $\pm$ 30.00       | 4.61 $\pm$ 0.08           | 3.55 $\pm$ 0.09           | 4.07 $\pm$ 0.03           | 3.28 $\pm$ 0.04           | 3.25 $\pm$ 0.03           | 5.37 $\pm$ 0.03           | 4.18 $\pm$ 0.02          
Dijkstra (ms)             | 5600.00 $\pm$ 70.00       | 17.50 $\pm$ 0.30          | 15.30 $\pm$ 0.40          | 18.80 $\pm$ 0.80          | 35.80 $\pm$ 0.50          | 18.00 $\pm$ 0.20          | 39.50 $\pm$ 0.30          | 20.00 $\pm$ 0.60         
Euler (ms)                | 3750.00 $\pm$ 40.00       | 26.60 $\pm$ 1.00          | 25.80 $\pm$ 0.50          | 36.30 $\pm$ 0.90          | 23.20 $\pm$ 1.30          | 11.10 $\pm$ 0.50          | 23.70 $\pm$ 0.40          | 14.80 $\pm$ 0.50         
Midpoint Explicit (ms)    | 7600.00 $\pm$ 50.00       | 53.00 $\pm$ 0.50          | 51.80 $\pm$ 1.80          | 68.50 $\pm$ 0.60          | 40.70 $\pm$ 0.50          | 19.10 $\pm$ 0.40          | 43.10 $\pm$ 0.70          | 16.50 $\pm$ 0.90         
Midpoint Fixed (ms)       | 37600.00 $\pm$ 200.00     | 293.00 $\pm$ 56.00        | 92.90 $\pm$ 0.50          | 311.00 $\pm$ 2.00         | 178.00 $\pm$ 1.00         | 73.30 $\pm$ 1.30          | 202.00 $\pm$ 1.00         | 51.50 $\pm$ 0.70         
RK4 (ms)                  | 19000.00 $\pm$ 200.00     | 155.00 $\pm$ 3.00         | 35.80 $\pm$ 0.60          | 125.00 $\pm$ 2.00         | 87.00 $\pm$ 2.20          | 31.70 $\pm$ 0.40          | 90.50 $\pm$ 1.00          | 27.70 $\pm$ 1.10         
FD - L Convection (ms)    | 2300.00 $\pm$ 40.00       | 1.45 $\pm$ 0.06           | 1.65 $\pm$ 0.06           | 2.91 $\pm$ 0.14           | 4.59 $\pm$ 0.38           | 1.54 $\pm$ 0.05           | 4.40 $\pm$ 0.10           | 1.35 $\pm$ 0.05          
FD - NL Convection (ms)   | 2910.00 $\pm$ 20.00       | 1.99 $\pm$ 0.02           | 1.71 $\pm$ 0.03           | 2.91 $\pm$ 0.07           | 4.70 $\pm$ 0.02           | 1.64 $\pm$ 0.05           | 4.49 $\pm$ 0.04           | 1.39 $\pm$ 0.03          
FD - Poisson (ms)         | 6400.00 $\pm$ 180.00      | 2.98 $\pm$ 0.05           | 5.51 $\pm$ 0.03           | 6.61 $\pm$ 0.04           | 3.73 $\pm$ 0.04           | 2.59 $\pm$ 0.03           | 6.32 $\pm$ 0.02           | 2.50 $\pm$ 0.04          
FD - Laplace (ms)         | 695.00 $\pm$ 3.00         | 64.30 $\pm$ 1.10          | 104.00 $\pm$ 1.00         | 190.00 $\pm$ 4.00         | 150.00 $\pm$ 0.00         | 56.60 $\pm$ 0.30          | 192.00 $\pm$ 0.00         | 55.40 $\pm$ 0.70         
M-D (ms)                  | 8690.00 $\pm$ 100.00      | 35.20 $\pm$ 0.20          | 53.60 $\pm$ 10.00         | 57.00 $\pm$ 0.30          | 106.00 $\pm$ 0.00         | 62.20 $\pm$ 0.10          | 88.90 $\pm$ 0.60          | 90.20 $\pm$ 0.20         
Splines (ms)              | 1780.00 $\pm$ 50.00       | -                         | -                         | 17.80 $\pm$ 0.30          | 13.40 $\pm$ 0.10          | 17.70 $\pm$ 0.00          | 15.10 $\pm$ 0.00          | 28.00 $\pm$ 0.50         

![Python 3.12 compilation results](./version_specific_results/pypi_performance_312_compilation.svg)
![Python 3.12 execution results](./version_specific_results/pypi_performance_312_execution.svg)
## Python 3.13 results
### Performance Comparison (as of 2.2.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.04                      | 2.12                      | 0.30                      | 1.46                      | 1.49                      | 1.50                      | 1.58                     
Bellman Ford              | -                         | 3.38                      | 3.69                      | 1.10                      | 1.65                      | 1.68                      | 1.67                      | 1.72                     
Dijkstra                  | -                         | 2.30                      | 2.67                      | 1.14                      | 1.73                      | 1.74                      | 1.78                      | 1.90                     
Euler                     | -                         | 2.66                      | 3.10                      | 3.28                      | 1.65                      | 1.63                      | 1.65                      | 1.71                     
Midpoint Explicit         | -                         | 2.93                      | 3.43                      | 3.55                      | 1.82                      | 1.82                      | 1.84                      | 1.92                     
Midpoint Fixed            | -                         | 3.31                      | 3.73                      | 3.73                      | 1.94                      | 1.93                      | 2.02                      | 2.07                     
RK4                       | -                         | 3.51                      | 3.95                      | 3.70                      | 2.25                      | 2.32                      | 2.29                      | 2.40                     
FD - L Convection         | -                         | 2.32                      | 2.69                      | 2.59                      | 1.57                      | 1.56                      | 1.58                      | 1.66                     
FD - NL Convection        | -                         | 3.45                      | 3.62                      | 2.67                      | 1.57                      | 1.56                      | 1.58                      | 1.66                     
FD - Poisson              | -                         | 3.44                      | 3.74                      | 4.06                      | 2.21                      | 1.85                      | 2.68                      | 2.09                     
FD - Laplace              | -                         | 7.01                      | 7.87                      | 5.32                      | 1.97                      | 2.01                      | 1.93                      | 2.16                     
M-D                       | -                         | 5.81                      | 6.35                      | 6.14                      | 2.88                      | 2.62                      | 3.44                      | 2.78                     
Splines                   | -                         | -                         | -                         | 0.75                      | 2.26                      | 1.91                      | 2.85                      | 2.07                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 495.00 $\pm$ 4.00         | 2.70 $\pm$ 0.00           | 3.68 $\pm$ 0.02           | 9.33 $\pm$ 0.42           | 1.33 $\pm$ 0.01           | 1.28 $\pm$ 0.00           | 3.71 $\pm$ 0.00           | 10.70 $\pm$ 0.20         
Bellman Ford (ms)         | 2200.00 $\pm$ 40.00       | 4.61 $\pm$ 0.02           | 3.51 $\pm$ 0.04           | 4.08 $\pm$ 0.03           | 3.29 $\pm$ 0.02           | 3.26 $\pm$ 0.02           | 5.39 $\pm$ 0.03           | 4.18 $\pm$ 0.01          
Dijkstra (ms)             | 5280.00 $\pm$ 60.00       | 17.10 $\pm$ 0.40          | 14.80 $\pm$ 0.10          | 19.00 $\pm$ 0.50          | 35.70 $\pm$ 0.50          | 16.70 $\pm$ 0.20          | 40.00 $\pm$ 0.50          | 20.30 $\pm$ 0.50         
Euler (ms)                | 3850.00 $\pm$ 30.00       | 26.80 $\pm$ 1.10          | 25.70 $\pm$ 0.80          | 36.10 $\pm$ 0.40          | 23.10 $\pm$ 0.80          | 11.20 $\pm$ 0.40          | 23.50 $\pm$ 0.50          | 15.20 $\pm$ 1.10         
Midpoint Explicit (ms)    | 7820.00 $\pm$ 40.00       | 52.60 $\pm$ 0.50          | 51.60 $\pm$ 1.90          | 68.30 $\pm$ 1.20          | 40.50 $\pm$ 0.60          | 19.20 $\pm$ 0.70          | 42.60 $\pm$ 0.60          | 16.90 $\pm$ 0.40         
Midpoint Fixed (ms)       | 39000.00 $\pm$ 200.00     | 269.00 $\pm$ 5.00         | 93.40 $\pm$ 1.80          | 311.00 $\pm$ 2.00         | 178.00 $\pm$ 1.00         | 74.40 $\pm$ 1.60          | 202.00 $\pm$ 1.00         | 52.50 $\pm$ 0.50         
RK4 (ms)                  | 19400.00 $\pm$ 200.00     | 157.00 $\pm$ 7.00         | 35.60 $\pm$ 0.40          | 125.00 $\pm$ 2.00         | 86.70 $\pm$ 0.70          | 32.10 $\pm$ 0.50          | 90.80 $\pm$ 0.60          | 28.60 $\pm$ 0.60         
FD - L Convection (ms)    | 2710.00 $\pm$ 30.00       | 1.46 $\pm$ 0.08           | 1.62 $\pm$ 0.03           | 2.83 $\pm$ 0.01           | 4.70 $\pm$ 0.37           | 1.66 $\pm$ 0.05           | 4.35 $\pm$ 0.11           | 1.54 $\pm$ 0.03          
FD - NL Convection (ms)   | 3450.00 $\pm$ 50.00       | 1.87 $\pm$ 0.03           | 1.65 $\pm$ 0.04           | 2.90 $\pm$ 0.03           | 4.70 $\pm$ 0.01           | 1.65 $\pm$ 0.04           | 4.14 $\pm$ 0.17           | 1.38 $\pm$ 0.05          
FD - Poisson (ms)         | 6880.00 $\pm$ 90.00       | 2.95 $\pm$ 0.03           | 5.58 $\pm$ 0.13           | 6.61 $\pm$ 0.04           | 3.76 $\pm$ 0.03           | 2.60 $\pm$ 0.03           | 6.47 $\pm$ 0.02           | 2.55 $\pm$ 0.03          
FD - Laplace (ms)         | 705.00 $\pm$ 4.00         | 64.30 $\pm$ 0.30          | 105.00 $\pm$ 1.00         | 190.00 $\pm$ 1.00         | 151.00 $\pm$ 1.00         | 59.10 $\pm$ 2.90          | 194.00 $\pm$ 0.00         | 55.60 $\pm$ 0.50         
M-D (ms)                  | 8890.00 $\pm$ 130.00      | 36.20 $\pm$ 1.60          | 50.40 $\pm$ 0.30          | 56.90 $\pm$ 0.20          | 106.00 $\pm$ 0.00         | 62.30 $\pm$ 0.30          | 88.70 $\pm$ 0.10          | 90.50 $\pm$ 0.10         
Splines (ms)              | 2010.00 $\pm$ 30.00       | -                         | -                         | 17.70 $\pm$ 0.10          | 13.60 $\pm$ 0.00          | 17.70 $\pm$ 0.10          | 15.20 $\pm$ 0.10          | 27.80 $\pm$ 0.10         

![Python 3.13 compilation results](./version_specific_results/pypi_performance_313_compilation.svg)
![Python 3.13 execution results](./version_specific_results/pypi_performance_313_execution.svg)
## Python 3.14 results
### Performance Comparison (as of 2.2.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.07                      | 2.14                      | 0.31                      | 1.48                      | 1.53                      | 1.55                      | 1.61                     
Bellman Ford              | -                         | 3.50                      | 3.81                      | 1.01                      | 1.72                      | 1.71                      | 1.74                      | 1.84                     
Dijkstra                  | -                         | 2.32                      | 2.66                      | 1.11                      | 1.72                      | 1.73                      | 1.76                      | 1.88                     
Euler                     | -                         | 2.61                      | 3.06                      | 3.24                      | 1.62                      | 1.60                      | 1.66                      | 1.74                     
Midpoint Explicit         | -                         | 2.95                      | 3.45                      | 3.61                      | 1.91                      | 1.89                      | 1.92                      | 2.02                     
Midpoint Fixed            | -                         | 3.34                      | 3.81                      | 3.77                      | 1.97                      | 1.96                      | 2.00                      | 2.09                     
RK4                       | -                         | 3.53                      | 4.10                      | 3.80                      | 2.36                      | 2.42                      | 2.33                      | 2.46                     
FD - L Convection         | -                         | 2.40                      | 2.75                      | 2.57                      | 1.59                      | 1.59                      | 1.63                      | 1.71                     
FD - NL Convection        | -                         | 3.52                      | 3.73                      | 2.73                      | 1.60                      | 1.59                      | 1.66                      | 1.69                     
FD - Poisson              | -                         | 3.58                      | 3.87                      | 4.20                      | 2.22                      | 1.88                      | 2.75                      | 2.15                     
FD - Laplace              | -                         | 7.05                      | 8.05                      | 5.43                      | 2.01                      | 2.08                      | 2.00                      | 2.21                     
M-D                       | -                         | 5.96                      | 6.41                      | 6.26                      | 2.90                      | 2.65                      | 3.45                      | 2.82                     
Splines                   | -                         | -                         | -                         | 0.74                      | 2.27                      | 1.90                      | 2.79                      | 2.07                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 517.00 $\pm$ 8.00         | 2.71 $\pm$ 0.01           | 3.67 $\pm$ 0.01           | 8.96 $\pm$ 0.49           | 1.33 $\pm$ 0.00           | 1.33 $\pm$ 0.00           | 3.78 $\pm$ 0.13           | 9.38 $\pm$ 0.18          
Bellman Ford (ms)         | 2130.00 $\pm$ 40.00       | 4.53 $\pm$ 0.01           | 3.52 $\pm$ 0.04           | 4.07 $\pm$ 0.03           | 3.27 $\pm$ 0.02           | 3.29 $\pm$ 0.02           | 5.50 $\pm$ 0.03           | 4.18 $\pm$ 0.02          
Dijkstra (ms)             | 5070.00 $\pm$ 50.00       | 17.00 $\pm$ 0.10          | 14.70 $\pm$ 0.10          | 18.00 $\pm$ 0.20          | 34.60 $\pm$ 0.20          | 17.50 $\pm$ 0.10          | 39.40 $\pm$ 0.20          | 19.60 $\pm$ 0.60         
Euler (ms)                | 3740.00 $\pm$ 40.00       | 25.90 $\pm$ 0.50          | 26.20 $\pm$ 0.60          | 35.80 $\pm$ 0.30          | 24.10 $\pm$ 3.60          | 11.00 $\pm$ 0.40          | 24.80 $\pm$ 3.90          | 15.20 $\pm$ 0.40         
Midpoint Explicit (ms)    | 7680.00 $\pm$ 110.00      | 52.90 $\pm$ 2.40          | 50.90 $\pm$ 1.00          | 69.00 $\pm$ 3.70          | 40.60 $\pm$ 0.50          | 19.10 $\pm$ 0.40          | 43.00 $\pm$ 0.70          | 16.20 $\pm$ 0.50         
Midpoint Fixed (ms)       | 38400.00 $\pm$ 500.00     | 279.00 $\pm$ 50.00        | 93.10 $\pm$ 0.90          | 312.00 $\pm$ 4.00         | 178.00 $\pm$ 1.00         | 73.10 $\pm$ 0.60          | 201.00 $\pm$ 0.00         | 50.70 $\pm$ 0.50         
RK4 (ms)                  | 19500.00 $\pm$ 300.00     | 158.00 $\pm$ 4.00         | 35.70 $\pm$ 0.40          | 132.00 $\pm$ 1.00         | 86.50 $\pm$ 0.50          | 32.00 $\pm$ 0.40          | 91.00 $\pm$ 0.50          | 28.10 $\pm$ 0.80         
FD - L Convection (ms)    | 2580.00 $\pm$ 20.00       | 1.66 $\pm$ 0.02           | 1.63 $\pm$ 0.03           | 2.86 $\pm$ 0.06           | 4.60 $\pm$ 0.02           | 1.66 $\pm$ 0.05           | 4.33 $\pm$ 0.11           | 1.52 $\pm$ 0.03          
FD - NL Convection (ms)   | 3270.00 $\pm$ 30.00       | 2.00 $\pm$ 0.02           | 1.70 $\pm$ 0.09           | 2.92 $\pm$ 0.04           | 4.69 $\pm$ 0.00           | 1.67 $\pm$ 0.05           | 4.49 $\pm$ 0.04           | 1.54 $\pm$ 0.03          
FD - Poisson (ms)         | 7120.00 $\pm$ 100.00      | 2.98 $\pm$ 0.02           | 5.55 $\pm$ 0.04           | 6.61 $\pm$ 0.03           | 3.77 $\pm$ 0.02           | 2.63 $\pm$ 0.03           | 6.37 $\pm$ 0.03           | 2.57 $\pm$ 0.03          
FD - Laplace (ms)         | 711.00 $\pm$ 2.00         | 67.10 $\pm$ 1.70          | 106.00 $\pm$ 3.00         | 191.00 $\pm$ 1.00         | 152.00 $\pm$ 1.00         | 57.50 $\pm$ 0.70          | 194.00 $\pm$ 1.00         | 55.90 $\pm$ 0.50         
M-D (ms)                  | 8960.00 $\pm$ 110.00      | 34.40 $\pm$ 0.30          | 50.20 $\pm$ 0.30          | 56.90 $\pm$ 0.10          | 105.00 $\pm$ 0.00         | 63.10 $\pm$ 2.20          | 88.70 $\pm$ 0.00          | 90.70 $\pm$ 0.10         
Splines (ms)              | 1930.00 $\pm$ 20.00       | -                         | -                         | 16.40 $\pm$ 0.20          | 13.40 $\pm$ 0.00          | 17.70 $\pm$ 0.00          | 15.20 $\pm$ 0.00          | 27.60 $\pm$ 0.10         

![Python 3.14 compilation results](./version_specific_results/pypi_performance_314_compilation.svg)
![Python 3.14 execution results](./version_specific_results/pypi_performance_314_execution.svg)
