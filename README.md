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
### Performance Comparison (as of Fri Jan 27 12:53:54 UTC 2023)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.47                      | 0.39                      | 1.88                      | 1.71                     
Bellman Ford              | -                         | 3.22                      | 1.09                      | 2.75                      | 2.76                     
Dijkstra                  | -                         | 3.28                      | 1.44                      | 2.86                      | 2.86                     
Euler                     | -                         | 3.72                      | 1.50                      | 2.74                      | 2.78                     
Midpoint Explicit         | -                         | 4.33                      | 2.32                      | 3.19                      | 3.15                     
Midpoint Fixed            | -                         | 4.87                      | 2.60                      | 3.11                      | 3.24                     
RK4                       | -                         | 5.16                      | 2.69                      | 3.74                      | 3.77                     
FD - L Convection         | -                         | 2.84                      | 0.37                      | 2.58                      | 2.65                     
FD - NL Convection        | -                         | 2.84                      | 0.35                      | 2.57                      | 2.73                     
FD - Poisson              | -                         | 7.69                      | 0.84                      | 2.66                      | 2.73                     
FD - Laplace              | -                         | 11.22                     | 2.60                      | 3.33                      | -                        
M-D                       | -                         | -                         | 6.15                      | 3.99                      | 3.75                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 421.00                    | 4.47                      | 21.10                     | 2.46                      | 2.62                     
Bellman Ford (ns)         | 68200.00                  | 422.00                    | 600.00                    | 249.00                    | 554.00                   
Dijkstra (ns)             | 34100.00                  | 378.00                    | 700.00                    | 299.00                    | 540.00                   
Euler (ms)                | 52.80                     | 0.76                      | 1.30                      | 0.15                      | 3.39                     
Midpoint Explicit (ms)    | 103.00                    | 1.77                      | 3.49                      | 0.26                      | 5.82                     
Midpoint Fixed (ms)       | 529.00                    | 9.94                      | 16.70                     | 1.03                      | 25.50                    
RK4 (ms)                  | 259.00                    | 2.31                      | 6.18                      | 0.29                      | 6.89                     
FD - L Convection (ms)    | 2300.00                   | 2.57                      | 9.43                      | 1.72                      | 1.83                     
FD - NL Convection (ms)   | 2930.00                   | 3.76                      | 10.00                     | 1.73                      | 1.86                     
FD - Poisson (ms)         | 4920.00                   | 3.20                      | 12.60                     | 4.12                      | 1.93                     
FD - Laplace (ms)         | 595.00                    | 344.00                    | 628.00                    | 0.05                      | -                        
M-D (ms)                  | 52400.00                  | -                         | 253.00                    | 310.00                    | 312.00                   

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.7 results
### Performance Comparison (as of 1.7.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.06                      | 0.38                      | 1.60                      | 1.48                     
Bellman Ford              | -                         | 2.69                      | 1.04                      | 2.49                      | 2.42                     
Dijkstra                  | -                         | 2.78                      | 1.39                      | 2.58                      | 2.52                     
Euler                     | -                         | 3.26                      | 1.46                      | 2.49                      | 2.48                     
Midpoint Explicit         | -                         | 3.79                      | 2.27                      | 2.83                      | 2.85                     
Midpoint Fixed            | -                         | 4.54                      | 2.59                      | 2.90                      | 2.94                     
RK4                       | -                         | 4.60                      | 2.64                      | 3.53                      | 3.46                     
FD - L Convection         | -                         | 2.42                      | 0.34                      | 2.33                      | 2.40                     
FD - NL Convection        | -                         | 2.43                      | 0.34                      | 2.34                      | 2.42                     
FD - Poisson              | -                         | 6.87                      | 0.83                      | 2.49                      | 2.48                     
FD - Laplace              | -                         | 10.45                     | 2.56                      | 3.14                      | -                        
M-D                       | -                         | -                         | 5.91                      | 3.72                      | 3.44                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 512.00 $\pm$ 14.00        | 4.00 $\pm$ 0.08           | 19.70 $\pm$ 0.70          | 2.30 $\pm$ 0.05           | 2.57 $\pm$ 0.06          
Bellman Ford (ns)         | 68600.00 $\pm$ 1800.00    | 398.00 $\pm$ 11.00        | 588.00 $\pm$ 18.00        | 241.00 $\pm$ 7.00         | 534.00 $\pm$ 14.00       
Dijkstra (ns)             | 36300.00 $\pm$ 1100.00    | 349.00 $\pm$ 10.00        | 407.00 $\pm$ 12.00        | 306.00 $\pm$ 9.00         | 523.00 $\pm$ 15.00       
Euler (ms)                | 59.50 $\pm$ 2.60          | 0.76 $\pm$ 0.02           | 1.21 $\pm$ 0.04           | 0.14 $\pm$ 0.00           | 3.26 $\pm$ 0.10          
Midpoint Explicit (ms)    | 121.00 $\pm$ 3.00         | 1.70 $\pm$ 0.04           | 3.13 $\pm$ 0.13           | 0.24 $\pm$ 0.01           | 5.80 $\pm$ 0.14          
Midpoint Fixed (ms)       | 608.00 $\pm$ 16.00        | 10.40 $\pm$ 0.80          | 17.30 $\pm$ 0.50          | 1.03 $\pm$ 0.03           | 25.70 $\pm$ 0.70         
RK4 (ms)                  | 279.00 $\pm$ 9.00         | 2.36 $\pm$ 0.05           | 6.22 $\pm$ 0.19           | 0.29 $\pm$ 0.01           | 6.90 $\pm$ 0.22          
FD - L Convection (ms)    | 2390.00 $\pm$ 50.00       | 2.48 $\pm$ 0.07           | 10.20 $\pm$ 0.20          | 1.64 $\pm$ 0.04           | 1.87 $\pm$ 0.06          
FD - NL Convection (ms)   | 3400.00 $\pm$ 50.00       | 3.76 $\pm$ 0.14           | 10.10 $\pm$ 0.20          | 1.73 $\pm$ 0.05           | 1.82 $\pm$ 0.04          
FD - Poisson (ms)         | 5000.00 $\pm$ 60.00       | 3.46 $\pm$ 0.07           | 11.30 $\pm$ 0.20          | 4.29 $\pm$ 0.12           | 1.90 $\pm$ 0.04          
FD - Laplace (ms)         | 568.00 $\pm$ 15.00        | 324.00 $\pm$ 9.00         | 623.00 $\pm$ 12.00        | 117.00 $\pm$ 3.00         | -                        
M-D (ms)                  | 57000.00 $\pm$ 1200.00    | -                         | 246.00 $\pm$ 7.00         | 304.00 $\pm$ 16.00        | 297.00 $\pm$ 9.00        

![Python 3.7 compilation results](./version_specific_results/pypi_performance_37_compilation.svg)
![Python 3.7 execution results](./version_specific_results/pypi_performance_37_execution.svg)
## Python 3.8 results
### Performance Comparison (as of 1.7.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.78                      | 0.32                      | 1.36                      | 1.30                     
Bellman Ford              | -                         | 2.40                      | 0.93                      | 2.22                      | 2.20                     
Dijkstra                  | -                         | 2.42                      | 1.22                      | 2.29                      | 2.27                     
Euler                     | -                         | 2.86                      | 1.29                      | 2.26                      | 2.26                     
Midpoint Explicit         | -                         | 3.39                      | 1.96                      | 2.56                      | 2.56                     
Midpoint Fixed            | -                         | 3.90                      | 2.26                      | 2.61                      | 2.66                     
RK4                       | -                         | 4.05                      | 2.33                      | 3.13                      | 3.11                     
FD - L Convection         | -                         | 2.14                      | 0.31                      | 2.09                      | 2.15                     
FD - NL Convection        | -                         | 2.12                      | 0.31                      | 2.10                      | 2.17                     
FD - Poisson              | -                         | 6.20                      | 0.73                      | 2.21                      | 2.23                     
FD - Laplace              | -                         | 9.25                      | 2.26                      | 2.80                      | -                        
M-D                       | -                         | -                         | 5.21                      | 3.23                      | 3.03                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 478.00 $\pm$ 3.00         | 9.72 $\pm$ 0.02           | 32.30 $\pm$ 0.20          | 3.28 $\pm$ 0.00           | 3.28 $\pm$ 0.00          
Bellman Ford (ns)         | 58700.00 $\pm$ 400.00     | 368.00 $\pm$ 1.00         | 541.00 $\pm$ 5.00         | 234.00 $\pm$ 1.00         | 487.00 $\pm$ 3.00        
Dijkstra (ns)             | 30500.00 $\pm$ 200.00     | 333.00 $\pm$ 1.00         | 356.00 $\pm$ 10.00        | 249.00 $\pm$ 2.00         | 480.00 $\pm$ 2.00        
Euler (ms)                | 46.50 $\pm$ 0.60          | 0.64 $\pm$ 0.01           | 1.28 $\pm$ 0.02           | 0.15 $\pm$ 0.00           | 2.62 $\pm$ 0.01          
Midpoint Explicit (ms)    | 94.70 $\pm$ 1.30          | 1.49 $\pm$ 0.02           | 3.17 $\pm$ 0.05           | 0.25 $\pm$ 0.01           | 4.63 $\pm$ 0.04          
Midpoint Fixed (ms)       | 483.00 $\pm$ 5.00         | 8.74 $\pm$ 0.06           | 17.50 $\pm$ 0.10          | 0.96 $\pm$ 0.00           | 20.00 $\pm$ 0.10         
RK4 (ms)                  | 238.00 $\pm$ 2.00         | 2.40 $\pm$ 0.01           | 6.33 $\pm$ 0.05           | 0.28 $\pm$ 0.00           | 5.46 $\pm$ 0.08          
FD - L Convection (ms)    | 2370.00 $\pm$ 40.00       | 2.55 $\pm$ 0.00           | 9.12 $\pm$ 0.15           | 1.83 $\pm$ 0.01           | 1.59 $\pm$ 0.07          
FD - NL Convection (ms)   | 2900.00 $\pm$ 30.00       | 4.16 $\pm$ 0.00           | 9.43 $\pm$ 0.11           | 1.72 $\pm$ 0.00           | 1.56 $\pm$ 0.00          
FD - Poisson (ms)         | 4140.00 $\pm$ 10.00       | 2.91 $\pm$ 0.00           | 10.90 $\pm$ 0.00          | 3.96 $\pm$ 0.00           | 2.06 $\pm$ 0.00          
FD - Laplace (ms)         | 605.00 $\pm$ 5.00         | 344.00 $\pm$ 1.00         | 561.00 $\pm$ 2.00         | 113.00 $\pm$ 0.00         | -                        
M-D (ms)                  | 50600.00 $\pm$ 1000.00    | -                         | 231.00 $\pm$ 1.00         | 302.00 $\pm$ 0.00         | 302.00 $\pm$ 0.00        

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.7.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.30                      | 0.41                      | 1.87                      | 1.66                     
Bellman Ford              | -                         | 3.01                      | 1.09                      | 2.78                      | 2.66                     
Dijkstra                  | -                         | 2.97                      | 1.44                      | 2.81                      | 2.76                     
Euler                     | -                         | 3.56                      | 1.47                      | 2.74                      | 2.75                     
Midpoint Explicit         | -                         | 4.16                      | 2.21                      | 3.13                      | 3.15                     
Midpoint Fixed            | -                         | 4.75                      | 2.59                      | 3.20                      | 3.23                     
RK4                       | -                         | 5.17                      | 2.71                      | 3.81                      | 3.75                     
FD - L Convection         | -                         | 2.70                      | 0.37                      | 2.59                      | 2.58                     
FD - NL Convection        | -                         | 2.68                      | 0.37                      | 2.61                      | 2.66                     
FD - Poisson              | -                         | 7.40                      | 0.91                      | 2.84                      | 2.76                     
FD - Laplace              | -                         | 11.55                     | 2.71                      | 3.42                      | -                        
M-D                       | -                         | -                         | 6.17                      | 3.95                      | 3.65                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 439.00 $\pm$ 5.00         | 4.46 $\pm$ 0.09           | 20.90 $\pm$ 0.60          | 2.48 $\pm$ 0.05           | 2.60 $\pm$ 0.06          
Bellman Ford (ns)         | 66700.00 $\pm$ 1800.00    | 436.00 $\pm$ 12.00        | 630.00 $\pm$ 10.00        | 246.00 $\pm$ 7.00         | 568.00 $\pm$ 17.00       
Dijkstra (ns)             | 33100.00 $\pm$ 700.00     | 390.00 $\pm$ 21.00        | 437.00 $\pm$ 9.00         | 313.00 $\pm$ 8.00         | 532.00 $\pm$ 13.00       
Euler (ms)                | 53.50 $\pm$ 1.10          | 0.78 $\pm$ 0.01           | 1.31 $\pm$ 0.05           | 0.15 $\pm$ 0.00           | 3.43 $\pm$ 0.06          
Midpoint Explicit (ms)    | 108.00 $\pm$ 2.00         | 1.82 $\pm$ 0.06           | 3.33 $\pm$ 0.09           | 0.27 $\pm$ 0.01           | 6.19 $\pm$ 0.08          
Midpoint Fixed (ms)       | 536.00 $\pm$ 15.00        | 10.50 $\pm$ 0.30          | 18.70 $\pm$ 0.40          | 1.12 $\pm$ 0.07           | 27.30 $\pm$ 0.50         
RK4 (ms)                  | 267.00 $\pm$ 6.00         | 2.61 $\pm$ 0.10           | 6.65 $\pm$ 0.15           | 0.32 $\pm$ 0.02           | 7.18 $\pm$ 0.19          
FD - L Convection (ms)    | 2640.00 $\pm$ 50.00       | 2.67 $\pm$ 0.09           | 10.90 $\pm$ 0.30          | 1.83 $\pm$ 0.06           | 1.83 $\pm$ 0.11          
FD - NL Convection (ms)   | 3320.00 $\pm$ 60.00       | 4.09 $\pm$ 0.08           | 10.70 $\pm$ 0.20          | 1.70 $\pm$ 0.04           | 1.94 $\pm$ 0.04          
FD - Poisson (ms)         | 4960.00 $\pm$ 70.00       | 3.53 $\pm$ 0.12           | 12.20 $\pm$ 0.20          | 4.66 $\pm$ 0.11           | 2.05 $\pm$ 0.04          
FD - Laplace (ms)         | 628.00 $\pm$ 10.00        | 350.00 $\pm$ 10.00        | 660.00 $\pm$ 12.00        | 126.00 $\pm$ 3.00         | -                        
M-D (ms)                  | 52400.00 $\pm$ 1300.00    | -                         | 259.00 $\pm$ 9.00         | 313.00 $\pm$ 6.00         | 317.00 $\pm$ 5.00        

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.7.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.53                      | 0.41                      | 1.74                      | 1.68                     
Bellman Ford              | -                         | 3.12                      | 1.08                      | 2.67                      | 2.64                     
Dijkstra                  | -                         | 3.23                      | 1.45                      | 2.71                      | 2.72                     
Euler                     | -                         | 3.71                      | 1.44                      | 2.64                      | 2.77                     
Midpoint Explicit         | -                         | 4.45                      | 2.32                      | 3.09                      | 3.08                     
Midpoint Fixed            | -                         | 5.10                      | 2.60                      | 3.14                      | 3.25                     
RK4                       | -                         | 5.34                      | 2.78                      | 3.66                      | 3.69                     
FD - L Convection         | -                         | 2.90                      | 0.38                      | 2.54                      | 2.62                     
FD - NL Convection        | -                         | 2.86                      | 0.36                      | 2.68                      | 2.67                     
FD - Poisson              | -                         | 7.68                      | 0.88                      | 2.68                      | 2.83                     
FD - Laplace              | -                         | 11.58                     | 2.67                      | 3.35                      | -                        
M-D                       | -                         | -                         | 5.25                      | 3.85                      | 3.55                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 437.00 $\pm$ 13.00        | 4.70 $\pm$ 0.40           | 30.70 $\pm$ 1.80          | 2.10 $\pm$ 0.10           | 2.09 $\pm$ 0.10          
Bellman Ford (ns)         | 63800.00 $\pm$ 2500.00    | 410.00 $\pm$ 17.00        | 578.00 $\pm$ 28.00        | 242.00 $\pm$ 14.00        | 553.00 $\pm$ 36.00       
Dijkstra (ns)             | 31400.00 $\pm$ 1300.00    | 381.00 $\pm$ 18.00        | 409.00 $\pm$ 27.00        | 308.00 $\pm$ 25.00        | 532.00 $\pm$ 32.00       
Euler (ms)                | 48.30 $\pm$ 2.40          | 0.73 $\pm$ 0.05           | 1.17 $\pm$ 0.02           | 0.18 $\pm$ 0.01           | 3.25 $\pm$ 0.14          
Midpoint Explicit (ms)    | 99.10 $\pm$ 4.70          | 1.65 $\pm$ 0.08           | 2.85 $\pm$ 0.09           | 0.33 $\pm$ 0.03           | 5.56 $\pm$ 0.21          
Midpoint Fixed (ms)       | 489.00 $\pm$ 24.00        | 9.49 $\pm$ 0.40           | 13.90 $\pm$ 0.60          | 1.18 $\pm$ 0.05           | 23.70 $\pm$ 1.30         
RK4 (ms)                  | 245.00 $\pm$ 12.00        | 2.28 $\pm$ 0.13           | 4.85 $\pm$ 0.11           | 0.40 $\pm$ 0.01           | 6.32 $\pm$ 0.14          
FD - L Convection (ms)    | 2340.00 $\pm$ 50.00       | 2.52 $\pm$ 0.12           | 9.74 $\pm$ 0.51           | 2.18 $\pm$ 0.07           | 2.83 $\pm$ 0.40          
FD - NL Convection (ms)   | 2950.00 $\pm$ 110.00      | 6.32 $\pm$ 0.20           | 9.71 $\pm$ 0.58           | 2.49 $\pm$ 0.19           | 3.55 $\pm$ 0.38          
FD - Poisson (ms)         | 4730.00 $\pm$ 110.00      | 4.66 $\pm$ 0.20           | 11.70 $\pm$ 0.60          | 5.63 $\pm$ 0.24           | 4.04 $\pm$ 0.12          
FD - Laplace (ms)         | 1270.00 $\pm$ 20.00       | 295.00 $\pm$ 13.00        | 750.00 $\pm$ 22.00        | 223.00 $\pm$ 7.00         | -                        
M-D (ms)                  | 48800.00 $\pm$ 900.00     | -                         | 286.00 $\pm$ 6.00         | 345.00 $\pm$ 7.00         | 349.00 $\pm$ 7.00        

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.7.1)
## Compilation time
Algorithm                 | python                    | pythran                   | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.16                      | 1.70                      | 1.57                     
Bellman Ford              | -                         | 2.66                      | 2.45                      | 2.44                     
Dijkstra                  | -                         | 2.64                      | 2.55                      | 2.50                     
Euler                     | -                         | 3.10                      | 2.48                      | 2.51                     
Midpoint Explicit         | -                         | 3.66                      | 2.80                      | 2.84                     
Midpoint Fixed            | -                         | 4.18                      | 2.85                      | 2.88                     
RK4                       | -                         | 4.43                      | 3.31                      | 3.35                     
FD - L Convection         | -                         | 2.45                      | 2.31                      | 2.40                     
FD - NL Convection        | -                         | 2.40                      | 2.35                      | 2.41                     
FD - Poisson              | -                         | 6.60                      | 2.45                      | 2.50                     
FD - Laplace              | -                         | 9.95                      | 3.06                      | -                        
M-D                       | -                         | -                         | 3.43                      | 3.29                     

## Execution time
Algorithm                 | python                    | pythran                   | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 399.00 $\pm$ 3.00         | 7.88 $\pm$ 0.00           | 3.17 $\pm$ 0.00           | 2.93 $\pm$ 0.01          
Bellman Ford (ns)         | 57000.00 $\pm$ 300.00     | 371.00 $\pm$ 4.00         | 226.00 $\pm$ 6.00         | 496.00 $\pm$ 9.00        
Dijkstra (ns)             | 27600.00 $\pm$ 400.00     | 319.00 $\pm$ 9.00         | 273.00 $\pm$ 6.00         | 476.00 $\pm$ 7.00        
Euler (\textmu s)         | 45800.00 $\pm$ 500.00     | 664.00 $\pm$ 3.00         | 131.00 $\pm$ 0.00         | 3010.00 $\pm$ 50.00      
Midpoint Explicit (ms)    | 93.40 $\pm$ 0.70          | 1.54 $\pm$ 0.02           | 0.23 $\pm$ 0.01           | 5.35 $\pm$ 0.03          
Midpoint Fixed (ms)       | 454.00 $\pm$ 6.00         | 9.03 $\pm$ 0.03           | 0.94 $\pm$ 0.01           | 23.30 $\pm$ 0.10         
RK4 (ms)                  | 224.00 $\pm$ 1.00         | 2.15 $\pm$ 0.01           | 0.26 $\pm$ 0.00           | 6.36 $\pm$ 0.03          
FD - L Convection (ms)    | 2000.00 $\pm$ 30.00       | 2.31 $\pm$ 0.01           | 1.75 $\pm$ 0.01           | 1.70 $\pm$ 0.04          
FD - NL Convection (ms)   | 2580.00 $\pm$ 50.00       | 3.55 $\pm$ 0.22           | 1.72 $\pm$ 0.02           | 1.85 $\pm$ 0.02          
FD - Poisson (ms)         | 4140.00 $\pm$ 20.00       | 2.91 $\pm$ 0.00           | 4.00 $\pm$ 0.04           | 1.77 $\pm$ 0.02          
FD - Laplace (ms)         | 521.00 $\pm$ 6.00         | 297.00 $\pm$ 3.00         | 110.00 $\pm$ 0.00         | -                        
M-D (ms)                  | 44500.00 $\pm$ 300.00     | -                         | 269.00 $\pm$ 0.00         | 274.00 $\pm$ 0.00        

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
