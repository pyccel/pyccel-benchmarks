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
### Performance Comparison (as of Tue Feb 13 09:57:15 UTC 2024)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.44                      | 2.31                      | 0.33                      | 1.29                      | 1.25                      | -                         | 1.36                     
Bellman Ford              | -                         | 3.57                      | 3.99                      | 1.13                      | -                         | -                         | -                         | -                        
Dijkstra                  | -                         | 2.50                      | 2.93                      | 1.63                      | 2.49                      | 2.61                      | -                         | 3.48                     
Euler                     | -                         | 2.90                      | 3.33                      | 2.08                      | 2.39                      | 2.62                      | -                         | 3.38                     
Midpoint Explicit         | -                         | 3.27                      | 3.73                      | 3.06                      | 2.58                      | 2.82                      | -                         | 3.60                     
Midpoint Fixed            | -                         | 3.62                      | 4.43                      | 3.26                      | 2.69                      | 2.92                      | -                         | 3.71                     
RK4                       | -                         | 3.97                      | 4.57                      | 3.83                      | 3.15                      | 3.32                      | -                         | 4.12                     
FD - L Convection         | -                         | 2.48                      | 2.88                      | 0.89                      | 2.33                      | 2.55                      | -                         | 3.33                     
FD - NL Convection        | -                         | 3.45                      | 3.86                      | 0.90                      | 2.35                      | 2.55                      | -                         | 3.35                     
FD - Poisson              | -                         | 3.54                      | 4.04                      | 1.34                      | 2.44                      | 2.66                      | -                         | 3.41                     
FD - Laplace              | -                         | 6.89                      | 9.12                      | 3.11                      | 2.80                      | 3.02                      | -                         | 3.91                     
M-D                       | -                         | 6.54                      | 7.67                      | 4.15                      | 3.21                      | 3.22                      | -                         | 4.35                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 317.00                    | 2.95                      | 3.47                      | 9.81                      | 1.50                      | 1.55                      | -                         | 3.92                     
Bellman Ford (ms)         | 1800.00                   | 4.17                      | 3.17                      | 3.86                      | -                         | -                         | -                         | -                        
Dijkstra (ms)             | 5010.00                   | 23.60                     | 17.90                     | 19.60                     | 19.70                     | 31.10                     | -                         | 22.80                    
Euler (ms)                | 3910.00                   | 28.70                     | 28.60                     | 39.90                     | 16.40                     | 144.00                    | -                         | 128.00                   
Midpoint Explicit (ms)    | 7880.00                   | 59.00                     | 54.60                     | 77.40                     | 21.90                     | 268.00                    | -                         | 248.00                   
Midpoint Fixed (ms)       | 39300.00                  | 249.00                    | 61.40                     | 397.00                    | 75.90                     | 1390.00                   | -                         | 1220.00                  
RK4 (ms)                  | 20100.00                  | 167.00                    | 37.50                     | 145.00                    | 36.00                     | 483.00                    | -                         | 403.00                   
FD - L Convection (ms)    | 2240.00                   | 1.61                      | 1.56                      | 2.68                      | 1.44                      | 1.65                      | -                         | 3.69                     
FD - NL Convection (ms)   | 2780.00                   | 1.82                      | 1.88                      | 2.82                      | 1.68                      | 1.99                      | -                         | 3.74                     
FD - Poisson (ms)         | 6150.00                   | 3.02                      | 2.60                      | 7.12                      | 2.69                      | 3.70                      | -                         | 8.74                     
FD - Laplace (ms)         | 574.00                    | 63.20                     | 151.00                    | 246.00                    | 58.30                     | 255.00                    | -                         | 305.00                   
M-D (ms)                  | 15600.00                  | 15.20                     | 52.10                     | 58.70                     | 54.10                     | 59.70                     | -                         | 59.40                    

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.8 results
### Performance Comparison (as of 1.10.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.89                      | 1.98                      | 0.33                      | 1.28                      | 1.23                      | 1.37                      | 1.30                     
Bellman Ford              | -                         | 3.30                      | 3.68                      | 1.08                      | 1.99                      | 1.97                      | 2.11                      | 2.44                     
Dijkstra                  | -                         | 2.30                      | 2.67                      | 1.58                      | 2.04                      | 1.99                      | 2.18                      | 2.51                     
Euler                     | -                         | 2.68                      | 3.07                      | 2.01                      | 1.95                      | 1.99                      | 2.09                      | 2.41                     
Midpoint Explicit         | -                         | 2.95                      | 3.43                      | 2.99                      | 2.23                      | 2.26                      | 2.37                      | 2.66                     
Midpoint Fixed            | -                         | 3.36                      | 4.00                      | 3.19                      | 2.28                      | 2.32                      | 2.42                      | 2.76                     
RK4                       | -                         | 3.68                      | 4.22                      | 3.76                      | 2.74                      | 2.72                      | 2.85                      | 3.10                     
FD - L Convection         | -                         | 2.23                      | 2.59                      | 0.85                      | 1.92                      | 1.95                      | 2.06                      | 2.38                     
FD - NL Convection        | -                         | 3.21                      | 3.51                      | 0.88                      | 1.93                      | 1.97                      | 2.06                      | 2.38                     
FD - Poisson              | -                         | 3.26                      | 3.77                      | 1.32                      | 2.04                      | 2.06                      | 2.20                      | 2.46                     
FD - Laplace              | -                         | 5.95                      | 7.91                      | 2.99                      | 2.40                      | 2.43                      | 2.48                      | 2.89                     
M-D                       | -                         | 6.03                      | 5.69                      | 3.99                      | 2.76                      | 2.59                      | 2.95                      | 3.38                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 328.00 $\pm$ 7.00         | 2.97 $\pm$ 0.04           | 3.47 $\pm$ 0.01           | 10.60 $\pm$ 0.30          | 1.55 $\pm$ 0.00           | 1.60 $\pm$ 0.03           | 7.11 $\pm$ 0.01           | 4.76 $\pm$ 0.00          
Bellman Ford (ms)         | 1860.00 $\pm$ 10.00       | 4.91 $\pm$ 0.01           | 3.19 $\pm$ 0.06           | 3.85 $\pm$ 0.07           | 2.95 $\pm$ 0.02           | 5.58 $\pm$ 0.02           | 3.98 $\pm$ 0.02           | 18.60 $\pm$ 0.20         
Dijkstra (ms)             | 4980.00 $\pm$ 50.00       | 26.30 $\pm$ 0.40          | 16.40 $\pm$ 0.10          | 19.10 $\pm$ 0.50          | 18.80 $\pm$ 0.40          | 30.50 $\pm$ 0.50          | 25.60 $\pm$ 0.40          | 22.10 $\pm$ 0.10         
Euler (ms)                | 3900.00 $\pm$ 30.00       | 28.90 $\pm$ 0.30          | 28.80 $\pm$ 0.90          | 38.80 $\pm$ 1.30          | 15.20 $\pm$ 0.70          | 143.00 $\pm$ 2.00         | 7.26 $\pm$ 0.42           | 126.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 7930.00 $\pm$ 60.00       | 59.50 $\pm$ 0.50          | 57.00 $\pm$ 0.70          | 81.70 $\pm$ 2.90          | 22.80 $\pm$ 0.70          | 279.00 $\pm$ 2.00         | 18.10 $\pm$ 0.40          | 253.00 $\pm$ 3.00        
Midpoint Fixed (ms)       | 40300.00 $\pm$ 300.00     | 511.00 $\pm$ 16.00        | 327.00 $\pm$ 10.00        | 389.00 $\pm$ 14.00        | 74.80 $\pm$ 0.60          | 1400.00 $\pm$ 20.00       | 65.30 $\pm$ 0.40          | 1230.00 $\pm$ 20.00      
RK4 (ms)                  | 20100.00 $\pm$ 100.00     | 165.00 $\pm$ 3.00         | 38.50 $\pm$ 1.00          | 147.00 $\pm$ 4.00         | 36.00 $\pm$ 0.50          | 482.00 $\pm$ 2.00         | 47.40 $\pm$ 0.30          | 408.00 $\pm$ 3.00        
FD - L Convection (ms)    | 2450.00 $\pm$ 20.00       | 1.47 $\pm$ 0.08           | 1.52 $\pm$ 0.05           | 2.70 $\pm$ 0.03           | 1.56 $\pm$ 0.20           | 1.64 $\pm$ 0.02           | 2.47 $\pm$ 0.01           | 3.69 $\pm$ 0.01          
FD - NL Convection (ms)   | 3000.00 $\pm$ 30.00       | 1.88 $\pm$ 0.04           | 1.79 $\pm$ 0.04           | 2.83 $\pm$ 0.04           | 1.89 $\pm$ 0.10           | 2.20 $\pm$ 0.01           | 2.81 $\pm$ 0.01           | 3.74 $\pm$ 0.01          
FD - Poisson (ms)         | 6430.00 $\pm$ 60.00       | 3.12 $\pm$ 0.19           | 2.70 $\pm$ 0.06           | 7.19 $\pm$ 0.05           | 2.81 $\pm$ 0.06           | 3.82 $\pm$ 0.04           | 5.36 $\pm$ 0.02           | 9.16 $\pm$ 0.22          
FD - Laplace (ms)         | 585.00 $\pm$ 2.00         | 90.80 $\pm$ 0.50          | 147.00 $\pm$ 1.00         | 251.00 $\pm$ 1.00         | 62.20 $\pm$ 0.90          | 311.00 $\pm$ 11.00        | 103.00 $\pm$ 1.00         | 309.00 $\pm$ 7.00        
M-D (ms)                  | 15800.00 $\pm$ 200.00     | 14.30 $\pm$ 0.00          | 51.40 $\pm$ 0.40          | 59.20 $\pm$ 0.20          | 58.50 $\pm$ 12.20         | 59.70 $\pm$ 0.20          | 85.30 $\pm$ 0.20          | 60.10 $\pm$ 0.20         

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.10.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.91                      | 1.97                      | 0.32                      | 1.28                      | 1.23                      | 1.37                      | 1.32                     
Bellman Ford              | -                         | 3.34                      | 3.65                      | 1.07                      | 1.99                      | 1.98                      | 2.10                      | 2.44                     
Dijkstra                  | -                         | 2.34                      | 2.69                      | 1.57                      | 2.05                      | 1.98                      | 2.19                      | 2.47                     
Euler                     | -                         | 2.63                      | 3.05                      | 2.01                      | 1.95                      | 1.99                      | 2.11                      | 2.43                     
Midpoint Explicit         | -                         | 2.96                      | 3.41                      | 2.97                      | 2.22                      | 2.27                      | 2.36                      | 2.65                     
Midpoint Fixed            | -                         | 3.38                      | 4.02                      | 3.18                      | 2.27                      | 2.32                      | 2.41                      | 2.75                     
RK4                       | -                         | 3.66                      | 4.21                      | 3.72                      | 2.71                      | 2.70                      | 2.85                      | 3.07                     
FD - L Convection         | -                         | 2.24                      | 2.61                      | 0.85                      | 1.91                      | 1.95                      | 2.10                      | 2.40                     
FD - NL Convection        | -                         | 3.13                      | 3.54                      | 0.86                      | 1.93                      | 1.96                      | 2.06                      | 2.41                     
FD - Poisson              | -                         | 3.28                      | 3.76                      | 1.31                      | 2.05                      | 2.06                      | 2.18                      | 2.46                     
FD - Laplace              | -                         | 5.95                      | 7.86                      | 2.98                      | 2.40                      | 2.42                      | 2.48                      | 2.88                     
M-D                       | -                         | 6.02                      | 5.73                      | 3.96                      | 2.75                      | 2.57                      | 2.92                      | 3.38                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 304.00 $\pm$ 3.00         | 2.99 $\pm$ 0.10           | 3.49 $\pm$ 0.07           | 10.70 $\pm$ 0.30          | 1.50 $\pm$ 0.00           | 1.51 $\pm$ 0.04           | 7.17 $\pm$ 0.21           | 4.77 $\pm$ 0.01          
Bellman Ford (ms)         | 1920.00 $\pm$ 10.00       | 4.91 $\pm$ 0.01           | 3.22 $\pm$ 0.05           | 3.89 $\pm$ 0.06           | 2.97 $\pm$ 0.02           | 6.11 $\pm$ 0.03           | 3.98 $\pm$ 0.01           | 18.60 $\pm$ 0.20         
Dijkstra (ms)             | 5170.00 $\pm$ 60.00       | 26.70 $\pm$ 0.50          | 16.80 $\pm$ 0.20          | 19.70 $\pm$ 0.40          | 18.40 $\pm$ 0.30          | 30.30 $\pm$ 0.40          | 25.60 $\pm$ 0.30          | 22.40 $\pm$ 0.10         
Euler (ms)                | 3880.00 $\pm$ 30.00       | 28.90 $\pm$ 0.30          | 28.30 $\pm$ 0.30          | 38.70 $\pm$ 1.40          | 14.70 $\pm$ 0.30          | 141.00 $\pm$ 2.00         | 6.84 $\pm$ 0.23           | 126.00 $\pm$ 3.00        
Midpoint Explicit (ms)    | 7890.00 $\pm$ 60.00       | 59.40 $\pm$ 0.40          | 56.70 $\pm$ 0.40          | 83.30 $\pm$ 1.70          | 23.20 $\pm$ 0.70          | 279.00 $\pm$ 2.00         | 18.40 $\pm$ 1.20          | 252.00 $\pm$ 11.00       
Midpoint Fixed (ms)       | 40100.00 $\pm$ 300.00     | 509.00 $\pm$ 5.00         | 325.00 $\pm$ 3.00         | 429.00 $\pm$ 117.00       | 74.80 $\pm$ 0.70          | 1380.00 $\pm$ 10.00       | 65.70 $\pm$ 1.60          | 1220.00 $\pm$ 10.00      
RK4 (ms)                  | 20000.00 $\pm$ 200.00     | 162.00 $\pm$ 2.00         | 37.90 $\pm$ 0.30          | 161.00 $\pm$ 29.00        | 36.30 $\pm$ 0.60          | 484.00 $\pm$ 3.00         | 47.80 $\pm$ 1.90          | 411.00 $\pm$ 2.00        
FD - L Convection (ms)    | 2400.00 $\pm$ 20.00       | 1.49 $\pm$ 0.07           | 1.47 $\pm$ 0.06           | 2.73 $\pm$ 0.08           | 1.75 $\pm$ 0.02           | 1.77 $\pm$ 0.10           | 2.45 $\pm$ 0.01           | 3.69 $\pm$ 0.01          
FD - NL Convection (ms)   | 2940.00 $\pm$ 30.00       | 1.83 $\pm$ 0.08           | 1.73 $\pm$ 0.07           | 2.84 $\pm$ 0.06           | 1.87 $\pm$ 0.09           | 2.07 $\pm$ 0.10           | 2.90 $\pm$ 0.01           | 3.74 $\pm$ 0.01          
FD - Poisson (ms)         | 6410.00 $\pm$ 90.00       | 3.03 $\pm$ 0.03           | 2.67 $\pm$ 0.04           | 7.26 $\pm$ 0.17           | 2.82 $\pm$ 0.01           | 3.79 $\pm$ 0.03           | 5.37 $\pm$ 0.02           | 9.31 $\pm$ 0.05          
FD - Laplace (ms)         | 587.00 $\pm$ 15.00        | 87.20 $\pm$ 0.30          | 145.00 $\pm$ 1.00         | 251.00 $\pm$ 1.00         | 63.10 $\pm$ 0.70          | 259.00 $\pm$ 1.00         | 104.00 $\pm$ 1.00         | 309.00 $\pm$ 2.00        
M-D (ms)                  | 15300.00 $\pm$ 200.00     | 14.30 $\pm$ 0.00          | 51.50 $\pm$ 0.50          | 60.20 $\pm$ 2.60          | 54.00 $\pm$ 0.10          | 59.30 $\pm$ 0.30          | 85.60 $\pm$ 0.80          | 63.10 $\pm$ 9.30         

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.10.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.28                      | 2.17                      | 0.33                      | 1.27                      | 1.23                      | 1.38                      | 1.31                     
Bellman Ford              | -                         | 3.57                      | 3.89                      | 1.11                      | 2.07                      | 2.03                      | 2.18                      | 2.48                     
Dijkstra                  | -                         | 2.44                      | 2.89                      | 1.58                      | 2.05                      | 1.99                      | 2.20                      | 2.50                     
Euler                     | -                         | 2.80                      | 3.34                      | 2.08                      | 2.01                      | 2.03                      | 2.12                      | 2.46                     
Midpoint Explicit         | -                         | 3.15                      | 3.67                      | 3.03                      | 2.22                      | 2.25                      | 2.34                      | 2.67                     
Midpoint Fixed            | -                         | 3.44                      | 4.17                      | 3.17                      | 2.26                      | 2.29                      | 2.39                      | 2.74                     
RK4                       | -                         | 4.10                      | 4.70                      | 3.81                      | 2.83                      | 2.77                      | 2.90                      | 3.13                     
FD - L Convection         | -                         | 2.47                      | 2.82                      | 0.88                      | 1.96                      | 2.00                      | 2.15                      | 2.46                     
FD - NL Convection        | -                         | 3.47                      | 3.78                      | 0.90                      | 2.00                      | 2.02                      | 2.12                      | 2.45                     
FD - Poisson              | -                         | 3.53                      | 4.06                      | 1.37                      | 2.12                      | 2.11                      | 2.25                      | 2.56                     
FD - Laplace              | -                         | 6.46                      | 8.34                      | 3.16                      | 2.55                      | 2.48                      | 2.52                      | 2.98                     
M-D                       | -                         | 6.23                      | 5.89                      | 3.96                      | 2.72                      | 2.51                      | 2.88                      | 3.41                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 313.00 $\pm$ 5.00         | 2.97 $\pm$ 0.09           | 3.50 $\pm$ 0.10           | 10.50 $\pm$ 0.30          | 1.55 $\pm$ 0.01           | 1.59 $\pm$ 0.00           | 7.12 $\pm$ 0.02           | 3.96 $\pm$ 0.11          
Bellman Ford (ms)         | 1760.00 $\pm$ 10.00       | 5.32 $\pm$ 0.02           | 3.18 $\pm$ 0.06           | 3.83 $\pm$ 0.05           | 3.01 $\pm$ 0.02           | 6.01 $\pm$ 0.06           | 3.98 $\pm$ 0.01           | 18.60 $\pm$ 0.10         
Dijkstra (ms)             | 4870.00 $\pm$ 40.00       | 25.30 $\pm$ 0.40          | 17.00 $\pm$ 0.40          | 19.40 $\pm$ 1.00          | 18.80 $\pm$ 0.40          | 31.50 $\pm$ 0.60          | 28.30 $\pm$ 0.60          | 22.20 $\pm$ 0.50         
Euler (ms)                | 3960.00 $\pm$ 20.00       | 29.50 $\pm$ 0.40          | 29.20 $\pm$ 1.10          | 39.90 $\pm$ 1.10          | 15.70 $\pm$ 0.50          | 144.00 $\pm$ 3.00         | 7.28 $\pm$ 0.42           | 126.00 $\pm$ 6.00        
Midpoint Explicit (ms)    | 7910.00 $\pm$ 50.00       | 59.30 $\pm$ 0.40          | 56.90 $\pm$ 0.50          | 81.50 $\pm$ 2.80          | 22.90 $\pm$ 0.60          | 280.00 $\pm$ 4.00         | 18.20 $\pm$ 0.50          | 252.00 $\pm$ 11.00       
Midpoint Fixed (ms)       | 40500.00 $\pm$ 200.00     | 530.00 $\pm$ 63.00        | 327.00 $\pm$ 7.00         | 385.00 $\pm$ 11.00        | 75.00 $\pm$ 0.90          | 1400.00 $\pm$ 20.00       | 65.50 $\pm$ 1.00          | 1240.00 $\pm$ 30.00      
RK4 (ms)                  | 20000.00 $\pm$ 100.00     | 163.00 $\pm$ 4.00         | 38.60 $\pm$ 0.50          | 146.00 $\pm$ 5.00         | 36.80 $\pm$ 0.60          | 488.00 $\pm$ 13.00        | 46.50 $\pm$ 0.40          | 411.00 $\pm$ 3.00        
FD - L Convection (ms)    | 2210.00 $\pm$ 30.00       | 1.67 $\pm$ 0.05           | 1.46 $\pm$ 0.07           | 2.71 $\pm$ 0.05           | 1.71 $\pm$ 0.07           | 1.73 $\pm$ 0.12           | 2.47 $\pm$ 0.02           | 3.67 $\pm$ 0.02          
FD - NL Convection (ms)   | 2730.00 $\pm$ 20.00       | 1.91 $\pm$ 0.08           | 1.79 $\pm$ 0.07           | 2.91 $\pm$ 0.20           | 1.83 $\pm$ 0.12           | 2.13 $\pm$ 0.08           | 2.90 $\pm$ 0.01           | 3.91 $\pm$ 0.09          
FD - Poisson (ms)         | 6450.00 $\pm$ 40.00       | 3.02 $\pm$ 0.04           | 2.72 $\pm$ 0.04           | 7.20 $\pm$ 0.03           | 2.81 $\pm$ 0.03           | 3.87 $\pm$ 0.03           | 5.37 $\pm$ 0.03           | 9.13 $\pm$ 0.03          
FD - Laplace (ms)         | 583.00 $\pm$ 11.00        | 88.80 $\pm$ 2.40          | 146.00 $\pm$ 5.00         | 246.00 $\pm$ 1.00         | 58.60 $\pm$ 0.40          | 260.00 $\pm$ 1.00         | 103.00 $\pm$ 0.00         | 311.00 $\pm$ 6.00        
M-D (ms)                  | 15200.00 $\pm$ 400.00     | 14.30 $\pm$ 0.10          | 52.20 $\pm$ 1.80          | 60.00 $\pm$ 2.20          | 54.60 $\pm$ 0.40          | 59.60 $\pm$ 1.10          | 86.00 $\pm$ 1.00          | 60.10 $\pm$ 0.60         

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.10.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 3.24                      | 3.27                      | 0.48                      | 1.71                      | 1.64                      | 1.80                      | 1.65                     
Bellman Ford              | -                         | 5.42                      | 6.18                      | 1.61                      | 2.95                      | 2.90                      | 3.14                      | 3.07                     
Dijkstra                  | -                         | 3.84                      | 4.23                      | 1.75                      | 2.97                      | 2.84                      | 3.17                      | 3.12                     
Euler                     | -                         | 4.30                      | 5.25                      | 2.27                      | 2.95                      | 2.86                      | 3.22                      | 3.01                     
Midpoint Explicit         | -                         | 4.89                      | 6.01                      | 3.24                      | 3.34                      | 3.41                      | 3.69                      | 3.53                     
Midpoint Fixed            | -                         | 5.50                      | 6.55                      | 3.34                      | 3.56                      | 3.62                      | 3.90                      | 3.86                     
RK4                       | -                         | 6.08                      | 6.97                      | 3.62                      | 3.84                      | 3.71                      | 4.37                      | 4.13                     
FD - L Convection         | -                         | 3.27                      | 3.98                      | 1.21                      | 2.79                      | 2.84                      | 3.09                      | 2.82                     
FD - NL Convection        | -                         | 5.07                      | 5.73                      | 1.24                      | 2.73                      | 2.59                      | 2.88                      | 2.87                     
FD - Poisson              | -                         | 5.39                      | 6.30                      | 1.82                      | 2.95                      | 2.94                      | 3.47                      | 3.10                     
FD - Laplace              | -                         | 10.45                     | 13.15                     | 3.42                      | 3.35                      | 3.43                      | 3.86                      | 3.78                     
M-D                       | -                         | 10.41                     | 9.81                      | 3.96                      | 3.75                      | 3.50                      | 4.41                      | 4.09                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 641.00 $\pm$ 35.00        | 9.11 $\pm$ 0.22           | 3.39 $\pm$ 0.09           | 32.60 $\pm$ 2.10          | 2.41 $\pm$ 0.06           | 2.53 $\pm$ 0.12           | 20.70 $\pm$ 0.50          | 6.09 $\pm$ 0.10          
Bellman Ford (ms)         | 3470.00 $\pm$ 60.00       | 8.08 $\pm$ 0.17           | 7.17 $\pm$ 0.21           | 7.88 $\pm$ 0.21           | 5.30 $\pm$ 0.10           | 10.60 $\pm$ 0.40          | 5.34 $\pm$ 0.11           | 6.39 $\pm$ 0.35          
Dijkstra (ms)             | 9100.00 $\pm$ 130.00      | 52.30 $\pm$ 2.00          | 39.90 $\pm$ 1.60          | 51.20 $\pm$ 2.40          | 51.50 $\pm$ 2.10          | 65.50 $\pm$ 1.80          | 65.60 $\pm$ 2.30          | 53.70 $\pm$ 1.60         
Euler (ms)                | 5650.00 $\pm$ 240.00      | 51.50 $\pm$ 1.50          | 56.20 $\pm$ 5.70          | 137.00 $\pm$ 5.00         | 27.30 $\pm$ 1.40          | 283.00 $\pm$ 11.00        | 10.80 $\pm$ 0.80          | 301.00 $\pm$ 6.00        
Midpoint Explicit (ms)    | 12000.00 $\pm$ 400.00     | 101.00 $\pm$ 3.00         | 103.00 $\pm$ 2.00         | 277.00 $\pm$ 10.00        | 43.40 $\pm$ 1.40          | 577.00 $\pm$ 8.00         | 29.70 $\pm$ 0.80          | 581.00 $\pm$ 11.00       
Midpoint Fixed (s)        | 56.30 $\pm$ 1.50          | 0.83 $\pm$ 0.02           | 0.56 $\pm$ 0.01           | 1.34 $\pm$ 0.03           | 0.14 $\pm$ 0.00           | 2.92 $\pm$ 0.05           | 0.09 $\pm$ 0.00           | 2.68 $\pm$ 0.06          
RK4 (ms)                  | 29200.00 $\pm$ 1300.00    | 233.00 $\pm$ 7.00         | 76.30 $\pm$ 2.80          | 460.00 $\pm$ 20.00        | 53.00 $\pm$ 2.10          | 908.00 $\pm$ 29.00        | 81.70 $\pm$ 7.70          | 933.00 $\pm$ 15.00       
FD - L Convection (ms)    | 3610.00 $\pm$ 140.00      | 3.56 $\pm$ 0.07           | 3.63 $\pm$ 0.10           | 4.68 $\pm$ 0.16           | 3.08 $\pm$ 0.09           | 4.13 $\pm$ 0.12           | 2.20 $\pm$ 0.04           | 5.56 $\pm$ 0.15          
FD - NL Convection (ms)   | 4510.00 $\pm$ 180.00      | 3.51 $\pm$ 0.26           | 3.47 $\pm$ 0.33           | 5.00 $\pm$ 0.29           | 3.21 $\pm$ 0.13           | 5.18 $\pm$ 0.08           | 2.36 $\pm$ 0.04           | 5.33 $\pm$ 0.15          
FD - Poisson (ms)         | 10400.00 $\pm$ 500.00     | 7.98 $\pm$ 0.23           | 10.80 $\pm$ 0.10          | 14.10 $\pm$ 0.30          | 8.35 $\pm$ 0.09           | 12.00 $\pm$ 0.70          | 8.53 $\pm$ 0.40           | 13.10 $\pm$ 0.40         
FD - Laplace (ms)         | 1280.00 $\pm$ 10.00       | 266.00 $\pm$ 5.00         | 351.00 $\pm$ 6.00         | 568.00 $\pm$ 14.00        | 192.00 $\pm$ 3.00         | 560.00 $\pm$ 12.00        | 201.00 $\pm$ 4.00         | 603.00 $\pm$ 7.00        
M-D (ms)                  | 22100.00 $\pm$ 1200.00    | 72.90 $\pm$ 2.60          | 93.00 $\pm$ 2.50          | 103.00 $\pm$ 1.00         | 139.00 $\pm$ 2.00         | 145.00 $\pm$ 2.00         | 105.00 $\pm$ 2.00         | 93.50 $\pm$ 2.50         

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
## Python 3.12 results
