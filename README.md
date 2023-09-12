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
Ackermann                 | -                         | 2.57                      | 2.34                      | 0.51                      | 1.62                      | 1.50                      | 1.75                      | 1.66                     
Bellman Ford              | -                         | 4.17                      | 4.27                      | 1.47                      | 2.68                      | 2.64                      | 2.95                      | 2.69                     
Dijkstra                  | -                         | 3.27                      | 3.20                      | 1.70                      | 2.90                      | 2.74                      | 3.05                      | 2.82                     
Euler                     | -                         | 3.62                      | 3.64                      | 2.21                      | 2.65                      | 2.69                      | 2.94                      | 2.73                     
Midpoint Explicit         | -                         | 4.18                      | 4.14                      | 3.08                      | 3.11                      | 3.12                      | 3.40                      | 3.17                     
Midpoint Fixed            | -                         | 4.76                      | 4.69                      | 3.27                      | 3.18                      | 3.19                      | 3.43                      | 3.13                     
RK4                       | -                         | 5.44                      | 5.46                      | 3.81                      | 3.91                      | 3.82                      | 4.30                      | 3.89                     
FD - L Convection         | -                         | 3.10                      | 3.07                      | 1.22                      | 2.62                      | 2.68                      | 2.92                      | 2.57                     
FD - NL Convection        | -                         | 3.97                      | 3.96                      | 1.29                      | 2.61                      | 2.72                      | 2.96                      | 2.70                     
FD - Poisson              | -                         | 4.19                      | 4.28                      | 1.86                      | 2.85                      | 2.89                      | 3.24                      | 2.67                     
FD - Laplace              | -                         | 8.59                      | 8.58                      | 3.48                      | 3.56                      | 3.49                      | 3.63                      | 3.34                     
M-D                       | -                         | 8.69                      | 8.73                      | 4.08                      | 4.05                      | 3.69                      | 4.53                      | 3.66                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 524.00 $\pm$ 4.00         | 3.20 $\pm$ 0.04           | 3.19 $\pm$ 0.01           | 16.60 $\pm$ 0.30          | 2.55 $\pm$ 0.00           | 2.52 $\pm$ 0.02           | 9.61 $\pm$ 0.01           | 4.54 $\pm$ 0.02          
Bellman Ford (ms)         | 3420.00 $\pm$ 10.00       | 9.26 $\pm$ 0.01           | 9.27 $\pm$ 0.02           | 7.33 $\pm$ 0.00           | 4.60 $\pm$ 0.00           | 7.75 $\pm$ 0.05           | 4.98 $\pm$ 0.01           | 8.17 $\pm$ 0.06          
Dijkstra (ms)             | 8900.00 $\pm$ 30.00       | 60.70 $\pm$ 0.30          | 57.00 $\pm$ 1.00          | 49.10 $\pm$ 0.30          | 46.20 $\pm$ 0.20          | 61.30 $\pm$ 1.50          | 73.40 $\pm$ 5.50          | 66.60 $\pm$ 1.10         
Euler (ms)                | 5770.00 $\pm$ 120.00      | 52.00 $\pm$ 0.50          | 52.30 $\pm$ 1.00          | 134.00 $\pm$ 1.00         | 24.30 $\pm$ 1.00          | 284.00 $\pm$ 5.00         | 14.70 $\pm$ 0.20          | 350.00 $\pm$ 7.00        
Midpoint Explicit (ms)    | 11800.00 $\pm$ 200.00     | 105.00 $\pm$ 1.00         | 106.00 $\pm$ 1.00         | 253.00 $\pm$ 2.00         | 45.90 $\pm$ 0.70          | 559.00 $\pm$ 5.00         | 42.50 $\pm$ 0.20          | 690.00 $\pm$ 6.00        
Midpoint Fixed (s)        | 58.90 $\pm$ 0.90          | 0.80 $\pm$ 0.02           | 0.80 $\pm$ 0.00           | 1.26 $\pm$ 0.01           | 0.12 $\pm$ 0.01           | 2.78 $\pm$ 0.03           | 0.15 $\pm$ 0.00           | 3.47 $\pm$ 0.06          
RK4 (ms)                  | 27800.00 $\pm$ 400.00     | 239.00 $\pm$ 2.00         | 240.00 $\pm$ 2.00         | 460.00 $\pm$ 3.00         | 55.00 $\pm$ 0.80          | 912.00 $\pm$ 8.00         | 121.00 $\pm$ 1.00         | 1010.00 $\pm$ 10.00      
FD - L Convection (ms)    | 4050.00 $\pm$ 140.00      | 3.99 $\pm$ 0.18           | 3.97 $\pm$ 0.14           | 4.16 $\pm$ 0.19           | 2.11 $\pm$ 0.08           | 3.22 $\pm$ 0.19           | 1.65 $\pm$ 0.28           | 10.10 $\pm$ 0.00         
FD - NL Convection (ms)   | 5190.00 $\pm$ 230.00      | 4.76 $\pm$ 0.02           | 4.68 $\pm$ 0.21           | 4.08 $\pm$ 0.10           | 2.19 $\pm$ 0.08           | 3.23 $\pm$ 0.18           | 1.37 $\pm$ 0.04           | 11.10 $\pm$ 0.10         
FD - Poisson (ms)         | 10500.00 $\pm$ 200.00     | 6.76 $\pm$ 0.06           | 6.79 $\pm$ 0.11           | 12.00 $\pm$ 0.10          | 4.44 $\pm$ 0.00           | 5.89 $\pm$ 0.04           | 4.63 $\pm$ 0.07           | 14.60 $\pm$ 0.00         
FD - Laplace (ms)         | 938.00 $\pm$ 15.00        | 278.00 $\pm$ 1.00         | 279.00 $\pm$ 2.00         | 458.00 $\pm$ 4.00         | 92.20 $\pm$ 2.20          | 479.00 $\pm$ 4.00         | 86.90 $\pm$ 2.60          | 1710.00 $\pm$ 0.00       
M-D (ms)                  | 22900.00 $\pm$ 400.00     | 63.50 $\pm$ 0.00          | 63.90 $\pm$ 1.00          | 88.10 $\pm$ 0.30          | 128.00 $\pm$ 2.00         | 132.00 $\pm$ 1.00         | 198.00 $\pm$ 2.00         | 130.00 $\pm$ 1.00        

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.38                      | 2.17                      | 0.45                      | 1.60                      | 1.45                      | 1.70                      | 1.62                     
Bellman Ford              | -                         | 3.93                      | 3.88                      | 1.42                      | 2.54                      | 2.50                      | 2.82                      | 2.47                     
Dijkstra                  | -                         | 2.91                      | 2.96                      | 1.48                      | 2.69                      | 2.40                      | 2.98                      | 2.52                     
Euler                     | -                         | 3.53                      | 3.48                      | 2.05                      | 2.51                      | 2.50                      | 2.87                      | 2.66                     
Midpoint Explicit         | -                         | 4.18                      | 3.96                      | 2.92                      | 3.07                      | 3.02                      | 3.40                      | 3.22                     
Midpoint Fixed            | -                         | 4.37                      | 4.41                      | 3.19                      | 2.92                      | 2.91                      | 3.45                      | 3.09                     
RK4                       | -                         | 5.30                      | 5.26                      | 3.57                      | 3.75                      | 3.71                      | 3.99                      | 3.70                     
FD - L Convection         | -                         | 3.04                      | 3.10                      | 1.24                      | 2.59                      | 2.66                      | 2.88                      | 2.62                     
FD - NL Convection        | -                         | 3.77                      | 3.94                      | 1.19                      | 2.54                      | 2.60                      | 2.73                      | 2.53                     
FD - Poisson              | -                         | 4.59                      | 4.37                      | 1.85                      | 3.07                      | 2.91                      | 3.25                      | 2.66                     
FD - Laplace              | -                         | 8.93                      | 8.66                      | 3.51                      | 3.39                      | 3.42                      | 3.33                      | 3.09                     
M-D                       | -                         | 8.02                      | 8.13                      | 3.80                      | 4.14                      | 3.75                      | 4.82                      | 3.97                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 433.00 $\pm$ 13.00        | 2.93 $\pm$ 0.10           | 2.84 $\pm$ 0.09           | 16.70 $\pm$ 0.50          | 2.55 $\pm$ 0.01           | 2.78 $\pm$ 0.05           | 8.03 $\pm$ 0.04           | 4.50 $\pm$ 0.10          
Bellman Ford (ms)         | 3160.00 $\pm$ 100.00      | 8.65 $\pm$ 0.31           | 8.85 $\pm$ 0.22           | 7.03 $\pm$ 0.23           | 4.16 $\pm$ 0.19           | 7.25 $\pm$ 0.28           | 4.60 $\pm$ 0.14           | 7.55 $\pm$ 0.21          
Dijkstra (ms)             | 8580.00 $\pm$ 200.00      | 51.80 $\pm$ 1.30          | 52.60 $\pm$ 1.30          | 43.20 $\pm$ 1.70          | 40.50 $\pm$ 1.20          | 54.00 $\pm$ 1.30          | 60.80 $\pm$ 1.50          | 59.30 $\pm$ 1.20         
Euler (ms)                | 5440.00 $\pm$ 130.00      | 49.50 $\pm$ 1.50          | 49.10 $\pm$ 1.40          | 130.00 $\pm$ 3.00         | 22.70 $\pm$ 0.80          | 274.00 $\pm$ 10.00        | 9.87 $\pm$ 0.52           | 340.00 $\pm$ 8.00        
Midpoint Explicit (ms)    | 11500.00 $\pm$ 400.00     | 96.50 $\pm$ 2.20          | 96.00 $\pm$ 1.30          | 248.00 $\pm$ 6.00         | 34.20 $\pm$ 0.90          | 562.00 $\pm$ 13.00        | 38.10 $\pm$ 0.60          | 694.00 $\pm$ 20.00       
Midpoint Fixed (s)        | 54.60 $\pm$ 1.20          | 0.72 $\pm$ 0.02           | 0.74 $\pm$ 0.03           | 1.20 $\pm$ 0.05           | 0.12 $\pm$ 0.01           | 2.60 $\pm$ 0.09           | 0.15 $\pm$ 0.00           | 3.17 $\pm$ 0.04          
RK4 (ms)                  | 25800.00 $\pm$ 700.00     | 233.00 $\pm$ 3.00         | 240.00 $\pm$ 11.00        | 438.00 $\pm$ 7.00         | 53.40 $\pm$ 1.00          | 887.00 $\pm$ 29.00        | 119.00 $\pm$ 5.00         | 962.00 $\pm$ 13.00       
FD - L Convection (ms)    | 3940.00 $\pm$ 60.00       | 3.46 $\pm$ 0.07           | 3.99 $\pm$ 0.04           | 4.00 $\pm$ 0.25           | 2.17 $\pm$ 0.06           | 3.22 $\pm$ 0.12           | 1.72 $\pm$ 0.09           | 10.10 $\pm$ 0.10         
FD - NL Convection (ms)   | 4870.00 $\pm$ 140.00      | 4.25 $\pm$ 0.27           | 4.00 $\pm$ 0.14           | 3.94 $\pm$ 0.12           | 1.95 $\pm$ 0.12           | 3.18 $\pm$ 0.12           | 1.21 $\pm$ 0.05           | 10.90 $\pm$ 0.10         
FD - Poisson (ms)         | 10400.00 $\pm$ 300.00     | 6.96 $\pm$ 0.30           | 7.01 $\pm$ 0.30           | 11.90 $\pm$ 0.20          | 4.52 $\pm$ 0.20           | 5.91 $\pm$ 0.19           | 4.37 $\pm$ 0.16           | 14.50 $\pm$ 0.10         
FD - Laplace (ms)         | 909.00 $\pm$ 34.00        | 279.00 $\pm$ 3.00         | 282.00 $\pm$ 1.00         | 456.00 $\pm$ 4.00         | 91.70 $\pm$ 2.60          | 482.00 $\pm$ 22.00        | 72.80 $\pm$ 4.50          | 1670.00 $\pm$ 50.00      
M-D (ms)                  | 21600.00 $\pm$ 700.00     | 61.60 $\pm$ 1.60          | 60.50 $\pm$ 1.60          | 84.50 $\pm$ 3.70          | 128.00 $\pm$ 1.00         | 133.00 $\pm$ 3.00         | 203.00 $\pm$ 6.00         | 140.00 $\pm$ 4.00        

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.55                      | 2.19                      | 0.41                      | 1.30                      | 1.24                      | 1.43                      | 1.40                     
Bellman Ford              | -                         | 3.65                      | 3.62                      | 1.23                      | 2.28                      | 2.24                      | 2.46                      | 2.29                     
Dijkstra                  | -                         | 2.88                      | 2.81                      | 1.38                      | 2.37                      | 2.27                      | 2.53                      | 2.28                     
Euler                     | -                         | 3.23                      | 3.22                      | 1.83                      | 2.23                      | 2.26                      | 2.49                      | 2.29                     
Midpoint Explicit         | -                         | 3.59                      | 3.69                      | 2.55                      | 2.55                      | 2.58                      | 2.81                      | 2.57                     
Midpoint Fixed            | -                         | 4.21                      | 4.16                      | 2.71                      | 2.63                      | 2.68                      | 2.89                      | 2.64                     
RK4                       | -                         | 4.72                      | 4.70                      | 3.11                      | 3.24                      | 3.20                      | 3.51                      | 3.19                     
FD - L Convection         | -                         | 2.72                      | 2.72                      | 1.00                      | 2.20                      | 2.19                      | 2.46                      | 2.16                     
FD - NL Convection        | -                         | 3.44                      | 3.48                      | 1.06                      | 2.22                      | 2.24                      | 2.47                      | 2.15                     
FD - Poisson              | -                         | 3.73                      | 3.70                      | 1.60                      | 2.39                      | 2.42                      | 2.74                      | 2.29                     
FD - Laplace              | -                         | 7.46                      | 7.42                      | 2.95                      | 2.83                      | 2.89                      | 3.12                      | 2.88                     
M-D                       | -                         | 7.58                      | 7.58                      | 3.43                      | 3.36                      | 3.07                      | 3.71                      | 3.02                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 444.00 $\pm$ 2.00         | 8.02 $\pm$ 0.01           | 8.03 $\pm$ 0.02           | 28.10 $\pm$ 0.20          | 3.10 $\pm$ 0.01           | 2.95 $\pm$ 0.00           | 17.10 $\pm$ 0.10          | 11.80 $\pm$ 0.00         
Bellman Ford (ms)         | 2860.00 $\pm$ 50.00       | 7.71 $\pm$ 0.00           | 7.72 $\pm$ 0.01           | 6.13 $\pm$ 0.01           | 3.86 $\pm$ 0.01           | 6.47 $\pm$ 0.01           | 4.17 $\pm$ 0.00           | 6.82 $\pm$ 0.01          
Dijkstra (ms)             | 7430.00 $\pm$ 40.00       | 49.90 $\pm$ 1.20          | 50.40 $\pm$ 0.70          | 46.30 $\pm$ 0.60          | 46.50 $\pm$ 3.40          | 59.50 $\pm$ 0.60          | 57.40 $\pm$ 0.70          | 56.80 $\pm$ 0.80         
Euler (ms)                | 4950.00 $\pm$ 130.00      | 41.70 $\pm$ 0.50          | 41.70 $\pm$ 0.30          | 111.00 $\pm$ 1.00         | 19.10 $\pm$ 0.60          | 238.00 $\pm$ 3.00         | 8.04 $\pm$ 0.33           | 292.00 $\pm$ 3.00        
Midpoint Explicit (ms)    | 10100.00 $\pm$ 200.00     | 87.60 $\pm$ 0.60          | 87.40 $\pm$ 0.60          | 213.00 $\pm$ 5.00         | 37.20 $\pm$ 2.50          | 473.00 $\pm$ 4.00         | 34.50 $\pm$ 0.60          | 582.00 $\pm$ 4.00        
Midpoint Fixed (s)        | 50.00 $\pm$ 1.20          | 0.66 $\pm$ 0.00           | 0.66 $\pm$ 0.00           | 1.05 $\pm$ 0.01           | 0.10 $\pm$ 0.00           | 2.35 $\pm$ 0.02           | 0.12 $\pm$ 0.00           | 2.90 $\pm$ 0.03          
RK4 (ms)                  | 25000.00 $\pm$ 600.00     | 199.00 $\pm$ 2.00         | 199.00 $\pm$ 3.00         | 385.00 $\pm$ 6.00         | 45.30 $\pm$ 2.80          | 772.00 $\pm$ 11.00        | 100.00 $\pm$ 1.00         | 853.00 $\pm$ 5.00        
FD - L Convection (ms)    | 3210.00 $\pm$ 30.00       | 2.86 $\pm$ 0.03           | 2.85 $\pm$ 0.02           | 3.34 $\pm$ 0.09           | 1.77 $\pm$ 0.04           | 2.55 $\pm$ 0.15           | 1.25 $\pm$ 0.15           | 8.38 $\pm$ 0.03          
FD - NL Convection (ms)   | 3960.00 $\pm$ 20.00       | 3.53 $\pm$ 0.02           | 3.51 $\pm$ 0.05           | 3.48 $\pm$ 0.19           | 1.84 $\pm$ 0.08           | 2.62 $\pm$ 0.18           | 1.15 $\pm$ 0.00           | 9.24 $\pm$ 0.03          
FD - Poisson (ms)         | 8930.00 $\pm$ 80.00       | 5.69 $\pm$ 0.01           | 5.70 $\pm$ 0.02           | 9.81 $\pm$ 0.04           | 3.74 $\pm$ 0.01           | 4.95 $\pm$ 0.05           | 3.47 $\pm$ 0.02           | 12.20 $\pm$ 0.00         
FD - Laplace (ms)         | 731.00 $\pm$ 6.00         | 233.00 $\pm$ 2.00         | 235.00 $\pm$ 1.00         | 381.00 $\pm$ 3.00         | 76.10 $\pm$ 1.80          | 418.00 $\pm$ 1.00         | 66.10 $\pm$ 2.90          | 1430.00 $\pm$ 10.00      
M-D (ms)                  | 19900.00 $\pm$ 400.00     | 53.00 $\pm$ 0.00          | 52.90 $\pm$ 0.00          | 74.30 $\pm$ 0.30          | 106.00 $\pm$ 0.00         | 110.00 $\pm$ 1.00         | 146.00 $\pm$ 4.00         | 108.00 $\pm$ 0.00        

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.9.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.55                      | 2.13                      | 0.36                      | 1.33                      | 1.27                      | 1.47                      | 1.44                     
Bellman Ford              | -                         | 3.54                      | 3.54                      | 1.17                      | 2.34                      | 2.25                      | 2.53                      | 2.31                     
Dijkstra                  | -                         | 2.73                      | 2.76                      | 1.30                      | 2.40                      | 2.29                      | 2.57                      | 2.31                     
Euler                     | -                         | 3.25                      | 3.26                      | 1.75                      | 2.34                      | 2.33                      | 2.61                      | 2.39                     
Midpoint Explicit         | -                         | 3.72                      | 3.70                      | 2.47                      | 2.67                      | 2.68                      | 2.91                      | 2.73                     
Midpoint Fixed            | -                         | 4.07                      | 4.09                      | 2.54                      | 2.69                      | 2.72                      | 2.90                      | 2.67                     
RK4                       | -                         | 4.62                      | 4.66                      | 2.88                      | 3.25                      | 3.30                      | 3.62                      | 3.36                     
FD - L Convection         | -                         | 2.81                      | 2.76                      | 0.97                      | 2.24                      | 2.32                      | 2.54                      | 2.28                     
FD - NL Convection        | -                         | 3.49                      | 3.49                      | 0.99                      | 2.24                      | 2.30                      | 2.53                      | 2.28                     
FD - Poisson              | -                         | 3.58                      | 3.58                      | 1.42                      | 2.37                      | 2.43                      | 2.74                      | 2.28                     
FD - Laplace              | -                         | 7.35                      | 7.44                      | 2.70                      | 2.88                      | 2.94                      | 3.06                      | 2.81                     
M-D                       | -                         | 7.45                      | 7.36                      | 3.25                      | 3.27                      | 3.01                      | 3.64                      | 2.98                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 419.00 $\pm$ 9.00         | 8.29 $\pm$ 1.02           | 8.02 $\pm$ 0.01           | 28.20 $\pm$ 0.20          | 3.10 $\pm$ 0.01           | 3.31 $\pm$ 0.01           | 21.70 $\pm$ 0.00          | 11.90 $\pm$ 0.00         
Bellman Ford (ms)         | 2730.00 $\pm$ 30.00       | 7.72 $\pm$ 0.01           | 7.72 $\pm$ 0.02           | 6.12 $\pm$ 0.00           | 3.84 $\pm$ 0.00           | 6.46 $\pm$ 0.01           | 4.17 $\pm$ 0.01           | 6.84 $\pm$ 0.01          
Dijkstra (ms)             | 7140.00 $\pm$ 60.00       | 46.90 $\pm$ 0.60          | 46.90 $\pm$ 0.20          | 40.90 $\pm$ 0.60          | 43.10 $\pm$ 3.70          | 49.50 $\pm$ 0.30          | 55.70 $\pm$ 0.60          | 54.40 $\pm$ 0.30         
Euler (ms)                | 4710.00 $\pm$ 90.00       | 43.80 $\pm$ 0.40          | 44.50 $\pm$ 2.20          | 115.00 $\pm$ 4.00         | 21.80 $\pm$ 0.60          | 237.00 $\pm$ 4.00         | 9.04 $\pm$ 0.31           | 292.00 $\pm$ 4.00        
Midpoint Explicit (ms)    | 9500.00 $\pm$ 110.00      | 84.80 $\pm$ 0.40          | 84.50 $\pm$ 0.50          | 208.00 $\pm$ 1.00         | 31.20 $\pm$ 0.60          | 484.00 $\pm$ 26.00        | 32.30 $\pm$ 0.30          | 577.00 $\pm$ 4.00        
Midpoint Fixed (s)        | 46.80 $\pm$ 0.50          | 0.68 $\pm$ 0.03           | 0.67 $\pm$ 0.02           | 1.05 $\pm$ 0.01           | 0.10 $\pm$ 0.00           | 2.35 $\pm$ 0.02           | 0.12 $\pm$ 0.00           | 2.88 $\pm$ 0.03          
RK4 (ms)                  | 23800.00 $\pm$ 1100.00    | 199.00 $\pm$ 1.00         | 201.00 $\pm$ 3.00         | 383.00 $\pm$ 2.00         | 46.60 $\pm$ 0.50          | 768.00 $\pm$ 5.00         | 102.00 $\pm$ 1.00         | 853.00 $\pm$ 8.00        
FD - L Convection (ms)    | 2970.00 $\pm$ 70.00       | 2.81 $\pm$ 0.01           | 2.80 $\pm$ 0.01           | 3.42 $\pm$ 0.17           | 1.75 $\pm$ 0.02           | 2.55 $\pm$ 0.09           | 1.03 $\pm$ 0.03           | 8.44 $\pm$ 0.03          
FD - NL Convection (ms)   | 3700.00 $\pm$ 30.00       | 3.39 $\pm$ 0.01           | 3.38 $\pm$ 0.01           | 3.46 $\pm$ 0.11           | 1.79 $\pm$ 0.02           | 2.61 $\pm$ 0.22           | 1.05 $\pm$ 0.02           | 9.22 $\pm$ 0.03          
FD - Poisson (ms)         | 8650.00 $\pm$ 190.00      | 6.06 $\pm$ 0.01           | 5.69 $\pm$ 0.01           | 9.77 $\pm$ 0.06           | 3.71 $\pm$ 0.01           | 4.92 $\pm$ 0.04           | 3.57 $\pm$ 0.05           | 12.20 $\pm$ 0.00         
FD - Laplace (ms)         | 735.00 $\pm$ 15.00        | 232.00 $\pm$ 1.00         | 234.00 $\pm$ 2.00         | 380.00 $\pm$ 2.00         | 76.40 $\pm$ 2.00          | 418.00 $\pm$ 2.00         | 65.20 $\pm$ 1.60          | 1430.00 $\pm$ 10.00      
M-D (ms)                  | 18200.00 $\pm$ 500.00     | 52.90 $\pm$ 0.00          | 53.00 $\pm$ 0.00          | 73.40 $\pm$ 0.30          | 106.00 $\pm$ 0.00         | 110.00 $\pm$ 0.00         | 153.00 $\pm$ 1.00         | 109.00 $\pm$ 1.00        

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
