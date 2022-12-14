# Benchmarks

Several tests are available for the user to benchmark Pyccel against other common accelerators, notably [pythran](https://pythran.readthedocs.io/en/latest/) and [numba](https://numba.pydata.org/).
The same code is used for all tests, only the decorators change.

The dependencies can be installed using the command `python3 -m pip install .`

The code can be executed by running the script `benchmarks/run_benchmarks.py`.
Additional options can be used with this script to add additional comparisons, change the output format, or change what is generated.

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
### Performance Comparison (as of Wed Dec 14 07:59:25 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.48                      | 0.40                      | 1.58                      | 1.48                     
Bellman Ford              | -                         | 3.25                      | 1.13                      | 2.31                      | 2.18                     
Dijkstra                  | -                         | 3.16                      | 1.46                      | 2.38                      | 2.26                     
Euler                     | -                         | 3.69                      | 1.51                      | 2.30                      | 2.27                     
Midpoint Explicit         | -                         | 4.48                      | 2.35                      | 2.72                      | 2.63                     
Midpoint Fixed            | -                         | 4.99                      | 2.72                      | 2.79                      | 2.79                     
RK4                       | -                         | 5.28                      | 2.80                      | 3.41                      | 3.29                     
FD - L Convection         | -                         | 2.94                      | 0.37                      | 2.17                      | 2.17                     
FD - NL Convection        | -                         | 2.88                      | 0.37                      | 2.17                      | 2.18                     
FD - Poisson              | -                         | 8.54                      | 0.90                      | 2.32                      | 2.26                     
FD - Laplace              | -                         | 12.40                     | 2.04                      | 2.99                      | -                        
M-D                       | -                         | -                         | 6.24                      | 3.52                      | 3.19                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 435.00                    | 4.61                      | 21.70                     | 2.52                      | 2.80                     
Bellman Ford (ns)         | 72100.00                  | 459.00                    | 800.00                    | 253.00                    | 552.00                   
Dijkstra (ns)             | 34500.00                  | 378.00                    | 600.00                    | 307.00                    | 573.00                   
Euler (ms)                | 54.40                     | 0.79                      | 1.32                      | 0.16                      | 3.47                     
Midpoint Explicit (ms)    | 111.00                    | 1.79                      | 3.21                      | 0.26                      | 6.23                     
Midpoint Fixed (ms)       | 544.00                    | 10.80                     | 19.30                     | 1.36                      | 27.40                    
RK4 (ms)                  | 288.00                    | 2.29                      | 6.93                      | 0.32                      | 7.60                     
FD - L Convection (ms)    | 2400.00                   | 1.91                      | 11.30                     | 1.79                      | 2.05                     
FD - NL Convection (ms)   | 3080.00                   | 2.21                      | 10.90                     | 1.75                      | 1.98                     
FD - Poisson (ms)         | 5150.00                   | 2.42                      | 12.60                     | 4.65                      | 2.05                     
FD - Laplace (\textmu s)  | 48.70                     | 2.89                      | 9920.00                   | 2.38                      | -                        
M-D (ms)                  | 54300.00                  | -                         | 256.00                    | 313.00                    | 325.00                   

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.7 results
### Performance Comparison (as of 1.7.0)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.90                      | 0.37                      | 1.33                      | 1.21                     
Bellman Ford              | -                         | 2.51                      | 1.02                      | 1.90                      | 1.83                     
Dijkstra                  | -                         | 2.55                      | 1.35                      | 1.97                      | 1.87                     
Euler                     | -                         | 3.05                      | 1.37                      | 1.93                      | 1.88                     
Midpoint Explicit         | -                         | 3.63                      | 2.10                      | 2.29                      | 2.21                     
Midpoint Fixed            | -                         | 4.28                      | 2.42                      | 2.36                      | 2.31                     
RK4                       | -                         | 4.36                      | 2.48                      | 2.89                      | 2.80                     
FD - L Convection         | -                         | 2.31                      | 0.33                      | 1.80                      | 1.79                     
FD - NL Convection        | -                         | 2.28                      | 0.33                      | 1.78                      | 1.80                     
FD - Poisson              | -                         | 7.01                      | 0.81                      | 1.90                      | 1.90                     
FD - Laplace              | -                         | 10.49                     | 1.84                      | 2.55                      | -                        
M-D                       | -                         | -                         | 5.50                      | 3.02                      | 2.72                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 518.00 $\pm$ 3.00         | 8.92 $\pm$ 0.00           | 31.10 $\pm$ 0.30          | 3.16 $\pm$ 0.00           | 3.33 $\pm$ 0.01          
Bellman Ford (ns)         | 64800.00 $\pm$ 1100.00    | 376.00 $\pm$ 5.00         | 544.00 $\pm$ 13.00        | 222.00 $\pm$ 6.00         | 488.00 $\pm$ 4.00        
Dijkstra (ns)             | 34100.00 $\pm$ 700.00     | 321.00 $\pm$ 5.00         | 378.00 $\pm$ 9.00         | 279.00 $\pm$ 8.00         | 477.00 $\pm$ 4.00        
Euler (ms)                | 56.30 $\pm$ 1.40          | 0.74 $\pm$ 0.01           | 1.13 $\pm$ 0.02           | 0.13 $\pm$ 0.00           | 2.95 $\pm$ 0.02          
Midpoint Explicit (ms)    | 114.00 $\pm$ 1.00         | 1.54 $\pm$ 0.03           | 2.88 $\pm$ 0.04           | 0.23 $\pm$ 0.01           | 5.30 $\pm$ 0.06          
Midpoint Fixed (ms)       | 568.00 $\pm$ 9.00         | 9.63 $\pm$ 0.18           | 15.90 $\pm$ 0.10          | 0.96 $\pm$ 0.05           | 23.40 $\pm$ 0.10         
RK4 (ms)                  | 262.00 $\pm$ 7.00         | 1.92 $\pm$ 0.01           | 5.74 $\pm$ 0.05           | 0.27 $\pm$ 0.00           | 6.35 $\pm$ 0.09          
FD - L Convection (ms)    | 2240.00 $\pm$ 90.00       | 1.76 $\pm$ 0.02           | 9.37 $\pm$ 0.05           | 1.65 $\pm$ 0.01           | 1.53 $\pm$ 0.02          
FD - NL Convection (ms)   | 3180.00 $\pm$ 50.00       | 1.83 $\pm$ 0.04           | 9.23 $\pm$ 0.06           | 1.65 $\pm$ 0.01           | 1.64 $\pm$ 0.02          
FD - Poisson (ms)         | 4670.00 $\pm$ 80.00       | 2.03 $\pm$ 0.01           | 10.50 $\pm$ 0.00          | 3.88 $\pm$ 0.00           | 1.76 $\pm$ 0.00          
FD - Laplace (\textmu s)  | 50.00 $\pm$ 0.80          | 2.37 $\pm$ 0.01           | 8.78 $\pm$ 0.06           | 1.98 $\pm$ 0.01           | -                        
M-D (ms)                  | 52700.00 $\pm$ 1000.00    | -                         | 221.00 $\pm$ 2.00         | 269.00 $\pm$ 0.00         | 274.00 $\pm$ 0.00        

![Python 3.7 compilation results](./version_specific_results/pypi_performance_37_compilation.svg)
![Python 3.7 execution results](./version_specific_results/pypi_performance_37_execution.svg)
## Python 3.8 results
### Performance Comparison (as of 1.7.0)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.75                      | 0.33                      | 1.21                      | 1.11                     
Bellman Ford              | -                         | 2.37                      | 0.91                      | 1.81                      | 1.71                     
Dijkstra                  | -                         | 2.38                      | 1.20                      | 1.87                      | 1.77                     
Euler                     | -                         | 2.83                      | 1.27                      | 1.83                      | 1.78                     
Midpoint Explicit         | -                         | 3.40                      | 1.95                      | 2.15                      | 2.09                     
Midpoint Fixed            | -                         | 3.92                      | 2.25                      | 2.21                      | 2.18                     
RK4                       | -                         | 4.06                      | 2.32                      | 2.71                      | 2.62                     
FD - L Convection         | -                         | 2.15                      | 0.31                      | 1.68                      | 1.68                     
FD - NL Convection        | -                         | 2.14                      | 0.31                      | 1.70                      | 1.70                     
FD - Poisson              | -                         | 6.59                      | 0.73                      | 1.78                      | 1.76                     
FD - Laplace              | -                         | 9.81                      | 1.68                      | 2.40                      | -                        
M-D                       | -                         | -                         | 5.18                      | 2.84                      | 2.55                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 475.00 $\pm$ 6.00         | 10.40 $\pm$ 0.10          | 32.30 $\pm$ 0.20          | 3.20 $\pm$ 0.00           | 3.33 $\pm$ 0.00          
Bellman Ford (ns)         | 58900.00 $\pm$ 700.00     | 371.00 $\pm$ 2.00         | 542.00 $\pm$ 5.00         | 225.00 $\pm$ 2.00         | 485.00 $\pm$ 7.00        
Dijkstra (ns)             | 30600.00 $\pm$ 200.00     | 320.00 $\pm$ 3.00         | 355.00 $\pm$ 8.00         | 245.00 $\pm$ 1.00         | 479.00 $\pm$ 6.00        
Euler (ms)                | 46.00 $\pm$ 0.70          | 0.63 $\pm$ 0.00           | 1.28 $\pm$ 0.02           | 0.14 $\pm$ 0.00           | 2.60 $\pm$ 0.02          
Midpoint Explicit (ms)    | 94.40 $\pm$ 1.30          | 1.45 $\pm$ 0.02           | 3.15 $\pm$ 0.04           | 0.24 $\pm$ 0.01           | 4.58 $\pm$ 0.03          
Midpoint Fixed (ms)       | 473.00 $\pm$ 6.00         | 8.90 $\pm$ 0.66           | 17.60 $\pm$ 0.20          | 1.01 $\pm$ 0.02           | 20.00 $\pm$ 0.60         
RK4 (ms)                  | 238.00 $\pm$ 4.00         | 2.06 $\pm$ 0.02           | 6.36 $\pm$ 0.07           | 0.28 $\pm$ 0.00           | 5.43 $\pm$ 0.06          
FD - L Convection (ms)    | 2330.00 $\pm$ 30.00       | 1.81 $\pm$ 0.00           | 9.23 $\pm$ 0.20           | 1.70 $\pm$ 0.01           | 1.55 $\pm$ 0.00          
FD - NL Convection (ms)   | 2930.00 $\pm$ 30.00       | 1.74 $\pm$ 0.06           | 9.41 $\pm$ 0.09           | 1.61 $\pm$ 0.00           | 1.58 $\pm$ 0.00          
FD - Poisson (ms)         | 4130.00 $\pm$ 20.00       | 2.35 $\pm$ 0.00           | 10.90 $\pm$ 0.10          | 3.95 $\pm$ 0.00           | 2.04 $\pm$ 0.01          
FD - Laplace (\textmu s)  | 52.00 $\pm$ 0.90          | 2.46 $\pm$ 0.03           | 8.95 $\pm$ 0.06           | 2.10 $\pm$ 0.01           | -                        
M-D (ms)                  | 50200.00 $\pm$ 1200.00    | -                         | 230.00 $\pm$ 2.00         | 302.00 $\pm$ 0.00         | 302.00 $\pm$ 0.00        

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.7.0)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.30                      | 0.41                      | 1.64                      | 1.50                     
Bellman Ford              | -                         | 3.10                      | 1.14                      | 2.31                      | 2.22                     
Dijkstra                  | -                         | 3.09                      | 1.50                      | 2.46                      | 2.30                     
Euler                     | -                         | 3.76                      | 1.56                      | 2.35                      | 2.29                     
Midpoint Explicit         | -                         | 4.53                      | 2.40                      | 2.75                      | 2.77                     
Midpoint Fixed            | -                         | 5.14                      | 2.75                      | 2.86                      | 2.83                     
RK4                       | -                         | 5.34                      | 2.86                      | 3.47                      | 3.36                     
FD - L Convection         | -                         | 2.79                      | 0.38                      | 2.20                      | 2.18                     
FD - NL Convection        | -                         | 2.82                      | 0.38                      | 2.21                      | 2.21                     
FD - Poisson              | -                         | 8.39                      | 0.91                      | 2.31                      | 2.33                     
FD - Laplace              | -                         | 12.89                     | 2.08                      | 3.06                      | -                        
M-D                       | -                         | -                         | 6.40                      | 3.63                      | 3.24                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 454.00 $\pm$ 3.00         | 4.77 $\pm$ 0.02           | 21.80 $\pm$ 0.00          | 2.57 $\pm$ 0.06           | 2.84 $\pm$ 0.03          
Bellman Ford (ns)         | 70700.00 $\pm$ 700.00     | 457.00 $\pm$ 24.00        | 643.00 $\pm$ 12.00        | 263.00 $\pm$ 8.00         | 582.00 $\pm$ 9.00        
Dijkstra (ns)             | 34300.00 $\pm$ 200.00     | 383.00 $\pm$ 3.00         | 452.00 $\pm$ 7.00         | 316.00 $\pm$ 1.00         | 557.00 $\pm$ 1.00        
Euler (ms)                | 53.90 $\pm$ 0.50          | 0.82 $\pm$ 0.02           | 1.34 $\pm$ 0.01           | 0.16 $\pm$ 0.00           | 3.53 $\pm$ 0.03          
Midpoint Explicit (ms)    | 111.00 $\pm$ 1.00         | 1.81 $\pm$ 0.03           | 3.50 $\pm$ 0.09           | 0.27 $\pm$ 0.01           | 6.33 $\pm$ 0.07          
Midpoint Fixed (ms)       | 553.00 $\pm$ 9.00         | 11.10 $\pm$ 0.00          | 19.30 $\pm$ 0.10          | 1.14 $\pm$ 0.04           | 27.80 $\pm$ 0.10         
RK4 (ms)                  | 276.00 $\pm$ 4.00         | 2.32 $\pm$ 0.03           | 6.95 $\pm$ 0.04           | 0.32 $\pm$ 0.01           | 7.52 $\pm$ 0.11          
FD - L Convection (ms)    | 2730.00 $\pm$ 30.00       | 2.04 $\pm$ 0.06           | 11.30 $\pm$ 0.10          | 1.86 $\pm$ 0.03           | 1.85 $\pm$ 0.02          
FD - NL Convection (ms)   | 3430.00 $\pm$ 40.00       | 2.28 $\pm$ 0.02           | 11.10 $\pm$ 0.10          | 1.94 $\pm$ 0.04           | 2.20 $\pm$ 0.03          
FD - Poisson (ms)         | 5120.00 $\pm$ 40.00       | 2.43 $\pm$ 0.01           | 12.60 $\pm$ 0.10          | 4.67 $\pm$ 0.00           | 2.11 $\pm$ 0.02          
FD - Laplace (\textmu s)  | 67.30 $\pm$ 2.20          | 3.03 $\pm$ 0.01           | 10.40 $\pm$ 0.10          | 2.35 $\pm$ 0.01           | -                        
M-D (ms)                  | 53900.00 $\pm$ 1200.00    | -                         | 265.00 $\pm$ 3.00         | 323.00 $\pm$ 1.00         | 329.00 $\pm$ 1.00        

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.7.0)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.03                      | 0.33                      | 1.35                      | 1.23                     
Bellman Ford              | -                         | 2.62                      | 0.95                      | 1.88                      | 1.83                     
Dijkstra                  | -                         | 2.64                      | 1.24                      | 1.90                      | 1.89                     
Euler                     | -                         | 3.06                      | 1.32                      | 1.94                      | 1.89                     
Midpoint Explicit         | -                         | 3.66                      | 2.02                      | 2.29                      | 2.18                     
Midpoint Fixed            | -                         | 4.22                      | 2.32                      | 2.34                      | 2.29                     
RK4                       | -                         | 4.41                      | 2.38                      | 2.80                      | 2.77                     
FD - L Convection         | -                         | 2.44                      | 0.32                      | 1.78                      | 1.80                     
FD - NL Convection        | -                         | 2.37                      | 0.31                      | 1.80                      | 1.79                     
FD - Poisson              | -                         | 6.91                      | 0.75                      | 1.88                      | 1.89                     
FD - Laplace              | -                         | 10.14                     | 1.74                      | 2.53                      | -                        
M-D                       | -                         | -                         | 5.25                      | 3.00                      | 2.65                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 394.00 $\pm$ 4.00         | 9.72 $\pm$ 0.02           | 32.30 $\pm$ 0.30          | 3.14 $\pm$ 0.00           | 3.28 $\pm$ 0.01          
Bellman Ford (ns)         | 57200.00 $\pm$ 500.00     | 348.00 $\pm$ 3.00         | 539.00 $\pm$ 4.00         | 211.00 $\pm$ 2.00         | 500.00 $\pm$ 11.00       
Dijkstra (ns)             | 30400.00 $\pm$ 400.00     | 320.00 $\pm$ 1.00         | 347.00 $\pm$ 5.00         | 252.00 $\pm$ 1.00         | 462.00 $\pm$ 6.00        
Euler (ms)                | 48.80 $\pm$ 0.50          | 0.64 $\pm$ 0.02           | 1.29 $\pm$ 0.03           | 0.14 $\pm$ 0.00           | 2.55 $\pm$ 0.02          
Midpoint Explicit (ms)    | 99.90 $\pm$ 1.40          | 1.45 $\pm$ 0.05           | 3.16 $\pm$ 0.04           | 0.24 $\pm$ 0.00           | 4.52 $\pm$ 0.07          
Midpoint Fixed (ms)       | 498.00 $\pm$ 4.00         | 8.78 $\pm$ 0.06           | 17.60 $\pm$ 0.20          | 0.97 $\pm$ 0.01           | 19.80 $\pm$ 0.20         
RK4 (ms)                  | 254.00 $\pm$ 2.00         | 2.08 $\pm$ 0.02           | 6.37 $\pm$ 0.07           | 0.28 $\pm$ 0.00           | 5.47 $\pm$ 0.17          
FD - L Convection (ms)    | 1910.00 $\pm$ 20.00       | 1.65 $\pm$ 0.09           | 9.18 $\pm$ 0.19           | 1.82 $\pm$ 0.06           | 1.77 $\pm$ 0.10          
FD - NL Convection (ms)   | 2440.00 $\pm$ 100.00      | 1.85 $\pm$ 0.10           | 9.46 $\pm$ 0.20           | 1.66 $\pm$ 0.08           | 1.70 $\pm$ 0.17          
FD - Poisson (ms)         | 4820.00 $\pm$ 190.00      | 2.35 $\pm$ 0.01           | 10.90 $\pm$ 0.00          | 3.96 $\pm$ 0.00           | 2.04 $\pm$ 0.00          
FD - Laplace (\textmu s)  | 55.10 $\pm$ 0.50          | 2.76 $\pm$ 0.03           | 8.86 $\pm$ 0.08           | 1.96 $\pm$ 0.01           | -                        
M-D (ms)                  | 51500.00 $\pm$ 1100.00    | -                         | 231.00 $\pm$ 2.00         | 305.00 $\pm$ 8.00         | 302.00 $\pm$ 0.00        

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.7.0)
## Compilation time
Algorithm                 | python                    | pythran                   | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.09                      | 1.40                      | 1.26                     
Bellman Ford              | -                         | 2.72                      | 2.00                      | 1.89                     
Dijkstra                  | -                         | 2.67                      | 2.10                      | 2.00                     
Euler                     | -                         | 3.18                      | 1.99                      | 1.95                     
Midpoint Explicit         | -                         | 3.87                      | 2.37                      | 2.25                     
Midpoint Fixed            | -                         | 4.27                      | 2.37                      | 2.36                     
RK4                       | -                         | 4.55                      | 2.86                      | 2.81                     
FD - L Convection         | -                         | 2.49                      | 1.82                      | 1.81                     
FD - NL Convection        | -                         | 2.48                      | 1.84                      | 1.87                     
FD - Poisson              | -                         | 7.13                      | 1.94                      | 1.91                     
FD - Laplace              | -                         | 10.65                     | 2.55                      | -                        
M-D                       | -                         | -                         | 2.91                      | 2.67                     

## Execution time
Algorithm                 | python                    | pythran                   | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 404.00 $\pm$ 3.00         | 7.89 $\pm$ 0.02           | 3.16 $\pm$ 0.00           | 3.34 $\pm$ 0.01          
Bellman Ford (ns)         | 58500.00 $\pm$ 300.00     | 379.00 $\pm$ 2.00         | 223.00 $\pm$ 2.00         | 499.00 $\pm$ 2.00        
Dijkstra (ns)             | 27500.00 $\pm$ 200.00     | 321.00 $\pm$ 2.00         | 269.00 $\pm$ 1.00         | 474.00 $\pm$ 2.00        
Euler (\textmu s)         | 45300.00 $\pm$ 700.00     | 684.00 $\pm$ 8.00         | 132.00 $\pm$ 7.00         | 2990.00 $\pm$ 120.00     
Midpoint Explicit (ms)    | 91.40 $\pm$ 1.40          | 1.51 $\pm$ 0.01           | 0.23 $\pm$ 0.00           | 5.30 $\pm$ 0.02          
Midpoint Fixed (ms)       | 448.00 $\pm$ 4.00         | 9.28 $\pm$ 0.01           | 0.94 $\pm$ 0.00           | 23.30 $\pm$ 0.00         
RK4 (ms)                  | 229.00 $\pm$ 4.00         | 1.92 $\pm$ 0.01           | 0.27 $\pm$ 0.00           | 6.31 $\pm$ 0.01          
FD - L Convection (ms)    | 2090.00 $\pm$ 40.00       | 1.58 $\pm$ 0.08           | 1.63 $\pm$ 0.01           | 1.55 $\pm$ 0.02          
FD - NL Convection (ms)   | 2660.00 $\pm$ 40.00       | 1.83 $\pm$ 0.05           | 1.64 $\pm$ 0.01           | 1.66 $\pm$ 0.02          
FD - Poisson (ms)         | 4270.00 $\pm$ 50.00       | 2.03 $\pm$ 0.01           | 3.88 $\pm$ 0.00           | 1.76 $\pm$ 0.00          
FD - Laplace (\textmu s)  | 51.70 $\pm$ 0.70          | 2.54 $\pm$ 0.05           | 2.06 $\pm$ 0.02           | -                        
M-D (ms)                  | 45500.00 $\pm$ 1500.00    | -                         | 269.00 $\pm$ 0.00         | 274.00 $\pm$ 0.00        

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
