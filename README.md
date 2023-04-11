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
Devel branch benchmarks failed on python 3.10!

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.7 results
### Performance Comparison (as of 1.7.3)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.11                      | 0.39                      | 1.62                      | 1.47                     
Bellman Ford              | -                         | 3.70                      | 1.23                      | 2.53                      | 2.46                     
Dijkstra                  | -                         | 2.76                      | 1.39                      | 2.59                      | 2.52                     
Euler                     | -                         | 3.12                      | 1.98                      | 2.47                      | 2.55                     
Midpoint Explicit         | -                         | 3.65                      | 2.73                      | 2.92                      | 2.92                     
Midpoint Fixed            | -                         | 4.49                      | 3.15                      | 3.00                      | 3.02                     
RK4                       | -                         | 4.85                      | 3.51                      | 3.64                      | 3.70                     
FD - L Convection         | -                         | 2.82                      | 1.10                      | 2.53                      | 2.57                     
FD - NL Convection        | -                         | 3.72                      | 1.25                      | 2.49                      | 2.56                     
FD - Poisson              | -                         | 4.55                      | 1.73                      | 2.71                      | 2.66                     
FD - Laplace              | -                         | 9.33                      | 3.22                      | 3.20                      | 3.26                     
M-D                       | -                         | 7.81                      | 3.95                      | 3.72                      | 3.35                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 508.00 $\pm$ 25.00        | 4.12 $\pm$ 0.17           | 19.90 $\pm$ 0.60          | 2.38 $\pm$ 0.07           | 2.45 $\pm$ 0.07          
Bellman Ford (ms)         | 2910.00 $\pm$ 90.00       | 6.71 $\pm$ 0.19           | 11.30 $\pm$ 0.30          | 4.23 $\pm$ 0.11           | 7.13 $\pm$ 0.18          
Dijkstra (ms)             | 8140.00 $\pm$ 140.00      | 48.80 $\pm$ 1.00          | 43.50 $\pm$ 0.90          | 40.20 $\pm$ 1.10          | 53.70 $\pm$ 1.50         
Euler (ms)                | 6330.00 $\pm$ 230.00      | 46.80 $\pm$ 1.60          | 131.00 $\pm$ 5.00         | 22.40 $\pm$ 1.40          | 258.00 $\pm$ 5.00        
Midpoint Explicit (ms)    | 12600.00 $\pm$ 300.00     | 91.30 $\pm$ 1.90          | 324.00 $\pm$ 7.00         | 31.00 $\pm$ 0.80          | 528.00 $\pm$ 16.00       
Midpoint Fixed (s)        | 61.80 $\pm$ 1.00          | 0.76 $\pm$ 0.02           | 1.79 $\pm$ 0.04           | 0.11 $\pm$ 0.00           | 2.57 $\pm$ 0.03          
RK4 (ms)                  | 28400.00 $\pm$ 600.00     | 224.00 $\pm$ 7.00         | 651.00 $\pm$ 26.00        | 38.70 $\pm$ 1.50          | 669.00 $\pm$ 12.00       
FD - L Convection (ms)    | 3320.00 $\pm$ 50.00       | 4.04 $\pm$ 0.10           | 15.20 $\pm$ 0.50          | 2.69 $\pm$ 0.11           | 2.78 $\pm$ 0.08          
FD - NL Convection (ms)   | 4570.00 $\pm$ 100.00      | 4.76 $\pm$ 0.09           | 16.40 $\pm$ 0.40          | 2.52 $\pm$ 0.07           | 3.19 $\pm$ 0.09          
FD - Poisson (ms)         | 9790.00 $\pm$ 180.00      | 7.14 $\pm$ 0.24           | 20.80 $\pm$ 0.60          | 4.23 $\pm$ 0.11           | 5.46 $\pm$ 0.15          
FD - Laplace (ms)         | 791.00 $\pm$ 16.00        | 238.00 $\pm$ 5.00         | 431.00 $\pm$ 8.00         | 89.30 $\pm$ 2.10          | 392.00 $\pm$ 13.00       
M-D (ms)                  | 23200.00 $\pm$ 700.00     | 59.40 $\pm$ 1.70          | 97.40 $\pm$ 2.90          | 115.00 $\pm$ 4.00         | 120.00 $\pm$ 4.00        

![Python 3.7 compilation results](./version_specific_results/pypi_performance_37_compilation.svg)
![Python 3.7 execution results](./version_specific_results/pypi_performance_37_execution.svg)
## Python 3.8 results
### Performance Comparison (as of 1.7.3)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.90                      | 0.34                      | 1.47                      | 1.37                     
Bellman Ford              | -                         | 3.28                      | 1.09                      | 2.34                      | 2.28                     
Dijkstra                  | -                         | 2.48                      | 1.22                      | 2.39                      | 2.33                     
Euler                     | -                         | 2.90                      | 1.69                      | 2.30                      | 2.33                     
Midpoint Explicit         | -                         | 3.34                      | 2.39                      | 2.65                      | 2.65                     
Midpoint Fixed            | -                         | 4.02                      | 2.67                      | 2.71                      | 2.73                     
RK4                       | -                         | 4.44                      | 2.99                      | 3.26                      | 3.25                     
FD - L Convection         | -                         | 2.54                      | 0.97                      | 2.25                      | 2.26                     
FD - NL Convection        | -                         | 3.32                      | 1.03                      | 2.24                      | 2.30                     
FD - Poisson              | -                         | 4.04                      | 1.44                      | 2.42                      | 2.41                     
FD - Laplace              | -                         | 8.52                      | 2.85                      | 2.88                      | 2.93                     
M-D                       | -                         | 7.10                      | 3.29                      | 3.26                      | 3.08                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 509.00 $\pm$ 2.00         | 7.90 $\pm$ 0.06           | 30.80 $\pm$ 0.30          | 3.17 $\pm$ 0.00           | 3.37 $\pm$ 0.02          
Bellman Ford (ms)         | 2650.00 $\pm$ 0.00        | 7.04 $\pm$ 0.00           | 9.70 $\pm$ 0.03           | 3.86 $\pm$ 0.00           | 6.48 $\pm$ 0.00          
Dijkstra (ms)             | 7070.00 $\pm$ 40.00       | 46.10 $\pm$ 0.90          | 41.30 $\pm$ 0.50          | 36.80 $\pm$ 0.70          | 51.50 $\pm$ 0.90         
Euler (ms)                | 4290.00 $\pm$ 30.00       | 39.30 $\pm$ 0.40          | 117.00 $\pm$ 1.00         | 19.00 $\pm$ 0.90          | 240.00 $\pm$ 5.00        
Midpoint Explicit (ms)    | 8830.00 $\pm$ 90.00       | 78.40 $\pm$ 1.30          | 295.00 $\pm$ 2.00         | 28.20 $\pm$ 0.40          | 470.00 $\pm$ 2.00        
Midpoint Fixed (s)        | 43.60 $\pm$ 0.40          | 0.66 $\pm$ 0.00           | 1.60 $\pm$ 0.00           | 0.10 $\pm$ 0.01           | 2.31 $\pm$ 0.00          
RK4 (ms)                  | 21400.00 $\pm$ 300.00     | 198.00 $\pm$ 0.00         | 588.00 $\pm$ 6.00         | 34.30 $\pm$ 0.70          | 599.00 $\pm$ 3.00        
FD - L Convection (ms)    | 3250.00 $\pm$ 90.00       | 4.44 $\pm$ 0.02           | 13.80 $\pm$ 0.00          | 2.58 $\pm$ 0.01           | 2.48 $\pm$ 0.01          
FD - NL Convection (ms)   | 3950.00 $\pm$ 40.00       | 4.01 $\pm$ 0.02           | 14.70 $\pm$ 0.00          | 2.54 $\pm$ 0.01           | 2.68 $\pm$ 0.10          
FD - Poisson (ms)         | 8220.00 $\pm$ 80.00       | 6.13 $\pm$ 0.04           | 18.80 $\pm$ 0.10          | 3.81 $\pm$ 0.01           | 4.92 $\pm$ 0.05          
FD - Laplace (ms)         | 694.00 $\pm$ 4.00         | 211.00 $\pm$ 1.00         | 385.00 $\pm$ 2.00         | 78.40 $\pm$ 1.30          | 364.00 $\pm$ 2.00        
M-D (ms)                  | 18300.00 $\pm$ 200.00     | 54.10 $\pm$ 0.00          | 88.70 $\pm$ 0.60          | 106.00 $\pm$ 0.00         | 110.00 $\pm$ 0.00        

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.7.3)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.74                      | 0.49                      | 2.08                      | 1.96                     
Bellman Ford              | -                         | 4.49                      | 1.51                      | 3.29                      | 3.19                     
Dijkstra                  | -                         | 3.64                      | 1.77                      | 3.33                      | 3.20                     
Euler                     | -                         | 4.06                      | 2.39                      | 3.08                      | 3.20                     
Midpoint Explicit         | -                         | 4.78                      | 3.42                      | 3.78                      | 3.70                     
Midpoint Fixed            | -                         | 5.78                      | 3.65                      | 3.70                      | 3.80                     
RK4                       | -                         | 6.16                      | 3.96                      | 4.54                      | 4.60                     
FD - L Convection         | -                         | 3.88                      | 1.45                      | 3.21                      | 3.15                     
FD - NL Convection        | -                         | 4.90                      | 1.50                      | 3.30                      | 3.35                     
FD - Poisson              | -                         | 5.88                      | 2.10                      | 3.43                      | 3.49                     
FD - Laplace              | -                         | 12.29                     | 3.99                      | 3.92                      | 4.04                     
M-D                       | -                         | 10.47                     | 4.31                      | 4.56                      | 4.37                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 554.00 $\pm$ 8.00         | 5.57 $\pm$ 0.19           | 36.00 $\pm$ 0.70          | 2.54 $\pm$ 0.08           | 2.54 $\pm$ 0.05          
Bellman Ford (ms)         | 3640.00 $\pm$ 40.00       | 7.86 $\pm$ 0.12           | 13.00 $\pm$ 0.80          | 5.44 $\pm$ 0.20           | 11.20 $\pm$ 0.60         
Dijkstra (ms)             | 9480.00 $\pm$ 380.00      | 51.50 $\pm$ 1.70          | 54.10 $\pm$ 2.10          | 43.30 $\pm$ 1.30          | 64.90 $\pm$ 1.60         
Euler (ms)                | 6050.00 $\pm$ 230.00      | 52.90 $\pm$ 2.60          | 126.00 $\pm$ 5.00         | 28.30 $\pm$ 1.30          | 294.00 $\pm$ 8.00        
Midpoint Explicit (ms)    | 11800.00 $\pm$ 300.00     | 113.00 $\pm$ 6.00         | 325.00 $\pm$ 16.00        | 45.10 $\pm$ 1.60          | 570.00 $\pm$ 13.00       
Midpoint Fixed (s)        | 59.00 $\pm$ 1.30          | 0.88 $\pm$ 0.03           | 1.70 $\pm$ 0.03           | 0.14 $\pm$ 0.00           | 2.79 $\pm$ 0.05          
RK4 (ms)                  | 30200.00 $\pm$ 700.00     | 242.00 $\pm$ 8.00         | 616.00 $\pm$ 14.00        | 51.00 $\pm$ 2.20          | 725.00 $\pm$ 13.00       
FD - L Convection (ms)    | 4080.00 $\pm$ 60.00       | 5.14 $\pm$ 0.27           | 18.50 $\pm$ 0.70          | 3.88 $\pm$ 0.15           | 5.45 $\pm$ 0.27          
FD - NL Convection (ms)   | 5130.00 $\pm$ 90.00       | 5.43 $\pm$ 0.16           | 19.80 $\pm$ 0.80          | 4.09 $\pm$ 0.20           | 6.72 $\pm$ 0.41          
FD - Poisson (ms)         | 11000.00 $\pm$ 200.00     | 11.40 $\pm$ 0.30          | 26.20 $\pm$ 0.70          | 8.88 $\pm$ 0.26           | 12.40 $\pm$ 0.50         
FD - Laplace (ms)         | 1250.00 $\pm$ 40.00       | 304.00 $\pm$ 7.00         | 575.00 $\pm$ 12.00        | 201.00 $\pm$ 3.00         | 584.00 $\pm$ 12.00       
M-D (ms)                  | 24800.00 $\pm$ 200.00     | 69.80 $\pm$ 1.70          | 118.00 $\pm$ 2.00         | 140.00 $\pm$ 3.00         | 143.00 $\pm$ 1.00        

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.7.3)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 3.02                      | 0.46                      | 1.99                      | 1.82                     
Bellman Ford              | -                         | 4.48                      | 1.43                      | 2.96                      | 3.04                     
Dijkstra                  | -                         | 3.47                      | 1.59                      | 3.05                      | 2.98                     
Euler                     | -                         | 4.03                      | 2.21                      | 2.96                      | 2.98                     
Midpoint Explicit         | -                         | 4.60                      | 3.12                      | 3.37                      | 3.46                     
Midpoint Fixed            | -                         | 5.47                      | 3.51                      | 3.59                      | 3.57                     
RK4                       | -                         | 5.93                      | 3.95                      | 4.20                      | 4.16                     
FD - L Convection         | -                         | 3.60                      | 1.24                      | 2.89                      | 2.94                     
FD - NL Convection        | -                         | 4.62                      | 1.35                      | 2.92                      | 2.99                     
FD - Poisson              | -                         | 5.46                      | 1.87                      | 3.13                      | 3.22                     
FD - Laplace              | -                         | 10.96                     | 3.62                      | 3.69                      | 3.70                     
M-D                       | -                         | 9.45                      | 4.00                      | 4.21                      | 3.99                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 497.00 $\pm$ 11.00        | 5.11 $\pm$ 0.10           | 35.40 $\pm$ 0.90          | 2.48 $\pm$ 0.06           | 2.41 $\pm$ 0.03          
Bellman Ford (ms)         | 3370.00 $\pm$ 50.00       | 9.12 $\pm$ 0.46           | 12.20 $\pm$ 0.20          | 5.51 $\pm$ 0.14           | 10.30 $\pm$ 0.30         
Dijkstra (ms)             | 8650.00 $\pm$ 60.00       | 44.10 $\pm$ 1.10          | 45.80 $\pm$ 1.30          | 38.40 $\pm$ 0.80          | 57.50 $\pm$ 2.00         
Euler (ms)                | 5710.00 $\pm$ 120.00      | 55.90 $\pm$ 1.40          | 112.00 $\pm$ 4.00         | 28.10 $\pm$ 1.00          | 269.00 $\pm$ 6.00        
Midpoint Explicit (ms)    | 11800.00 $\pm$ 300.00     | 111.00 $\pm$ 3.00         | 284.00 $\pm$ 7.00         | 47.00 $\pm$ 1.30          | 529.00 $\pm$ 14.00       
Midpoint Fixed (s)        | 58.90 $\pm$ 1.20          | 0.86 $\pm$ 0.05           | 1.59 $\pm$ 0.02           | 0.15 $\pm$ 0.00           | 2.61 $\pm$ 0.08          
RK4 (ms)                  | 29200.00 $\pm$ 900.00     | 257.00 $\pm$ 5.00         | 559.00 $\pm$ 8.00         | 58.40 $\pm$ 1.20          | 678.00 $\pm$ 11.00       
FD - L Convection (ms)    | 3700.00 $\pm$ 100.00      | 4.78 $\pm$ 0.09           | 19.30 $\pm$ 0.50          | 3.22 $\pm$ 0.13           | 3.43 $\pm$ 0.28          
FD - NL Convection (ms)   | 4580.00 $\pm$ 40.00       | 5.25 $\pm$ 0.13           | 18.10 $\pm$ 0.60          | 3.15 $\pm$ 0.07           | 3.67 $\pm$ 0.20          
FD - Poisson (ms)         | 10500.00 $\pm$ 100.00     | 14.20 $\pm$ 0.20          | 26.00 $\pm$ 0.40          | 7.46 $\pm$ 0.05           | 10.00 $\pm$ 0.23         
FD - Laplace (ms)         | 1070.00 $\pm$ 10.00       | 324.00 $\pm$ 6.00         | 564.00 $\pm$ 12.00        | 168.00 $\pm$ 3.00         | 486.00 $\pm$ 5.00        
M-D (ms)                  | 22900.00 $\pm$ 300.00     | 76.50 $\pm$ 1.00          | 109.00 $\pm$ 5.00         | 132.00 $\pm$ 5.00         | 134.00 $\pm$ 3.00        

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.7.3)
## Compilation time
Algorithm                 | python                    | pythran                   | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.42                      | 1.73                      | 1.59                     
Bellman Ford              | -                         | 3.47                      | 2.57                      | 2.52                     
Dijkstra                  | -                         | 2.73                      | 2.64                      | 2.55                     
Euler                     | -                         | 3.11                      | 2.56                      | 2.57                     
Midpoint Explicit         | -                         | 3.57                      | 2.88                      | 2.91                     
Midpoint Fixed            | -                         | 4.25                      | 2.90                      | 2.99                     
RK4                       | -                         | 4.61                      | 3.38                      | 3.39                     
FD - L Convection         | -                         | 2.77                      | 2.43                      | 2.48                     
FD - NL Convection        | -                         | 3.57                      | 2.47                      | 2.48                     
FD - Poisson              | -                         | 4.18                      | 2.63                      | 2.61                     
FD - Laplace              | -                         | 8.66                      | 3.07                      | 3.11                     
M-D                       | -                         | 7.29                      | 3.39                      | 3.25                     

## Execution time
Algorithm                 | python                    | pythran                   | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 397.00 $\pm$ 1.00         | 7.89 $\pm$ 0.00           | 3.27 $\pm$ 0.00           | 3.31 $\pm$ 0.01          
Bellman Ford (ms)         | 2550.00 $\pm$ 30.00       | 7.06 $\pm$ 0.02           | 3.84 $\pm$ 0.01           | 6.45 $\pm$ 0.00          
Dijkstra (ms)             | 6740.00 $\pm$ 30.00       | 45.30 $\pm$ 0.30          | 36.30 $\pm$ 0.20          | 50.10 $\pm$ 0.70         
Euler (ms)                | 4510.00 $\pm$ 100.00      | 41.20 $\pm$ 0.50          | 21.70 $\pm$ 0.80          | 236.00 $\pm$ 3.00        
Midpoint Explicit (ms)    | 9130.00 $\pm$ 120.00      | 78.80 $\pm$ 0.60          | 31.10 $\pm$ 1.60          | 468.00 $\pm$ 3.00        
Midpoint Fixed (s)        | 45.40 $\pm$ 0.50          | 0.66 $\pm$ 0.00           | 0.10 $\pm$ 0.01           | 2.32 $\pm$ 0.00          
RK4 (ms)                  | 22600.00 $\pm$ 300.00     | 199.00 $\pm$ 1.00         | 35.30 $\pm$ 0.70          | 595.00 $\pm$ 3.00        
FD - L Convection (ms)    | 2800.00 $\pm$ 50.00       | 4.43 $\pm$ 0.01           | 2.54 $\pm$ 0.01           | 2.55 $\pm$ 0.23          
FD - NL Convection (ms)   | 3510.00 $\pm$ 50.00       | 4.00 $\pm$ 0.01           | 2.52 $\pm$ 0.04           | 2.62 $\pm$ 0.07          
FD - Poisson (ms)         | 8180.00 $\pm$ 110.00      | 6.17 $\pm$ 0.05           | 3.84 $\pm$ 0.01           | 4.92 $\pm$ 0.02          
FD - Laplace (ms)         | 710.00 $\pm$ 10.00        | 211.00 $\pm$ 0.00         | 78.40 $\pm$ 1.30          | 363.00 $\pm$ 2.00        
M-D (ms)                  | 17900.00 $\pm$ 200.00     | 54.10 $\pm$ 0.00          | 106.00 $\pm$ 0.00         | 110.00 $\pm$ 0.00        

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
