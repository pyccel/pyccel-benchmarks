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
### Performance Comparison (as of Tue Nov 15 18:25:41 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.56                      | 1.30                      | 1.18                     
Bellman Ford              | -                         | 2.86                      | 1.88                      | 1.78                     
Dijkstra                  | -                         | 2.93                      | 1.95                      | -                        

## Execution time
Algorithm                 | python                    | pythran                   | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 416.00 $\pm$ 2.00         | 22.00 $\pm$ 0.20          | 14.30 $\pm$ 0.10          | 13.80 $\pm$ 0.10         
Bellman Ford (ns)         | 56400.00 $\pm$ 200.00     | 368.00 $\pm$ 2.00         | 230.00 $\pm$ 2.00         | 472.00 $\pm$ 3.00        
Dijkstra (ns)             | 27700.00 $\pm$ 100.00     | 360.00 $\pm$ 2.00         | 259.00 $\pm$ 4.00         | -                        
