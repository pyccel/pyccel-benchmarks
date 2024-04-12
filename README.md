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
### Performance Comparison (as of Fri Apr 12 13:23:13 UTC 2024)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.38                      | -                         | 0.32                      | 1.28                      | 1.22                      | 1.35                      | 1.35                     
Bellman Ford              | -                         | 3.55                      | -                         | 1.11                      | 3.60                      | 3.89                      | 3.73                      | 4.39                     
Dijkstra                  | -                         | 2.49                      | -                         | 1.61                      | 3.73                      | 3.89                      | 3.84                      | 4.38                     
Euler                     | -                         | 2.87                      | -                         | 2.06                      | 3.57                      | 3.93                      | 3.74                      | 4.39                     
Midpoint Explicit         | -                         | 3.36                      | -                         | 3.04                      | 3.87                      | 4.17                      | 3.97                      | 4.60                     
Midpoint Fixed            | -                         | 3.65                      | -                         | 3.33                      | 3.95                      | 4.22                      | 4.09                      | 4.79                     
RK4                       | -                         | 3.95                      | -                         | 3.80                      | 4.49                      | 4.79                      | 4.67                      | 5.23                     
FD - L Convection         | -                         | 2.48                      | -                         | 0.88                      | 3.58                      | 3.88                      | 3.71                      | 4.33                     
FD - NL Convection        | -                         | 3.56                      | -                         | 0.91                      | 3.56                      | 3.91                      | 3.77                      | 4.39                     
FD - Poisson              | -                         | 3.51                      | -                         | 1.41                      | 3.70                      | 3.95                      | 4.22                      | 4.36                     
FD - Laplace              | -                         | 6.85                      | -                         | 3.11                      | 4.03                      | 4.32                      | 4.28                      | 4.84                     
M-D                       | -                         | 6.66                      | -                         | 4.15                      | 4.47                      | 4.65                      | 4.60                      | 5.46                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 299.00                    | 2.95                      | -                         | 9.82                      | 1.50                      | 1.55                      | 7.74                      | 3.93                     
Bellman Ford (ms)         | 1880.00                   | 4.17                      | -                         | 3.83                      | 3.01                      | 6.07                      | 4.20                      | 18.00                    
Dijkstra (ms)             | 4950.00                   | 24.90                     | -                         | 20.30                     | 19.30                     | 29.60                     | 25.10                     | 22.90                    
Euler (ms)                | 3800.00                   | 33.00                     | -                         | 40.10                     | 14.80                     | 144.00                    | 15.00                     | 129.00                   
Midpoint Explicit (ms)    | 7760.00                   | 59.40                     | -                         | 79.10                     | 22.60                     | 281.00                    | 16.40                     | 317.00                   
Midpoint Fixed (ms)       | 39300.00                  | 256.00                    | -                         | 396.00                    | 75.40                     | 1420.00                   | 65.70                     | 1270.00                  
RK4 (ms)                  | 19800.00                  | 163.00                    | -                         | 146.00                    | 39.40                     | 485.00                    | 39.00                     | 406.00                   
FD - L Convection (ms)    | 2290.00                   | 1.71                      | -                         | 2.65                      | 1.44                      | 1.63                      | 1.32                      | 3.67                     
FD - NL Convection (ms)   | 2890.00                   | 1.97                      | -                         | 2.80                      | 1.78                      | 1.99                      | 1.38                      | 3.74                     
FD - Poisson (ms)         | 6380.00                   | 3.22                      | -                         | 7.16                      | 2.69                      | 3.80                      | 2.59                      | 7.78                     
FD - Laplace (ms)         | 588.00                    | 64.20                     | -                         | 245.00                    | 58.10                     | 280.00                    | 59.50                     | 335.00                   
M-D (ms)                  | 14900.00                  | 15.20                     | -                         | 59.00                     | 54.30                     | 59.60                     | 78.20                     | 62.00                    

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.8 results
### Performance Comparison (as of 1.11.2)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.94                      | 2.04                      | 0.32                      | 1.29                      | 1.23                      | 1.36                      | 1.32                     
Bellman Ford              | -                         | 3.37                      | 3.72                      | 1.08                      | 2.40                      | 2.60                      | 2.53                      | 3.38                     
Dijkstra                  | -                         | 2.35                      | 2.72                      | 1.59                      | 2.47                      | 2.62                      | 2.64                      | 3.42                     
Euler                     | -                         | 2.70                      | 3.13                      | 2.01                      | 2.39                      | 2.59                      | 2.50                      | 3.35                     
Midpoint Explicit         | -                         | 3.14                      | 3.61                      | 3.03                      | 2.67                      | 2.90                      | 2.78                      | 3.62                     
Midpoint Fixed            | -                         | 3.46                      | 4.23                      | 3.19                      | 2.71                      | 2.96                      | 2.87                      | 3.69                     
RK4                       | -                         | 3.73                      | 4.34                      | 3.74                      | 3.20                      | 3.35                      | 3.27                      | 4.07                     
FD - L Convection         | -                         | 2.30                      | 2.70                      | 0.86                      | 2.34                      | 2.56                      | 2.50                      | 3.32                     
FD - NL Convection        | -                         | 3.36                      | 3.74                      | 0.88                      | 2.38                      | 2.61                      | 2.55                      | 3.33                     
FD - Poisson              | -                         | 3.36                      | 3.86                      | 1.33                      | 2.47                      | 2.67                      | 3.06                      | 3.40                     
FD - Laplace              | -                         | 6.61                      | 8.76                      | 3.02                      | 2.81                      | 3.02                      | 3.05                      | 3.87                     
M-D                       | -                         | 6.30                      | 7.24                      | 4.00                      | 3.19                      | 3.20                      | 3.38                      | 4.34                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 323.00 $\pm$ 5.00         | 2.96 $\pm$ 0.04           | 3.48 $\pm$ 0.04           | 10.80 $\pm$ 0.10          | 1.50 $\pm$ 0.00           | 1.54 $\pm$ 0.00           | 10.10 $\pm$ 0.50          | 4.77 $\pm$ 0.01          
Bellman Ford (ms)         | 1860.00 $\pm$ 30.00       | 4.92 $\pm$ 0.01           | 3.27 $\pm$ 0.06           | 3.85 $\pm$ 0.05           | 2.95 $\pm$ 0.02           | 6.05 $\pm$ 0.02           | 4.43 $\pm$ 0.02           | 18.40 $\pm$ 0.30         
Dijkstra (ms)             | 4970.00 $\pm$ 60.00       | 26.90 $\pm$ 0.40          | 16.90 $\pm$ 0.30          | 19.70 $\pm$ 0.60          | 18.90 $\pm$ 0.40          | 30.50 $\pm$ 0.60          | 24.00 $\pm$ 0.40          | 22.80 $\pm$ 0.40         
Euler (ms)                | 3900.00 $\pm$ 20.00       | 29.50 $\pm$ 0.90          | 28.50 $\pm$ 0.40          | 39.10 $\pm$ 1.30          | 15.20 $\pm$ 0.50          | 145.00 $\pm$ 1.00         | 14.40 $\pm$ 0.40          | 132.00 $\pm$ 8.00        
Midpoint Explicit (ms)    | 7960.00 $\pm$ 50.00       | 60.70 $\pm$ 5.70          | 56.70 $\pm$ 0.30          | 82.00 $\pm$ 3.40          | 24.00 $\pm$ 0.50          | 284.00 $\pm$ 2.00         | 16.20 $\pm$ 0.40          | 254.00 $\pm$ 2.00        
Midpoint Fixed (ms)       | 41100.00 $\pm$ 400.00     | 255.00 $\pm$ 1.00         | 63.10 $\pm$ 0.40          | 395.00 $\pm$ 14.00        | 74.80 $\pm$ 0.50          | 1400.00 $\pm$ 20.00       | 61.20 $\pm$ 2.50          | 1260.00 $\pm$ 20.00      
RK4 (ms)                  | 20500.00 $\pm$ 100.00     | 165.00 $\pm$ 3.00         | 38.20 $\pm$ 0.90          | 146.00 $\pm$ 6.00         | 36.20 $\pm$ 0.70          | 493.00 $\pm$ 9.00         | 38.80 $\pm$ 1.00          | 433.00 $\pm$ 39.00       
FD - L Convection (ms)    | 2410.00 $\pm$ 20.00       | 1.45 $\pm$ 0.03           | 1.53 $\pm$ 0.02           | 2.71 $\pm$ 0.08           | 1.57 $\pm$ 0.11           | 1.67 $\pm$ 0.09           | 1.52 $\pm$ 0.01           | 3.72 $\pm$ 0.02          
FD - NL Convection (ms)   | 2990.00 $\pm$ 30.00       | 1.98 $\pm$ 0.05           | 1.83 $\pm$ 0.04           | 2.82 $\pm$ 0.05           | 1.79 $\pm$ 0.11           | 1.99 $\pm$ 0.01           | 1.52 $\pm$ 0.01           | 3.75 $\pm$ 0.01          
FD - Poisson (ms)         | 6480.00 $\pm$ 50.00       | 3.04 $\pm$ 0.10           | 2.74 $\pm$ 0.18           | 7.23 $\pm$ 0.06           | 2.80 $\pm$ 0.01           | 3.83 $\pm$ 0.02           | 2.69 $\pm$ 0.02           | 8.96 $\pm$ 0.04          
FD - Laplace (ms)         | 599.00 $\pm$ 13.00        | 68.80 $\pm$ 2.20          | 153.00 $\pm$ 1.00         | 251.00 $\pm$ 2.00         | 62.70 $\pm$ 0.70          | 284.00 $\pm$ 1.00         | 62.90 $\pm$ 0.60          | 307.00 $\pm$ 1.00        
M-D (ms)                  | 15800.00 $\pm$ 100.00     | 15.20 $\pm$ 0.00          | 51.90 $\pm$ 0.40          | 59.80 $\pm$ 1.60          | 54.30 $\pm$ 0.20          | 59.40 $\pm$ 0.20          | 70.60 $\pm$ 0.80          | 64.50 $\pm$ 0.20         

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.11.2)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.91                      | 2.02                      | 0.32                      | 1.27                      | 1.24                      | 1.34                      | 1.31                     
Bellman Ford              | -                         | 3.31                      | 3.70                      | 1.06                      | 2.39                      | 2.56                      | 2.53                      | 3.36                     
Dijkstra                  | -                         | 2.31                      | 2.70                      | 1.57                      | 2.45                      | 2.58                      | 2.62                      | 3.40                     
Euler                     | -                         | 2.67                      | 3.08                      | 1.99                      | 2.36                      | 2.57                      | 2.50                      | 3.28                     
Midpoint Explicit         | -                         | 3.03                      | 3.51                      | 2.96                      | 2.62                      | 2.83                      | 2.72                      | 3.57                     
Midpoint Fixed            | -                         | 3.40                      | 4.16                      | 3.18                      | 2.67                      | 2.90                      | 2.81                      | 3.65                     
RK4                       | -                         | 3.68                      | 4.27                      | 3.70                      | 3.11                      | 3.29                      | 3.21                      | 4.06                     
FD - L Convection         | -                         | 2.25                      | 2.65                      | 0.84                      | 2.32                      | 2.55                      | 2.50                      | 3.30                     
FD - NL Convection        | -                         | 3.22                      | 3.61                      | 0.85                      | 2.33                      | 2.54                      | 2.51                      | 3.29                     
FD - Poisson              | -                         | 3.29                      | 3.80                      | 1.32                      | 2.45                      | 2.64                      | 3.02                      | 3.36                     
FD - Laplace              | -                         | 6.50                      | 8.59                      | 3.00                      | 2.81                      | 3.01                      | 3.02                      | 3.83                     
M-D                       | -                         | 6.18                      | 7.14                      | 3.99                      | 3.14                      | 3.18                      | 3.32                      | 4.26                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 299.00 $\pm$ 4.00         | 3.00 $\pm$ 0.14           | 3.47 $\pm$ 0.01           | 10.60 $\pm$ 0.40          | 1.50 $\pm$ 0.00           | 1.50 $\pm$ 0.00           | 8.97 $\pm$ 0.31           | 4.77 $\pm$ 0.01          
Bellman Ford (ms)         | 1890.00 $\pm$ 20.00       | 4.17 $\pm$ 0.02           | 3.27 $\pm$ 0.06           | 3.87 $\pm$ 0.07           | 2.99 $\pm$ 0.01           | 5.57 $\pm$ 0.03           | 4.41 $\pm$ 0.02           | 18.60 $\pm$ 0.10         
Dijkstra (ms)             | 5090.00 $\pm$ 90.00       | 24.40 $\pm$ 0.40          | 16.10 $\pm$ 0.10          | 19.30 $\pm$ 0.40          | 17.80 $\pm$ 0.40          | 30.70 $\pm$ 0.40          | 23.20 $\pm$ 0.50          | 22.40 $\pm$ 0.40         
Euler (ms)                | 3840.00 $\pm$ 30.00       | 28.30 $\pm$ 0.30          | 28.70 $\pm$ 2.00          | 38.60 $\pm$ 1.10          | 14.90 $\pm$ 0.60          | 142.00 $\pm$ 2.00         | 14.30 $\pm$ 0.30          | 128.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 7840.00 $\pm$ 50.00       | 59.60 $\pm$ 0.50          | 56.40 $\pm$ 0.40          | 80.40 $\pm$ 2.20          | 23.10 $\pm$ 0.50          | 284.00 $\pm$ 4.00         | 15.80 $\pm$ 0.40          | 253.00 $\pm$ 3.00        
Midpoint Fixed (ms)       | 40000.00 $\pm$ 300.00     | 255.00 $\pm$ 1.00         | 63.30 $\pm$ 0.60          | 403.00 $\pm$ 39.00        | 74.90 $\pm$ 0.90          | 1400.00 $\pm$ 10.00       | 61.50 $\pm$ 4.70          | 1250.00 $\pm$ 20.00      
RK4 (ms)                  | 20000.00 $\pm$ 200.00     | 162.00 $\pm$ 1.00         | 37.70 $\pm$ 0.30          | 146.00 $\pm$ 2.00         | 35.30 $\pm$ 0.60          | 492.00 $\pm$ 12.00        | 37.60 $\pm$ 0.40          | 408.00 $\pm$ 3.00        
FD - L Convection (ms)    | 2480.00 $\pm$ 50.00       | 1.67 $\pm$ 0.03           | 1.57 $\pm$ 0.02           | 2.69 $\pm$ 0.04           | 1.76 $\pm$ 0.03           | 1.72 $\pm$ 0.12           | 1.32 $\pm$ 0.01           | 3.69 $\pm$ 0.01          
FD - NL Convection (ms)   | 3030.00 $\pm$ 20.00       | 1.94 $\pm$ 0.06           | 1.77 $\pm$ 0.07           | 2.82 $\pm$ 0.04           | 1.77 $\pm$ 0.11           | 2.07 $\pm$ 0.12           | 1.53 $\pm$ 0.01           | 3.75 $\pm$ 0.01          
FD - Poisson (ms)         | 6430.00 $\pm$ 40.00       | 3.03 $\pm$ 0.13           | 2.74 $\pm$ 0.28           | 7.20 $\pm$ 0.06           | 2.75 $\pm$ 0.01           | 3.83 $\pm$ 0.03           | 2.65 $\pm$ 0.01           | 8.93 $\pm$ 0.03          
FD - Laplace (ms)         | 590.00 $\pm$ 6.00         | 64.80 $\pm$ 0.40          | 152.00 $\pm$ 1.00         | 252.00 $\pm$ 5.00         | 59.10 $\pm$ 1.70          | 255.00 $\pm$ 1.00         | 60.10 $\pm$ 2.70          | 306.00 $\pm$ 1.00        
M-D (ms)                  | 15300.00 $\pm$ 200.00     | 15.30 $\pm$ 0.10          | 51.80 $\pm$ 0.20          | 59.10 $\pm$ 0.20          | 54.00 $\pm$ 0.60          | 59.50 $\pm$ 0.10          | 68.00 $\pm$ 0.90          | 61.10 $\pm$ 1.20         

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.11.2)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.53                      | 2.39                      | 0.34                      | 1.29                      | 1.22                      | 1.36                      | 1.38                     
Bellman Ford              | -                         | 3.70                      | 3.94                      | 1.12                      | 2.44                      | 2.69                      | 2.58                      | 3.39                     
Dijkstra                  | -                         | 2.53                      | 2.91                      | 1.62                      | 2.49                      | 2.65                      | 2.64                      | 3.44                     
Euler                     | -                         | 3.01                      | 3.49                      | 2.07                      | 2.44                      | 2.70                      | 2.56                      | 3.36                     
Midpoint Explicit         | -                         | 3.47                      | 3.95                      | 3.18                      | 2.78                      | 2.90                      | 2.78                      | 3.63                     
Midpoint Fixed            | -                         | 3.69                      | 4.53                      | 3.31                      | 2.70                      | 3.04                      | 2.88                      | 3.84                     
RK4                       | -                         | 4.07                      | 4.82                      | 3.94                      | 3.24                      | 3.31                      | 3.25                      | 4.26                     
FD - L Convection         | -                         | 2.45                      | 2.89                      | 0.91                      | 2.39                      | 2.53                      | 2.49                      | 3.32                     
FD - NL Convection        | -                         | 3.53                      | 3.92                      | 0.93                      | 2.41                      | 2.56                      | 2.55                      | 3.32                     
FD - Poisson              | -                         | 3.55                      | 4.09                      | 1.40                      | 2.53                      | 2.68                      | 3.02                      | 3.41                     
FD - Laplace              | -                         | 7.03                      | 9.02                      | 3.11                      | 2.78                      | 3.07                      | 3.18                      | 4.06                     
M-D                       | -                         | 6.91                      | 8.01                      | 4.15                      | 3.16                      | 3.20                      | 3.32                      | 4.35                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 315.00 $\pm$ 4.00         | 2.99 $\pm$ 0.11           | 3.47 $\pm$ 0.01           | 10.70 $\pm$ 0.20          | 1.50 $\pm$ 0.01           | 1.50 $\pm$ 0.00           | 9.21 $\pm$ 0.11           | 3.93 $\pm$ 0.01          
Bellman Ford (ms)         | 1780.00 $\pm$ 20.00       | 4.18 $\pm$ 0.03           | 3.26 $\pm$ 0.06           | 3.84 $\pm$ 0.07           | 3.02 $\pm$ 0.04           | 6.05 $\pm$ 0.03           | 4.28 $\pm$ 0.09           | 18.70 $\pm$ 0.20         
Dijkstra (ms)             | 4940.00 $\pm$ 50.00       | 23.90 $\pm$ 0.50          | 17.70 $\pm$ 0.60          | 21.70 $\pm$ 1.10          | 20.60 $\pm$ 0.50          | 31.70 $\pm$ 0.50          | 24.80 $\pm$ 0.70          | 23.70 $\pm$ 0.30         
Euler (ms)                | 3960.00 $\pm$ 40.00       | 29.40 $\pm$ 0.40          | 29.10 $\pm$ 0.40          | 39.70 $\pm$ 1.30          | 16.10 $\pm$ 0.50          | 146.00 $\pm$ 3.00         | 15.10 $\pm$ 0.50          | 129.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 7970.00 $\pm$ 40.00       | 59.80 $\pm$ 0.30          | 57.20 $\pm$ 0.70          | 81.80 $\pm$ 2.40          | 23.60 $\pm$ 0.70          | 284.00 $\pm$ 8.00         | 16.20 $\pm$ 0.40          | 256.00 $\pm$ 6.00        
Midpoint Fixed (ms)       | 40600.00 $\pm$ 200.00     | 258.00 $\pm$ 1.00         | 63.70 $\pm$ 0.40          | 434.00 $\pm$ 157.00       | 75.70 $\pm$ 0.70          | 1420.00 $\pm$ 20.00       | 61.00 $\pm$ 1.90          | 1260.00 $\pm$ 30.00      
RK4 (ms)                  | 20100.00 $\pm$ 100.00     | 162.00 $\pm$ 3.00         | 38.80 $\pm$ 0.60          | 162.00 $\pm$ 51.00        | 33.60 $\pm$ 0.50          | 489.00 $\pm$ 4.00         | 38.50 $\pm$ 0.60          | 418.00 $\pm$ 14.00       
FD - L Convection (ms)    | 2290.00 $\pm$ 20.00       | 1.67 $\pm$ 0.07           | 1.58 $\pm$ 0.02           | 2.73 $\pm$ 0.05           | 1.54 $\pm$ 0.11           | 1.71 $\pm$ 0.11           | 1.51 $\pm$ 0.01           | 3.70 $\pm$ 0.01          
FD - NL Convection (ms)   | 2840.00 $\pm$ 20.00       | 1.87 $\pm$ 0.06           | 1.83 $\pm$ 0.04           | 2.85 $\pm$ 0.10           | 2.04 $\pm$ 0.17           | 2.13 $\pm$ 0.08           | 1.40 $\pm$ 0.01           | 3.76 $\pm$ 0.08          
FD - Poisson (ms)         | 6480.00 $\pm$ 100.00      | 3.02 $\pm$ 0.05           | 2.71 $\pm$ 0.05           | 7.22 $\pm$ 0.04           | 2.79 $\pm$ 0.01           | 3.80 $\pm$ 0.03           | 2.70 $\pm$ 0.05           | 8.95 $\pm$ 0.03          
FD - Laplace (ms)         | 602.00 $\pm$ 15.00        | 68.50 $\pm$ 0.40          | 152.00 $\pm$ 1.00         | 246.00 $\pm$ 1.00         | 62.80 $\pm$ 0.50          | 259.00 $\pm$ 1.00         | 64.00 $\pm$ 0.60          | 306.00 $\pm$ 1.00        
M-D (ms)                  | 15200.00 $\pm$ 100.00     | 15.20 $\pm$ 0.00          | 52.00 $\pm$ 0.20          | 59.80 $\pm$ 1.30          | 54.20 $\pm$ 0.10          | 59.50 $\pm$ 0.30          | 69.20 $\pm$ 0.60          | 60.40 $\pm$ 0.50         

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.11.2)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.32                      | 2.23                      | 0.28                      | 1.25                      | 1.18                      | 1.32                      | 1.27                     
Bellman Ford              | -                         | 3.35                      | 3.74                      | 1.08                      | 2.33                      | 2.54                      | 2.48                      | 3.30                     
Dijkstra                  | -                         | 2.34                      | 2.74                      | 1.53                      | 2.42                      | 2.54                      | 2.56                      | 3.34                     
Euler                     | -                         | 2.68                      | 3.13                      | 1.93                      | 2.36                      | 2.51                      | 2.47                      | 3.31                     
Midpoint Explicit         | -                         | 3.05                      | 3.63                      | 2.91                      | 2.56                      | 2.78                      | 2.66                      | 3.54                     
Midpoint Fixed            | -                         | 3.39                      | 4.17                      | 3.08                      | 2.65                      | 2.80                      | 2.77                      | 3.58                     
RK4                       | -                         | 3.73                      | 4.32                      | 3.58                      | 3.00                      | 3.18                      | 3.15                      | 3.95                     
FD - L Convection         | -                         | 2.34                      | 2.78                      | 0.84                      | 2.28                      | 2.49                      | 2.44                      | 3.24                     
FD - NL Convection        | -                         | 3.36                      | 3.79                      | 0.84                      | 2.28                      | 2.55                      | 2.49                      | 3.26                     
FD - Poisson              | -                         | 3.32                      | 3.85                      | 1.25                      | 2.38                      | 2.59                      | 2.97                      | 3.32                     
FD - Laplace              | -                         | 6.54                      | 8.62                      | 2.83                      | 2.73                      | 2.92                      | 2.97                      | 3.77                     
M-D                       | -                         | 6.20                      | 7.15                      | 3.87                      | 3.04                      | 3.07                      | 3.20                      | 4.22                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 471.00 $\pm$ 23.00        | 2.96 $\pm$ 0.04           | 3.52 $\pm$ 0.15           | 10.70 $\pm$ 0.20          | 1.50 $\pm$ 0.00           | 1.55 $\pm$ 0.01           | 8.29 $\pm$ 0.35           | 3.93 $\pm$ 0.00          
Bellman Ford (ms)         | 2060.00 $\pm$ 10.00       | 4.17 $\pm$ 0.02           | 3.22 $\pm$ 0.04           | 3.85 $\pm$ 0.06           | 2.98 $\pm$ 0.02           | 5.92 $\pm$ 0.04           | 4.40 $\pm$ 0.02           | 18.70 $\pm$ 0.20         
Dijkstra (ms)             | 5190.00 $\pm$ 40.00       | 26.30 $\pm$ 0.40          | 17.00 $\pm$ 0.40          | 19.10 $\pm$ 0.50          | 19.60 $\pm$ 0.50          | 30.50 $\pm$ 0.40          | 23.80 $\pm$ 0.60          | 22.50 $\pm$ 0.50         
Euler (ms)                | 3740.00 $\pm$ 20.00       | 28.50 $\pm$ 0.30          | 28.50 $\pm$ 0.30          | 37.90 $\pm$ 0.40          | 15.30 $\pm$ 0.70          | 144.00 $\pm$ 4.00         | 14.30 $\pm$ 0.40          | 131.00 $\pm$ 5.00        
Midpoint Explicit (ms)    | 7710.00 $\pm$ 180.00      | 59.40 $\pm$ 0.30          | 56.70 $\pm$ 0.50          | 73.70 $\pm$ 1.10          | 23.00 $\pm$ 0.50          | 284.00 $\pm$ 3.00         | 16.70 $\pm$ 2.30          | 253.00 $\pm$ 1.00        
Midpoint Fixed (ms)       | 39100.00 $\pm$ 400.00     | 255.00 $\pm$ 1.00         | 63.10 $\pm$ 0.40          | 378.00 $\pm$ 3.00         | 74.80 $\pm$ 0.50          | 1400.00 $\pm$ 20.00       | 61.50 $\pm$ 4.30          | 1250.00 $\pm$ 20.00      
RK4 (ms)                  | 19500.00 $\pm$ 100.00     | 168.00 $\pm$ 4.00         | 37.80 $\pm$ 0.40          | 139.00 $\pm$ 6.00         | 32.40 $\pm$ 0.60          | 488.00 $\pm$ 3.00         | 37.90 $\pm$ 0.60          | 410.00 $\pm$ 10.00       
FD - L Convection (ms)    | 2330.00 $\pm$ 30.00       | 1.70 $\pm$ 0.07           | 1.64 $\pm$ 0.11           | 2.69 $\pm$ 0.02           | 1.78 $\pm$ 0.01           | 1.61 $\pm$ 0.02           | 1.31 $\pm$ 0.01           | 3.70 $\pm$ 0.01          
FD - NL Convection (ms)   | 2910.00 $\pm$ 60.00       | 1.85 $\pm$ 0.13           | 1.75 $\pm$ 0.06           | 2.83 $\pm$ 0.03           | 1.97 $\pm$ 0.28           | 2.06 $\pm$ 0.08           | 1.53 $\pm$ 0.01           | 3.74 $\pm$ 0.01          
FD - Poisson (ms)         | 6210.00 $\pm$ 110.00      | 3.02 $\pm$ 0.08           | 2.80 $\pm$ 0.29           | 7.20 $\pm$ 0.09           | 2.81 $\pm$ 0.02           | 3.84 $\pm$ 0.02           | 2.68 $\pm$ 0.09           | 8.93 $\pm$ 0.04          
FD - Laplace (ms)         | 613.00 $\pm$ 18.00        | 68.50 $\pm$ 0.40          | 153.00 $\pm$ 5.00         | 246.00 $\pm$ 1.00         | 63.60 $\pm$ 2.20          | 258.00 $\pm$ 1.00         | 63.30 $\pm$ 0.60          | 306.00 $\pm$ 2.00        
M-D (ms)                  | 14800.00 $\pm$ 100.00     | 15.20 $\pm$ 0.00          | 51.90 $\pm$ 0.30          | 59.40 $\pm$ 0.40          | 54.10 $\pm$ 0.20          | 59.70 $\pm$ 0.10          | 71.10 $\pm$ 1.10          | 60.40 $\pm$ 0.40         

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
## Python 3.12 results
### Performance Comparison (as of 1.11.2)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | -                         | -                         | 0.31                      | 1.38                      | 1.35                      | 1.46                      | 1.43                     
Bellman Ford              | -                         | -                         | -                         | 1.27                      | 2.52                      | 2.72                      | 2.66                      | 3.60                     
Dijkstra                  | -                         | -                         | -                         | 1.66                      | 2.63                      | 2.73                      | 2.76                      | 3.59                     
Euler                     | -                         | -                         | -                         | 2.09                      | 2.50                      | 2.74                      | 2.62                      | 3.49                     
Midpoint Explicit         | -                         | -                         | -                         | 3.05                      | 2.78                      | 3.02                      | 2.91                      | 3.77                     
Midpoint Fixed            | -                         | -                         | -                         | 3.30                      | 2.93                      | 3.14                      | 3.03                      | 3.89                     
RK4                       | -                         | -                         | -                         | 3.79                      | 3.33                      | 3.55                      | 3.50                      | 4.34                     
FD - L Convection         | -                         | -                         | -                         | 0.93                      | 2.47                      | 2.68                      | 2.67                      | 3.48                     
FD - NL Convection        | -                         | -                         | -                         | 0.91                      | 2.47                      | 2.72                      | 2.65                      | 3.47                     
FD - Poisson              | -                         | -                         | -                         | 1.38                      | 2.63                      | 2.84                      | 3.19                      | 3.56                     
FD - Laplace              | -                         | -                         | -                         | 3.07                      | 3.06                      | 3.26                      | 3.30                      | 4.18                     
M-D                       | -                         | -                         | -                         | 4.10                      | 3.40                      | 3.37                      | 3.63                      | 4.54                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 471.00 $\pm$ 5.00         | -                         | -                         | 10.70 $\pm$ 0.30          | 1.55 $\pm$ 0.00           | 1.62 $\pm$ 0.10           | 8.32 $\pm$ 0.38           | 4.36 $\pm$ 0.01          
Bellman Ford (ms)         | 2550.00 $\pm$ 40.00       | -                         | -                         | 3.88 $\pm$ 0.07           | 2.96 $\pm$ 0.02           | 5.95 $\pm$ 0.03           | 4.39 $\pm$ 0.02           | 18.20 $\pm$ 0.30         
Dijkstra (ms)             | 6930.00 $\pm$ 40.00       | -                         | -                         | 20.50 $\pm$ 0.60          | 19.40 $\pm$ 0.40          | 30.90 $\pm$ 0.60          | 24.70 $\pm$ 0.40          | 22.70 $\pm$ 0.40         
Euler (ms)                | 4780.00 $\pm$ 30.00       | -                         | -                         | 37.60 $\pm$ 0.30          | 15.30 $\pm$ 0.30          | 144.00 $\pm$ 1.00         | 14.90 $\pm$ 0.50          | 131.00 $\pm$ 3.00        
Midpoint Explicit (ms)    | 9600.00 $\pm$ 60.00       | -                         | -                         | 75.70 $\pm$ 5.40          | 23.60 $\pm$ 0.50          | 284.00 $\pm$ 2.00         | 16.50 $\pm$ 1.20          | 253.00 $\pm$ 1.00        
Midpoint Fixed (s)        | 47.80 $\pm$ 0.20          | -                         | -                         | 0.38 $\pm$ 0.01           | 0.08 $\pm$ 0.00           | 1.40 $\pm$ 0.01           | 0.06 $\pm$ 0.01           | 1.25 $\pm$ 0.01          
RK4 (ms)                  | 24100.00 $\pm$ 200.00     | -                         | -                         | 144.00 $\pm$ 11.00        | 33.90 $\pm$ 0.80          | 496.00 $\pm$ 8.00         | 38.70 $\pm$ 1.80          | 409.00 $\pm$ 1.00        
FD - L Convection (ms)    | 2890.00 $\pm$ 40.00       | -                         | -                         | 2.70 $\pm$ 0.05           | 1.56 $\pm$ 0.10           | 1.73 $\pm$ 0.12           | 1.32 $\pm$ 0.01           | 3.70 $\pm$ 0.01          
FD - NL Convection (ms)   | 3570.00 $\pm$ 30.00       | -                         | -                         | 2.84 $\pm$ 0.06           | 1.84 $\pm$ 0.03           | 2.06 $\pm$ 0.08           | 1.54 $\pm$ 0.01           | 3.74 $\pm$ 0.01          
FD - Poisson (ms)         | 8130.00 $\pm$ 120.00      | -                         | -                         | 7.38 $\pm$ 0.54           | 2.78 $\pm$ 0.01           | 3.80 $\pm$ 0.03           | 2.69 $\pm$ 0.01           | 8.94 $\pm$ 0.02          
FD - Laplace (ms)         | 605.00 $\pm$ 9.00         | -                         | -                         | 246.00 $\pm$ 1.00         | 64.00 $\pm$ 1.40          | 260.00 $\pm$ 1.00         | 61.60 $\pm$ 2.60          | 308.00 $\pm$ 12.00       
M-D (ms)                  | 18400.00 $\pm$ 200.00     | -                         | -                         | 59.10 $\pm$ 0.30          | 57.60 $\pm$ 4.50          | 59.90 $\pm$ 1.20          | 71.70 $\pm$ 1.70          | 62.80 $\pm$ 1.70         

![Python 3.12 compilation results](./version_specific_results/pypi_performance_312_compilation.svg)
![Python 3.12 execution results](./version_specific_results/pypi_performance_312_execution.svg)
