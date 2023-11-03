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
### Performance Comparison (as of Fri Nov  3 21:23:18 UTC 2023)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.59                      | 0.41                      | 1.34                      | 1.29                     
Bellman Ford              | -                         | 3.74                      | 1.28                      | 2.31                      | 2.26                     
Dijkstra                  | -                         | 2.94                      | 1.43                      | 2.43                      | 2.32                     
Euler                     | -                         | 3.33                      | 1.95                      | 2.28                      | 2.32                     
Midpoint Explicit         | -                         | 3.81                      | 2.64                      | 2.63                      | 2.68                     
Midpoint Fixed            | -                         | 4.38                      | 2.80                      | 2.73                      | 2.72                     
RK4                       | -                         | 4.97                      | 3.17                      | 3.40                      | 3.30                     
FD - L Convection         | -                         | 2.86                      | 1.02                      | 2.24                      | 2.25                     
FD - NL Convection        | -                         | 3.58                      | 1.10                      | 2.22                      | 2.30                     
FD - Poisson              | -                         | 3.74                      | 1.60                      | 2.39                      | 2.45                     
FD - Laplace              | -                         | 7.56                      | 3.00                      | 2.82                      | 2.91                     
M-D                       | -                         | 7.66                      | 3.46                      | 3.40                      | 3.12                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 444.00                    | 8.02                      | 28.00                     | 2.98                      | 3.30                     
Bellman Ford (ms)         | 2900.00                   | 7.71                      | 6.36                      | 3.83                      | 6.44                     
Dijkstra (ms)             | 7390.00                   | 47.40                     | 43.10                     | 35.50                     | 50.90                    
Euler (ms)                | 4710.00                   | 42.40                     | 112.00                    | 19.60                     | 241.00                   
Midpoint Explicit (ms)    | 9480.00                   | 86.50                     | 224.00                    | 30.40                     | 475.00                   
Midpoint Fixed (s)        | 51.60                     | 0.68                      | 1.10                      | 0.10                      | 2.38                     
RK4 (ms)                  | 23700.00                  | 199.00                    | 385.00                    | 45.30                     | 777.00                   
FD - L Convection (ms)    | 3030.00                   | 2.86                      | 3.39                      | 1.77                      | 2.81                     
FD - NL Convection (ms)   | 3890.00                   | 3.42                      | 3.36                      | 1.75                      | 2.88                     
FD - Poisson (ms)         | 9020.00                   | 5.68                      | 9.72                      | 3.69                      | 4.96                     
FD - Laplace (ms)         | 742.00                    | 234.00                    | 374.00                    | 75.50                     | 416.00                   
M-D (ms)                  | 19500.00                  | 52.90                     | 73.60                     | 106.00                    | 110.00                   

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.8 results
### Performance Comparison (as of 1.10.0)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.98                      | 0.39                      | 1.22                      | 1.18                     
Bellman Ford              | -                         | 3.33                      | 1.22                      | 2.18                      | 2.13                     
Dijkstra                  | -                         | 2.55                      | 1.35                      | 2.25                      | 2.16                     
Euler                     | -                         | 2.93                      | 1.81                      | 2.11                      | 2.14                     
Midpoint Explicit         | -                         | 3.33                      | 2.54                      | 2.48                      | 2.50                     
Midpoint Fixed            | -                         | 3.83                      | 2.69                      | 2.51                      | 2.55                     
RK4                       | -                         | 4.24                      | 3.01                      | 3.08                      | 3.07                     
FD - L Convection         | -                         | 2.36                      | 0.96                      | 2.05                      | 2.07                     
FD - NL Convection        | -                         | 3.09                      | 1.03                      | 2.09                      | 2.13                     
FD - Poisson              | -                         | 3.39                      | 1.49                      | 2.25                      | 2.27                     
FD - Laplace              | -                         | 6.72                      | 2.87                      | 2.68                      | 2.73                     
M-D                       | -                         | 6.98                      | 3.38                      | 3.20                      | 2.94                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 402.00 $\pm$ 1.00         | 9.90 $\pm$ 0.03           | 27.50 $\pm$ 0.80          | 3.20 $\pm$ 0.00           | 3.26 $\pm$ 0.00          
Bellman Ford (ms)         | 2600.00 $\pm$ 10.00       | 6.73 $\pm$ 0.00           | 6.34 $\pm$ 0.02           | 4.45 $\pm$ 0.00           | 6.57 $\pm$ 0.01          
Dijkstra (ms)             | 6880.00 $\pm$ 20.00       | 39.40 $\pm$ 0.40          | 34.10 $\pm$ 0.70          | 31.60 $\pm$ 1.70          | 49.10 $\pm$ 0.70         
Euler (ms)                | 4930.00 $\pm$ 80.00       | 41.50 $\pm$ 11.00         | 108.00 $\pm$ 0.00         | 18.80 $\pm$ 0.90          | 205.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 10100.00 $\pm$ 200.00     | 76.10 $\pm$ 0.40          | 214.00 $\pm$ 9.00         | 29.00 $\pm$ 0.60          | 404.00 $\pm$ 5.00        
Midpoint Fixed (s)        | 50.70 $\pm$ 0.30          | 0.60 $\pm$ 0.01           | 1.09 $\pm$ 0.02           | 0.10 $\pm$ 0.00           | 2.01 $\pm$ 0.08          
RK4 (ms)                  | 25300.00 $\pm$ 200.00     | 218.00 $\pm$ 1.00         | 411.00 $\pm$ 10.00        | 42.40 $\pm$ 2.60          | 671.00 $\pm$ 9.00        
FD - L Convection (ms)    | 3080.00 $\pm$ 20.00       | 2.81 $\pm$ 0.00           | 3.19 $\pm$ 0.15           | 1.63 $\pm$ 0.02           | 2.48 $\pm$ 0.06          
FD - NL Convection (ms)   | 3870.00 $\pm$ 10.00       | 3.08 $\pm$ 0.00           | 3.36 $\pm$ 0.06           | 1.64 $\pm$ 0.01           | 2.53 $\pm$ 0.00          
FD - Poisson (ms)         | 8920.00 $\pm$ 220.00      | 5.78 $\pm$ 0.00           | 10.20 $\pm$ 0.30          | 4.20 $\pm$ 0.01           | 5.30 $\pm$ 0.01          
FD - Laplace (ms)         | 731.00 $\pm$ 5.00         | 251.00 $\pm$ 1.00         | 390.00 $\pm$ 5.00         | 78.50 $\pm$ 1.60          | 316.00 $\pm$ 2.00        
M-D (ms)                  | 20800.00 $\pm$ 100.00     | 65.20 $\pm$ 0.00          | 79.50 $\pm$ 1.40          | 120.00 $\pm$ 0.00         | 122.00 $\pm$ 0.00        

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.10.0)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.37                      | 0.52                      | 1.41                      | 1.35                     
Bellman Ford              | -                         | 3.81                      | 1.36                      | 2.42                      | 2.35                     
Dijkstra                  | -                         | 3.01                      | 1.67                      | 2.54                      | 2.52                     
Euler                     | -                         | 3.73                      | 2.22                      | 2.58                      | 2.58                     
Midpoint Explicit         | -                         | 4.43                      | 3.23                      | 3.08                      | 3.07                     
Midpoint Fixed            | -                         | 5.26                      | 3.47                      | 3.26                      | 3.39                     
RK4                       | -                         | 5.83                      | 3.85                      | 4.04                      | 3.76                     
FD - L Convection         | -                         | 3.19                      | 1.29                      | 2.61                      | 2.72                     
FD - NL Convection        | -                         | 4.07                      | 1.40                      | 2.68                      | 2.69                     
FD - Poisson              | -                         | 4.57                      | 1.97                      | 2.89                      | 2.92                     
FD - Laplace              | -                         | 9.17                      | 3.64                      | 3.46                      | 3.55                     
M-D                       | -                         | 9.06                      | 4.12                      | 4.18                      | 3.96                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 434.00 $\pm$ 12.00        | 8.21 $\pm$ 0.19           | 28.50 $\pm$ 2.40          | 2.15 $\pm$ 0.10           | 2.17 $\pm$ 0.06          
Bellman Ford (ms)         | 3090.00 $\pm$ 120.00      | 7.94 $\pm$ 0.37           | 7.17 $\pm$ 0.32           | 4.85 $\pm$ 0.16           | 8.81 $\pm$ 0.15          
Dijkstra (ms)             | 8050.00 $\pm$ 320.00      | 43.70 $\pm$ 1.90          | 44.30 $\pm$ 1.80          | 38.90 $\pm$ 6.90          | 54.40 $\pm$ 2.40         
Euler (ms)                | 5210.00 $\pm$ 350.00      | 52.50 $\pm$ 2.10          | 130.00 $\pm$ 5.00         | 28.40 $\pm$ 1.30          | 276.00 $\pm$ 5.00        
Midpoint Explicit (ms)    | 10700.00 $\pm$ 300.00     | 108.00 $\pm$ 8.00         | 246.00 $\pm$ 7.00         | 46.60 $\pm$ 1.80          | 513.00 $\pm$ 9.00        
Midpoint Fixed (s)        | 57.50 $\pm$ 2.20          | 0.81 $\pm$ 0.05           | 1.31 $\pm$ 0.03           | 0.15 $\pm$ 0.00           | 2.68 $\pm$ 0.03          
RK4 (ms)                  | 28500.00 $\pm$ 700.00     | 252.00 $\pm$ 5.00         | 474.00 $\pm$ 16.00        | 61.30 $\pm$ 3.20          | 879.00 $\pm$ 17.00       
FD - L Convection (ms)    | 3940.00 $\pm$ 70.00       | 3.94 $\pm$ 0.19           | 4.18 $\pm$ 0.13           | 2.37 $\pm$ 0.14           | 3.51 $\pm$ 0.14          
FD - NL Convection (ms)   | 4850.00 $\pm$ 70.00       | 4.67 $\pm$ 0.32           | 4.46 $\pm$ 0.13           | 2.67 $\pm$ 0.16           | 3.87 $\pm$ 0.17          
FD - Poisson (ms)         | 10300.00 $\pm$ 200.00     | 14.10 $\pm$ 0.40          | 14.40 $\pm$ 0.30          | 7.66 $\pm$ 0.28           | 10.10 $\pm$ 0.20         
FD - Laplace (ms)         | 1160.00 $\pm$ 10.00       | 383.00 $\pm$ 10.00        | 554.00 $\pm$ 8.00         | 170.00 $\pm$ 3.00         | 496.00 $\pm$ 8.00        
M-D (ms)                  | 22600.00 $\pm$ 700.00     | 74.70 $\pm$ 1.80          | 103.00 $\pm$ 2.00         | 134.00 $\pm$ 7.00         | 137.00 $\pm$ 5.00        

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.10.0)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 3.31                      | 0.56                      | 1.78                      | 1.63                     
Bellman Ford              | -                         | 4.51                      | 1.62                      | 2.83                      | 2.82                     
Dijkstra                  | -                         | 3.62                      | 1.81                      | 2.92                      | 2.78                     
Euler                     | -                         | 4.07                      | 2.46                      | 2.55                      | 2.73                     
Midpoint Explicit         | -                         | 4.58                      | 3.50                      | 3.10                      | 3.33                     
Midpoint Fixed            | -                         | 5.46                      | 3.45                      | 2.97                      | 3.03                     
RK4                       | -                         | 5.93                      | 4.16                      | 3.95                      | 3.96                     
FD - L Convection         | -                         | 3.12                      | 1.16                      | 2.51                      | 2.60                     
FD - NL Convection        | -                         | 4.27                      | 1.38                      | 2.39                      | 2.62                     
FD - Poisson              | -                         | 4.41                      | 1.83                      | 2.96                      | 2.92                     
FD - Laplace              | -                         | 8.39                      | 3.61                      | 3.42                      | 3.23                     
M-D                       | -                         | 10.14                     | 4.57                      | 3.62                      | 3.33                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 509.00 $\pm$ 21.00        | 9.03 $\pm$ 0.37           | 32.50 $\pm$ 2.10          | 2.46 $\pm$ 0.06           | 2.50 $\pm$ 0.06          
Bellman Ford (ms)         | 3260.00 $\pm$ 70.00       | 9.04 $\pm$ 0.43           | 7.99 $\pm$ 0.18           | 5.60 $\pm$ 0.44           | 10.50 $\pm$ 0.60         
Dijkstra (ms)             | 8670.00 $\pm$ 230.00      | 46.20 $\pm$ 1.20          | 48.90 $\pm$ 2.50          | 39.00 $\pm$ 1.80          | 58.40 $\pm$ 1.30         
Euler (ms)                | 5530.00 $\pm$ 240.00      | 55.80 $\pm$ 1.50          | 130.00 $\pm$ 8.00         | 28.40 $\pm$ 1.80          | 281.00 $\pm$ 17.00       
Midpoint Explicit (ms)    | 11500.00 $\pm$ 700.00     | 109.00 $\pm$ 3.00         | 261.00 $\pm$ 12.00        | 47.20 $\pm$ 1.30          | 551.00 $\pm$ 25.00       
Midpoint Fixed (s)        | 56.90 $\pm$ 2.20          | 0.79 $\pm$ 0.01           | 1.32 $\pm$ 0.05           | 0.14 $\pm$ 0.01           | 2.66 $\pm$ 0.06          
RK4 (ms)                  | 27500.00 $\pm$ 1400.00    | 258.00 $\pm$ 16.00        | 482.00 $\pm$ 21.00        | 61.10 $\pm$ 4.10          | 912.00 $\pm$ 36.00       
FD - L Convection (ms)    | 3420.00 $\pm$ 160.00      | 3.67 $\pm$ 0.20           | 4.02 $\pm$ 0.19           | 2.70 $\pm$ 0.21           | 3.38 $\pm$ 0.26          
FD - NL Convection (ms)   | 4600.00 $\pm$ 250.00      | 4.65 $\pm$ 0.61           | 4.33 $\pm$ 0.15           | 2.65 $\pm$ 0.16           | 3.72 $\pm$ 0.26          
FD - Poisson (ms)         | 10400.00 $\pm$ 200.00     | 12.70 $\pm$ 0.40          | 14.40 $\pm$ 0.70          | 7.58 $\pm$ 0.34           | 10.80 $\pm$ 0.70         
FD - Laplace (ms)         | 1180.00 $\pm$ 40.00       | 358.00 $\pm$ 12.00        | 557.00 $\pm$ 16.00        | 170.00 $\pm$ 6.00         | 494.00 $\pm$ 12.00       
M-D (ms)                  | 23000.00 $\pm$ 800.00     | 76.20 $\pm$ 2.60          | 105.00 $\pm$ 4.00         | 128.00 $\pm$ 7.00         | 131.00 $\pm$ 8.00        

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.10.0)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.58                      | 0.35                      | 1.39                      | 1.30                     
Bellman Ford              | -                         | 3.64                      | 1.22                      | 2.34                      | 2.25                     
Dijkstra                  | -                         | 2.82                      | 1.36                      | 2.43                      | 2.37                     
Euler                     | -                         | 3.14                      | 1.77                      | 2.27                      | 2.27                     
Midpoint Explicit         | -                         | 3.55                      | 2.39                      | 2.60                      | 2.65                     
Midpoint Fixed            | -                         | 4.25                      | 2.64                      | 2.71                      | 2.73                     
RK4                       | -                         | 4.69                      | 2.91                      | 3.20                      | 3.18                     
FD - L Convection         | -                         | 2.66                      | 0.99                      | 2.17                      | 2.22                     
FD - NL Convection        | -                         | 3.53                      | 1.01                      | 2.26                      | 2.28                     
FD - Poisson              | -                         | 3.73                      | 1.47                      | 2.35                      | 2.42                     
FD - Laplace              | -                         | 7.39                      | 2.75                      | 2.79                      | 2.87                     
M-D                       | -                         | 7.45                      | 3.27                      | 3.26                      | 3.08                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 550.00 $\pm$ 25.00        | 8.04 $\pm$ 0.03           | 28.10 $\pm$ 0.20          | 2.98 $\pm$ 0.01           | 3.31 $\pm$ 0.01          
Bellman Ford (ms)         | 2880.00 $\pm$ 20.00       | 7.72 $\pm$ 0.01           | 6.36 $\pm$ 0.01           | 3.85 $\pm$ 0.00           | 6.49 $\pm$ 0.01          
Dijkstra (ms)             | 7250.00 $\pm$ 50.00       | 46.90 $\pm$ 0.40          | 40.80 $\pm$ 1.00          | 36.40 $\pm$ 0.70          | 50.90 $\pm$ 0.90         
Euler (ms)                | 4580.00 $\pm$ 120.00      | 41.20 $\pm$ 0.40          | 111.00 $\pm$ 1.00         | 19.50 $\pm$ 0.60          | 241.00 $\pm$ 3.00        
Midpoint Explicit (ms)    | 9370.00 $\pm$ 170.00      | 85.30 $\pm$ 0.70          | 207.00 $\pm$ 1.00         | 29.70 $\pm$ 0.70          | 479.00 $\pm$ 2.00        
Midpoint Fixed (s)        | 45.70 $\pm$ 0.40          | 0.67 $\pm$ 0.00           | 1.05 $\pm$ 0.02           | 0.10 $\pm$ 0.01           | 2.38 $\pm$ 0.02          
RK4 (ms)                  | 23100.00 $\pm$ 200.00     | 199.00 $\pm$ 1.00         | 383.00 $\pm$ 1.00         | 46.10 $\pm$ 0.90          | 776.00 $\pm$ 5.00        
FD - L Convection (ms)    | 2990.00 $\pm$ 40.00       | 2.87 $\pm$ 0.02           | 3.29 $\pm$ 0.09           | 1.77 $\pm$ 0.01           | 2.57 $\pm$ 0.22          
FD - NL Convection (ms)   | 3720.00 $\pm$ 30.00       | 3.36 $\pm$ 0.02           | 3.49 $\pm$ 0.14           | 1.81 $\pm$ 0.03           | 2.61 $\pm$ 0.09          
FD - Poisson (ms)         | 8590.00 $\pm$ 80.00       | 5.69 $\pm$ 0.00           | 9.76 $\pm$ 0.02           | 3.74 $\pm$ 0.02           | 4.93 $\pm$ 0.02          
FD - Laplace (ms)         | 779.00 $\pm$ 4.00         | 234.00 $\pm$ 1.00         | 384.00 $\pm$ 4.00         | 76.00 $\pm$ 1.30          | 417.00 $\pm$ 2.00        
M-D (ms)                  | 18500.00 $\pm$ 400.00     | 52.90 $\pm$ 0.00          | 74.10 $\pm$ 0.60          | 106.00 $\pm$ 0.00         | 110.00 $\pm$ 0.00        

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
