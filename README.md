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
### Performance Comparison (as of Fri Oct 13 18:06:02 UTC 2023)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.60                      | 0.42                      | 1.35                      | 1.30                     
Bellman Ford              | -                         | 3.80                      | 1.29                      | 2.29                      | 2.25                     
Dijkstra                  | -                         | 2.98                      | 1.45                      | 2.40                      | 2.32                     
Euler                     | -                         | 3.43                      | 1.94                      | 2.31                      | 2.33                     
Midpoint Explicit         | -                         | 3.82                      | 2.65                      | 2.63                      | 2.63                     
Midpoint Fixed            | -                         | 4.26                      | 2.76                      | 2.67                      | 2.64                     
RK4                       | -                         | 4.96                      | 3.15                      | 3.40                      | 3.19                     
FD - L Convection         | -                         | 2.81                      | 1.02                      | 2.19                      | 2.22                     
FD - NL Convection        | -                         | 3.55                      | 1.09                      | 2.20                      | 2.24                     
FD - Poisson              | -                         | 3.75                      | 1.59                      | 2.40                      | 2.41                     
FD - Laplace              | -                         | 7.47                      | 2.99                      | 2.80                      | 2.87                     
M-D                       | -                         | 7.75                      | 3.49                      | 3.38                      | 3.13                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 444.00                    | 8.03                      | 28.00                     | 2.98                      | 3.30                     
Bellman Ford (ms)         | 2880.00                   | 7.71                      | 6.39                      | 3.82                      | 6.45                     
Dijkstra (ms)             | 7410.00                   | 47.70                     | 43.50                     | 36.60                     | 50.00                    
Euler (ms)                | 4650.00                   | 44.10                     | 112.00                    | 20.80                     | 241.00                   
Midpoint Explicit (ms)    | 9910.00                   | 83.90                     | 207.00                    | 30.10                     | 477.00                   
Midpoint Fixed (s)        | 48.90                     | 0.66                      | 1.07                      | 0.10                      | 2.36                     
RK4 (ms)                  | 24800.00                  | 200.00                    | 394.00                    | 45.30                     | 771.00                   
FD - L Convection (ms)    | 3030.00                   | 2.90                      | 3.26                      | 1.74                      | 2.84                     
FD - NL Convection (ms)   | 3860.00                   | 3.41                      | 3.97                      | 1.76                      | 2.58                     
FD - Poisson (ms)         | 9040.00                   | 5.68                      | 9.74                      | 3.70                      | 4.89                     
FD - Laplace (ms)         | 753.00                    | 233.00                    | 383.00                    | 73.00                     | 402.00                   
M-D (ms)                  | 19800.00                  | 52.90                     | 74.20                     | 106.00                    | 110.00                   

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.7 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.11                      | 0.37                      | 1.31                      | 1.25                     
Bellman Ford              | -                         | 3.42                      | 1.22                      | 2.31                      | 2.25                     
Dijkstra                  | -                         | 2.63                      | 1.37                      | 2.37                      | 2.27                     
Euler                     | -                         | 2.97                      | 1.85                      | 2.27                      | 2.29                     
Midpoint Explicit         | -                         | 3.48                      | 2.66                      | 2.68                      | 2.70                     
Midpoint Fixed            | -                         | 3.96                      | 2.90                      | 2.69                      | 2.73                     
RK4                       | -                         | 4.47                      | 3.23                      | 3.35                      | 3.30                     
FD - L Convection         | -                         | 2.54                      | 1.07                      | 2.21                      | 2.26                     
FD - NL Convection        | -                         | 3.27                      | 1.15                      | 2.23                      | 2.28                     
FD - Poisson              | -                         | 3.51                      | 1.61                      | 2.42                      | 2.42                     
FD - Laplace              | -                         | 7.15                      | 3.11                      | 2.91                      | 2.93                     
M-D                       | -                         | 7.47                      | 3.57                      | 3.42                      | 3.12                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 509.00 $\pm$ 5.00         | 7.92 $\pm$ 0.03           | 31.00 $\pm$ 0.40          | 2.98 $\pm$ 0.00           | 3.31 $\pm$ 0.00          
Bellman Ford (ms)         | 2860.00 $\pm$ 150.00      | 5.95 $\pm$ 0.05           | 9.70 $\pm$ 0.02           | 3.83 $\pm$ 0.01           | 6.45 $\pm$ 0.02          
Dijkstra (ms)             | 7810.00 $\pm$ 60.00       | 47.70 $\pm$ 0.10          | 43.70 $\pm$ 0.40          | 37.80 $\pm$ 0.10          | 49.50 $\pm$ 0.10         
Euler (ms)                | 5800.00 $\pm$ 70.00       | 44.20 $\pm$ 0.30          | 116.00 $\pm$ 1.00         | 21.20 $\pm$ 0.70          | 239.00 $\pm$ 6.00        
Midpoint Explicit (ms)    | 11800.00 $\pm$ 200.00     | 87.80 $\pm$ 0.60          | 292.00 $\pm$ 2.00         | 32.10 $\pm$ 1.70          | 473.00 $\pm$ 2.00        
Midpoint Fixed (s)        | 59.60 $\pm$ 1.50          | 0.68 $\pm$ 0.00           | 1.60 $\pm$ 0.02           | 0.11 $\pm$ 0.01           | 2.33 $\pm$ 0.02          
RK4 (ms)                  | 26600.00 $\pm$ 500.00     | 202.00 $\pm$ 3.00         | 578.00 $\pm$ 1.00         | 46.80 $\pm$ 1.00          | 763.00 $\pm$ 2.00        
FD - L Convection (ms)    | 3190.00 $\pm$ 50.00       | 2.88 $\pm$ 0.02           | 13.90 $\pm$ 0.00          | 1.73 $\pm$ 0.03           | 2.73 $\pm$ 0.16          
FD - NL Convection (ms)   | 4330.00 $\pm$ 50.00       | 3.41 $\pm$ 0.01           | 14.70 $\pm$ 0.00          | 1.76 $\pm$ 0.05           | 2.58 $\pm$ 0.01          
FD - Poisson (ms)         | 9410.00 $\pm$ 210.00      | 6.41 $\pm$ 0.01           | 18.70 $\pm$ 0.10          | 3.70 $\pm$ 0.01           | 4.91 $\pm$ 0.01          
FD - Laplace (ms)         | 703.00 $\pm$ 8.00         | 232.00 $\pm$ 1.00         | 386.00 $\pm$ 2.00         | 77.40 $\pm$ 1.70          | 403.00 $\pm$ 3.00        
M-D (ms)                  | 21900.00 $\pm$ 500.00     | 52.80 $\pm$ 0.00          | 88.30 $\pm$ 1.30          | 106.00 $\pm$ 0.00         | 110.00 $\pm$ 0.00        

![Python 3.7 compilation results](./version_specific_results/pypi_performance_37_compilation.svg)
![Python 3.7 execution results](./version_specific_results/pypi_performance_37_execution.svg)
## Python 3.8 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.96                      | 0.39                      | 1.20                      | 1.14                     
Bellman Ford              | -                         | 3.26                      | 1.19                      | 2.15                      | 2.12                     
Dijkstra                  | -                         | 2.47                      | 1.33                      | 2.23                      | 2.14                     
Euler                     | -                         | 2.81                      | 1.80                      | 2.11                      | 2.16                     
Midpoint Explicit         | -                         | 3.18                      | 2.47                      | 2.46                      | 2.49                     
Midpoint Fixed            | -                         | 3.72                      | 2.64                      | 2.51                      | 2.57                     
RK4                       | -                         | 4.15                      | 2.99                      | 3.05                      | 3.01                     
FD - L Convection         | -                         | 2.35                      | 0.94                      | 2.06                      | 2.09                     
FD - NL Convection        | -                         | 3.03                      | 1.00                      | 2.08                      | 2.12                     
FD - Poisson              | -                         | 3.26                      | 1.46                      | 2.23                      | 2.26                     
FD - Laplace              | -                         | 6.50                      | 2.78                      | 2.65                      | 2.71                     
M-D                       | -                         | 6.79                      | 3.31                      | 3.16                      | 2.90                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 404.00 $\pm$ 3.00         | 9.81 $\pm$ 0.00           | 27.20 $\pm$ 0.20          | 3.28 $\pm$ 0.01           | 3.26 $\pm$ 0.00          
Bellman Ford (ms)         | 2530.00 $\pm$ 80.00       | 6.74 $\pm$ 0.02           | 6.33 $\pm$ 0.00           | 4.44 $\pm$ 0.01           | 6.57 $\pm$ 0.01          
Dijkstra (ms)             | 6710.00 $\pm$ 40.00       | 38.60 $\pm$ 0.50          | 32.70 $\pm$ 0.90          | 31.00 $\pm$ 0.50          | 48.20 $\pm$ 0.60         
Euler (ms)                | 4860.00 $\pm$ 20.00       | 37.60 $\pm$ 0.40          | 108.00 $\pm$ 0.00         | 18.30 $\pm$ 0.70          | 203.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 9920.00 $\pm$ 40.00       | 75.90 $\pm$ 2.30          | 210.00 $\pm$ 3.00         | 27.80 $\pm$ 0.70          | 396.00 $\pm$ 2.00        
Midpoint Fixed (s)        | 49.90 $\pm$ 0.60          | 0.61 $\pm$ 0.01           | 1.09 $\pm$ 0.01           | 0.10 $\pm$ 0.00           | 1.98 $\pm$ 0.03          
RK4 (ms)                  | 24900.00 $\pm$ 200.00     | 219.00 $\pm$ 2.00         | 416.00 $\pm$ 22.00        | 40.60 $\pm$ 0.90          | 658.00 $\pm$ 11.00       
FD - L Convection (ms)    | 2970.00 $\pm$ 50.00       | 2.82 $\pm$ 0.00           | 3.19 $\pm$ 0.13           | 1.63 $\pm$ 0.02           | 2.99 $\pm$ 0.00          
FD - NL Convection (ms)   | 3720.00 $\pm$ 30.00       | 3.09 $\pm$ 0.00           | 3.43 $\pm$ 0.13           | 1.61 $\pm$ 0.06           | 2.94 $\pm$ 0.14          
FD - Poisson (ms)         | 8360.00 $\pm$ 110.00      | 5.78 $\pm$ 0.03           | 10.10 $\pm$ 0.00          | 4.19 $\pm$ 0.00           | 5.30 $\pm$ 0.01          
FD - Laplace (ms)         | 697.00 $\pm$ 3.00         | 251.00 $\pm$ 1.00         | 391.00 $\pm$ 4.00         | 78.50 $\pm$ 1.60          | 366.00 $\pm$ 1.00        
M-D (ms)                  | 20600.00 $\pm$ 100.00     | 65.00 $\pm$ 0.10          | 78.50 $\pm$ 0.50          | 120.00 $\pm$ 0.00         | 122.00 $\pm$ 0.00        

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.48                      | 0.47                      | 1.51                      | 1.44                     
Bellman Ford              | -                         | 4.08                      | 1.42                      | 2.67                      | 2.63                     
Dijkstra                  | -                         | 3.10                      | 1.62                      | 2.75                      | 2.66                     
Euler                     | -                         | 3.58                      | 2.20                      | 2.65                      | 2.68                     
Midpoint Explicit         | -                         | 3.98                      | 3.04                      | 3.02                      | 3.08                     
Midpoint Fixed            | -                         | 4.73                      | 3.23                      | 3.19                      | 3.25                     
RK4                       | -                         | 5.28                      | 3.66                      | 3.89                      | 3.86                     
FD - L Convection         | -                         | 3.08                      | 1.18                      | 2.59                      | 2.65                     
FD - NL Convection        | -                         | 3.91                      | 1.25                      | 2.58                      | 2.65                     
FD - Poisson              | -                         | 4.12                      | 1.78                      | 2.81                      | 2.82                     
FD - Laplace              | -                         | 8.36                      | 3.45                      | 3.34                      | 3.44                     
M-D                       | -                         | 8.53                      | 4.02                      | 3.94                      | 3.60                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 482.00 $\pm$ 3.00         | 3.03 $\pm$ 0.00           | 17.00 $\pm$ 0.40          | 2.56 $\pm$ 0.00           | 2.78 $\pm$ 0.00          
Bellman Ford (ms)         | 3490.00 $\pm$ 90.00       | 9.26 $\pm$ 0.01           | 7.63 $\pm$ 0.01           | 4.59 $\pm$ 0.01           | 7.76 $\pm$ 0.01          
Dijkstra (ms)             | 8820.00 $\pm$ 30.00       | 55.20 $\pm$ 0.50          | 45.10 $\pm$ 0.80          | 43.20 $\pm$ 0.40          | 57.00 $\pm$ 0.80         
Euler (ms)                | 5490.00 $\pm$ 40.00       | 50.30 $\pm$ 0.30          | 134.00 $\pm$ 1.00         | 24.40 $\pm$ 0.80          | 281.00 $\pm$ 4.00        
Midpoint Explicit (ms)    | 11300.00 $\pm$ 100.00     | 96.90 $\pm$ 0.60          | 249.00 $\pm$ 1.00         | 35.40 $\pm$ 0.50          | 556.00 $\pm$ 3.00        
Midpoint Fixed (s)        | 56.10 $\pm$ 1.00          | 0.80 $\pm$ 0.01           | 1.26 $\pm$ 0.00           | 0.12 $\pm$ 0.01           | 2.77 $\pm$ 0.02          
RK4 (ms)                  | 27500.00 $\pm$ 200.00     | 245.00 $\pm$ 7.00         | 460.00 $\pm$ 3.00         | 56.00 $\pm$ 2.90          | 926.00 $\pm$ 74.00       
FD - L Convection (ms)    | 3990.00 $\pm$ 20.00       | 3.66 $\pm$ 0.07           | 4.01 $\pm$ 0.17           | 1.98 $\pm$ 0.07           | 2.91 $\pm$ 0.02          
FD - NL Convection (ms)   | 5000.00 $\pm$ 20.00       | 4.21 $\pm$ 0.04           | 4.11 $\pm$ 0.14           | 2.08 $\pm$ 0.06           | 3.19 $\pm$ 0.17          
FD - Poisson (ms)         | 10600.00 $\pm$ 0.00       | 7.23 $\pm$ 0.02           | 11.70 $\pm$ 0.10          | 4.44 $\pm$ 0.01           | 5.88 $\pm$ 0.00          
FD - Laplace (ms)         | 870.00 $\pm$ 8.00         | 279.00 $\pm$ 2.00         | 457.00 $\pm$ 4.00         | 90.50 $\pm$ 1.90          | 500.00 $\pm$ 2.00        
M-D (ms)                  | 22300.00 $\pm$ 200.00     | 63.50 $\pm$ 0.00          | 88.20 $\pm$ 0.40          | 127.00 $\pm$ 0.00         | 132.00 $\pm$ 0.00        

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 3.65                      | 0.59                      | 1.84                      | 1.78                     
Bellman Ford              | -                         | 5.14                      | 1.76                      | 3.21                      | 3.04                     
Dijkstra                  | -                         | 4.05                      | 1.99                      | 3.32                      | 3.11                     
Euler                     | -                         | 4.64                      | 2.73                      | 3.13                      | 3.22                     
Midpoint Explicit         | -                         | 5.05                      | 3.75                      | 3.60                      | 3.70                     
Midpoint Fixed            | -                         | 6.03                      | 3.94                      | 3.63                      | 3.75                     
RK4                       | -                         | 6.70                      | 4.51                      | 4.45                      | 4.50                     
FD - L Convection         | -                         | 3.84                      | 1.45                      | 3.16                      | 3.20                     
FD - NL Convection        | -                         | 5.04                      | 1.54                      | 3.11                      | 3.27                     
FD - Poisson              | -                         | 5.32                      | 2.18                      | 3.33                      | 3.44                     
FD - Laplace              | -                         | 10.88                     | 4.08                      | 3.98                      | 3.97                     
M-D                       | -                         | 10.58                     | 5.39                      | 4.71                      | 4.14                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 570.00 $\pm$ 11.00        | 10.30 $\pm$ 0.30          | 33.80 $\pm$ 0.60          | 2.66 $\pm$ 0.11           | 2.71 $\pm$ 0.07          
Bellman Ford (ms)         | 3780.00 $\pm$ 50.00       | 8.22 $\pm$ 0.26           | 8.78 $\pm$ 0.25           | 5.75 $\pm$ 0.20           | 11.60 $\pm$ 0.40         
Dijkstra (ms)             | 9740.00 $\pm$ 90.00       | 53.20 $\pm$ 2.40          | 54.50 $\pm$ 2.60          | 45.80 $\pm$ 1.60          | 68.50 $\pm$ 2.40         
Euler (ms)                | 6940.00 $\pm$ 340.00      | 55.70 $\pm$ 2.40          | 148.00 $\pm$ 5.00         | 30.90 $\pm$ 1.40          | 316.00 $\pm$ 7.00        
Midpoint Explicit (ms)    | 13700.00 $\pm$ 900.00     | 107.00 $\pm$ 4.00         | 302.00 $\pm$ 19.00        | 45.90 $\pm$ 2.50          | 600.00 $\pm$ 17.00       
Midpoint Fixed (s)        | 68.90 $\pm$ 4.10          | 0.87 $\pm$ 0.01           | 1.43 $\pm$ 0.03           | 0.14 $\pm$ 0.01           | 2.96 $\pm$ 0.05          
RK4 (ms)                  | 34000.00 $\pm$ 1900.00    | 284.00 $\pm$ 19.00        | 533.00 $\pm$ 11.00        | 64.00 $\pm$ 3.40          | 996.00 $\pm$ 17.00       
FD - L Convection (ms)    | 4310.00 $\pm$ 80.00       | 4.32 $\pm$ 0.14           | 4.86 $\pm$ 0.18           | 3.45 $\pm$ 0.37           | 5.01 $\pm$ 0.61          
FD - NL Convection (ms)   | 5350.00 $\pm$ 90.00       | 5.31 $\pm$ 0.22           | 5.17 $\pm$ 0.17           | 3.54 $\pm$ 0.37           | 6.10 $\pm$ 0.65          
FD - Poisson (ms)         | 11800.00 $\pm$ 100.00     | 11.50 $\pm$ 0.40          | 15.00 $\pm$ 0.40          | 9.31 $\pm$ 0.53           | 12.50 $\pm$ 0.30         
FD - Laplace (ms)         | 1240.00 $\pm$ 30.00       | 393.00 $\pm$ 10.00        | 595.00 $\pm$ 15.00        | 203.00 $\pm$ 5.00         | 591.00 $\pm$ 13.00       
M-D (ms)                  | 26200.00 $\pm$ 600.00     | 80.20 $\pm$ 6.70          | 110.00 $\pm$ 5.00         | 146.00 $\pm$ 6.00         | 151.00 $\pm$ 3.00        

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.43                      | 0.35                      | 1.24                      | 1.19                     
Bellman Ford              | -                         | 3.42                      | 1.14                      | 2.22                      | 2.19                     
Dijkstra                  | -                         | 2.60                      | 1.27                      | 2.30                      | 2.20                     
Euler                     | -                         | 2.99                      | 1.71                      | 2.17                      | 2.21                     
Midpoint Explicit         | -                         | 3.34                      | 2.37                      | 2.47                      | 2.57                     
Midpoint Fixed            | -                         | 3.86                      | 2.51                      | 2.53                      | 2.59                     
RK4                       | -                         | 4.30                      | 2.79                      | 3.03                      | 3.05                     
FD - L Convection         | -                         | 2.54                      | 0.91                      | 2.10                      | 2.15                     
FD - NL Convection        | -                         | 3.25                      | 0.97                      | 2.12                      | 2.21                     
FD - Poisson              | -                         | 3.42                      | 1.40                      | 2.28                      | 2.30                     
FD - Laplace              | -                         | 6.71                      | 2.61                      | 2.70                      | 2.77                     
M-D                       | -                         | 7.05                      | 3.20                      | 3.17                      | 2.95                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 406.00 $\pm$ 4.00         | 9.89 $\pm$ 0.01           | 27.10 $\pm$ 0.20          | 3.14 $\pm$ 0.01           | 3.24 $\pm$ 0.00          
Bellman Ford (ms)         | 2620.00 $\pm$ 50.00       | 6.73 $\pm$ 0.01           | 6.34 $\pm$ 0.01           | 4.46 $\pm$ 0.00           | 6.59 $\pm$ 0.01          
Dijkstra (ms)             | 6430.00 $\pm$ 30.00       | 42.20 $\pm$ 0.50          | 35.20 $\pm$ 0.60          | 32.80 $\pm$ 0.40          | 49.80 $\pm$ 0.50         
Euler (ms)                | 4970.00 $\pm$ 20.00       | 39.90 $\pm$ 0.60          | 108.00 $\pm$ 0.00         | 20.40 $\pm$ 0.50          | 203.00 $\pm$ 3.00        
Midpoint Explicit (ms)    | 10100.00 $\pm$ 0.00       | 78.00 $\pm$ 4.20          | 215.00 $\pm$ 14.00        | 29.70 $\pm$ 0.90          | 401.00 $\pm$ 2.00        
Midpoint Fixed (s)        | 49.50 $\pm$ 0.20          | 0.61 $\pm$ 0.01           | 1.10 $\pm$ 0.03           | 0.10 $\pm$ 0.00           | 1.98 $\pm$ 0.02          
RK4 (ms)                  | 25000.00 $\pm$ 100.00     | 223.00 $\pm$ 6.00         | 405.00 $\pm$ 6.00         | 41.90 $\pm$ 0.70          | 666.00 $\pm$ 4.00        
FD - L Convection (ms)    | 2670.00 $\pm$ 30.00       | 2.92 $\pm$ 0.06           | 3.25 $\pm$ 0.19           | 1.70 $\pm$ 0.01           | 2.62 $\pm$ 0.13          
FD - NL Convection (ms)   | 3260.00 $\pm$ 30.00       | 3.36 $\pm$ 0.08           | 3.40 $\pm$ 0.11           | 1.61 $\pm$ 0.01           | 2.64 $\pm$ 0.32          
FD - Poisson (ms)         | 8180.00 $\pm$ 130.00      | 5.78 $\pm$ 0.00           | 10.10 $\pm$ 0.10          | 4.20 $\pm$ 0.01           | 5.31 $\pm$ 0.00          
FD - Laplace (ms)         | 367.00 $\pm$ 2.00         | 251.00 $\pm$ 1.00         | 390.00 $\pm$ 3.00         | 77.10 $\pm$ 0.80          | 365.00 $\pm$ 0.00        
M-D (ms)                  | 20000.00 $\pm$ 100.00     | 65.00 $\pm$ 0.00          | 78.30 $\pm$ 0.50          | 120.00 $\pm$ 0.00         | 122.00 $\pm$ 0.00        

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
