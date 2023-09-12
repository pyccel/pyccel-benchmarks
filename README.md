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
### Performance Comparison (as of Wed Sep  6 17:58:10 UTC 2023)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.50                      | 0.40                      | 1.27                      | 1.22                     
Bellman Ford              | -                         | 3.56                      | 1.20                      | 2.24                      | 2.19                     
Dijkstra                  | -                         | 2.80                      | 1.38                      | 2.33                      | 2.22                     
Euler                     | -                         | 3.09                      | 1.83                      | 2.20                      | 2.24                     
Midpoint Explicit         | -                         | 3.46                      | 2.53                      | 2.51                      | 2.55                     
Midpoint Fixed            | -                         | 3.99                      | 2.68                      | 2.58                      | 2.65                     
RK4                       | -                         | 4.67                      | 3.08                      | 3.28                      | 3.15                     
FD - L Convection         | -                         | 2.64                      | 0.98                      | 2.14                      | 2.15                     
FD - NL Convection        | -                         | 3.38                      | 1.05                      | 2.17                      | 2.19                     
FD - Poisson              | -                         | 3.62                      | 1.51                      | 2.32                      | 2.35                     
FD - Laplace              | -                         | 7.10                      | 2.88                      | 2.75                      | 2.81                     
M-D                       | -                         | 7.23                      | 3.37                      | 3.27                      | 2.98                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 442.00                    | 9.52                      | 28.00                     | 3.17                      | 3.30                     
Bellman Ford (ms)         | 2810.00                   | 7.71                      | 6.36                      | 3.82                      | 6.44                     
Dijkstra (ms)             | 7370.00                   | 45.40                     | 38.50                     | 35.80                     | 47.70                    
Euler (ms)                | 4790.00                   | 40.60                     | 111.00                    | 18.00                     | 240.00                   
Midpoint Explicit (ms)    | 9780.00                   | 78.90                     | 208.00                    | 27.10                     | 469.00                   
Midpoint Fixed (s)        | 49.20                     | 0.66                      | 1.06                      | 0.10                      | 2.32                     
RK4 (ms)                  | 24300.00                  | 200.00                    | 407.00                    | 42.70                     | 758.00                   
FD - L Convection (ms)    | 3110.00                   | 2.89                      | 3.84                      | 1.73                      | 2.84                     
FD - NL Convection (ms)   | 3820.00                   | 3.39                      | 3.42                      | 1.81                      | 2.86                     
FD - Poisson (ms)         | 8910.00                   | 5.70                      | 9.74                      | 3.68                      | 4.90                     
FD - Laplace (ms)         | 687.00                    | 232.00                    | 376.00                    | 73.30                     | 414.00                   
M-D (ms)                  | 19300.00                  | 52.90                     | 73.10                     | 106.00                    | 110.00                   

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
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.98                      | 1.87                      | 0.39                      | 1.22                      | 1.15                      | 1.33                      | 1.31                     
Bellman Ford              | -                         | 3.26                      | 3.26                      | 1.18                      | 2.16                      | 2.13                      | 2.59                      | 2.87                     
Dijkstra                  | -                         | 2.49                      | 2.47                      | 1.35                      | 2.26                      | 2.15                      | 2.58                      | 2.73                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 400.00 $\pm$ 4.00         | 9.89 $\pm$ 0.01           | 9.90 $\pm$ 0.02           | 27.10 $\pm$ 0.20          | 3.21 $\pm$ 0.01           | 3.27 $\pm$ 0.01           | 22.10 $\pm$ 0.00          | 16.60 $\pm$ 0.00         
Bellman Ford (ms)         | 2580.00 $\pm$ 0.00        | 6.73 $\pm$ 0.02           | 6.73 $\pm$ 0.00           | 6.09 $\pm$ 0.02           | 4.44 $\pm$ 0.00           | 6.57 $\pm$ 0.00           | 4.54 $\pm$ 0.01           | 6.59 $\pm$ 0.01          
Dijkstra (ms)             | 6880.00 $\pm$ 30.00       | 39.00 $\pm$ 0.40          | 39.20 $\pm$ 0.50          | 32.90 $\pm$ 1.10          | 31.10 $\pm$ 0.50          | 48.30 $\pm$ 0.50          | 48.80 $\pm$ 0.50          | 49.80 $\pm$ 0.50         

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.52                      | 2.34                      | 0.48                      | 1.56                      | 1.48                      | 1.71                      | 1.66                     
Bellman Ford              | -                         | 4.21                      | 4.13                      | 1.42                      | 2.71                      | 2.65                      | 3.21                      | 3.55                     
Dijkstra                  | -                         | 3.22                      | 3.19                      | 1.67                      | 2.82                      | 2.70                      | 3.17                      | 3.41                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 478.00 $\pm$ 2.00         | 3.14 $\pm$ 0.02           | 3.16 $\pm$ 0.03           | 16.80 $\pm$ 0.30          | 2.66 $\pm$ 0.02           | 2.50 $\pm$ 0.02           | 8.03 $\pm$ 0.02           | 4.53 $\pm$ 0.03          
Bellman Ford (ms)         | 3350.00 $\pm$ 30.00       | 9.23 $\pm$ 0.06           | 9.11 $\pm$ 0.07           | 7.28 $\pm$ 0.05           | 4.56 $\pm$ 0.05           | 7.66 $\pm$ 0.05           | 4.93 $\pm$ 0.04           | 9.63 $\pm$ 0.14          
Dijkstra (ms)             | 8650.00 $\pm$ 40.00       | 56.90 $\pm$ 1.70          | 57.30 $\pm$ 0.30          | 49.50 $\pm$ 0.30          | 45.10 $\pm$ 0.40          | 60.30 $\pm$ 0.30          | 67.90 $\pm$ 0.80          | 64.40 $\pm$ 0.30         

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 3.24                      | 2.81                      | 0.56                      | 1.64                      | 1.45                      | 1.80                      | 1.66                     
Bellman Ford              | -                         | 4.58                      | 4.46                      | 1.53                      | 2.95                      | 2.85                      | 3.34                      | 3.45                     
Dijkstra                  | -                         | 3.59                      | 3.89                      | 1.84                      | 3.02                      | 2.84                      | 3.19                      | 3.34                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 498.00 $\pm$ 18.00        | 8.62 $\pm$ 0.28           | 9.30 $\pm$ 0.12           | 31.50 $\pm$ 1.10          | 2.35 $\pm$ 0.08           | 2.40 $\pm$ 0.08           | 20.50 $\pm$ 0.70          | 4.90 $\pm$ 0.11          
Bellman Ford (ms)         | 3400.00 $\pm$ 100.00      | 7.21 $\pm$ 0.23           | 7.23 $\pm$ 0.32           | 7.72 $\pm$ 0.18           | 5.32 $\pm$ 0.12           | 10.30 $\pm$ 0.10          | 5.35 $\pm$ 0.11           | 9.77 $\pm$ 0.41          
Dijkstra (ms)             | 8710.00 $\pm$ 220.00      | 54.80 $\pm$ 1.80          | 57.60 $\pm$ 2.30          | 56.90 $\pm$ 2.90          | 48.00 $\pm$ 0.80          | 69.60 $\pm$ 1.60          | 64.10 $\pm$ 1.90          | 70.90 $\pm$ 2.30         

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 3.18                      | 2.54                      | 0.50                      | 1.59                      | 1.50                      | 1.88                      | 1.76                     
Bellman Ford              | -                         | 4.31                      | 4.27                      | 1.55                      | 2.97                      | 2.70                      | 3.26                      | 3.78                     
Dijkstra                  | -                         | 3.35                      | 3.48                      | 1.56                      | 2.83                      | 2.73                      | 3.23                      | 3.62                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 525.00 $\pm$ 17.00        | 3.37 $\pm$ 0.20           | 3.32 $\pm$ 0.14           | 17.70 $\pm$ 1.10          | 2.67 $\pm$ 0.10           | 2.78 $\pm$ 0.00           | 9.81 $\pm$ 0.25           | 5.47 $\pm$ 0.19          
Bellman Ford (ms)         | 3370.00 $\pm$ 110.00      | 9.47 $\pm$ 0.47           | 10.10 $\pm$ 0.50          | 7.72 $\pm$ 0.32           | 4.87 $\pm$ 0.16           | 7.98 $\pm$ 0.43           | 5.00 $\pm$ 0.00           | 9.85 $\pm$ 0.22          
Dijkstra (ms)             | 8700.00 $\pm$ 290.00      | 53.40 $\pm$ 2.20          | 56.20 $\pm$ 2.00          | 46.70 $\pm$ 1.70          | 43.10 $\pm$ 0.50          | 58.90 $\pm$ 3.10          | 61.80 $\pm$ 0.60          | 63.10 $\pm$ 3.40         

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
