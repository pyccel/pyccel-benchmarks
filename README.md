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
### Performance Comparison (as of Tue Mar 10 18:43:02 UTC 2026)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.99                      | 2.11                      | 0.31                      | 1.43                      | 1.46                      | 1.47                      | 1.55                     
Bellman Ford              | -                         | 3.43                      | 3.68                      | 1.06                      | 1.60                      | 1.60                      | 1.64                      | 1.71                     
Dijkstra                  | -                         | 2.32                      | 2.65                      | 1.13                      | 1.70                      | 1.70                      | 1.72                      | 1.85                     
Euler                     | -                         | 2.61                      | 3.04                      | 3.19                      | 1.59                      | 1.58                      | 1.62                      | 1.70                     
Midpoint Explicit         | -                         | 2.92                      | 3.40                      | 3.55                      | 1.82                      | 1.82                      | 1.85                      | 1.92                     
Midpoint Fixed            | -                         | 3.30                      | 3.74                      | 3.68                      | 1.93                      | 1.91                      | 1.94                      | 2.01                     
RK4                       | -                         | 3.44                      | 3.95                      | 3.70                      | 2.27                      | 2.30                      | 2.25                      | 2.37                     
FD - L Convection         | -                         | 2.31                      | 2.67                      | 2.48                      | 1.54                      | 1.55                      | 1.57                      | 1.66                     
FD - NL Convection        | -                         | 3.34                      | 3.59                      | 2.60                      | 1.56                      | 1.55                      | 1.57                      | 1.65                     
FD - Poisson              | -                         | 3.46                      | 3.76                      | 4.08                      | 2.17                      | 1.84                      | 2.65                      | 2.07                     
FD - Laplace              | -                         | 6.87                      | 7.62                      | 5.34                      | 1.94                      | 1.99                      | 1.91                      | 2.13                     
M-D                       | -                         | 5.80                      | 6.31                      | 6.17                      | 2.85                      | 2.61                      | 3.41                      | 2.79                     
Splines                   | -                         | -                         | -                         | 0.74                      | 2.22                      | 1.85                      | 2.72                      | 2.01                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 479.00                    | 2.75                      | 3.68                      | 8.61                      | 1.33                      | 1.28                      | 3.70                      | 9.65                     
Bellman Ford (ms)         | 2010.00                   | 4.63                      | 3.50                      | 4.07                      | 3.28                      | 3.28                      | 5.34                      | 4.15                     
Dijkstra (ms)             | 5700.00                   | 16.50                     | 14.30                     | 17.40                     | 35.10                     | 15.90                     | 38.50                     | 18.90                    
Euler (ms)                | 3760.00                   | 26.50                     | 25.00                     | 35.30                     | 21.50                     | 11.40                     | 23.10                     | 14.60                    
Midpoint Explicit (ms)    | 7550.00                   | 56.80                     | 54.80                     | 67.10                     | 40.80                     | 19.40                     | 42.50                     | 16.60                    
Midpoint Fixed (ms)       | 37200.00                  | 267.00                    | 92.20                     | 311.00                    | 178.00                    | 72.00                     | 201.00                    | 51.60                    
RK4 (ms)                  | 18700.00                  | 153.00                    | 36.00                     | 124.00                    | 89.00                     | 47.20                     | 90.60                     | 28.30                    
FD - L Convection (ms)    | 2490.00                   | 1.50                      | 1.59                      | 2.82                      | 5.09                      | 1.64                      | 4.34                      | 1.43                     
FD - NL Convection (ms)   | 2870.00                   | 1.99                      | 1.69                      | 2.86                      | 4.69                      | 1.54                      | 4.43                      | 1.52                     
FD - Poisson (ms)         | 6560.00                   | 2.90                      | 5.54                      | 6.43                      | 3.76                      | 2.57                      | 6.32                      | 2.52                     
FD - Laplace (ms)         | 699.00                    | 63.60                     | 104.00                    | 189.00                    | 150.00                    | 56.30                     | 197.00                    | 54.60                    
M-D (ms)                  | 8610.00                   | 35.70                     | 50.40                     | 56.80                     | 106.00                    | 62.20                     | 89.20                     | 90.40                    
Splines (ms)              | 1740.00                   | -                         | -                         | 18.10                     | 13.60                     | 17.60                     | 15.10                     | 28.00                    

![Development compilation results](./version_specific_results/devel_performance_312_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_312_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 2.2.2)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.06                      | 2.07                      | 0.34                      | 1.41                      | 1.43                      | 1.45                      | 1.52                     
Bellman Ford              | -                         | 3.39                      | 3.73                      | 1.00                      | 1.58                      | 1.58                      | 1.62                      | 1.69                     
Dijkstra                  | -                         | 2.39                      | 2.71                      | 1.15                      | 1.67                      | 1.68                      | 1.72                      | 1.83                     
Euler                     | -                         | 2.61                      | 3.04                      | 3.35                      | 1.57                      | 1.56                      | 1.60                      | 1.68                     
Midpoint Explicit         | -                         | 2.97                      | 3.46                      | 3.79                      | 1.78                      | 1.79                      | 1.82                      | 1.90                     
Midpoint Fixed            | -                         | 3.39                      | 3.80                      | 3.94                      | 1.85                      | 1.84                      | 1.88                      | 1.96                     
RK4                       | -                         | 3.50                      | 4.00                      | 3.94                      | 2.24                      | 2.27                      | 2.24                      | 2.36                     
FD - L Convection         | -                         | 2.31                      | 2.66                      | 2.58                      | 1.51                      | 1.52                      | 1.55                      | 1.63                     
FD - NL Convection        | -                         | 3.23                      | 3.59                      | 2.74                      | 1.54                      | 1.53                      | 1.56                      | 1.63                     
FD - Poisson              | -                         | 3.46                      | 3.78                      | 4.39                      | 2.14                      | 1.82                      | 2.65                      | 2.06                     
FD - Laplace              | -                         | 6.97                      | 7.81                      | 5.71                      | 1.92                      | 1.97                      | 1.88                      | 2.10                     
M-D                       | -                         | 6.08                      | 6.37                      | 6.45                      | 2.87                      | 2.64                      | 3.43                      | 2.80                     
Splines                   | -                         | -                         | -                         | 0.66                      | 2.19                      | 1.83                      | 2.71                      | 2.00                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 309.00 $\pm$ 2.00         | 2.92 $\pm$ 0.00           | 3.68 $\pm$ 0.05           | 9.29 $\pm$ 0.51           | 1.23 $\pm$ 0.02           | 1.32 $\pm$ 0.00           | 4.08 $\pm$ 0.07           | 9.52 $\pm$ 0.16          
Bellman Ford (ms)         | 1830.00 $\pm$ 20.00       | 4.52 $\pm$ 0.02           | 3.61 $\pm$ 0.03           | 4.06 $\pm$ 0.02           | 3.28 $\pm$ 0.03           | 3.23 $\pm$ 0.02           | 5.40 $\pm$ 0.12           | 3.82 $\pm$ 0.01          
Dijkstra (ms)             | 5020.00 $\pm$ 50.00       | 17.60 $\pm$ 0.10          | 15.40 $\pm$ 0.10          | 18.50 $\pm$ 0.50          | 35.00 $\pm$ 0.10          | 17.20 $\pm$ 0.10          | 39.80 $\pm$ 0.10          | 19.60 $\pm$ 0.10         
Euler (ms)                | 3420.00 $\pm$ 20.00       | 25.50 $\pm$ 0.50          | 26.00 $\pm$ 0.90          | 35.20 $\pm$ 0.70          | 22.60 $\pm$ 0.70          | 10.90 $\pm$ 0.40          | 23.30 $\pm$ 0.40          | 15.30 $\pm$ 1.00         
Midpoint Explicit (ms)    | 7010.00 $\pm$ 30.00       | 52.10 $\pm$ 1.20          | 50.80 $\pm$ 0.50          | 68.30 $\pm$ 5.10          | 40.60 $\pm$ 0.40          | 18.80 $\pm$ 0.40          | 42.70 $\pm$ 0.40          | 16.30 $\pm$ 1.50         
Midpoint Fixed (ms)       | 35100.00 $\pm$ 100.00     | 268.00 $\pm$ 2.00         | 93.80 $\pm$ 1.00          | 306.00 $\pm$ 1.00         | 179.00 $\pm$ 0.00         | 72.60 $\pm$ 1.30          | 201.00 $\pm$ 1.00         | 55.10 $\pm$ 0.50         
RK4 (ms)                  | 17200.00 $\pm$ 100.00     | 154.00 $\pm$ 4.00         | 35.10 $\pm$ 0.60          | 125.00 $\pm$ 5.00         | 86.40 $\pm$ 1.30          | 31.50 $\pm$ 0.40          | 91.50 $\pm$ 0.50          | 27.50 $\pm$ 0.50         
FD - L Convection (ms)    | 2310.00 $\pm$ 20.00       | 1.69 $\pm$ 0.05           | 1.45 $\pm$ 0.03           | 2.84 $\pm$ 0.03           | 4.29 $\pm$ 0.03           | 1.52 $\pm$ 0.01           | 4.52 $\pm$ 0.01           | 1.52 $\pm$ 0.04          
FD - NL Convection (ms)   | 2890.00 $\pm$ 20.00       | 1.92 $\pm$ 0.05           | 1.81 $\pm$ 0.04           | 2.91 $\pm$ 0.08           | 4.69 $\pm$ 0.00           | 1.61 $\pm$ 0.06           | 4.54 $\pm$ 0.06           | 1.43 $\pm$ 0.06          
FD - Poisson (ms)         | 6290.00 $\pm$ 40.00       | 3.01 $\pm$ 0.19           | 5.45 $\pm$ 0.04           | 6.60 $\pm$ 0.06           | 3.67 $\pm$ 0.02           | 2.61 $\pm$ 0.03           | 6.27 $\pm$ 0.03           | 2.54 $\pm$ 0.04          
FD - Laplace (ms)         | 630.00 $\pm$ 8.00         | 66.40 $\pm$ 1.80          | 103.00 $\pm$ 0.00         | 190.00 $\pm$ 1.00         | 151.00 $\pm$ 0.00         | 56.80 $\pm$ 0.70          | 193.00 $\pm$ 1.00         | 55.20 $\pm$ 0.30         
M-D (ms)                  | 15000.00 $\pm$ 100.00     | 35.90 $\pm$ 0.80          | 50.40 $\pm$ 0.10          | 57.00 $\pm$ 0.40          | 106.00 $\pm$ 0.00         | 62.80 $\pm$ 1.00          | 89.30 $\pm$ 0.20          | 90.90 $\pm$ 0.50         
Splines (ms)              | 1940.00 $\pm$ 40.00       | -                         | -                         | 17.60 $\pm$ 0.10          | 13.60 $\pm$ 0.00          | 17.70 $\pm$ 0.00          | 15.20 $\pm$ 0.00          | 27.60 $\pm$ 0.00         

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 2.2.2)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.14                      | 2.13                      | 0.30                      | 1.44                      | 1.48                      | 1.45                      | 1.52                     
Bellman Ford              | -                         | 3.42                      | 3.72                      | 1.05                      | 1.65                      | 1.58                      | 1.64                      | 1.71                     
Dijkstra                  | -                         | 2.38                      | 2.71                      | 1.14                      | 1.72                      | 1.76                      | 1.75                      | 1.95                     
Euler                     | -                         | 2.70                      | 3.05                      | 3.51                      | 1.63                      | 1.61                      | 1.64                      | 1.70                     
Midpoint Explicit         | -                         | 3.08                      | 3.58                      | 3.96                      | 1.86                      | 1.90                      | 1.95                      | 1.99                     
Midpoint Fixed            | -                         | 3.40                      | 3.85                      | 3.98                      | 1.92                      | 1.85                      | 1.89                      | 2.00                     
RK4                       | -                         | 3.59                      | 3.97                      | 4.05                      | 2.17                      | 2.24                      | 2.17                      | 2.30                     
FD - L Convection         | -                         | 2.36                      | 2.74                      | 2.61                      | 1.53                      | 1.54                      | 1.57                      | 1.66                     
FD - NL Convection        | -                         | 3.27                      | 3.61                      | 2.73                      | 1.63                      | 1.63                      | 1.64                      | 1.68                     
FD - Poisson              | -                         | 3.56                      | 4.02                      | 4.40                      | 2.28                      | 1.91                      | 2.77                      | 2.17                     
FD - Laplace              | -                         | 7.52                      | 8.32                      | 5.69                      | 1.93                      | 1.99                      | 1.92                      | 2.17                     
M-D                       | -                         | 5.81                      | 6.32                      | 6.41                      | 2.77                      | 2.51                      | 3.33                      | 2.70                     
Splines                   | -                         | -                         | -                         | 0.67                      | 2.16                      | 1.80                      | 2.70                      | 1.98                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 475.00 $\pm$ 3.00         | 2.92 $\pm$ 0.01           | 3.70 $\pm$ 0.10           | 9.11 $\pm$ 0.62           | 1.24 $\pm$ 0.00           | 1.32 $\pm$ 0.01           | 4.37 $\pm$ 0.01           | 9.86 $\pm$ 0.32          
Bellman Ford (ms)         | 1870.00 $\pm$ 20.00       | 4.53 $\pm$ 0.03           | 3.60 $\pm$ 0.07           | 4.05 $\pm$ 0.02           | 3.29 $\pm$ 0.02           | 3.25 $\pm$ 0.04           | 5.39 $\pm$ 0.03           | 3.84 $\pm$ 0.01          
Dijkstra (ms)             | 4910.00 $\pm$ 30.00       | 18.80 $\pm$ 0.10          | 15.40 $\pm$ 0.20          | 19.10 $\pm$ 0.70          | 35.60 $\pm$ 0.40          | 17.10 $\pm$ 0.10          | 41.60 $\pm$ 0.20          | 20.80 $\pm$ 0.50         
Euler (ms)                | 3340.00 $\pm$ 40.00       | 25.80 $\pm$ 0.40          | 26.40 $\pm$ 0.40          | 35.70 $\pm$ 0.50          | 22.90 $\pm$ 0.80          | 11.30 $\pm$ 0.50          | 23.70 $\pm$ 0.70          | 15.40 $\pm$ 0.60         
Midpoint Explicit (ms)    | 6810.00 $\pm$ 100.00      | 52.30 $\pm$ 0.60          | 52.20 $\pm$ 2.00          | 68.00 $\pm$ 1.80          | 40.70 $\pm$ 0.60          | 19.90 $\pm$ 0.50          | 43.30 $\pm$ 0.60          | 16.00 $\pm$ 0.40         
Midpoint Fixed (ms)       | 34400.00 $\pm$ 400.00     | 284.00 $\pm$ 32.00        | 94.30 $\pm$ 0.70          | 306.00 $\pm$ 2.00         | 180.00 $\pm$ 1.00         | 73.60 $\pm$ 0.70          | 202.00 $\pm$ 1.00         | 53.30 $\pm$ 0.80         
RK4 (ms)                  | 17000.00 $\pm$ 200.00     | 155.00 $\pm$ 3.00         | 35.20 $\pm$ 0.40          | 124.00 $\pm$ 1.00         | 87.10 $\pm$ 3.60          | 32.00 $\pm$ 0.40          | 91.40 $\pm$ 0.60          | 27.50 $\pm$ 0.50         
FD - L Convection (ms)    | 2210.00 $\pm$ 120.00      | 1.42 $\pm$ 0.02           | 1.49 $\pm$ 0.02           | 2.87 $\pm$ 0.05           | 4.78 $\pm$ 0.39           | 1.66 $\pm$ 0.05           | 4.27 $\pm$ 0.30           | 1.52 $\pm$ 0.02          
FD - NL Convection (ms)   | 2770.00 $\pm$ 90.00       | 2.00 $\pm$ 0.02           | 1.80 $\pm$ 0.03           | 2.89 $\pm$ 0.04           | 4.70 $\pm$ 0.01           | 1.64 $\pm$ 0.06           | 4.52 $\pm$ 0.04           | 1.53 $\pm$ 0.04          
FD - Poisson (ms)         | 5750.00 $\pm$ 50.00       | 3.04 $\pm$ 0.08           | 5.58 $\pm$ 0.04           | 6.63 $\pm$ 0.03           | 3.75 $\pm$ 0.02           | 2.69 $\pm$ 0.05           | 6.38 $\pm$ 0.02           | 2.58 $\pm$ 0.02          
FD - Laplace (ms)         | 714.00 $\pm$ 3.00         | 63.40 $\pm$ 0.40          | 103.00 $\pm$ 1.00         | 190.00 $\pm$ 1.00         | 151.00 $\pm$ 0.00         | 60.50 $\pm$ 3.30          | 194.00 $\pm$ 1.00         | 57.00 $\pm$ 2.30         
M-D (ms)                  | 8000.00 $\pm$ 50.00       | 34.20 $\pm$ 0.20          | 50.50 $\pm$ 0.40          | 57.10 $\pm$ 0.20          | 106.00 $\pm$ 0.00         | 62.30 $\pm$ 0.80          | 88.80 $\pm$ 0.20          | 90.70 $\pm$ 0.10         
Splines (ms)              | 1730.00 $\pm$ 20.00       | -                         | -                         | 18.20 $\pm$ 0.40          | 13.50 $\pm$ 0.20          | 17.70 $\pm$ 0.30          | 15.30 $\pm$ 0.10          | 27.50 $\pm$ 0.10         

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
## Python 3.12 results
### Performance Comparison (as of 2.2.2)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.47                      | 2.18                      | 0.30                      | 1.45                      | 1.56                      | 1.53                      | 1.56                     
Bellman Ford              | -                         | 3.51                      | 3.89                      | 1.08                      | 1.69                      | 1.68                      | 1.65                      | 1.86                     
Dijkstra                  | -                         | 2.38                      | 2.80                      | 1.15                      | 1.70                      | 1.71                      | 1.74                      | 1.85                     
Euler                     | -                         | 2.65                      | 3.17                      | 3.26                      | 1.74                      | 1.68                      | 1.65                      | 1.72                     
Midpoint Explicit         | -                         | 3.07                      | 3.53                      | 3.64                      | 2.22                      | 1.88                      | 2.02                      | 1.97                     
Midpoint Fixed            | -                         | 3.36                      | 4.11                      | 3.85                      | 2.21                      | 1.94                      | 2.19                      | 2.14                     
RK4                       | -                         | 3.49                      | 4.03                      | 4.08                      | 2.34                      | 2.52                      | 2.65                      | 2.52                     
FD - L Convection         | -                         | 2.47                      | 2.81                      | 2.60                      | 1.74                      | 1.72                      | 1.63                      | 1.71                     
FD - NL Convection        | -                         | 4.01                      | 3.81                      | 2.70                      | 1.77                      | 1.64                      | 1.87                      | 1.81                     
FD - Poisson              | -                         | 3.58                      | 4.10                      | 4.40                      | 2.39                      | 1.98                      | 2.76                      | 2.25                     
FD - Laplace              | -                         | 6.93                      | 8.04                      | 5.63                      | 2.23                      | 2.25                      | 2.00                      | 2.57                     
M-D                       | -                         | 6.29                      | 6.60                      | 6.26                      | 2.89                      | 2.77                      | 3.52                      | 2.82                     
Splines                   | -                         | -                         | -                         | 0.75                      | 2.51                      | 1.87                      | 3.32                      | 2.02                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 496.00 $\pm$ 15.00        | 2.70 $\pm$ 0.01           | 3.67 $\pm$ 0.01           | 9.14 $\pm$ 0.49           | 1.33 $\pm$ 0.00           | 1.32 $\pm$ 0.01           | 3.71 $\pm$ 0.00           | 9.54 $\pm$ 0.17          
Bellman Ford (ms)         | 2030.00 $\pm$ 40.00       | 4.59 $\pm$ 0.03           | 3.58 $\pm$ 0.27           | 4.06 $\pm$ 0.02           | 3.28 $\pm$ 0.02           | 3.25 $\pm$ 0.03           | 5.39 $\pm$ 0.05           | 4.19 $\pm$ 0.03          
Dijkstra (ms)             | 5660.00 $\pm$ 70.00       | 17.90 $\pm$ 0.40          | 15.10 $\pm$ 0.40          | 18.50 $\pm$ 0.60          | 38.20 $\pm$ 2.10          | 16.10 $\pm$ 0.10          | 39.60 $\pm$ 0.90          | 19.40 $\pm$ 0.10         
Euler (ms)                | 3750.00 $\pm$ 50.00       | 26.40 $\pm$ 0.60          | 25.60 $\pm$ 0.40          | 36.10 $\pm$ 0.50          | 23.10 $\pm$ 1.00          | 10.80 $\pm$ 0.40          | 23.70 $\pm$ 0.60          | 15.70 $\pm$ 0.60         
Midpoint Explicit (ms)    | 7620.00 $\pm$ 70.00       | 52.80 $\pm$ 0.50          | 51.80 $\pm$ 1.90          | 67.80 $\pm$ 0.30          | 40.50 $\pm$ 0.60          | 19.00 $\pm$ 0.60          | 43.10 $\pm$ 0.70          | 16.10 $\pm$ 0.60         
Midpoint Fixed (ms)       | 37300.00 $\pm$ 200.00     | 268.00 $\pm$ 1.00         | 93.40 $\pm$ 0.60          | 311.00 $\pm$ 2.00         | 180.00 $\pm$ 2.00         | 73.30 $\pm$ 0.50          | 202.00 $\pm$ 1.00         | 52.70 $\pm$ 0.60         
RK4 (ms)                  | 18900.00 $\pm$ 200.00     | 154.00 $\pm$ 2.00         | 35.70 $\pm$ 0.60          | 126.00 $\pm$ 2.00         | 86.30 $\pm$ 1.90          | 32.50 $\pm$ 0.60          | 91.50 $\pm$ 0.70          | 29.30 $\pm$ 0.80         
FD - L Convection (ms)    | 2270.00 $\pm$ 30.00       | 1.53 $\pm$ 0.03           | 1.61 $\pm$ 0.03           | 2.87 $\pm$ 0.08           | 4.37 $\pm$ 0.23           | 1.66 $\pm$ 0.11           | 4.48 $\pm$ 0.04           | 1.51 $\pm$ 0.04          
FD - NL Convection (ms)   | 2860.00 $\pm$ 20.00       | 1.88 $\pm$ 0.03           | 1.70 $\pm$ 0.03           | 2.92 $\pm$ 0.09           | 4.69 $\pm$ 0.00           | 1.55 $\pm$ 0.05           | 4.51 $\pm$ 0.04           | 1.54 $\pm$ 0.04          
FD - Poisson (ms)         | 6420.00 $\pm$ 70.00       | 2.94 $\pm$ 0.04           | 5.54 $\pm$ 0.03           | 6.62 $\pm$ 0.03           | 3.77 $\pm$ 0.06           | 2.65 $\pm$ 0.06           | 6.61 $\pm$ 0.38           | 2.56 $\pm$ 0.03          
FD - Laplace (ms)         | 697.00 $\pm$ 4.00         | 66.70 $\pm$ 1.60          | 106.00 $\pm$ 1.00         | 190.00 $\pm$ 1.00         | 151.00 $\pm$ 1.00         | 61.50 $\pm$ 0.90          | 194.00 $\pm$ 1.00         | 60.00 $\pm$ 1.40         
M-D (ms)                  | 8700.00 $\pm$ 80.00       | 35.30 $\pm$ 0.10          | 50.30 $\pm$ 0.20          | 57.50 $\pm$ 1.10          | 107.00 $\pm$ 0.00         | 62.30 $\pm$ 0.10          | 88.90 $\pm$ 0.10          | 90.70 $\pm$ 0.10         
Splines (ms)              | 1800.00 $\pm$ 30.00       | -                         | -                         | 17.80 $\pm$ 0.40          | 13.60 $\pm$ 0.00          | 17.70 $\pm$ 0.00          | 15.30 $\pm$ 0.50          | 27.70 $\pm$ 0.10         

![Python 3.12 compilation results](./version_specific_results/pypi_performance_312_compilation.svg)
![Python 3.12 execution results](./version_specific_results/pypi_performance_312_execution.svg)
## Python 3.13 results
### Performance Comparison (as of 2.2.2)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.04                      | 2.14                      | 0.29                      | 1.44                      | 1.47                      | 1.47                      | 1.55                     
Bellman Ford              | -                         | 3.45                      | 3.73                      | 1.12                      | 1.62                      | 1.61                      | 1.65                      | 1.76                     
Dijkstra                  | -                         | 2.32                      | 2.66                      | 1.16                      | 1.74                      | 1.73                      | 1.75                      | 1.87                     
Euler                     | -                         | 2.69                      | 3.09                      | 3.26                      | 1.59                      | 1.59                      | 1.64                      | 1.73                     
Midpoint Explicit         | -                         | 3.03                      | 3.51                      | 3.65                      | 1.82                      | 1.81                      | 1.84                      | 1.92                     
Midpoint Fixed            | -                         | 3.27                      | 3.78                      | 3.69                      | 1.90                      | 1.90                      | 1.93                      | 2.01                     
RK4                       | -                         | 3.50                      | 4.00                      | 3.73                      | 2.24                      | 2.28                      | 2.24                      | 2.36                     
FD - L Convection         | -                         | 2.31                      | 2.68                      | 2.56                      | 1.54                      | 1.55                      | 1.58                      | 1.66                     
FD - NL Convection        | -                         | 3.36                      | 3.60                      | 2.66                      | 1.56                      | 1.58                      | 1.65                      | 1.72                     
FD - Poisson              | -                         | 3.54                      | 3.77                      | 4.09                      | 2.19                      | 1.87                      | 2.68                      | 2.08                     
FD - Laplace              | -                         | 6.90                      | 7.71                      | 5.28                      | 1.94                      | 2.01                      | 1.91                      | 2.11                     
M-D                       | -                         | 6.02                      | 6.71                      | 6.35                      | 2.99                      | 2.73                      | 3.52                      | 2.91                     
Splines                   | -                         | -                         | -                         | 0.77                      | 2.34                      | 1.99                      | 2.90                      | 2.12                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 496.00 $\pm$ 7.00         | 2.71 $\pm$ 0.06           | 3.67 $\pm$ 0.02           | 8.90 $\pm$ 0.47           | 1.33 $\pm$ 0.00           | 1.32 $\pm$ 0.00           | 3.71 $\pm$ 0.01           | 10.50 $\pm$ 0.20         
Bellman Ford (ms)         | 2250.00 $\pm$ 30.00       | 4.59 $\pm$ 0.02           | 3.53 $\pm$ 0.04           | 4.07 $\pm$ 0.02           | 3.31 $\pm$ 0.10           | 3.26 $\pm$ 0.04           | 5.38 $\pm$ 0.03           | 4.17 $\pm$ 0.02          
Dijkstra (ms)             | 5320.00 $\pm$ 60.00       | 16.80 $\pm$ 0.10          | 14.70 $\pm$ 0.10          | 18.80 $\pm$ 0.60          | 35.80 $\pm$ 0.30          | 16.60 $\pm$ 0.40          | 39.40 $\pm$ 0.20          | 19.20 $\pm$ 0.30         
Euler (ms)                | 3920.00 $\pm$ 30.00       | 26.50 $\pm$ 0.50          | 27.90 $\pm$ 6.60          | 37.20 $\pm$ 3.70          | 22.20 $\pm$ 0.80          | 11.10 $\pm$ 0.60          | 23.40 $\pm$ 0.30          | 15.10 $\pm$ 0.50         
Midpoint Explicit (ms)    | 7940.00 $\pm$ 70.00       | 53.30 $\pm$ 0.80          | 51.20 $\pm$ 0.60          | 68.40 $\pm$ 0.60          | 41.50 $\pm$ 3.80          | 19.00 $\pm$ 0.50          | 43.90 $\pm$ 3.60          | 16.80 $\pm$ 0.70         
Midpoint Fixed (ms)       | 39400.00 $\pm$ 200.00     | 268.00 $\pm$ 1.00         | 93.30 $\pm$ 0.60          | 311.00 $\pm$ 3.00         | 178.00 $\pm$ 1.00         | 72.60 $\pm$ 0.70          | 201.00 $\pm$ 1.00         | 50.80 $\pm$ 0.70         
RK4 (ms)                  | 19600.00 $\pm$ 100.00     | 155.00 $\pm$ 3.00         | 35.70 $\pm$ 0.60          | 125.00 $\pm$ 1.00         | 84.80 $\pm$ 0.60          | 32.10 $\pm$ 0.40          | 90.10 $\pm$ 0.50          | 28.20 $\pm$ 0.50         
FD - L Convection (ms)    | 2740.00 $\pm$ 90.00       | 1.55 $\pm$ 0.04           | 1.64 $\pm$ 0.04           | 2.86 $\pm$ 0.04           | 4.55 $\pm$ 0.35           | 1.66 $\pm$ 0.05           | 4.34 $\pm$ 0.12           | 1.35 $\pm$ 0.06          
FD - NL Convection (ms)   | 3490.00 $\pm$ 110.00      | 1.87 $\pm$ 0.03           | 1.67 $\pm$ 0.05           | 2.90 $\pm$ 0.04           | 4.71 $\pm$ 0.05           | 1.55 $\pm$ 0.05           | 4.22 $\pm$ 0.21           | 1.54 $\pm$ 0.03          
FD - Poisson (ms)         | 6910.00 $\pm$ 150.00      | 3.00 $\pm$ 0.15           | 5.58 $\pm$ 0.09           | 6.63 $\pm$ 0.04           | 3.75 $\pm$ 0.03           | 2.61 $\pm$ 0.02           | 6.44 $\pm$ 0.03           | 2.56 $\pm$ 0.02          
FD - Laplace (ms)         | 707.00 $\pm$ 6.00         | 64.40 $\pm$ 0.50          | 106.00 $\pm$ 3.00         | 190.00 $\pm$ 2.00         | 151.00 $\pm$ 1.00         | 60.90 $\pm$ 0.50          | 197.00 $\pm$ 0.00         | 59.50 $\pm$ 0.50         
M-D (ms)                  | 9060.00 $\pm$ 290.00      | 36.10 $\pm$ 1.00          | 50.40 $\pm$ 0.30          | 57.30 $\pm$ 0.50          | 106.00 $\pm$ 2.00         | 62.20 $\pm$ 0.20          | 88.90 $\pm$ 0.30          | 90.50 $\pm$ 1.20         
Splines (ms)              | 2020.00 $\pm$ 30.00       | -                         | -                         | 17.80 $\pm$ 0.20          | 13.40 $\pm$ 0.00          | 17.70 $\pm$ 0.10          | 15.20 $\pm$ 0.10          | 27.80 $\pm$ 0.10         

![Python 3.13 compilation results](./version_specific_results/pypi_performance_313_compilation.svg)
![Python 3.13 execution results](./version_specific_results/pypi_performance_313_execution.svg)
## Python 3.14 results
### Performance Comparison (as of 2.2.2)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.05                      | 2.19                      | 0.30                      | 1.48                      | 1.50                      | 1.52                      | 1.59                     
Bellman Ford              | -                         | 3.38                      | 3.76                      | 0.98                      | 1.64                      | 1.64                      | 1.69                      | 1.73                     
Dijkstra                  | -                         | 2.34                      | 2.68                      | 1.10                      | 1.74                      | 1.79                      | 1.78                      | 1.88                     
Euler                     | -                         | 2.64                      | 3.06                      | 3.21                      | 1.62                      | 1.61                      | 1.66                      | 1.73                     
Midpoint Explicit         | -                         | 2.97                      | 3.41                      | 3.54                      | 1.94                      | 1.96                      | 1.99                      | 2.01                     
Midpoint Fixed            | -                         | 3.35                      | 3.76                      | 3.68                      | 1.97                      | 1.96                      | 2.01                      | 2.12                     
RK4                       | -                         | 3.47                      | 3.98                      | 3.71                      | 2.40                      | 2.46                      | 2.41                      | 2.57                     
FD - L Convection         | -                         | 2.35                      | 2.76                      | 2.62                      | 1.63                      | 1.62                      | 1.66                      | 1.78                     
FD - NL Convection        | -                         | 3.49                      | 3.69                      | 2.67                      | 1.60                      | 1.61                      | 1.62                      | 1.70                     
FD - Poisson              | -                         | 3.45                      | 3.80                      | 4.11                      | 2.21                      | 1.87                      | 2.70                      | 2.10                     
FD - Laplace              | -                         | 7.07                      | 7.88                      | 5.45                      | 2.03                      | 2.11                      | 1.99                      | 2.21                     
M-D                       | -                         | 6.07                      | 6.67                      | 6.16                      | 2.90                      | 2.68                      | 3.56                      | 2.84                     
Splines                   | -                         | -                         | -                         | 0.74                      | 2.33                      | 1.90                      | 2.79                      | 2.08                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_gnu_c              | pyccel_gnu_fortran        | pyccel_intel_c            | pyccel_intel_fortran     
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 505.00 $\pm$ 3.00         | 2.70 $\pm$ 0.00           | 3.67 $\pm$ 0.02           | 8.92 $\pm$ 0.49           | 1.23 $\pm$ 0.00           | 1.28 $\pm$ 0.00           | 3.81 $\pm$ 0.12           | 9.32 $\pm$ 0.15          
Bellman Ford (ms)         | 2150.00 $\pm$ 40.00       | 4.53 $\pm$ 0.02           | 3.57 $\pm$ 0.09           | 4.12 $\pm$ 0.18           | 3.28 $\pm$ 0.02           | 3.24 $\pm$ 0.02           | 5.49 $\pm$ 0.03           | 4.17 $\pm$ 0.02          
Dijkstra (ms)             | 5090.00 $\pm$ 80.00       | 17.20 $\pm$ 0.30          | 15.10 $\pm$ 0.20          | 18.00 $\pm$ 0.40          | 34.40 $\pm$ 0.40          | 16.50 $\pm$ 0.40          | 39.30 $\pm$ 0.30          | 19.70 $\pm$ 0.20         
Euler (ms)                | 3710.00 $\pm$ 40.00       | 25.90 $\pm$ 0.60          | 26.00 $\pm$ 0.50          | 36.30 $\pm$ 0.50          | 22.50 $\pm$ 0.80          | 10.60 $\pm$ 0.00          | 23.30 $\pm$ 0.30          | 14.70 $\pm$ 0.50         
Midpoint Explicit (ms)    | 7640.00 $\pm$ 120.00      | 52.60 $\pm$ 0.50          | 51.50 $\pm$ 1.80          | 68.00 $\pm$ 0.60          | 40.20 $\pm$ 0.40          | 19.80 $\pm$ 0.50          | 44.00 $\pm$ 3.80          | 15.80 $\pm$ 0.50         
Midpoint Fixed (ms)       | 38000.00 $\pm$ 500.00     | 267.00 $\pm$ 3.00         | 92.50 $\pm$ 0.50          | 325.00 $\pm$ 46.00        | 178.00 $\pm$ 2.00         | 73.50 $\pm$ 1.30          | 202.00 $\pm$ 1.00         | 50.80 $\pm$ 0.40         
RK4 (ms)                  | 18800.00 $\pm$ 200.00     | 158.00 $\pm$ 3.00         | 35.60 $\pm$ 0.60          | 132.00 $\pm$ 1.00         | 87.70 $\pm$ 2.50          | 32.00 $\pm$ 0.10          | 91.40 $\pm$ 1.50          | 28.70 $\pm$ 0.50         
FD - L Convection (ms)    | 2560.00 $\pm$ 20.00       | 1.68 $\pm$ 0.04           | 1.62 $\pm$ 0.03           | 2.84 $\pm$ 0.05           | 4.58 $\pm$ 0.01           | 1.67 $\pm$ 0.06           | 4.33 $\pm$ 0.16           | 1.52 $\pm$ 0.03          
FD - NL Convection (ms)   | 3230.00 $\pm$ 30.00       | 2.02 $\pm$ 0.05           | 1.65 $\pm$ 0.04           | 2.91 $\pm$ 0.06           | 4.69 $\pm$ 0.00           | 1.63 $\pm$ 0.03           | 4.19 $\pm$ 0.22           | 1.39 $\pm$ 0.02          
FD - Poisson (ms)         | 7000.00 $\pm$ 80.00       | 2.99 $\pm$ 0.03           | 5.58 $\pm$ 0.05           | 6.64 $\pm$ 0.04           | 3.76 $\pm$ 0.03           | 2.62 $\pm$ 0.03           | 6.48 $\pm$ 0.05           | 2.55 $\pm$ 0.03          
FD - Laplace (ms)         | 714.00 $\pm$ 14.00        | 63.60 $\pm$ 0.50          | 106.00 $\pm$ 1.00         | 191.00 $\pm$ 1.00         | 151.00 $\pm$ 0.00         | 60.50 $\pm$ 1.80          | 193.00 $\pm$ 1.00         | 59.70 $\pm$ 0.40         
M-D (ms)                  | 8900.00 $\pm$ 60.00       | 34.40 $\pm$ 0.20          | 50.30 $\pm$ 0.30          | 57.00 $\pm$ 0.10          | 107.00 $\pm$ 0.00         | 62.40 $\pm$ 0.30          | 88.80 $\pm$ 0.20          | 90.90 $\pm$ 0.60         
Splines (ms)              | 1930.00 $\pm$ 20.00       | -                         | -                         | 16.40 $\pm$ 0.20          | 13.60 $\pm$ 0.00          | 18.80 $\pm$ 3.50          | 15.20 $\pm$ 0.20          | 27.90 $\pm$ 0.10         

![Python 3.14 compilation results](./version_specific_results/pypi_performance_314_compilation.svg)
![Python 3.14 execution results](./version_specific_results/pypi_performance_314_execution.svg)
