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
### Performance Comparison (as of Tue Oct 17 12:44:32 UTC 2023)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.64                      | 0.43                      | 1.38                      | 1.26                     
Bellman Ford              | -                         | 3.78                      | 1.33                      | 2.36                      | 2.31                     
Dijkstra                  | -                         | 2.92                      | 1.47                      | 2.48                      | 2.36                     
Euler                     | -                         | 3.37                      | 1.95                      | 2.36                      | 2.33                     
Midpoint Explicit         | -                         | 3.90                      | 2.69                      | 2.68                      | 2.70                     
Midpoint Fixed            | -                         | 4.44                      | 2.85                      | 2.72                      | 2.73                     
RK4                       | -                         | 5.18                      | 3.34                      | 3.45                      | 3.32                     
FD - L Convection         | -                         | 2.90                      | 1.06                      | 2.30                      | 2.36                     
FD - NL Convection        | -                         | 3.71                      | 1.14                      | 2.32                      | 2.38                     
FD - Poisson              | -                         | 4.00                      | 1.63                      | 2.49                      | 2.48                     
FD - Laplace              | -                         | 7.79                      | 3.07                      | 2.86                      | 2.98                     
M-D                       | -                         | 7.63                      | 3.41                      | 3.36                      | 3.07                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 444.00                    | 8.03                      | 28.40                     | 3.08                      | 3.30                     
Bellman Ford (ms)         | 2890.00                   | 7.71                      | 6.36                      | 3.84                      | 6.46                     
Dijkstra (ms)             | 7410.00                   | 47.80                     | 43.10                     | 38.70                     | 50.20                    
Euler (ms)                | 4740.00                   | 43.00                     | 112.00                    | 21.50                     | 241.00                   
Midpoint Explicit (ms)    | 10100.00                  | 84.00                     | 208.00                    | 30.50                     | 476.00                   
Midpoint Fixed (s)        | 49.10                     | 0.66                      | 1.07                      | 0.10                      | 2.36                     
RK4 (ms)                  | 24400.00                  | 202.00                    | 382.00                    | 47.00                     | 774.00                   
FD - L Convection (ms)    | 3160.00                   | 2.89                      | 3.23                      | 1.74                      | 2.49                     
FD - NL Convection (ms)   | 4040.00                   | 3.40                      | 3.33                      | 1.80                      | 2.58                     
FD - Poisson (ms)         | 8740.00                   | 5.69                      | 9.68                      | 3.69                      | 4.97                     
FD - Laplace (ms)         | 735.00                    | 232.00                    | 374.00                    | 72.80                     | 414.00                   
M-D (ms)                  | 19600.00                  | 52.90                     | 73.10                     | 106.00                    | 110.00                   

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.8 results
### Performance Comparison (as of 1.9.2)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.75                      | 0.55                      | 1.64                      | 1.59                     
Bellman Ford              | -                         | 4.28                      | 1.58                      | 2.82                      | 2.66                     
Dijkstra                  | -                         | 3.35                      | 1.87                      | 2.92                      | 2.73                     
Euler                     | -                         | 3.89                      | 2.43                      | 2.72                      | 2.69                     
Midpoint Explicit         | -                         | 4.46                      | 3.36                      | 3.30                      | 3.43                     
Midpoint Fixed            | -                         | 5.07                      | 3.59                      | 3.22                      | 3.28                     
RK4                       | -                         | 5.64                      | 3.95                      | 3.92                      | 4.17                     
FD - L Convection         | -                         | 3.19                      | 1.25                      | 2.62                      | 2.79                     
FD - NL Convection        | -                         | 4.27                      | 1.39                      | 2.65                      | 2.72                     
FD - Poisson              | -                         | 4.58                      | 1.98                      | 3.17                      | 3.08                     
FD - Laplace              | -                         | 9.28                      | 3.68                      | 3.53                      | 3.46                     
M-D                       | -                         | 9.14                      | 4.21                      | 4.14                      | 3.79                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 567.00 $\pm$ 8.00         | 9.69 $\pm$ 0.23           | 32.20 $\pm$ 0.60          | 2.52 $\pm$ 0.08           | 2.59 $\pm$ 0.04          
Bellman Ford (ms)         | 3600.00 $\pm$ 140.00      | 7.41 $\pm$ 0.30           | 7.93 $\pm$ 0.19           | 5.18 $\pm$ 0.14           | 10.00 $\pm$ 0.30         
Dijkstra (ms)             | 9310.00 $\pm$ 340.00      | 48.10 $\pm$ 2.60          | 51.30 $\pm$ 2.30          | 40.90 $\pm$ 1.40          | 60.90 $\pm$ 1.40         
Euler (ms)                | 5820.00 $\pm$ 190.00      | 48.10 $\pm$ 1.10          | 134.00 $\pm$ 3.00         | 25.20 $\pm$ 0.90          | 293.00 $\pm$ 6.00        
Midpoint Explicit (ms)    | 11900.00 $\pm$ 300.00     | 97.00 $\pm$ 3.70          | 276.00 $\pm$ 12.00        | 42.30 $\pm$ 1.00          | 589.00 $\pm$ 19.00       
Midpoint Fixed (s)        | 60.20 $\pm$ 1.30          | 0.77 $\pm$ 0.01           | 1.32 $\pm$ 0.03           | 0.13 $\pm$ 0.00           | 2.82 $\pm$ 0.06          
RK4 (ms)                  | 28500.00 $\pm$ 600.00     | 235.00 $\pm$ 4.00         | 482.00 $\pm$ 17.00        | 53.10 $\pm$ 2.20          | 950.00 $\pm$ 20.00       
FD - L Convection (ms)    | 4230.00 $\pm$ 140.00      | 3.90 $\pm$ 0.09           | 4.79 $\pm$ 0.24           | 3.38 $\pm$ 0.23           | 4.17 $\pm$ 0.14          
FD - NL Convection (ms)   | 5480.00 $\pm$ 210.00      | 4.94 $\pm$ 0.10           | 5.29 $\pm$ 0.62           | 3.83 $\pm$ 0.15           | 5.91 $\pm$ 0.62          
FD - Poisson (ms)         | 10700.00 $\pm$ 300.00     | 10.40 $\pm$ 0.20          | 14.40 $\pm$ 0.50          | 8.64 $\pm$ 0.32           | 12.00 $\pm$ 0.30         
FD - Laplace (ms)         | 1220.00 $\pm$ 10.00       | 359.00 $\pm$ 5.00         | 565.00 $\pm$ 9.00         | 193.00 $\pm$ 3.00         | 563.00 $\pm$ 5.00        
M-D (ms)                  | 23800.00 $\pm$ 800.00     | 67.10 $\pm$ 3.10          | 104.00 $\pm$ 1.00         | 140.00 $\pm$ 3.00         | 145.00 $\pm$ 3.00        

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.9.2)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.10                      | 0.41                      | 1.30                      | 1.24                     
Bellman Ford              | -                         | 3.52                      | 1.24                      | 2.25                      | 2.19                     
Dijkstra                  | -                         | 2.68                      | 1.39                      | 2.35                      | 2.22                     
Euler                     | -                         | 3.16                      | 1.88                      | 2.28                      | 2.35                     
Midpoint Explicit         | -                         | 3.51                      | 2.63                      | 2.54                      | 2.56                     
Midpoint Fixed            | -                         | 4.00                      | 2.68                      | 2.60                      | 2.64                     
RK4                       | -                         | 4.58                      | 3.09                      | 3.19                      | 3.15                     
FD - L Convection         | -                         | 2.55                      | 0.99                      | 2.14                      | 2.16                     
FD - NL Convection        | -                         | 3.30                      | 1.06                      | 2.14                      | 2.19                     
FD - Poisson              | -                         | 3.51                      | 1.53                      | 2.30                      | 2.33                     
FD - Laplace              | -                         | 7.25                      | 2.89                      | 2.78                      | 2.81                     
M-D                       | -                         | 7.33                      | 3.37                      | 3.27                      | 2.99                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 425.00 $\pm$ 2.00         | 9.52 $\pm$ 0.00           | 28.10 $\pm$ 0.20          | 3.11 $\pm$ 0.00           | 2.95 $\pm$ 0.00          
Bellman Ford (ms)         | 2850.00 $\pm$ 10.00       | 7.72 $\pm$ 0.02           | 6.36 $\pm$ 0.02           | 3.86 $\pm$ 0.00           | 6.48 $\pm$ 0.01          
Dijkstra (ms)             | 7420.00 $\pm$ 20.00       | 46.80 $\pm$ 0.60          | 41.90 $\pm$ 1.10          | 37.30 $\pm$ 0.60          | 50.70 $\pm$ 0.60         
Euler (ms)                | 4850.00 $\pm$ 110.00      | 43.40 $\pm$ 0.40          | 112.00 $\pm$ 1.00         | 21.30 $\pm$ 0.60          | 241.00 $\pm$ 3.00        
Midpoint Explicit (ms)    | 9880.00 $\pm$ 250.00      | 83.90 $\pm$ 0.40          | 207.00 $\pm$ 1.00         | 29.20 $\pm$ 0.80          | 477.00 $\pm$ 4.00        
Midpoint Fixed (s)        | 49.50 $\pm$ 1.30          | 0.66 $\pm$ 0.00           | 1.06 $\pm$ 0.02           | 0.10 $\pm$ 0.00           | 2.37 $\pm$ 0.02          
RK4 (ms)                  | 24400.00 $\pm$ 700.00     | 199.00 $\pm$ 1.00         | 383.00 $\pm$ 2.00         | 44.30 $\pm$ 1.00          | 773.00 $\pm$ 4.00        
FD - L Convection (ms)    | 3430.00 $\pm$ 30.00       | 2.87 $\pm$ 0.03           | 3.40 $\pm$ 0.26           | 1.79 $\pm$ 0.07           | 2.80 $\pm$ 0.01          
FD - NL Convection (ms)   | 4280.00 $\pm$ 10.00       | 3.48 $\pm$ 0.10           | 3.42 $\pm$ 0.11           | 1.82 $\pm$ 0.06           | 2.81 $\pm$ 0.09          
FD - Poisson (ms)         | 8980.00 $\pm$ 100.00      | 5.78 $\pm$ 0.01           | 9.85 $\pm$ 0.09           | 3.71 $\pm$ 0.01           | 4.89 $\pm$ 0.02          
FD - Laplace (ms)         | 766.00 $\pm$ 6.00         | 233.00 $\pm$ 1.00         | 383.00 $\pm$ 4.00         | 76.50 $\pm$ 1.80          | 417.00 $\pm$ 2.00        
M-D (ms)                  | 19500.00 $\pm$ 400.00     | 53.00 $\pm$ 0.00          | 74.30 $\pm$ 0.40          | 106.00 $\pm$ 0.00         | 110.00 $\pm$ 0.00        

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.9.2)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.99                      | 0.49                      | 1.58                      | 1.47                     
Bellman Ford              | -                         | 4.38                      | 1.48                      | 2.71                      | 2.66                     
Dijkstra                  | -                         | 3.38                      | 1.67                      | 2.79                      | 2.69                     
Euler                     | -                         | 3.90                      | 2.25                      | 2.68                      | 2.72                     
Midpoint Explicit         | -                         | 4.39                      | 3.09                      | 3.02                      | 3.10                     
Midpoint Fixed            | -                         | 5.00                      | 3.25                      | 3.14                      | 3.17                     
RK4                       | -                         | 5.53                      | 3.77                      | 3.84                      | 3.82                     
FD - L Convection         | -                         | 3.28                      | 1.20                      | 2.60                      | 2.63                     
FD - NL Convection        | -                         | 4.11                      | 1.28                      | 2.61                      | 2.60                     
FD - Poisson              | -                         | 4.47                      | 1.85                      | 2.80                      | 2.88                     
FD - Laplace              | -                         | 8.69                      | 3.56                      | 3.33                      | 3.39                     
M-D                       | -                         | 8.91                      | 4.08                      | 3.96                      | 3.60                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 490.00 $\pm$ 1.00         | 3.03 $\pm$ 0.01           | 16.80 $\pm$ 0.30          | 2.56 $\pm$ 0.01           | 2.51 $\pm$ 0.01          
Bellman Ford (ms)         | 3480.00 $\pm$ 30.00       | 9.28 $\pm$ 0.08           | 7.63 $\pm$ 0.01           | 4.62 $\pm$ 0.03           | 7.75 $\pm$ 0.01          
Dijkstra (ms)             | 8890.00 $\pm$ 20.00       | 53.80 $\pm$ 0.40          | 45.30 $\pm$ 0.60          | 40.20 $\pm$ 0.50          | 56.90 $\pm$ 0.50         
Euler (ms)                | 5660.00 $\pm$ 80.00       | 51.90 $\pm$ 0.40          | 134.00 $\pm$ 1.00         | 24.30 $\pm$ 0.60          | 283.00 $\pm$ 4.00        
Midpoint Explicit (ms)    | 11400.00 $\pm$ 200.00     | 100.00 $\pm$ 1.00         | 250.00 $\pm$ 2.00         | 35.00 $\pm$ 0.60          | 561.00 $\pm$ 4.00        
Midpoint Fixed (s)        | 59.30 $\pm$ 2.50          | 0.80 $\pm$ 0.01           | 1.26 $\pm$ 0.02           | 0.12 $\pm$ 0.01           | 2.80 $\pm$ 0.02          
RK4 (ms)                  | 29000.00 $\pm$ 900.00     | 239.00 $\pm$ 2.00         | 463.00 $\pm$ 9.00         | 54.10 $\pm$ 0.60          | 918.00 $\pm$ 4.00        
FD - L Convection (ms)    | 3860.00 $\pm$ 60.00       | 3.54 $\pm$ 0.03           | 4.01 $\pm$ 0.12           | 1.92 $\pm$ 0.05           | 3.08 $\pm$ 0.20          
FD - NL Convection (ms)   | 4780.00 $\pm$ 70.00       | 4.19 $\pm$ 0.07           | 4.10 $\pm$ 0.08           | 2.05 $\pm$ 0.07           | 3.20 $\pm$ 0.19          
FD - Poisson (ms)         | 10600.00 $\pm$ 100.00     | 6.83 $\pm$ 0.11           | 11.80 $\pm$ 0.20          | 4.46 $\pm$ 0.06           | 5.95 $\pm$ 0.07          
FD - Laplace (ms)         | 911.00 $\pm$ 20.00        | 282.00 $\pm$ 3.00         | 456.00 $\pm$ 5.00         | 91.70 $\pm$ 3.10          | 501.00 $\pm$ 2.00        
M-D (ms)                  | 22800.00 $\pm$ 400.00     | 63.30 $\pm$ 0.20          | 88.10 $\pm$ 0.70          | 127.00 $\pm$ 0.00         | 132.00 $\pm$ 0.00        

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.9.2)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 3.25                      | 0.48                      | 1.60                      | 1.56                     
Bellman Ford              | -                         | 4.66                      | 1.61                      | 2.76                      | 2.72                     
Dijkstra                  | -                         | 3.53                      | 1.79                      | 2.93                      | 2.80                     
Euler                     | -                         | 4.23                      | 2.31                      | 2.76                      | 2.92                     
Midpoint Explicit         | -                         | 4.71                      | 3.00                      | 3.31                      | 3.48                     
Midpoint Fixed            | -                         | 5.26                      | 3.36                      | 3.25                      | 3.22                     
RK4                       | -                         | 6.06                      | 3.79                      | 3.83                      | 3.90                     
FD - L Convection         | -                         | 3.45                      | 1.23                      | 2.63                      | 2.73                     
FD - NL Convection        | -                         | 4.60                      | 1.26                      | 2.71                      | 2.84                     
FD - Poisson              | -                         | 4.91                      | 1.85                      | 3.09                      | 3.20                     
FD - Laplace              | -                         | 9.80                      | 3.43                      | 3.59                      | 3.61                     
M-D                       | -                         | 9.59                      | 3.99                      | 4.03                      | 3.62                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 651.00 $\pm$ 23.00        | 9.10 $\pm$ 0.38           | 32.10 $\pm$ 1.30          | 2.45 $\pm$ 0.06           | 2.46 $\pm$ 0.05          
Bellman Ford (ms)         | 3620.00 $\pm$ 180.00      | 7.45 $\pm$ 0.21           | 7.94 $\pm$ 0.25           | 5.07 $\pm$ 0.12           | 10.40 $\pm$ 0.40         
Dijkstra (ms)             | 8850.00 $\pm$ 180.00      | 49.10 $\pm$ 1.80          | 52.30 $\pm$ 2.50          | 42.30 $\pm$ 1.60          | 62.40 $\pm$ 1.50         
Euler (ms)                | 6270.00 $\pm$ 400.00      | 49.50 $\pm$ 1.50          | 137.00 $\pm$ 5.00         | 28.10 $\pm$ 1.70          | 302.00 $\pm$ 6.00        
Midpoint Explicit (ms)    | 12900.00 $\pm$ 700.00     | 96.80 $\pm$ 2.90          | 263.00 $\pm$ 8.00         | 42.00 $\pm$ 2.00          | 582.00 $\pm$ 12.00       
Midpoint Fixed (s)        | 62.80 $\pm$ 4.30          | 0.77 $\pm$ 0.01           | 1.33 $\pm$ 0.07           | 0.13 $\pm$ 0.01           | 2.78 $\pm$ 0.04          
RK4 (ms)                  | 31700.00 $\pm$ 3100.00    | 245.00 $\pm$ 8.00         | 469.00 $\pm$ 9.00         | 55.90 $\pm$ 3.10          | 927.00 $\pm$ 20.00       
FD - L Convection (ms)    | 4250.00 $\pm$ 480.00      | 3.92 $\pm$ 0.13           | 4.75 $\pm$ 0.18           | 3.10 $\pm$ 0.14           | 5.23 $\pm$ 0.12          
FD - NL Convection (ms)   | 5140.00 $\pm$ 650.00      | 4.84 $\pm$ 0.23           | 5.03 $\pm$ 0.26           | 3.23 $\pm$ 0.61           | 6.44 $\pm$ 0.11          
FD - Poisson (ms)         | 12100.00 $\pm$ 1200.00    | 10.90 $\pm$ 0.40          | 14.40 $\pm$ 0.40          | 8.74 $\pm$ 0.27           | 12.00 $\pm$ 0.30         
FD - Laplace (ms)         | 1230.00 $\pm$ 30.00       | 359.00 $\pm$ 7.00         | 573.00 $\pm$ 10.00        | 195.00 $\pm$ 5.00         | 578.00 $\pm$ 10.00       
M-D (ms)                  | 24400.00 $\pm$ 2300.00    | 64.80 $\pm$ 1.60          | 107.00 $\pm$ 5.00         | 140.00 $\pm$ 2.00         | 144.00 $\pm$ 2.00        

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
