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
Ackermann                 | -                         | 2.14                      | 2.32                      | 0.42                      | 1.38                      | 1.30                      | 1.45                      | 1.44                     
Bellman Ford              | -                         | 4.15                      | 4.46                      | 1.29                      | 2.31                      | 2.27                      | 2.51                      | 2.33                     
Dijkstra                  | -                         | 2.81                      | 3.25                      | 1.48                      | 2.41                      | 2.30                      | 2.58                      | 2.35                     
Euler                     | -                         | 3.22                      | 3.63                      | 1.90                      | 2.28                      | 2.33                      | 2.56                      | 2.35                     
Midpoint Explicit         | -                         | 3.70                      | 4.21                      | 2.64                      | 2.66                      | 2.67                      | 2.86                      | 2.65                     
Midpoint Fixed            | -                         | 4.17                      | 4.96                      | 2.79                      | 2.70                      | 2.76                      | 2.93                      | 2.69                     
RK4                       | -                         | 4.67                      | 5.12                      | 3.15                      | 3.29                      | 3.26                      | 3.56                      | 3.25                     
FD - L Convection         | -                         | 2.59                      | 2.96                      | 1.03                      | 2.22                      | 2.24                      | 2.45                      | 2.25                     
FD - NL Convection        | -                         | 3.91                      | 4.14                      | 1.07                      | 2.21                      | 2.29                      | 2.52                      | 2.24                     
FD - Poisson              | -                         | 3.99                      | 4.50                      | 1.58                      | 2.38                      | 2.40                      | 2.74                      | 2.26                     
FD - Laplace              | -                         | 7.97                      | 9.33                      | 2.97                      | 2.89                      | 2.96                      | 3.03                      | 2.81                     
M-D                       | -                         | 8.51                      | 7.55                      | 3.57                      | 3.47                      | 3.19                      | 3.85                      | 3.13                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 476.00 $\pm$ 4.00         | 8.03 $\pm$ 0.01           | 11.70 $\pm$ 0.00          | 28.20 $\pm$ 0.20          | 3.17 $\pm$ 0.01           | 2.95 $\pm$ 0.02           | 21.70 $\pm$ 0.00          | 11.90 $\pm$ 0.00         
Bellman Ford (ms)         | 2850.00 $\pm$ 10.00       | 6.16 $\pm$ 0.00           | 5.15 $\pm$ 0.00           | 6.12 $\pm$ 0.01           | 3.85 $\pm$ 0.00           | 6.48 $\pm$ 0.00           | 4.18 $\pm$ 0.01           | 6.85 $\pm$ 0.01          
Dijkstra (ms)             | 7440.00 $\pm$ 50.00       | 43.50 $\pm$ 0.50          | 36.80 $\pm$ 0.30          | 44.10 $\pm$ 0.40          | 39.60 $\pm$ 0.30          | 52.70 $\pm$ 0.90          | 60.20 $\pm$ 0.90          | 55.00 $\pm$ 0.10         
Euler (ms)                | 4790.00 $\pm$ 90.00       | 41.50 $\pm$ 0.40          | 41.10 $\pm$ 0.40          | 114.00 $\pm$ 2.00         | 22.00 $\pm$ 0.80          | 241.00 $\pm$ 4.00         | 13.90 $\pm$ 0.10          | 295.00 $\pm$ 5.00        
Midpoint Explicit (ms)    | 9720.00 $\pm$ 170.00      | 87.50 $\pm$ 0.30          | 88.70 $\pm$ 1.90          | 211.00 $\pm$ 1.00         | 35.20 $\pm$ 1.90          | 472.00 $\pm$ 3.00         | 31.60 $\pm$ 0.50          | 580.00 $\pm$ 4.00        
Midpoint Fixed (s)        | 48.50 $\pm$ 0.70          | 0.67 $\pm$ 0.02           | 0.50 $\pm$ 0.00           | 1.05 $\pm$ 0.01           | 0.10 $\pm$ 0.00           | 2.35 $\pm$ 0.02           | 0.13 $\pm$ 0.00           | 2.89 $\pm$ 0.03          
RK4 (ms)                  | 23400.00 $\pm$ 400.00     | 181.00 $\pm$ 2.00         | 162.00 $\pm$ 1.00         | 383.00 $\pm$ 2.00         | 46.30 $\pm$ 1.80          | 765.00 $\pm$ 3.00         | 102.00 $\pm$ 2.00         | 847.00 $\pm$ 5.00        
FD - L Convection (ms)    | 3430.00 $\pm$ 140.00      | 1.95 $\pm$ 0.02           | 2.08 $\pm$ 0.01           | 3.32 $\pm$ 0.11           | 1.80 $\pm$ 0.06           | 2.69 $\pm$ 0.17           | 1.32 $\pm$ 0.18           | 8.43 $\pm$ 0.04          
FD - NL Convection (ms)   | 4250.00 $\pm$ 170.00      | 1.98 $\pm$ 0.02           | 1.98 $\pm$ 0.02           | 3.42 $\pm$ 0.07           | 1.83 $\pm$ 0.08           | 2.75 $\pm$ 0.15           | 1.06 $\pm$ 0.02           | 9.23 $\pm$ 0.03          
FD - Poisson (ms)         | 8770.00 $\pm$ 220.00      | 3.85 $\pm$ 0.00           | 3.57 $\pm$ 0.01           | 9.82 $\pm$ 0.07           | 3.70 $\pm$ 0.00           | 4.89 $\pm$ 0.03           | 3.64 $\pm$ 0.06           | 12.20 $\pm$ 0.00         
FD - Laplace (ms)         | 764.00 $\pm$ 8.00         | 122.00 $\pm$ 2.00         | 336.00 $\pm$ 2.00         | 381.00 $\pm$ 3.00         | 77.20 $\pm$ 2.30          | 393.00 $\pm$ 1.00         | 65.80 $\pm$ 2.00          | 1430.00 $\pm$ 0.00       
M-D (ms)                  | 19500.00 $\pm$ 300.00     | 55.30 $\pm$ 0.20          | 64.80 $\pm$ 0.30          | 74.60 $\pm$ 0.60          | 106.00 $\pm$ 1.00         | 110.00 $\pm$ 0.00         | 155.00 $\pm$ 2.00         | 109.00 $\pm$ 2.00        

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.89                      | 3.20                      | 0.59                      | 1.71                      | 1.64                      | 1.89                      | 1.89                     
Bellman Ford              | -                         | 5.10                      | 6.00                      | 1.63                      | 2.97                      | 2.96                      | 3.03                      | 2.74                     
Dijkstra                  | -                         | 3.71                      | 4.24                      | 1.89                      | 3.10                      | 2.99                      | 3.25                      | 2.89                     
Euler                     | -                         | 4.10                      | 5.10                      | 2.79                      | 2.92                      | 3.06                      | 3.42                      | 2.79                     
Midpoint Explicit         | -                         | 5.04                      | 6.16                      | 3.60                      | 3.60                      | 3.43                      | 3.59                      | 3.23                     
Midpoint Fixed            | -                         | 5.87                      | 7.29                      | 3.94                      | 3.66                      | 3.63                      | 4.20                      | 3.48                     
RK4                       | -                         | 6.48                      | 7.72                      | 4.47                      | 4.50                      | 4.41                      | 5.06                      | 4.23                     
FD - L Convection         | -                         | 3.79                      | 4.59                      | 1.49                      | 3.25                      | 2.97                      | 3.36                      | 2.91                     
FD - NL Convection        | -                         | 5.91                      | 6.30                      | 1.45                      | 3.19                      | 3.09                      | 3.44                      | 2.99                     
FD - Poisson              | -                         | 5.82                      | 6.75                      | 2.17                      | 3.19                      | 3.10                      | 3.78                      | 2.93                     
FD - Laplace              | -                         | 11.29                     | 13.77                     | 4.01                      | 4.11                      | 4.16                      | 4.34                      | 3.74                     
M-D                       | -                         | 11.58                     | 10.48                     | 4.69                      | 4.66                      | 4.18                      | 5.08                      | 3.85                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 535.00 $\pm$ 22.00        | 9.79 $\pm$ 0.33           | 4.71 $\pm$ 0.13           | 32.90 $\pm$ 1.50          | 2.51 $\pm$ 0.19           | 2.48 $\pm$ 0.12           | 21.20 $\pm$ 1.00          | 4.69 $\pm$ 0.17          
Bellman Ford (ms)         | 3500.00 $\pm$ 90.00       | 7.76 $\pm$ 0.37           | 7.24 $\pm$ 0.33           | 7.76 $\pm$ 0.34           | 5.46 $\pm$ 0.29           | 10.60 $\pm$ 0.40          | 5.45 $\pm$ 0.15           | 10.30 $\pm$ 0.40         
Dijkstra (ms)             | 9280.00 $\pm$ 170.00      | 52.40 $\pm$ 2.10          | 41.10 $\pm$ 1.10          | 54.00 $\pm$ 2.60          | 47.30 $\pm$ 3.50          | 72.90 $\pm$ 3.10          | 67.40 $\pm$ 2.10          | 79.00 $\pm$ 5.00         
Euler (ms)                | 6030.00 $\pm$ 190.00      | 51.10 $\pm$ 3.20          | 59.00 $\pm$ 4.80          | 137.00 $\pm$ 11.00        | 25.90 $\pm$ 1.90          | 295.00 $\pm$ 18.00        | 16.50 $\pm$ 1.10          | 278.00 $\pm$ 17.00       
Midpoint Explicit (ms)    | 12200.00 $\pm$ 400.00     | 114.00 $\pm$ 10.00        | 122.00 $\pm$ 12.00        | 290.00 $\pm$ 9.00         | 45.20 $\pm$ 1.10          | 583.00 $\pm$ 19.00        | 32.60 $\pm$ 1.80          | 581.00 $\pm$ 15.00       
Midpoint Fixed (s)        | 64.30 $\pm$ 2.30          | 0.94 $\pm$ 0.15           | 0.67 $\pm$ 0.05           | 1.43 $\pm$ 0.05           | 0.15 $\pm$ 0.01           | 2.95 $\pm$ 0.08           | 0.10 $\pm$ 0.00           | 2.96 $\pm$ 0.06          
RK4 (ms)                  | 31100.00 $\pm$ 400.00     | 255.00 $\pm$ 14.00        | 78.20 $\pm$ 2.30          | 524.00 $\pm$ 24.00        | 62.30 $\pm$ 2.30          | 1020.00 $\pm$ 40.00       | 82.80 $\pm$ 4.00          | 915.00 $\pm$ 21.00       
FD - L Convection (ms)    | 4290.00 $\pm$ 60.00       | 3.63 $\pm$ 0.07           | 3.36 $\pm$ 0.36           | 4.81 $\pm$ 0.12           | 3.31 $\pm$ 0.38           | 5.19 $\pm$ 0.48           | 2.32 $\pm$ 0.08           | 10.40 $\pm$ 0.30         
FD - NL Convection (ms)   | 5380.00 $\pm$ 70.00       | 3.86 $\pm$ 0.18           | 3.47 $\pm$ 0.13           | 5.12 $\pm$ 0.19           | 3.33 $\pm$ 0.20           | 6.31 $\pm$ 0.49           | 2.46 $\pm$ 0.14           | 12.20 $\pm$ 0.30         
FD - Poisson (ms)         | 11200.00 $\pm$ 100.00     | 8.41 $\pm$ 0.26           | 11.40 $\pm$ 0.40          | 15.20 $\pm$ 0.70          | 8.97 $\pm$ 0.28           | 12.30 $\pm$ 0.40          | 8.70 $\pm$ 0.22           | 16.20 $\pm$ 0.40         
FD - Laplace (ms)         | 1250.00 $\pm$ 20.00       | 283.00 $\pm$ 8.00         | 374.00 $\pm$ 10.00        | 593.00 $\pm$ 19.00        | 201.00 $\pm$ 5.00         | 594.00 $\pm$ 15.00        | 216.00 $\pm$ 7.00         | 754.00 $\pm$ 15.00       
M-D (ms)                  | 24200.00 $\pm$ 300.00     | 75.30 $\pm$ 1.70          | 95.30 $\pm$ 2.20          | 108.00 $\pm$ 3.00         | 145.00 $\pm$ 7.00         | 150.00 $\pm$ 5.00         | 111.00 $\pm$ 4.00         | 145.00 $\pm$ 7.00        

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 3.35                      | 3.39                      | 0.57                      | 1.70                      | 1.61                      | 1.81                      | 1.80                     
Bellman Ford              | -                         | 5.61                      | 6.24                      | 1.63                      | 3.11                      | 3.15                      | 3.35                      | 2.84                     
Dijkstra                  | -                         | 3.91                      | 4.53                      | 1.93                      | 3.08                      | 3.05                      | 3.35                      | 2.88                     
Euler                     | -                         | 4.42                      | 5.19                      | 2.54                      | 2.92                      | 2.97                      | 3.23                      | 2.90                     
Midpoint Explicit         | -                         | 5.17                      | 6.04                      | 3.52                      | 3.34                      | 3.44                      | 3.68                      | 3.34                     
Midpoint Fixed            | -                         | 5.73                      | 6.94                      | 3.71                      | 3.50                      | 3.53                      | 3.81                      | 3.42                     
RK4                       | -                         | 6.74                      | 7.66                      | 4.26                      | 4.35                      | 4.27                      | 4.59                      | 4.08                     
FD - L Convection         | -                         | 3.85                      | 4.41                      | 1.41                      | 2.87                      | 2.86                      | 3.20                      | 2.69                     
FD - NL Convection        | -                         | 5.60                      | 6.11                      | 1.51                      | 2.94                      | 2.99                      | 3.22                      | 2.73                     
FD - Poisson              | -                         | 5.66                      | 6.61                      | 2.11                      | 3.11                      | 3.20                      | 3.60                      | 2.88                     
FD - Laplace              | -                         | 11.03                     | 13.44                     | 3.99                      | 3.72                      | 3.77                      | 4.03                      | 3.63                     
M-D                       | -                         | 11.37                     | 10.56                     | 4.90                      | 4.42                      | 3.99                      | 4.94                      | 3.81                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 531.00 $\pm$ 9.00         | 9.49 $\pm$ 0.35           | 4.60 $\pm$ 0.12           | 32.60 $\pm$ 0.60          | 2.52 $\pm$ 0.04           | 2.52 $\pm$ 0.05           | 21.70 $\pm$ 0.80          | 5.19 $\pm$ 0.09          
Bellman Ford (ms)         | 3600.00 $\pm$ 50.00       | 8.12 $\pm$ 0.14           | 7.20 $\pm$ 0.22           | 7.88 $\pm$ 0.20           | 5.51 $\pm$ 0.23           | 10.80 $\pm$ 0.40          | 5.40 $\pm$ 0.11           | 10.00 $\pm$ 0.20         
Dijkstra (ms)             | 9370.00 $\pm$ 250.00      | 53.90 $\pm$ 1.60          | 41.70 $\pm$ 1.20          | 59.60 $\pm$ 3.50          | 43.60 $\pm$ 1.30          | 67.30 $\pm$ 3.80          | 60.50 $\pm$ 1.90          | 66.90 $\pm$ 5.40         
Euler (ms)                | 6400.00 $\pm$ 230.00      | 51.20 $\pm$ 2.60          | 52.20 $\pm$ 1.60          | 142.00 $\pm$ 6.00         | 28.20 $\pm$ 0.80          | 302.00 $\pm$ 7.00         | 12.50 $\pm$ 0.50          | 288.00 $\pm$ 10.00       
Midpoint Explicit (ms)    | 13300.00 $\pm$ 600.00     | 103.00 $\pm$ 9.00         | 110.00 $\pm$ 6.00         | 277.00 $\pm$ 6.00         | 45.20 $\pm$ 4.10          | 582.00 $\pm$ 11.00        | 30.00 $\pm$ 1.10          | 567.00 $\pm$ 13.00       
Midpoint Fixed (s)        | 66.30 $\pm$ 3.40          | 0.85 $\pm$ 0.02           | 0.63 $\pm$ 0.08           | 1.38 $\pm$ 0.03           | 0.14 $\pm$ 0.00           | 2.90 $\pm$ 0.05           | 0.09 $\pm$ 0.00           | 2.82 $\pm$ 0.05          
RK4 (ms)                  | 31600.00 $\pm$ 900.00     | 242.00 $\pm$ 5.00         | 77.00 $\pm$ 2.30          | 511.00 $\pm$ 8.00         | 60.10 $\pm$ 2.00          | 994.00 $\pm$ 19.00        | 80.70 $\pm$ 2.20          | 897.00 $\pm$ 16.00       
FD - L Convection (ms)    | 3990.00 $\pm$ 30.00       | 3.01 $\pm$ 0.19           | 3.22 $\pm$ 0.33           | 4.64 $\pm$ 0.13           | 3.07 $\pm$ 0.29           | 4.68 $\pm$ 0.55           | 2.21 $\pm$ 0.03           | 10.20 $\pm$ 0.20         
FD - NL Convection (ms)   | 4930.00 $\pm$ 40.00       | 3.62 $\pm$ 0.19           | 3.30 $\pm$ 0.31           | 4.96 $\pm$ 0.18           | 3.37 $\pm$ 0.29           | 5.75 $\pm$ 0.64           | 2.38 $\pm$ 0.05           | 12.10 $\pm$ 0.30         
FD - Poisson (ms)         | 11200.00 $\pm$ 100.00     | 7.98 $\pm$ 0.26           | 11.00 $\pm$ 0.20          | 14.80 $\pm$ 0.80          | 8.56 $\pm$ 0.21           | 11.80 $\pm$ 0.10          | 8.52 $\pm$ 0.12           | 15.70 $\pm$ 0.50         
FD - Laplace (ms)         | 1090.00 $\pm$ 180.00      | 269.00 $\pm$ 6.00         | 357.00 $\pm$ 8.00         | 568.00 $\pm$ 10.00        | 192.00 $\pm$ 6.00         | 564.00 $\pm$ 4.00         | 203.00 $\pm$ 5.00         | 719.00 $\pm$ 10.00       
M-D (ms)                  | 25500.00 $\pm$ 500.00     | 73.10 $\pm$ 1.60          | 95.50 $\pm$ 3.90          | 104.00 $\pm$ 2.00         | 139.00 $\pm$ 2.00         | 145.00 $\pm$ 3.00         | 105.00 $\pm$ 1.00         | 144.00 $\pm$ 3.00        

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.60                      | 2.53                      | 0.36                      | 1.37                      | 1.28                      | 1.49                      | 1.51                     
Bellman Ford              | -                         | 4.25                      | 4.48                      | 1.18                      | 2.35                      | 2.27                      | 2.58                      | 2.36                     
Dijkstra                  | -                         | 3.35                      | 3.28                      | 1.33                      | 2.44                      | 2.33                      | 2.68                      | 2.37                     
Euler                     | -                         | 3.32                      | 3.77                      | 1.72                      | 2.27                      | 2.30                      | 2.58                      | 2.35                     
Midpoint Explicit         | -                         | 3.70                      | 4.21                      | 2.39                      | 2.70                      | 2.66                      | 3.03                      | 2.67                     
Midpoint Fixed            | -                         | 4.26                      | 5.07                      | 2.56                      | 2.70                      | 2.74                      | 2.96                      | 2.73                     
RK4                       | -                         | 4.81                      | 5.32                      | 2.86                      | 3.22                      | 3.21                      | 3.52                      | 3.23                     
FD - L Convection         | -                         | 2.81                      | 3.19                      | 0.96                      | 2.24                      | 2.27                      | 2.54                      | 2.27                     
FD - NL Convection        | -                         | 4.23                      | 4.35                      | 1.02                      | 2.26                      | 2.33                      | 2.54                      | 2.27                     
FD - Poisson              | -                         | 4.08                      | 4.74                      | 1.42                      | 2.42                      | 2.44                      | 2.82                      | 2.35                     
FD - Laplace              | -                         | 8.27                      | 9.52                      | 2.67                      | 2.84                      | 2.91                      | 3.08                      | 2.81                     
M-D                       | -                         | 8.27                      | 7.18                      | 3.27                      | 3.32                      | 3.07                      | 3.74                      | 3.01                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 415.00 $\pm$ 6.00         | 8.03 $\pm$ 0.01           | 11.70 $\pm$ 0.00          | 28.10 $\pm$ 0.20          | 3.17 $\pm$ 0.00           | 2.95 $\pm$ 0.00           | 21.70 $\pm$ 0.00          | 11.80 $\pm$ 0.00         
Bellman Ford (ms)         | 2720.00 $\pm$ 30.00       | 6.13 $\pm$ 0.00           | 5.13 $\pm$ 0.02           | 6.11 $\pm$ 0.00           | 3.84 $\pm$ 0.01           | 6.45 $\pm$ 0.01           | 4.14 $\pm$ 0.00           | 6.81 $\pm$ 0.01          
Dijkstra (ms)             | 7130.00 $\pm$ 60.00       | 57.00 $\pm$ 0.90          | 51.90 $\pm$ 3.90          | 59.00 $\pm$ 0.60          | 52.70 $\pm$ 0.80          | 69.40 $\pm$ 1.60          | 77.20 $\pm$ 0.70          | 71.00 $\pm$ 0.50         
Euler (ms)                | 4670.00 $\pm$ 50.00       | 42.90 $\pm$ 3.30          | 40.70 $\pm$ 0.80          | 113.00 $\pm$ 1.00         | 21.20 $\pm$ 1.00          | 257.00 $\pm$ 5.00         | 12.70 $\pm$ 0.30          | 314.00 $\pm$ 5.00        
Midpoint Explicit (ms)    | 9590.00 $\pm$ 180.00      | 86.60 $\pm$ 0.40          | 91.40 $\pm$ 0.60          | 215.00 $\pm$ 5.00         | 39.50 $\pm$ 2.00          | 513.00 $\pm$ 4.00         | 32.40 $\pm$ 1.70          | 623.00 $\pm$ 8.00        
Midpoint Fixed (s)        | 47.80 $\pm$ 0.90          | 0.68 $\pm$ 0.02           | 0.52 $\pm$ 0.02           | 1.06 $\pm$ 0.02           | 0.11 $\pm$ 0.01           | 2.51 $\pm$ 0.08           | 0.13 $\pm$ 0.00           | 3.01 $\pm$ 0.05          
RK4 (ms)                  | 23100.00 $\pm$ 300.00     | 185.00 $\pm$ 6.00         | 164.00 $\pm$ 2.00         | 388.00 $\pm$ 6.00         | 47.00 $\pm$ 0.90          | 809.00 $\pm$ 3.00         | 102.00 $\pm$ 1.00         | 900.00 $\pm$ 18.00       
FD - L Convection (ms)    | 2970.00 $\pm$ 70.00       | 1.48 $\pm$ 0.02           | 1.93 $\pm$ 0.01           | 3.31 $\pm$ 0.10           | 1.75 $\pm$ 0.02           | 2.55 $\pm$ 0.09           | 0.97 $\pm$ 0.02           | 8.42 $\pm$ 0.04          
FD - NL Convection (ms)   | 3690.00 $\pm$ 30.00       | 1.98 $\pm$ 0.02           | 1.95 $\pm$ 0.02           | 3.37 $\pm$ 0.09           | 1.80 $\pm$ 0.03           | 2.63 $\pm$ 0.22           | 1.16 $\pm$ 0.00           | 9.23 $\pm$ 0.03          
FD - Poisson (ms)         | 8620.00 $\pm$ 100.00      | 3.86 $\pm$ 0.01           | 3.59 $\pm$ 0.01           | 9.89 $\pm$ 0.12           | 3.75 $\pm$ 0.01           | 4.94 $\pm$ 0.01           | 3.47 $\pm$ 0.01           | 12.20 $\pm$ 0.00         
FD - Laplace (ms)         | 704.00 $\pm$ 6.00         | 122.00 $\pm$ 2.00         | 332.00 $\pm$ 2.00         | 381.00 $\pm$ 3.00         | 75.60 $\pm$ 1.60          | 417.00 $\pm$ 2.00         | 64.40 $\pm$ 2.90          | 1430.00 $\pm$ 0.00       
M-D (ms)                  | 18000.00 $\pm$ 200.00     | 55.20 $\pm$ 0.00          | 63.40 $\pm$ 0.30          | 73.20 $\pm$ 0.80          | 106.00 $\pm$ 0.00         | 110.00 $\pm$ 0.00         | 146.00 $\pm$ 1.00         | 109.00 $\pm$ 0.00        

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
