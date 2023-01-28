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
Ackermann                 | -                         | 2.29                      | 0.45                      | 1.83                      | 1.72                     
Bellman Ford              | -                         | 3.15                      | 1.20                      | 2.71                      | 2.89                     
Dijkstra                  | -                         | 3.04                      | 1.72                      | 2.85                      | 2.87                     
Euler                     | -                         | 3.68                      | 1.63                      | 2.73                      | 2.79                     
Midpoint Explicit         | -                         | 4.25                      | 2.49                      | 3.16                      | 3.17                     
Midpoint Fixed            | -                         | 4.98                      | 2.86                      | 3.21                      | 3.26                     
RK4                       | -                         | 5.09                      | 2.97                      | 3.90                      | 3.93                     
FD - L Convection         | -                         | 2.73                      | 0.39                      | 2.82                      | 2.64                     
FD - NL Convection        | -                         | 2.72                      | 0.38                      | 2.71                      | 2.69                     
FD - Poisson              | -                         | 8.05                      | 0.96                      | 2.73                      | 2.76                     
FD - Laplace              | -                         | 11.85                     | 2.88                      | 3.49                      | -                        
M-D                       | -                         | -                         | 6.95                      | 4.21                      | 4.00                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 589.00 $\pm$ 24.00        | 4.44 $\pm$ 0.02           | 21.80 $\pm$ 0.00          | 2.60 $\pm$ 0.10           | 2.69 $\pm$ 0.01          
Bellman Ford (ns)         | 76600.00 $\pm$ 1000.00    | 441.00 $\pm$ 4.00         | 658.00 $\pm$ 21.00        | 273.00 $\pm$ 10.00        | 595.00 $\pm$ 7.00        
Dijkstra (ns)             | 40600.00 $\pm$ 500.00     | 411.00 $\pm$ 15.00        | 452.00 $\pm$ 10.00        | 342.00 $\pm$ 9.00         | 579.00 $\pm$ 10.00       
Euler (ms)                | 66.70 $\pm$ 1.00          | 0.82 $\pm$ 0.00           | 1.32 $\pm$ 0.01           | 0.16 $\pm$ 0.00           | 3.74 $\pm$ 0.12          
Midpoint Explicit (ms)    | 135.00 $\pm$ 2.00         | 1.89 $\pm$ 0.06           | 3.43 $\pm$ 0.04           | 0.28 $\pm$ 0.01           | 6.45 $\pm$ 0.17          
Midpoint Fixed (ms)       | 670.00 $\pm$ 11.00        | 11.80 $\pm$ 0.40          | 19.00 $\pm$ 0.10          | 1.12 $\pm$ 0.00           | 27.70 $\pm$ 0.20         
RK4 (ms)                  | 307.00 $\pm$ 6.00         | 2.70 $\pm$ 0.10           | 6.95 $\pm$ 0.19           | 0.33 $\pm$ 0.01           | 7.53 $\pm$ 0.03          
FD - L Convection (ms)    | 2640.00 $\pm$ 40.00       | 2.78 $\pm$ 0.03           | 11.20 $\pm$ 0.00          | 1.94 $\pm$ 0.10           | 2.10 $\pm$ 0.07          
FD - NL Convection (ms)   | 3770.00 $\pm$ 30.00       | 4.16 $\pm$ 0.02           | 11.10 $\pm$ 0.10          | 1.94 $\pm$ 0.03           | 1.96 $\pm$ 0.02          
FD - Poisson (ms)         | 5530.00 $\pm$ 70.00       | 4.04 $\pm$ 0.17           | 12.50 $\pm$ 0.00          | 4.66 $\pm$ 0.01           | 2.13 $\pm$ 0.04          
FD - Laplace (ms)         | 647.00 $\pm$ 9.00         | 355.00 $\pm$ 5.00         | 681.00 $\pm$ 1.00         | 131.00 $\pm$ 4.00         | -                        
M-D (ms)                  | 63500.00 $\pm$ 1500.00    | -                         | 264.00 $\pm$ 0.00         | 329.00 $\pm$ 8.00         | 329.00 $\pm$ 0.00        

![Python 3.7 compilation results](./version_specific_results/pypi_performance_37_compilation.svg)
![Python 3.7 execution results](./version_specific_results/pypi_performance_37_execution.svg)
## Python 3.8 results
### Performance Comparison (as of 1.7.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.83                      | 0.33                      | 1.40                      | 1.32                     
Bellman Ford              | -                         | 2.42                      | 0.94                      | 2.26                      | 2.22                     
Dijkstra                  | -                         | 2.47                      | 1.25                      | 2.34                      | 2.31                     
Euler                     | -                         | 2.88                      | 1.30                      | 2.24                      | 2.31                     
Midpoint Explicit         | -                         | 3.44                      | 2.01                      | 2.56                      | 2.58                     
Midpoint Fixed            | -                         | 3.91                      | 2.30                      | 2.64                      | 2.69                     
RK4                       | -                         | 4.11                      | 2.37                      | 3.11                      | 3.14                     
FD - L Convection         | -                         | 2.24                      | 0.32                      | 2.10                      | 2.17                     
FD - NL Convection        | -                         | 2.17                      | 0.31                      | 2.12                      | 2.18                     
FD - Poisson              | -                         | 6.27                      | 0.74                      | 2.23                      | 2.26                     
FD - Laplace              | -                         | 9.37                      | 2.28                      | 2.84                      | -                        
M-D                       | -                         | -                         | 5.26                      | 3.31                      | 3.06                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 478.00 $\pm$ 2.00         | 9.72 $\pm$ 0.02           | 32.40 $\pm$ 0.20          | 3.28 $\pm$ 0.00           | 3.28 $\pm$ 0.00          
Bellman Ford (ns)         | 59200.00 $\pm$ 2600.00    | 369.00 $\pm$ 1.00         | 540.00 $\pm$ 3.00         | 224.00 $\pm$ 4.00         | 487.00 $\pm$ 3.00        
Dijkstra (ns)             | 30600.00 $\pm$ 600.00     | 333.00 $\pm$ 2.00         | 351.00 $\pm$ 3.00         | 249.00 $\pm$ 2.00         | 479.00 $\pm$ 1.00        
Euler (ms)                | 46.30 $\pm$ 0.30          | 0.64 $\pm$ 0.01           | 1.27 $\pm$ 0.01           | 0.14 $\pm$ 0.00           | 2.60 $\pm$ 0.02          
Midpoint Explicit (ms)    | 94.50 $\pm$ 0.90          | 1.49 $\pm$ 0.02           | 3.18 $\pm$ 0.07           | 0.24 $\pm$ 0.01           | 4.61 $\pm$ 0.03          
Midpoint Fixed (ms)       | 480.00 $\pm$ 4.00         | 8.79 $\pm$ 0.07           | 17.50 $\pm$ 0.20          | 0.96 $\pm$ 0.02           | 19.80 $\pm$ 0.10         
RK4 (ms)                  | 237.00 $\pm$ 2.00         | 2.40 $\pm$ 0.02           | 6.33 $\pm$ 0.05           | 0.28 $\pm$ 0.00           | 5.44 $\pm$ 0.02          
FD - L Convection (ms)    | 2370.00 $\pm$ 50.00       | 2.55 $\pm$ 0.00           | 9.14 $\pm$ 0.13           | 1.83 $\pm$ 0.01           | 1.56 $\pm$ 0.00          
FD - NL Convection (ms)   | 2910.00 $\pm$ 30.00       | 4.16 $\pm$ 0.00           | 9.41 $\pm$ 0.05           | 1.72 $\pm$ 0.00           | 1.56 $\pm$ 0.00          
FD - Poisson (ms)         | 4150.00 $\pm$ 10.00       | 2.91 $\pm$ 0.00           | 10.90 $\pm$ 0.10          | 3.95 $\pm$ 0.00           | 2.04 $\pm$ 0.00          
FD - Laplace (ms)         | 608.00 $\pm$ 7.00         | 346.00 $\pm$ 3.00         | 561.00 $\pm$ 2.00         | 114.00 $\pm$ 0.00         | -                        
M-D (ms)                  | 50500.00 $\pm$ 1000.00    | -                         | 230.00 $\pm$ 1.00         | 302.00 $\pm$ 1.00         | 304.00 $\pm$ 0.00        

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.7.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.03                      | 0.35                      | 1.61                      | 1.48                     
Bellman Ford              | -                         | 2.64                      | 0.97                      | 2.39                      | 2.40                     
Dijkstra                  | -                         | 2.71                      | 1.27                      | 2.55                      | 2.44                     
Euler                     | -                         | 3.13                      | 1.32                      | 2.44                      | 2.44                     
Midpoint Explicit         | -                         | 3.79                      | 2.04                      | 2.75                      | 2.82                     
Midpoint Fixed            | -                         | 4.25                      | 2.37                      | 2.89                      | 2.91                     
RK4                       | -                         | 4.62                      | 2.45                      | 3.40                      | 3.41                     
FD - L Convection         | -                         | 2.50                      | 0.34                      | 2.38                      | 2.43                     
FD - NL Convection        | -                         | 2.51                      | 0.34                      | 2.38                      | 2.50                     
FD - Poisson              | -                         | 6.75                      | 0.77                      | 2.40                      | 2.44                     
FD - Laplace              | -                         | 10.28                     | 2.35                      | 3.03                      | -                        
M-D                       | -                         | -                         | 5.44                      | 3.54                      | 3.33                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 410.00 $\pm$ 2.00         | 7.89 $\pm$ 0.01           | 30.90 $\pm$ 0.30          | 3.09 $\pm$ 0.01           | 3.12 $\pm$ 0.00          
Bellman Ford (ns)         | 58900.00 $\pm$ 400.00     | 368.00 $\pm$ 4.00         | 537.00 $\pm$ 14.00        | 221.00 $\pm$ 1.00         | 487.00 $\pm$ 4.00        
Dijkstra (ns)             | 29000.00 $\pm$ 1000.00    | 323.00 $\pm$ 1.00         | 373.00 $\pm$ 5.00         | 264.00 $\pm$ 0.00         | 474.00 $\pm$ 3.00        
Euler (ms)                | 45.60 $\pm$ 0.80          | 0.66 $\pm$ 0.00           | 1.13 $\pm$ 0.00           | 0.13 $\pm$ 0.00           | 3.00 $\pm$ 0.01          
Midpoint Explicit (ms)    | 92.60 $\pm$ 1.00          | 1.53 $\pm$ 0.01           | 2.91 $\pm$ 0.02           | 0.23 $\pm$ 0.01           | 5.38 $\pm$ 0.09          
Midpoint Fixed (ms)       | 461.00 $\pm$ 7.00         | 9.12 $\pm$ 0.25           | 16.10 $\pm$ 0.20          | 0.96 $\pm$ 0.04           | 23.40 $\pm$ 0.00         
RK4 (ms)                  | 230.00 $\pm$ 4.00         | 2.15 $\pm$ 0.01           | 5.80 $\pm$ 0.04           | 0.27 $\pm$ 0.02           | 6.41 $\pm$ 0.05          
FD - L Convection (ms)    | 2260.00 $\pm$ 30.00       | 2.32 $\pm$ 0.00           | 9.38 $\pm$ 0.05           | 1.72 $\pm$ 0.02           | 1.54 $\pm$ 0.03          
FD - NL Convection (ms)   | 2870.00 $\pm$ 40.00       | 3.48 $\pm$ 0.03           | 9.22 $\pm$ 0.03           | 1.64 $\pm$ 0.01           | 1.66 $\pm$ 0.02          
FD - Poisson (ms)         | 4270.00 $\pm$ 30.00       | 2.90 $\pm$ 0.00           | 10.50 $\pm$ 0.10          | 3.88 $\pm$ 0.00           | 1.76 $\pm$ 0.01          
FD - Laplace (ms)         | 526.00 $\pm$ 3.00         | 296.00 $\pm$ 2.00         | 567.00 $\pm$ 2.00         | 106.00 $\pm$ 0.00         | -                        
M-D (ms)                  | 45400.00 $\pm$ 1200.00    | -                         | 223.00 $\pm$ 2.00         | 269.00 $\pm$ 0.00         | 274.00 $\pm$ 0.00        

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.7.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.17                      | 0.35                      | 1.63                      | 1.50                     
Bellman Ford              | -                         | 2.83                      | 0.97                      | 2.40                      | 2.39                     
Dijkstra                  | -                         | 2.81                      | 1.27                      | 2.47                      | 2.44                     
Euler                     | -                         | 3.26                      | 1.31                      | 2.40                      | 2.43                     
Midpoint Explicit         | -                         | 3.82                      | 2.04                      | 2.74                      | 2.73                     
Midpoint Fixed            | -                         | 4.32                      | 2.32                      | 2.79                      | 2.83                     
RK4                       | -                         | 4.50                      | 2.36                      | 3.26                      | 3.27                     
FD - L Convection         | -                         | 2.46                      | 0.32                      | 2.27                      | 2.30                     
FD - NL Convection        | -                         | 2.47                      | 0.32                      | 2.25                      | 2.33                     
FD - Poisson              | -                         | 6.71                      | 0.76                      | 2.34                      | 2.40                     
FD - Laplace              | -                         | 10.00                     | 2.32                      | 2.97                      | -                        
M-D                       | -                         | -                         | 5.28                      | 3.39                      | 3.19                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 408.00 $\pm$ 6.00         | 7.91 $\pm$ 0.00           | 30.90 $\pm$ 0.30          | 2.99 $\pm$ 0.01           | 2.96 $\pm$ 0.01          
Bellman Ford (ns)         | 60200.00 $\pm$ 1100.00    | 364.00 $\pm$ 1.00         | 528.00 $\pm$ 4.00         | 216.00 $\pm$ 4.00         | 490.00 $\pm$ 5.00        
Dijkstra (ns)             | 29500.00 $\pm$ 200.00     | 321.00 $\pm$ 2.00         | 376.00 $\pm$ 10.00        | 261.00 $\pm$ 0.00         | 468.00 $\pm$ 2.00        
Euler (ms)                | 44.60 $\pm$ 0.30          | 0.67 $\pm$ 0.01           | 1.11 $\pm$ 0.01           | 0.13 $\pm$ 0.00           | 3.01 $\pm$ 0.01          
Midpoint Explicit (ms)    | 92.40 $\pm$ 1.00          | 1.54 $\pm$ 0.03           | 2.89 $\pm$ 0.02           | 0.22 $\pm$ 0.00           | 5.32 $\pm$ 0.01          
Midpoint Fixed (ms)       | 453.00 $\pm$ 8.00         | 9.07 $\pm$ 0.04           | 16.00 $\pm$ 0.20          | 0.94 $\pm$ 0.00           | 23.30 $\pm$ 0.00         
RK4 (ms)                  | 228.00 $\pm$ 2.00         | 2.16 $\pm$ 0.03           | 5.75 $\pm$ 0.05           | 0.27 $\pm$ 0.02           | 6.37 $\pm$ 0.05          
FD - L Convection (ms)    | 2140.00 $\pm$ 40.00       | 2.31 $\pm$ 0.01           | 9.41 $\pm$ 0.10           | 1.66 $\pm$ 0.03           | 1.61 $\pm$ 0.09          
FD - NL Convection (ms)   | 2690.00 $\pm$ 20.00       | 3.46 $\pm$ 0.03           | 9.23 $\pm$ 0.06           | 1.69 $\pm$ 0.07           | 1.65 $\pm$ 0.07          
FD - Poisson (ms)         | 4280.00 $\pm$ 50.00       | 2.93 $\pm$ 0.06           | 10.40 $\pm$ 0.00          | 3.88 $\pm$ 0.00           | 1.76 $\pm$ 0.00          
FD - Laplace (ms)         | 525.00 $\pm$ 8.00         | 296.00 $\pm$ 3.00         | 568.00 $\pm$ 1.00         | 107.00 $\pm$ 1.00         | -                        
M-D (ms)                  | 46200.00 $\pm$ 900.00     | -                         | 222.00 $\pm$ 4.00         | 269.00 $\pm$ 0.00         | 274.00 $\pm$ 0.00        

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
Python 3.11 benchmarks failed!

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
