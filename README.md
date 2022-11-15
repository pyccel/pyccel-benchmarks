# Benchmarks

Several tests are available for the user to benchmark Pyccel against other common accelerators, notably [pythran](https://pythran.readthedocs.io/en/latest/) and [numba](https://numba.pydata.org/).
The same code is used for all tests, only the decorators change.

The code can be executed by running the script `run_benchmarks.py`.
Additional options can be used with this script to add additional comparisons, change the output format, or change what is generated.

Run `python3 run_benchmarks.py --help` for more details.

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
## Python 3.7 results
### Performance Comparison (as of Tue Nov 15 18:16:30 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.36                      | 0.35                      | 1.23                      | 1.12                     
Bellman Ford              | -                         | 2.65                      | 0.97                      | 1.77                      | 1.71                     
Dijkstra                  | -                         | 2.74                      | 1.31                      | 1.90                      | -                        

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 444.00 $\pm$ 4.00         | 22.00 $\pm$ 0.20          | 32.30 $\pm$ 0.20          | 14.30 $\pm$ 0.00          | 13.60 $\pm$ 0.00         
Bellman Ford (ns)         | 68800.00 $\pm$ 1900.00    | 369.00 $\pm$ 2.00         | 536.00 $\pm$ 5.00         | 235.00 $\pm$ 2.00         | 476.00 $\pm$ 5.00        
Dijkstra (ns)             | 35100.00 $\pm$ 400.00     | 370.00 $\pm$ 4.00         | 353.00 $\pm$ 3.00         | 256.00 $\pm$ 1.00         | -                        
## Python 3.8 results
### Performance Comparison (as of Tue Nov 15 18:14:10 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.35                      | 0.33                      | 1.21                      | 1.13                     
Bellman Ford              | -                         | 2.69                      | 0.94                      | 1.77                      | 1.70                     
Dijkstra                  | -                         | 2.73                      | 1.25                      | 1.88                      | -                        

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 432.00 $\pm$ 3.00         | 22.00 $\pm$ 0.20          | 32.30 $\pm$ 0.20          | 13.20 $\pm$ 0.00          | 13.70 $\pm$ 0.00         
Bellman Ford (ns)         | 58600.00 $\pm$ 400.00     | 367.00 $\pm$ 2.00         | 537.00 $\pm$ 3.00         | 221.00 $\pm$ 2.00         | 469.00 $\pm$ 5.00        
Dijkstra (ns)             | 29700.00 $\pm$ 100.00     | 354.00 $\pm$ 4.00         | 354.00 $\pm$ 3.00         | 245.00 $\pm$ 2.00         | -                        
## Python 3.9 results
### Performance Comparison (as of Tue Nov 15 18:14:08 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.38                      | 0.33                      | 1.27                      | 1.15                     
Bellman Ford              | -                         | 2.75                      | 0.91                      | 1.79                      | 1.73                     
Dijkstra                  | -                         | 2.77                      | 1.22                      | 1.91                      | -                        

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 388.00 $\pm$ 2.00         | 22.00 $\pm$ 0.20          | 32.30 $\pm$ 0.30          | 14.30 $\pm$ 0.00          | 13.70 $\pm$ 0.00         
Bellman Ford (ns)         | 56600.00 $\pm$ 200.00     | 355.00 $\pm$ 4.00         | 524.00 $\pm$ 4.00         | 212.00 $\pm$ 2.00         | 451.00 $\pm$ 4.00        
Dijkstra (ns)             | 28300.00 $\pm$ 200.00     | 344.00 $\pm$ 5.00         | 347.00 $\pm$ 8.00         | 234.00 $\pm$ 1.00         | -                        
## Python 3.10 results
### Performance Comparison (as of Tue Nov 15 18:12:05 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 3.63                      | 0.49                      | 1.82                      | 1.58                     
Bellman Ford              | -                         | 3.96                      | 1.31                      | 2.46                      | 2.32                     
Dijkstra                  | -                         | 4.21                      | 1.68                      | 2.60                      | -                        

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 505.00 $\pm$ 16.00        | 20.00 $\pm$ 1.10          | 35.20 $\pm$ 1.20          | 4.04 $\pm$ 0.18           | 4.47 $\pm$ 0.14          
Bellman Ford (ns)         | 75000.00 $\pm$ 2600.00    | 481.00 $\pm$ 22.00        | 683.00 $\pm$ 24.00        | 278.00 $\pm$ 11.00        | 600.00 $\pm$ 21.00       
Dijkstra (ns)             | 36600.00 $\pm$ 1200.00    | 428.00 $\pm$ 19.00        | 484.00 $\pm$ 21.00        | 341.00 $\pm$ 10.00        | -                        
## Python 3.11 results
### Performance Comparison (as of Tue Nov 15 21:50:40 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.51                      | 1.27                      | 1.15                     
Bellman Ford              | -                         | 2.83                      | 1.83                      | 1.74                     
Dijkstra                  | -                         | 2.84                      | 1.90                      | -                        
Euler                     | -                         | 3.36                      | 1.85                      | 1.78                     
Midpoint Explicit         | -                         | 4.13                      | 2.15                      | 2.07                     
Midpoint Fixed            | -                         | 4.95                      | 2.21                      | 2.17                     
RK4                       | -                         | 5.02                      | 2.56                      | -                        
FD - L Convection         | -                         | 2.51                      | 1.70                      | 1.70                     
FD - NL Convection        | -                         | 2.52                      | 1.70                      | 1.71                     
FD - Poisson              | -                         | 7.85                      | 1.83                      | 1.80                     
FD - Laplace              | -                         | 12.72                     | 2.33                      | -                        
M-D                       | -                         | -                         | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran                   | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 413.00 $\pm$ 2.00         | 22.00 $\pm$ 0.20          | 13.20 $\pm$ 0.00          | 14.30 $\pm$ 0.00         
Bellman Ford (ns)         | 56300.00 $\pm$ 200.00     | 368.00 $\pm$ 1.00         | 224.00 $\pm$ 2.00         | 471.00 $\pm$ 4.00        
Dijkstra (ns)             | 27700.00 $\pm$ 100.00     | 361.00 $\pm$ 4.00         | 255.00 $\pm$ 1.00         | -                        
Euler (\textmu s)         | 49100.00 $\pm$ 300.00     | 486.00 $\pm$ 11.00        | 143.00 $\pm$ 5.00         | 2670.00 $\pm$ 10.00      
Midpoint Explicit (ms)    | 98.40 $\pm$ 0.60          | 1.18 $\pm$ 0.02           | 0.18 $\pm$ 0.00           | 4.83 $\pm$ 0.06          
Midpoint Fixed (ms)       | 496.00 $\pm$ 2.00         | 7.40 $\pm$ 0.06           | 0.63 $\pm$ 0.01           | 21.30 $\pm$ 0.20         
RK4 (ms)                  | 249.00 $\pm$ 1.00         | 1.85 $\pm$ 0.01           | 0.64 $\pm$ 0.03           | -                        
FD - L Convection (ms)    | 1960.00 $\pm$ 10.00       | 1.80 $\pm$ 0.11           | 1.86 $\pm$ 0.00           | 1.80 $\pm$ 0.02          
FD - NL Convection (ms)   | 2460.00 $\pm$ 10.00       | 2.16 $\pm$ 0.01           | 1.63 $\pm$ 0.00           | 1.58 $\pm$ 0.00          
FD - Poisson (ms)         | 4210.00 $\pm$ 30.00       | 2.28 $\pm$ 0.00           | 3.87 $\pm$ 0.01           | 2.01 $\pm$ 0.01          
FD - Laplace (\textmu s)  | 54.70 $\pm$ 3.40          | 2.41 $\pm$ 0.02           | 2.27 $\pm$ 0.05           | -                        
M-D (s)                   | 50.10 $\pm$ 0.20          | -                         | -                         | -                        
