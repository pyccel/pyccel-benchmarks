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
### Performance Comparison (as of Tue Mar  7 16:26:07 UTC 2023)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.43                      | 0.35                      | 1.61                      | 1.51                     
Bellman Ford              | -                         | 3.53                      | 1.11                      | 2.42                      | 2.43                     
Dijkstra                  | -                         | 2.79                      | 1.26                      | 2.47                      | 2.45                     
Euler                     | -                         | 3.15                      | 1.70                      | 2.36                      | 2.39                     
Midpoint Explicit         | -                         | 3.55                      | 2.40                      | 2.72                      | 2.76                     
Midpoint Fixed            | -                         | 4.35                      | 2.76                      | 2.83                      | 2.90                     
RK4                       | -                         | 4.87                      | 3.07                      | 3.42                      | 3.37                     
FD - L Convection         | -                         | 2.77                      | 0.98                      | 2.31                      | 2.35                     
FD - NL Convection        | -                         | 3.58                      | 1.04                      | 2.33                      | 2.42                     
FD - Poisson              | -                         | 4.29                      | 1.47                      | 2.49                      | 2.51                     
FD - Laplace              | -                         | 8.65                      | 2.85                      | 2.95                      | 3.03                     
M-D                       | -                         | 7.29                      | 3.29                      | 3.32                      | 3.14                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 406.00                    | 7.88                      | 30.60                     | 3.15                      | 3.34                     
Bellman Ford (ms)         | 2640.00                   | 7.11                      | 9.69                      | 3.84                      | 6.44                     
Dijkstra (ms)             | 6890.00                   | 45.40                     | 40.10                     | 35.10                     | 50.30                    
Euler (ms)                | 4610.00                   | 40.80                     | 116.00                    | 19.10                     | 236.00                   
Midpoint Explicit (ms)    | 9730.00                   | 77.10                     | 312.00                    | 29.20                     | 465.00                   
Midpoint Fixed (s)        | 47.40                     | 0.66                      | 1.60                      | 0.10                      | 2.31                     
RK4 (ms)                  | 23700.00                  | 198.00                    | 582.00                    | 34.40                     | 592.00                   
FD - L Convection (ms)    | 2820.00                   | 4.42                      | 13.70                     | 2.56                      | 2.80                     
FD - NL Convection (ms)   | 3550.00                   | 4.02                      | 14.60                     | 2.51                      | 2.57                     
FD - Poisson (ms)         | 8120.00                   | 6.13                      | 18.70                     | 3.77                      | 4.89                     
FD - Laplace (ms)         | 698.00                    | 211.00                    | 390.00                    | 76.10                     | 362.00                   
M-D (ms)                  | 18600.00                  | 54.00                     | 87.40                     | 106.00                    | 110.00                   

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.7 results
### Performance Comparison (as of 1.7.2)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.07                      | 0.38                      | 1.61                      | 1.50                     
Bellman Ford              | -                         | 3.46                      | 1.19                      | 2.56                      | 2.45                     
Dijkstra                  | -                         | 2.77                      | 1.38                      | 2.50                      | 2.46                     
Euler                     | -                         | 3.31                      | 1.84                      | 2.45                      | 2.47                     
Midpoint Explicit         | -                         | 3.54                      | 2.67                      | 2.84                      | 2.82                     
Midpoint Fixed            | -                         | 4.41                      | 3.03                      | 2.89                      | 2.87                     
RK4                       | -                         | 4.67                      | 3.42                      | 3.39                      | 3.46                     
FD - L Convection         | -                         | 2.68                      | 1.07                      | 2.36                      | 2.50                     
FD - NL Convection        | -                         | 3.56                      | 1.12                      | 2.36                      | 2.44                     
FD - Poisson              | -                         | 4.39                      | 1.62                      | 2.63                      | 2.54                     
FD - Laplace              | -                         | 9.13                      | 3.25                      | 3.18                      | 3.12                     
M-D                       | -                         | 7.55                      | 3.61                      | 3.44                      | 3.35                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 479.00 $\pm$ 15.00        | 3.98 $\pm$ 0.10           | 19.50 $\pm$ 0.70          | 2.45 $\pm$ 0.06           | 2.43 $\pm$ 0.08          
Bellman Ford (ms)         | 2770.00 $\pm$ 40.00       | 6.57 $\pm$ 0.28           | 10.50 $\pm$ 0.20          | 4.13 $\pm$ 0.09           | 6.99 $\pm$ 0.27          
Dijkstra (ms)             | 7820.00 $\pm$ 110.00      | 45.70 $\pm$ 1.20          | 43.20 $\pm$ 1.40          | 39.00 $\pm$ 1.20          | 53.90 $\pm$ 1.00         
Euler (ms)                | 5960.00 $\pm$ 160.00      | 45.00 $\pm$ 1.60          | 124.00 $\pm$ 4.00         | 20.50 $\pm$ 0.70          | 253.00 $\pm$ 8.00        
Midpoint Explicit (ms)    | 12000.00 $\pm$ 300.00     | 88.40 $\pm$ 2.50          | 319.00 $\pm$ 11.00        | 31.20 $\pm$ 1.50          | 513.00 $\pm$ 7.00        
Midpoint Fixed (s)        | 60.20 $\pm$ 2.10          | 0.73 $\pm$ 0.01           | 1.71 $\pm$ 0.03           | 0.11 $\pm$ 0.00           | 2.52 $\pm$ 0.05          
RK4 (ms)                  | 27300.00 $\pm$ 700.00     | 213.00 $\pm$ 10.00        | 624.00 $\pm$ 10.00        | 36.60 $\pm$ 1.70          | 643.00 $\pm$ 11.00       
FD - L Convection (ms)    | 3200.00 $\pm$ 70.00       | 3.80 $\pm$ 0.10           | 14.80 $\pm$ 0.40          | 2.64 $\pm$ 0.13           | 2.76 $\pm$ 0.10          
FD - NL Convection (ms)   | 4380.00 $\pm$ 100.00      | 4.50 $\pm$ 0.15           | 15.90 $\pm$ 0.70          | 2.43 $\pm$ 0.08           | 3.12 $\pm$ 0.08          
FD - Poisson (ms)         | 9490.00 $\pm$ 120.00      | 6.90 $\pm$ 0.32           | 20.40 $\pm$ 0.90          | 4.08 $\pm$ 0.10           | 5.30 $\pm$ 0.13          
FD - Laplace (ms)         | 785.00 $\pm$ 21.00        | 220.00 $\pm$ 5.00         | 417.00 $\pm$ 10.00        | 85.50 $\pm$ 2.70          | 419.00 $\pm$ 9.00        
M-D (ms)                  | 22200.00 $\pm$ 500.00     | 59.00 $\pm$ 2.90          | 94.80 $\pm$ 2.30          | 114.00 $\pm$ 4.00         | 117.00 $\pm$ 3.00        

![Python 3.7 compilation results](./version_specific_results/pypi_performance_37_compilation.svg)
![Python 3.7 execution results](./version_specific_results/pypi_performance_37_execution.svg)
## Python 3.8 results
### Performance Comparison (as of 1.7.2)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.80                      | 0.33                      | 1.39                      | 1.31                     
Bellman Ford              | -                         | 3.14                      | 1.08                      | 2.27                      | 2.22                     
Dijkstra                  | -                         | 2.34                      | 1.20                      | 2.32                      | 2.24                     
Euler                     | -                         | 2.74                      | 1.66                      | 2.22                      | 2.26                     
Midpoint Explicit         | -                         | 3.18                      | 2.35                      | 2.60                      | 2.60                     
Midpoint Fixed            | -                         | 3.87                      | 2.68                      | 2.61                      | 2.66                     
RK4                       | -                         | 4.20                      | 2.99                      | 3.18                      | 3.17                     
FD - L Convection         | -                         | 2.48                      | 0.96                      | 2.21                      | 2.22                     
FD - NL Convection        | -                         | 3.20                      | 1.00                      | 2.19                      | 2.21                     
FD - Poisson              | -                         | 3.87                      | 1.43                      | 2.39                      | 2.37                     
FD - Laplace              | -                         | 7.90                      | 2.77                      | 2.81                      | 2.88                     
M-D                       | -                         | 6.83                      | 3.27                      | 3.21                      | 3.00                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 478.00 $\pm$ 3.00         | 9.74 $\pm$ 0.02           | 32.30 $\pm$ 0.30          | 3.14 $\pm$ 0.00           | 3.28 $\pm$ 0.00          
Bellman Ford (ms)         | 2610.00 $\pm$ 70.00       | 6.46 $\pm$ 0.01           | 10.50 $\pm$ 0.00          | 4.45 $\pm$ 0.00           | 6.57 $\pm$ 0.00          
Dijkstra (ms)             | 6870.00 $\pm$ 20.00       | 37.90 $\pm$ 0.40          | 32.10 $\pm$ 0.60          | 29.60 $\pm$ 0.50          | 47.50 $\pm$ 0.50         
Euler (ms)                | 4640.00 $\pm$ 30.00       | 36.80 $\pm$ 0.50          | 125.00 $\pm$ 1.00         | 17.10 $\pm$ 0.40          | 201.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 9430.00 $\pm$ 60.00       | 73.70 $\pm$ 0.70          | 318.00 $\pm$ 7.00         | 29.10 $\pm$ 0.70          | 400.00 $\pm$ 4.00        
Midpoint Fixed (s)        | 48.50 $\pm$ 0.60          | 0.63 $\pm$ 0.02           | 1.75 $\pm$ 0.01           | 0.10 $\pm$ 0.00           | 1.97 $\pm$ 0.01          
RK4 (ms)                  | 23800.00 $\pm$ 300.00     | 219.00 $\pm$ 1.00         | 638.00 $\pm$ 8.00         | 33.70 $\pm$ 0.60          | 526.00 $\pm$ 17.00       
FD - L Convection (ms)    | 3130.00 $\pm$ 50.00       | 4.92 $\pm$ 0.00           | 13.80 $\pm$ 0.10          | 2.64 $\pm$ 0.13           | 2.93 $\pm$ 0.06          
FD - NL Convection (ms)   | 3840.00 $\pm$ 50.00       | 4.13 $\pm$ 0.01           | 14.80 $\pm$ 0.10          | 2.47 $\pm$ 0.06           | 2.93 $\pm$ 0.05          
FD - Poisson (ms)         | 8090.00 $\pm$ 30.00       | 6.43 $\pm$ 0.00           | 18.90 $\pm$ 0.00          | 4.28 $\pm$ 0.01           | 5.30 $\pm$ 0.01          
FD - Laplace (ms)         | 683.00 $\pm$ 4.00         | 226.00 $\pm$ 0.00         | 397.00 $\pm$ 3.00         | 81.70 $\pm$ 0.50          | 365.00 $\pm$ 1.00        
M-D (ms)                  | 20400.00 $\pm$ 300.00     | 65.70 $\pm$ 1.10          | 91.30 $\pm$ 0.80          | 120.00 $\pm$ 0.00         | 121.00 $\pm$ 0.00        

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.7.2)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.85                      | 0.32                      | 1.44                      | 1.35                     
Bellman Ford              | -                         | 3.22                      | 1.06                      | 2.29                      | 2.28                     
Dijkstra                  | -                         | 2.46                      | 1.20                      | 2.39                      | 2.32                     
Euler                     | -                         | 2.81                      | 1.65                      | 2.27                      | 2.30                     
Midpoint Explicit         | -                         | 3.27                      | 2.34                      | 2.60                      | 2.66                     
Midpoint Fixed            | -                         | 3.92                      | 2.57                      | 2.68                      | 2.73                     
RK4                       | -                         | 4.27                      | 2.96                      | 3.22                      | 3.22                     
FD - L Convection         | -                         | 2.53                      | 0.95                      | 2.26                      | 2.28                     
FD - NL Convection        | -                         | 3.29                      | 0.99                      | 2.25                      | 2.28                     
FD - Poisson              | -                         | 3.95                      | 1.41                      | 2.42                      | 2.40                     
FD - Laplace              | -                         | 8.03                      | 2.75                      | 2.84                      | 2.90                     
M-D                       | -                         | 6.92                      | 3.24                      | 3.26                      | 3.09                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 387.00 $\pm$ 1.00         | 9.73 $\pm$ 0.02           | 32.30 $\pm$ 0.30          | 3.14 $\pm$ 0.00           | 3.35 $\pm$ 0.07          
Bellman Ford (ms)         | 2570.00 $\pm$ 30.00       | 6.47 $\pm$ 0.02           | 10.50 $\pm$ 0.00          | 4.44 $\pm$ 0.00           | 6.57 $\pm$ 0.01          
Dijkstra (ms)             | 6710.00 $\pm$ 10.00       | 38.20 $\pm$ 0.80          | 32.40 $\pm$ 0.50          | 30.90 $\pm$ 0.30          | 47.00 $\pm$ 0.60         
Euler (ms)                | 5020.00 $\pm$ 110.00      | 37.20 $\pm$ 0.70          | 125.00 $\pm$ 1.00         | 18.10 $\pm$ 0.30          | 200.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 10100.00 $\pm$ 200.00     | 73.20 $\pm$ 0.70          | 314.00 $\pm$ 3.00         | 28.60 $\pm$ 1.50          | 399.00 $\pm$ 5.00        
Midpoint Fixed (s)        | 51.20 $\pm$ 0.80          | 0.62 $\pm$ 0.01           | 1.76 $\pm$ 0.02           | 0.10 $\pm$ 0.00           | 1.98 $\pm$ 0.00          
RK4 (ms)                  | 25800.00 $\pm$ 500.00     | 220.00 $\pm$ 3.00         | 641.00 $\pm$ 14.00        | 33.90 $\pm$ 0.50          | 521.00 $\pm$ 17.00       
FD - L Convection (ms)    | 2950.00 $\pm$ 20.00       | 4.92 $\pm$ 0.00           | 13.80 $\pm$ 0.00          | 2.58 $\pm$ 0.05           | 2.50 $\pm$ 0.01          
FD - NL Convection (ms)   | 3640.00 $\pm$ 20.00       | 4.13 $\pm$ 0.00           | 14.80 $\pm$ 0.20          | 2.43 $\pm$ 0.01           | 2.62 $\pm$ 0.32          
FD - Poisson (ms)         | 8540.00 $\pm$ 110.00      | 6.41 $\pm$ 0.05           | 19.10 $\pm$ 0.30          | 4.27 $\pm$ 0.00           | 5.30 $\pm$ 0.01          
FD - Laplace (ms)         | 683.00 $\pm$ 3.00         | 226.00 $\pm$ 0.00         | 399.00 $\pm$ 4.00         | 81.60 $\pm$ 0.30          | 373.00 $\pm$ 2.00        
M-D (ms)                  | 20600.00 $\pm$ 500.00     | 65.50 $\pm$ 0.20          | 91.00 $\pm$ 0.20          | 120.00 $\pm$ 0.00         | 121.00 $\pm$ 0.00        

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.7.2)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.72                      | 0.45                      | 1.88                      | 1.77                     
Bellman Ford              | -                         | 4.34                      | 1.46                      | 2.86                      | 2.91                     
Dijkstra                  | -                         | 3.46                      | 1.53                      | 2.97                      | 2.99                     
Euler                     | -                         | 3.88                      | 2.09                      | 2.91                      | 2.91                     
Midpoint Explicit         | -                         | 4.40                      | 2.94                      | 3.19                      | 3.35                     
Midpoint Fixed            | -                         | 5.35                      | 3.36                      | 3.36                      | 3.44                     
RK4                       | -                         | 5.85                      | 3.93                      | 4.14                      | 4.19                     
FD - L Convection         | -                         | 3.41                      | 1.27                      | 2.82                      | 2.88                     
FD - NL Convection        | -                         | 4.48                      | 1.29                      | 2.79                      | 2.98                     
FD - Poisson              | -                         | 5.30                      | 1.87                      | 3.05                      | 3.09                     
FD - Laplace              | -                         | 10.71                     | 3.62                      | 3.63                      | 3.78                     
M-D                       | -                         | 9.37                      | 3.81                      | 4.10                      | 4.11                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 476.00 $\pm$ 11.00        | 4.97 $\pm$ 0.26           | 32.80 $\pm$ 1.30          | 2.30 $\pm$ 0.09           | 2.37 $\pm$ 0.12          
Bellman Ford (ms)         | 3120.00 $\pm$ 60.00       | 8.87 $\pm$ 0.54           | 11.70 $\pm$ 0.40          | 5.22 $\pm$ 0.18           | 9.92 $\pm$ 0.36          
Dijkstra (ms)             | 8170.00 $\pm$ 120.00      | 43.40 $\pm$ 1.20          | 45.90 $\pm$ 2.70          | 37.50 $\pm$ 1.00          | 55.70 $\pm$ 2.10         
Euler (ms)                | 5380.00 $\pm$ 90.00       | 54.30 $\pm$ 2.80          | 108.00 $\pm$ 4.00         | 28.50 $\pm$ 2.10          | 270.00 $\pm$ 22.00       
Midpoint Explicit (ms)    | 10900.00 $\pm$ 200.00     | 107.00 $\pm$ 5.00         | 269.00 $\pm$ 10.00        | 44.40 $\pm$ 2.00          | 500.00 $\pm$ 17.00       
Midpoint Fixed (s)        | 54.60 $\pm$ 0.50          | 0.80 $\pm$ 0.03           | 1.55 $\pm$ 0.09           | 0.15 $\pm$ 0.01           | 2.53 $\pm$ 0.04          
RK4 (ms)                  | 27500.00 $\pm$ 500.00     | 244.00 $\pm$ 8.00         | 541.00 $\pm$ 20.00        | 62.60 $\pm$ 3.80          | 654.00 $\pm$ 12.00       
FD - L Convection (ms)    | 3470.00 $\pm$ 90.00       | 4.59 $\pm$ 0.24           | 18.30 $\pm$ 0.70          | 3.15 $\pm$ 0.11           | 3.34 $\pm$ 0.21          
FD - NL Convection (ms)   | 4320.00 $\pm$ 70.00       | 5.03 $\pm$ 0.21           | 17.30 $\pm$ 1.00          | 3.09 $\pm$ 0.11           | 3.75 $\pm$ 0.17          
FD - Poisson (ms)         | 10200.00 $\pm$ 300.00     | 14.20 $\pm$ 0.70          | 25.20 $\pm$ 0.80          | 7.79 $\pm$ 0.24           | 9.99 $\pm$ 0.24          
FD - Laplace (ms)         | 1110.00 $\pm$ 20.00       | 309.00 $\pm$ 11.00        | 562.00 $\pm$ 11.00        | 171.00 $\pm$ 6.00         | 493.00 $\pm$ 10.00       
M-D (ms)                  | 21400.00 $\pm$ 200.00     | 73.10 $\pm$ 3.60          | 108.00 $\pm$ 4.00         | 127.00 $\pm$ 4.00         | 133.00 $\pm$ 6.00        

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.7.2)
## Compilation time
Algorithm                 | python                    | pythran                   | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.03                      | 1.57                      | 1.50                     
Bellman Ford              | -                         | 3.34                      | 2.45                      | 2.41                     
Dijkstra                  | -                         | 2.53                      | 2.50                      | 2.46                     
Euler                     | -                         | 2.94                      | 2.43                      | 2.48                     
Midpoint Explicit         | -                         | 3.36                      | 2.74                      | 2.80                     
Midpoint Fixed            | -                         | 4.02                      | 2.83                      | 2.86                     
RK4                       | -                         | 4.39                      | 3.30                      | 3.33                     
FD - L Convection         | -                         | 2.67                      | 2.38                      | 2.40                     
FD - NL Convection        | -                         | 3.39                      | 2.38                      | 2.43                     
FD - Poisson              | -                         | 4.06                      | 2.59                      | 2.56                     
FD - Laplace              | -                         | 8.23                      | 2.99                      | 3.03                     
M-D                       | -                         | 7.03                      | 3.32                      | 3.16                     

## Execution time
Algorithm                 | python                    | pythran                   | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 399.00 $\pm$ 3.00         | 9.73 $\pm$ 0.02           | 3.28 $\pm$ 0.00           | 3.26 $\pm$ 0.00          
Bellman Ford (ms)         | 2660.00 $\pm$ 20.00       | 6.46 $\pm$ 0.01           | 4.46 $\pm$ 0.01           | 6.59 $\pm$ 0.01          
Dijkstra (ms)             | 6520.00 $\pm$ 40.00       | 40.90 $\pm$ 2.90          | 31.00 $\pm$ 0.50          | 48.30 $\pm$ 0.40         
Euler (ms)                | 4920.00 $\pm$ 20.00       | 37.60 $\pm$ 0.60          | 19.60 $\pm$ 1.00          | 201.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 9840.00 $\pm$ 80.00       | 73.40 $\pm$ 0.60          | 29.40 $\pm$ 1.10          | 402.00 $\pm$ 10.00       
Midpoint Fixed (s)        | 49.10 $\pm$ 0.30          | 0.63 $\pm$ 0.01           | 0.10 $\pm$ 0.00           | 1.98 $\pm$ 0.03          
RK4 (ms)                  | 24700.00 $\pm$ 300.00     | 220.00 $\pm$ 3.00         | 34.30 $\pm$ 0.70          | 517.00 $\pm$ 7.00        
FD - L Convection (ms)    | 2630.00 $\pm$ 50.00       | 4.92 $\pm$ 0.00           | 2.59 $\pm$ 0.05           | 2.62 $\pm$ 0.13          
FD - NL Convection (ms)   | 3210.00 $\pm$ 20.00       | 4.13 $\pm$ 0.01           | 2.52 $\pm$ 0.01           | 2.64 $\pm$ 0.16          
FD - Poisson (ms)         | 8130.00 $\pm$ 260.00      | 6.36 $\pm$ 0.01           | 4.34 $\pm$ 0.00           | 5.31 $\pm$ 0.01          
FD - Laplace (ms)         | 683.00 $\pm$ 4.00         | 227.00 $\pm$ 0.00         | 81.80 $\pm$ 0.30          | 366.00 $\pm$ 1.00        
M-D (ms)                  | 19800.00 $\pm$ 100.00     | 65.40 $\pm$ 0.20          | 120.00 $\pm$ 0.00         | 127.00 $\pm$ 17.00       

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
