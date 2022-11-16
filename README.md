# Benchmarks

Several tests are available for the user to benchmark Pyccel against other common accelerators, notably [pythran](https://pythran.readthedocs.io/en/latest/) and [numba](https://numba.pydata.org/).
The same code is used for all tests, only the decorators change.

The code can be executed by running the script `run_benchmarks.py`.
Additional options can be used with this script to add additional comparisons, change the output format, or change what is generated.

Run `python3 run_benchmarks.py --help` for more details.

The results below are presented for the current state of the development branch of pyccel, as well as the most recent version of pyccel available on pypi.
## Tests used

The tests used can be found in the [benchmark_code/](./benchmark_code) directory

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
### Performance Comparison (as of Wed Nov 16 20:48:57 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.10                      | 0.28                      | 1.02                      | 0.98                     
Bellman Ford              | -                         | 2.34                      | 0.76                      | 1.47                      | 1.41                     
Dijkstra                  | -                         | 2.37                      | 1.00                      | 1.52                      | -                        
Euler                     | -                         | 2.77                      | 0.85                      | 1.50                      | 1.44                     
Midpoint Explicit         | -                         | 3.45                      | 1.21                      | 1.76                      | 1.69                     
Midpoint Fixed            | -                         | 4.08                      | 1.28                      | 1.81                      | 1.76                     
RK4                       | -                         | 3.98                      | 1.32                      | 2.22                      | 2.14                     
FD - L Convection         | -                         | 2.08                      | 0.24                      | 1.38                      | 1.37                     
FD - NL Convection        | -                         | 2.07                      | 0.24                      | 1.38                      | 1.37                     
FD - Poisson              | -                         | 6.26                      | 0.54                      | 1.46                      | 1.45                     
FD - Laplace              | -                         | 10.00                     | 1.12                      | 1.99                      | -                        
M-D                       | -                         | -                         | 2.58                      | 2.30                      | 2.07                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 314.00                    | 10.20                     | 18.00                     | 2.62                      | 3.04                     
Bellman Ford (ns)         | 45700.00                  | 242.00                    | 480.00                    | 157.00                    | 351.00                   
Dijkstra (ns)             | 22200.00                  | 222.00                    | 421.00                    | 195.00                    | -                        
Euler (\textmu s)         | 38400.00                  | 412.00                    | 475.00                    | 112.00                    | 1770.00                  
Midpoint Explicit (ms)    | 78.70                     | 0.97                      | 1.07                      | 0.15                      | 3.00                     
Midpoint Fixed (ms)       | 409.00                    | 6.26                      | 5.94                      | 0.54                      | 12.20                    
RK4 (ms)                  | 204.00                    | 1.61                      | 2.08                      | 0.20                      | 3.46                     
FD - L Convection (ms)    | 1610.00                   | 0.98                      | 7.29                      | 1.21                      | 1.19                     
FD - NL Convection (ms)   | 2010.00                   | 1.46                      | 7.16                      | 0.92                      | 1.28                     
FD - Poisson (ms)         | 3310.00                   | 1.53                      | 7.60                      | 2.65                      | 1.37                     
FD - Laplace (\textmu s)  | 32.40                     | 2.08                      | 5470.00                   | 1.27                      | -                        
M-D (ms)                  | 39100.00                  | -                         | 160.00                    | 133.00                    | 146.00                   
## Python 3.7 results
### Performance Comparison (as of Wed Nov 16 12:31:43 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 3.47                      | 0.51                      | 1.70                      | 1.53                     
Bellman Ford              | -                         | 3.83                      | 1.49                      | 2.43                      | 2.25                     
Dijkstra                  | -                         | 3.89                      | 1.91                      | 2.48                      | -                        
Euler                     | -                         | 4.52                      | 1.76                      | 2.39                      | 2.31                     
Midpoint Explicit         | -                         | 5.90                      | 2.69                      | 2.83                      | 2.85                     
Midpoint Fixed            | -                         | 6.62                      | 3.06                      | 3.11                      | 3.00                     
RK4                       | -                         | 7.01                      | 3.51                      | 3.70                      | -                        
FD - L Convection         | -                         | 3.39                      | 0.47                      | 2.30                      | 2.23                     
FD - NL Convection        | -                         | 3.34                      | 0.45                      | 2.28                      | 2.27                     
FD - Poisson              | -                         | 11.03                     | 1.01                      | 2.43                      | 2.42                     
FD - Laplace              | -                         | 18.16                     | 2.28                      | 3.01                      | -                        
M-D                       | -                         | -                         | 6.25                      | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 613.00 $\pm$ 15.00        | 20.30 $\pm$ 1.40          | 34.40 $\pm$ 1.40          | 3.85 $\pm$ 0.16           | 4.41 $\pm$ 0.18          
Bellman Ford (ns)         | 80000.00 $\pm$ 4200.00    | 495.00 $\pm$ 25.00        | 670.00 $\pm$ 25.00        | 301.00 $\pm$ 12.00        | 629.00 $\pm$ 20.00       
Dijkstra (ns)             | 43300.00 $\pm$ 2500.00    | 463.00 $\pm$ 25.00        | 488.00 $\pm$ 21.00        | 348.00 $\pm$ 14.00        | -                        
Euler (ms)                | 73.30 $\pm$ 4.10          | 0.71 $\pm$ 0.03           | 1.27 $\pm$ 0.04           | 0.22 $\pm$ 0.02           | 3.86 $\pm$ 0.13          
Midpoint Explicit (ms)    | 149.00 $\pm$ 8.00         | 1.71 $\pm$ 0.12           | 3.11 $\pm$ 0.11           | 0.27 $\pm$ 0.02           | 6.84 $\pm$ 0.31          
Midpoint Fixed (ms)       | 740.00 $\pm$ 30.00        | 9.69 $\pm$ 0.45           | 16.00 $\pm$ 0.60          | 0.76 $\pm$ 0.03           | 29.70 $\pm$ 1.00         
RK4 (ms)                  | 341.00 $\pm$ 15.00        | 2.56 $\pm$ 0.10           | 5.84 $\pm$ 0.26           | 0.95 $\pm$ 0.05           | -                        
FD - L Convection (ms)    | 2710.00 $\pm$ 150.00      | 2.28 $\pm$ 0.09           | 11.30 $\pm$ 0.40          | 2.73 $\pm$ 0.06           | 3.47 $\pm$ 0.07          
FD - NL Convection (ms)   | 3820.00 $\pm$ 130.00      | 2.47 $\pm$ 0.07           | 11.20 $\pm$ 0.50          | 2.47 $\pm$ 0.08           | 3.46 $\pm$ 0.10          
FD - Poisson (ms)         | 5570.00 $\pm$ 120.00      | 4.43 $\pm$ 0.15           | 13.30 $\pm$ 0.50          | 5.77 $\pm$ 0.13           | 4.29 $\pm$ 0.16          
FD - Laplace (\textmu s)  | 124.00 $\pm$ 8.00         | 3.62 $\pm$ 0.13           | 13.10 $\pm$ 0.30          | 3.26 $\pm$ 0.14           | -                        
M-D (s)                   | 66.30 $\pm$ 2.00          | -                         | 0.31 $\pm$ 0.01           | -                         | -                        
## Python 3.8 results
### Performance Comparison (as of Wed Nov 16 12:02:13 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.33                      | 0.33                      | 1.22                      | 1.11                     
Bellman Ford              | -                         | 2.73                      | 0.94                      | 1.78                      | 1.70                     
Dijkstra                  | -                         | 2.79                      | 1.26                      | 1.86                      | -                        
Euler                     | -                         | 3.23                      | 1.29                      | 1.82                      | 1.72                     
Midpoint Explicit         | -                         | 4.09                      | 1.98                      | 2.17                      | 2.07                     
Midpoint Fixed            | -                         | 4.94                      | 2.30                      | 2.19                      | 2.14                     
RK4                       | -                         | 4.87                      | 2.34                      | 2.53                      | -                        
FD - L Convection         | -                         | 2.37                      | 0.32                      | 1.67                      | 1.64                     
FD - NL Convection        | -                         | 2.38                      | 0.31                      | 1.68                      | 1.67                     
FD - Poisson              | -                         | 7.74                      | 0.74                      | 1.80                      | 1.73                     
FD - Laplace              | -                         | 12.83                     | 1.70                      | 2.25                      | -                        
M-D                       | -                         | -                         | 5.20                      | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 431.00 $\pm$ 4.00         | 22.00 $\pm$ 0.20          | 32.30 $\pm$ 0.30          | 13.20 $\pm$ 0.00          | 13.70 $\pm$ 0.00         
Bellman Ford (ns)         | 58900.00 $\pm$ 1400.00    | 368.00 $\pm$ 2.00         | 540.00 $\pm$ 3.00         | 240.00 $\pm$ 3.00         | 470.00 $\pm$ 1.00        
Dijkstra (ns)             | 29800.00 $\pm$ 100.00     | 351.00 $\pm$ 2.00         | 355.00 $\pm$ 5.00         | 245.00 $\pm$ 1.00         | -                        
Euler (ms)                | 47.90 $\pm$ 0.90          | 0.49 $\pm$ 0.01           | 1.27 $\pm$ 0.02           | 0.14 $\pm$ 0.01           | 2.70 $\pm$ 0.02          
Midpoint Explicit (ms)    | 99.10 $\pm$ 2.80          | 1.17 $\pm$ 0.02           | 3.10 $\pm$ 0.01           | 0.18 $\pm$ 0.00           | 4.86 $\pm$ 0.10          
Midpoint Fixed (ms)       | 497.00 $\pm$ 11.00        | 7.27 $\pm$ 0.06           | 17.50 $\pm$ 0.20          | 0.62 $\pm$ 0.04           | 21.50 $\pm$ 0.60         
RK4 (ms)                  | 249.00 $\pm$ 5.00         | 1.88 $\pm$ 0.01           | 6.35 $\pm$ 0.05           | 0.65 $\pm$ 0.03           | -                        
FD - L Convection (ms)    | 2530.00 $\pm$ 110.00      | 1.87 $\pm$ 0.01           | 9.22 $\pm$ 0.22           | 1.80 $\pm$ 0.00           | 1.80 $\pm$ 0.00          
FD - NL Convection (ms)   | 2780.00 $\pm$ 10.00       | 1.81 $\pm$ 0.01           | 9.43 $\pm$ 0.10           | 1.63 $\pm$ 0.00           | 1.58 $\pm$ 0.08          
FD - Poisson (ms)         | 4270.00 $\pm$ 30.00       | 2.29 $\pm$ 0.03           | 10.90 $\pm$ 0.10          | 3.87 $\pm$ 0.01           | 2.03 $\pm$ 0.00          
FD - Laplace (\textmu s)  | 54.40 $\pm$ 1.10          | 2.38 $\pm$ 0.02           | 8.92 $\pm$ 0.08           | 2.27 $\pm$ 0.01           | -                        
M-D (s)                   | 52.50 $\pm$ 2.20          | -                         | 0.23 $\pm$ 0.00           | -                         | -                        
## Python 3.9 results
### Performance Comparison (as of Wed Nov 16 12:05:41 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.95                      | 0.38                      | 1.53                      | 1.41                     
Bellman Ford              | -                         | 3.18                      | 1.05                      | 2.16                      | 2.09                     
Dijkstra                  | -                         | 3.31                      | 1.44                      | 2.35                      | -                        
Euler                     | -                         | 3.81                      | 1.50                      | 2.21                      | 2.16                     
Midpoint Explicit         | -                         | 4.79                      | 2.20                      | 2.58                      | 2.48                     
Midpoint Fixed            | -                         | 5.75                      | 2.71                      | 2.60                      | 2.55                     
RK4                       | -                         | 6.06                      | 2.62                      | 3.07                      | -                        
FD - L Convection         | -                         | 2.88                      | 0.38                      | 2.05                      | 2.03                     
FD - NL Convection        | -                         | 2.87                      | 0.35                      | 2.07                      | 1.98                     
FD - Poisson              | -                         | 9.15                      | 0.83                      | 2.15                      | 2.07                     
FD - Laplace              | -                         | 15.01                     | 2.05                      | 2.68                      | -                        
M-D                       | -                         | -                         | 6.01                      | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 432.00 $\pm$ 5.00         | 13.60 $\pm$ 0.50          | 21.60 $\pm$ 0.70          | 3.88 $\pm$ 0.14           | 3.94 $\pm$ 0.15          
Bellman Ford (ns)         | 68500.00 $\pm$ 1500.00    | 424.00 $\pm$ 24.00        | 626.00 $\pm$ 32.00        | 265.00 $\pm$ 10.00        | 564.00 $\pm$ 23.00       
Dijkstra (ns)             | 33200.00 $\pm$ 800.00     | 397.00 $\pm$ 9.00         | 427.00 $\pm$ 12.00        | 311.00 $\pm$ 9.00         | -                        
Euler (ms)                | 52.00 $\pm$ 1.50          | 0.64 $\pm$ 0.01           | 1.28 $\pm$ 0.03           | 0.17 $\pm$ 0.01           | 3.47 $\pm$ 0.07          
Midpoint Explicit (ms)    | 113.00 $\pm$ 6.00         | 1.46 $\pm$ 0.03           | 3.40 $\pm$ 0.13           | 0.20 $\pm$ 0.01           | 6.18 $\pm$ 0.11          
Midpoint Fixed (ms)       | 546.00 $\pm$ 17.00        | 9.15 $\pm$ 0.23           | 18.10 $\pm$ 0.40          | 0.92 $\pm$ 0.27           | 27.30 $\pm$ 0.50         
RK4 (ms)                  | 273.00 $\pm$ 11.00        | 2.13 $\pm$ 0.06           | 6.70 $\pm$ 0.24           | 0.91 $\pm$ 0.04           | -                        
FD - L Convection (ms)    | 2640.00 $\pm$ 30.00       | 2.02 $\pm$ 0.06           | 10.80 $\pm$ 0.20          | 1.81 $\pm$ 0.10           | 2.02 $\pm$ 0.08          
FD - NL Convection (ms)   | 3270.00 $\pm$ 60.00       | 1.90 $\pm$ 0.08           | 10.80 $\pm$ 0.40          | 1.75 $\pm$ 0.04           | 2.19 $\pm$ 0.11          
FD - Poisson (ms)         | 4960.00 $\pm$ 110.00      | 2.34 $\pm$ 0.04           | 12.10 $\pm$ 0.30          | 4.40 $\pm$ 0.08           | 2.10 $\pm$ 0.08          
FD - Laplace (\textmu s)  | 61.40 $\pm$ 1.50          | 2.74 $\pm$ 0.11           | 10.20 $\pm$ 0.40          | 2.78 $\pm$ 0.10           | -                        
M-D (s)                   | 51.80 $\pm$ 1.10          | -                         | 0.26 $\pm$ 0.01           | -                         | -                        
## Python 3.10 results
### Performance Comparison (as of Wed Nov 16 12:07:56 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 3.38                      | 0.43                      | 1.66                      | 1.53                     
Bellman Ford              | -                         | 3.64                      | 1.15                      | 2.29                      | 2.23                     
Dijkstra                  | -                         | 3.65                      | 1.45                      | 2.38                      | -                        
Euler                     | -                         | 4.35                      | 1.60                      | 2.32                      | 2.25                     
Midpoint Explicit         | -                         | 5.31                      | 2.46                      | 2.78                      | 2.71                     
Midpoint Fixed            | -                         | 6.23                      | 2.85                      | 2.71                      | 2.69                     
RK4                       | -                         | 6.27                      | 2.85                      | 3.23                      | -                        
FD - L Convection         | -                         | 3.27                      | 0.38                      | 2.19                      | 2.18                     
FD - NL Convection        | -                         | 3.30                      | 0.37                      | 2.08                      | 2.18                     
FD - Poisson              | -                         | 10.23                     | 0.92                      | 2.33                      | 2.33                     
FD - Laplace              | -                         | 16.22                     | 2.13                      | 2.73                      | -                        
M-D                       | -                         | -                         | 6.18                      | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 445.00 $\pm$ 14.00        | 13.80 $\pm$ 0.50          | 21.50 $\pm$ 0.60          | 3.98 $\pm$ 0.05           | 4.04 $\pm$ 0.11          
Bellman Ford (ns)         | 72100.00 $\pm$ 1800.00    | 441.00 $\pm$ 21.00        | 628.00 $\pm$ 9.00         | 261.00 $\pm$ 9.00         | 568.00 $\pm$ 20.00       
Dijkstra (ns)             | 34400.00 $\pm$ 1000.00    | 421.00 $\pm$ 14.00        | 432.00 $\pm$ 13.00        | 320.00 $\pm$ 13.00        | -                        
Euler (ms)                | 53.50 $\pm$ 0.70          | 0.67 $\pm$ 0.02           | 1.32 $\pm$ 0.02           | 0.17 $\pm$ 0.01           | 3.60 $\pm$ 0.08          
Midpoint Explicit (ms)    | 109.00 $\pm$ 2.00         | 1.47 $\pm$ 0.02           | 3.37 $\pm$ 0.06           | 0.21 $\pm$ 0.02           | 6.39 $\pm$ 0.13          
Midpoint Fixed (ms)       | 545.00 $\pm$ 14.00        | 9.72 $\pm$ 0.32           | 18.60 $\pm$ 0.30          | 0.81 $\pm$ 0.03           | 29.20 $\pm$ 1.10         
RK4 (ms)                  | 278.00 $\pm$ 11.00        | 2.18 $\pm$ 0.04           | 6.80 $\pm$ 0.12           | 0.89 $\pm$ 0.03           | -                        
FD - L Convection (ms)    | 2560.00 $\pm$ 30.00       | 2.05 $\pm$ 0.04           | 11.00 $\pm$ 0.30          | 1.95 $\pm$ 0.12           | 1.87 $\pm$ 0.08          
FD - NL Convection (ms)   | 3180.00 $\pm$ 20.00       | 2.04 $\pm$ 0.15           | 10.80 $\pm$ 0.20          | 1.86 $\pm$ 0.12           | 2.06 $\pm$ 0.13          
FD - Poisson (ms)         | 4970.00 $\pm$ 60.00       | 2.48 $\pm$ 0.09           | 12.50 $\pm$ 0.50          | 4.74 $\pm$ 0.13           | 2.12 $\pm$ 0.07          
FD - Laplace (\textmu s)  | 64.60 $\pm$ 2.20          | 2.77 $\pm$ 0.09           | 10.20 $\pm$ 0.10          | 2.69 $\pm$ 0.09           | -                        
M-D (s)                   | 53.60 $\pm$ 0.90          | -                         | 0.26 $\pm$ 0.00           | -                         | -                        
## Python 3.11 results
### Performance Comparison (as of Wed Nov 16 11:46:10 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.65                      | 1.31                      | 1.18                     
Bellman Ford              | -                         | 2.91                      | 1.89                      | 1.76                     
Dijkstra                  | -                         | 2.89                      | 1.94                      | -                        
Euler                     | -                         | 3.44                      | 1.88                      | 1.82                     
Midpoint Explicit         | -                         | 4.28                      | 2.19                      | 2.13                     
Midpoint Fixed            | -                         | 5.05                      | 2.25                      | 2.21                     
RK4                       | -                         | 5.08                      | 2.59                      | -                        
FD - L Convection         | -                         | 2.59                      | 1.74                      | 1.73                     
FD - NL Convection        | -                         | 2.59                      | 1.73                      | 1.73                     
FD - Poisson              | -                         | 7.94                      | 1.85                      | 1.80                     
FD - Laplace              | -                         | 13.02                     | 2.33                      | -                        
M-D                       | -                         | -                         | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran                   | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 415.00 $\pm$ 2.00         | 22.00 $\pm$ 0.20          | 14.30 $\pm$ 0.00          | 14.30 $\pm$ 0.00         
Bellman Ford (ns)         | 56500.00 $\pm$ 200.00     | 368.00 $\pm$ 1.00         | 218.00 $\pm$ 2.00         | 473.00 $\pm$ 5.00        
Dijkstra (ns)             | 27800.00 $\pm$ 100.00     | 361.00 $\pm$ 2.00         | 256.00 $\pm$ 1.00         | -                        
Euler (\textmu s)         | 49000.00 $\pm$ 200.00     | 483.00 $\pm$ 8.00         | 145.00 $\pm$ 7.00         | 2680.00 $\pm$ 30.00      
Midpoint Explicit (ms)    | 98.30 $\pm$ 0.50          | 1.17 $\pm$ 0.02           | 0.18 $\pm$ 0.00           | 4.79 $\pm$ 0.02          
Midpoint Fixed (ms)       | 496.00 $\pm$ 3.00         | 7.42 $\pm$ 0.19           | 0.59 $\pm$ 0.00           | 21.20 $\pm$ 0.10         
RK4 (ms)                  | 250.00 $\pm$ 1.00         | 1.85 $\pm$ 0.01           | 0.64 $\pm$ 0.02           | -                        
FD - L Convection (ms)    | 1970.00 $\pm$ 10.00       | 1.80 $\pm$ 0.11           | 1.86 $\pm$ 0.00           | 1.80 $\pm$ 0.01          
FD - NL Convection (ms)   | 2460.00 $\pm$ 20.00       | 2.16 $\pm$ 0.01           | 1.64 $\pm$ 0.02           | 1.58 $\pm$ 0.00          
FD - Poisson (ms)         | 4220.00 $\pm$ 40.00       | 2.29 $\pm$ 0.01           | 3.87 $\pm$ 0.00           | 2.01 $\pm$ 0.05          
FD - Laplace (\textmu s)  | 53.90 $\pm$ 0.40          | 2.41 $\pm$ 0.01           | 2.32 $\pm$ 0.05           | -                        
M-D (s)                   | 50.20 $\pm$ 0.30          | -                         | -                         | -                        
