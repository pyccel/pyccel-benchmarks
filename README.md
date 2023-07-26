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
### Performance Comparison (as of Wed Jul 26 14:17:43 UTC 2023)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.60                      | 0.40                      | 1.29                      | 1.26                     
Bellman Ford              | -                         | 3.62                      | 1.23                      | 2.26                      | 2.20                     
Dijkstra                  | -                         | 2.78                      | 1.37                      | 2.31                      | 2.20                     
Euler                     | -                         | 3.16                      | 1.84                      | 2.18                      | 2.22                     
Midpoint Explicit         | -                         | 3.56                      | 2.54                      | 2.53                      | 2.54                     
Midpoint Fixed            | -                         | 4.40                      | 2.86                      | 2.68                      | 2.72                     
RK4                       | -                         | 5.03                      | 3.24                      | 3.35                      | 3.29                     
FD - L Convection         | -                         | 2.83                      | 1.04                      | 2.25                      | 2.24                     
FD - NL Convection        | -                         | 3.69                      | 1.12                      | 2.27                      | 2.26                     
FD - Poisson              | -                         | 3.84                      | 1.60                      | 2.46                      | 2.46                     
FD - Laplace              | -                         | 7.75                      | 3.05                      | 2.90                      | 2.92                     
M-D                       | -                         | 7.80                      | 3.49                      | 3.37                      | 3.12                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 453.00                    | 8.01                      | 28.40                     | 3.08                      | 2.94                     
Bellman Ford (ms)         | 2870.00                   | 7.71                      | 6.36                      | 3.83                      | 6.47                     
Dijkstra (ms)             | 7350.00                   | 46.10                     | 39.40                     | 34.50                     | 49.30                    
Euler (ms)                | 4820.00                   | 39.00                     | 111.00                    | 19.10                     | 236.00                   
Midpoint Explicit (ms)    | 9830.00                   | 79.50                     | 209.00                    | 27.70                     | 468.00                   
Midpoint Fixed (s)        | 49.70                     | 0.66                      | 1.04                      | 0.10                      | 2.32                     
RK4 (ms)                  | 24000.00                  | 207.00                    | 382.00                    | 45.70                     | 766.00                   
FD - L Convection (ms)    | 3070.00                   | 4.49                      | 3.27                      | 1.73                      | 2.48                     
FD - NL Convection (ms)   | 3920.00                   | 3.37                      | 3.38                      | 1.76                      | 2.85                     
FD - Poisson (ms)         | 9010.00                   | 5.68                      | 9.76                      | 3.69                      | 4.90                     
FD - Laplace (ms)         | 719.00                    | 233.00                    | 375.00                    | 73.60                     | 391.00                   
M-D (ms)                  | 19200.00                  | 53.00                     | 73.90                     | 106.00                    | 110.00                   

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.7 results
### Performance Comparison (as of 1.8.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.24                      | 0.37                      | 1.30                      | 1.33                     
Bellman Ford              | -                         | 3.38                      | 1.24                      | 2.32                      | 2.33                     
Dijkstra                  | -                         | 2.68                      | 1.37                      | 2.50                      | 2.28                     
Euler                     | -                         | 3.12                      | 1.88                      | 2.28                      | 2.25                     
Midpoint Explicit         | -                         | 3.50                      | 2.74                      | 2.59                      | 2.62                     
Midpoint Fixed            | -                         | 3.99                      | 2.94                      | 2.70                      | 2.76                     
RK4                       | -                         | 4.57                      | 3.34                      | 3.33                      | 3.30                     
FD - L Convection         | -                         | 2.55                      | 1.08                      | 2.16                      | 2.21                     
FD - NL Convection        | -                         | 3.36                      | 1.16                      | 2.22                      | 2.38                     
FD - Poisson              | -                         | 3.48                      | 1.60                      | 2.42                      | 2.43                     
FD - Laplace              | -                         | 7.28                      | 3.10                      | 2.89                      | 2.90                     
M-D                       | -                         | 6.97                      | 3.43                      | 3.25                      | 2.98                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 515.00 $\pm$ 6.00         | 7.90 $\pm$ 0.00           | 31.30 $\pm$ 0.40          | 3.09 $\pm$ 0.00           | 3.31 $\pm$ 0.03          
Bellman Ford (ms)         | 2810.00 $\pm$ 30.00       | 5.94 $\pm$ 0.04           | 9.70 $\pm$ 0.01           | 3.84 $\pm$ 0.00           | 6.46 $\pm$ 0.00          
Dijkstra (ms)             | 7820.00 $\pm$ 140.00      | 48.70 $\pm$ 1.40          | 43.10 $\pm$ 0.90          | 36.00 $\pm$ 0.50          | 49.60 $\pm$ 0.70         
Euler (ms)                | 5810.00 $\pm$ 110.00      | 44.80 $\pm$ 0.40          | 116.00 $\pm$ 1.00         | 19.90 $\pm$ 1.20          | 237.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 11800.00 $\pm$ 200.00     | 83.10 $\pm$ 0.40          | 291.00 $\pm$ 2.00         | 30.10 $\pm$ 0.90          | 468.00 $\pm$ 2.00        
Midpoint Fixed (s)        | 59.10 $\pm$ 1.30          | 0.68 $\pm$ 0.00           | 1.59 $\pm$ 0.02           | 0.10 $\pm$ 0.00           | 2.31 $\pm$ 0.01          
RK4 (ms)                  | 26600.00 $\pm$ 400.00     | 202.00 $\pm$ 1.00         | 584.00 $\pm$ 13.00        | 45.90 $\pm$ 0.90          | 776.00 $\pm$ 43.00       
FD - L Convection (ms)    | 3220.00 $\pm$ 70.00       | 2.90 $\pm$ 0.01           | 13.90 $\pm$ 0.00          | 1.75 $\pm$ 0.03           | 2.86 $\pm$ 0.11          
FD - NL Convection (ms)   | 4340.00 $\pm$ 50.00       | 3.43 $\pm$ 0.04           | 14.70 $\pm$ 0.00          | 1.69 $\pm$ 0.03           | 2.58 $\pm$ 0.01          
FD - Poisson (ms)         | 9540.00 $\pm$ 350.00      | 5.69 $\pm$ 0.01           | 18.70 $\pm$ 0.10          | 3.71 $\pm$ 0.01           | 4.90 $\pm$ 0.02          
FD - Laplace (ms)         | 743.00 $\pm$ 39.00        | 234.00 $\pm$ 1.00         | 386.00 $\pm$ 1.00         | 78.00 $\pm$ 2.50          | 417.00 $\pm$ 1.00        
M-D (ms)                  | 21800.00 $\pm$ 500.00     | 52.80 $\pm$ 0.00          | 88.00 $\pm$ 1.00          | 106.00 $\pm$ 0.00         | 110.00 $\pm$ 0.00        

![Python 3.7 compilation results](./version_specific_results/pypi_performance_37_compilation.svg)
![Python 3.7 execution results](./version_specific_results/pypi_performance_37_execution.svg)
## Python 3.8 results
### Performance Comparison (as of 1.8.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.68                      | 0.52                      | 1.61                      | 1.53                     
Bellman Ford              | -                         | 4.28                      | 1.53                      | 2.76                      | 2.74                     
Dijkstra                  | -                         | 3.27                      | 1.72                      | 2.88                      | 2.73                     
Euler                     | -                         | 3.74                      | 2.27                      | 2.77                      | 2.73                     
Midpoint Explicit         | -                         | 4.25                      | 3.18                      | 3.14                      | 3.25                     
Midpoint Fixed            | -                         | 4.98                      | 3.42                      | 3.26                      | 3.32                     
RK4                       | -                         | 5.55                      | 3.80                      | 3.98                      | 3.98                     
FD - L Convection         | -                         | 3.13                      | 1.26                      | 2.66                      | 2.69                     
FD - NL Convection        | -                         | 4.13                      | 1.32                      | 2.66                      | 2.74                     
FD - Poisson              | -                         | 4.30                      | 1.89                      | 2.87                      | 2.85                     
FD - Laplace              | -                         | 8.89                      | 3.64                      | 3.50                      | 3.55                     
M-D                       | -                         | 8.98                      | 4.16                      | 4.07                      | 3.80                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 557.00 $\pm$ 6.00         | 3.13 $\pm$ 0.04           | 17.50 $\pm$ 0.50          | 2.79 $\pm$ 0.08           | 2.89 $\pm$ 0.07          
Bellman Ford (ms)         | 3540.00 $\pm$ 40.00       | 9.53 $\pm$ 0.15           | 7.93 $\pm$ 0.23           | 4.75 $\pm$ 0.09           | 7.97 $\pm$ 0.15          
Dijkstra (ms)             | 9220.00 $\pm$ 60.00       | 56.90 $\pm$ 1.30          | 48.40 $\pm$ 1.70          | 45.10 $\pm$ 1.50          | 59.00 $\pm$ 2.10         
Euler (ms)                | 6010.00 $\pm$ 50.00       | 51.20 $\pm$ 1.20          | 139.00 $\pm$ 2.00         | 25.70 $\pm$ 0.80          | 289.00 $\pm$ 3.00        
Midpoint Explicit (ms)    | 12100.00 $\pm$ 100.00     | 101.00 $\pm$ 3.00         | 261.00 $\pm$ 6.00         | 36.70 $\pm$ 1.40          | 575.00 $\pm$ 8.00        
Midpoint Fixed (s)        | 60.80 $\pm$ 0.60          | 0.83 $\pm$ 0.02           | 1.31 $\pm$ 0.02           | 0.13 $\pm$ 0.01           | 2.83 $\pm$ 0.02          
RK4 (ms)                  | 29000.00 $\pm$ 300.00     | 252.00 $\pm$ 8.00         | 473.00 $\pm$ 5.00         | 56.20 $\pm$ 1.90          | 928.00 $\pm$ 14.00       
FD - L Convection (ms)    | 4160.00 $\pm$ 80.00       | 5.61 $\pm$ 0.13           | 4.25 $\pm$ 0.27           | 2.18 $\pm$ 0.15           | 3.33 $\pm$ 0.24          
FD - NL Convection (ms)   | 5170.00 $\pm$ 70.00       | 4.18 $\pm$ 0.06           | 4.31 $\pm$ 0.18           | 2.21 $\pm$ 0.13           | 3.10 $\pm$ 0.08          
FD - Poisson (ms)         | 10800.00 $\pm$ 100.00     | 7.04 $\pm$ 0.17           | 12.10 $\pm$ 0.20          | 4.58 $\pm$ 0.08           | 6.18 $\pm$ 0.15          
FD - Laplace (ms)         | 909.00 $\pm$ 15.00        | 290.00 $\pm$ 4.00         | 472.00 $\pm$ 5.00         | 95.50 $\pm$ 3.00          | 490.00 $\pm$ 8.00        
M-D (ms)                  | 23700.00 $\pm$ 200.00     | 65.20 $\pm$ 1.70          | 91.60 $\pm$ 1.60          | 132.00 $\pm$ 3.00         | 136.00 $\pm$ 4.00        

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.8.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.37                      | 0.46                      | 1.40                      | 1.29                     
Bellman Ford              | -                         | 3.78                      | 1.44                      | 2.46                      | 2.46                     
Dijkstra                  | -                         | 2.94                      | 1.56                      | 2.53                      | 2.33                     
Euler                     | -                         | 3.34                      | 2.04                      | 2.33                      | 2.35                     
Midpoint Explicit         | -                         | 3.76                      | 2.78                      | 2.69                      | 2.70                     
Midpoint Fixed            | -                         | 4.38                      | 3.02                      | 2.89                      | 2.80                     
RK4                       | -                         | 5.06                      | 3.41                      | 3.45                      | 3.38                     
FD - L Convection         | -                         | 2.82                      | 1.08                      | 2.32                      | 2.32                     
FD - NL Convection        | -                         | 3.66                      | 1.14                      | 2.35                      | 2.29                     
FD - Poisson              | -                         | 4.12                      | 2.03                      | 2.52                      | 2.51                     
FD - Laplace              | -                         | 7.76                      | 3.10                      | 3.00                      | 3.18                     
M-D                       | -                         | 7.89                      | 3.76                      | 3.55                      | 3.21                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 451.00 $\pm$ 14.00        | 7.94 $\pm$ 0.23           | 27.20 $\pm$ 0.70          | 2.09 $\pm$ 0.05           | 2.22 $\pm$ 0.12          
Bellman Ford (ms)         | 2910.00 $\pm$ 60.00       | 7.88 $\pm$ 0.41           | 7.20 $\pm$ 0.43           | 4.70 $\pm$ 0.19           | 8.96 $\pm$ 0.45          
Dijkstra (ms)             | 7600.00 $\pm$ 110.00      | 40.50 $\pm$ 2.10          | 43.10 $\pm$ 2.10          | 35.00 $\pm$ 1.70          | 51.90 $\pm$ 2.20         
Euler (ms)                | 5090.00 $\pm$ 210.00      | 50.80 $\pm$ 6.20          | 115.00 $\pm$ 5.00         | 24.70 $\pm$ 1.40          | 240.00 $\pm$ 12.00       
Midpoint Explicit (ms)    | 10200.00 $\pm$ 100.00     | 96.70 $\pm$ 3.90          | 223.00 $\pm$ 7.00         | 41.20 $\pm$ 3.10          | 468.00 $\pm$ 16.00       
Midpoint Fixed (s)        | 51.00 $\pm$ 0.50          | 0.79 $\pm$ 0.17           | 1.16 $\pm$ 0.02           | 0.13 $\pm$ 0.01           | 2.30 $\pm$ 0.07          
RK4 (ms)                  | 25100.00 $\pm$ 400.00     | 225.00 $\pm$ 11.00        | 415.00 $\pm$ 14.00        | 52.10 $\pm$ 2.10          | 779.00 $\pm$ 25.00       
FD - L Convection (ms)    | 3470.00 $\pm$ 40.00       | 3.35 $\pm$ 0.06           | 3.89 $\pm$ 0.16           | 2.47 $\pm$ 0.12           | 2.98 $\pm$ 0.22          
FD - NL Convection (ms)   | 4300.00 $\pm$ 40.00       | 4.04 $\pm$ 0.06           | 4.20 $\pm$ 0.31           | 2.44 $\pm$ 0.17           | 3.38 $\pm$ 0.34          
FD - Poisson (ms)         | 9460.00 $\pm$ 340.00      | 13.40 $\pm$ 0.50          | 13.40 $\pm$ 0.80          | 7.17 $\pm$ 0.15           | 9.67 $\pm$ 0.28          
FD - Laplace (ms)         | 1040.00 $\pm$ 20.00       | 347.00 $\pm$ 9.00         | 522.00 $\pm$ 14.00        | 166.00 $\pm$ 8.00         | 467.00 $\pm$ 11.00       
M-D (ms)                  | 20300.00 $\pm$ 400.00     | 68.00 $\pm$ 3.50          | 99.70 $\pm$ 4.50          | 121.00 $\pm$ 4.00         | 124.00 $\pm$ 3.00        

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.8.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.58                      | 0.41                      | 1.33                      | 1.25                     
Bellman Ford              | -                         | 3.70                      | 1.26                      | 2.29                      | 2.23                     
Dijkstra                  | -                         | 2.84                      | 1.41                      | 2.38                      | 2.27                     
Euler                     | -                         | 3.19                      | 1.87                      | 2.24                      | 2.27                     
Midpoint Explicit         | -                         | 3.59                      | 2.63                      | 2.59                      | 2.62                     
Midpoint Fixed            | -                         | 4.25                      | 2.76                      | 2.61                      | 2.68                     
RK4                       | -                         | 4.77                      | 3.12                      | 3.22                      | 3.22                     
FD - L Convection         | -                         | 2.75                      | 1.01                      | 2.21                      | 2.20                     
FD - NL Convection        | -                         | 3.55                      | 1.09                      | 2.21                      | 2.22                     
FD - Poisson              | -                         | 3.70                      | 1.55                      | 2.39                      | 2.38                     
FD - Laplace              | -                         | 7.48                      | 2.99                      | 2.75                      | 2.84                     
M-D                       | -                         | 7.50                      | 3.45                      | 3.29                      | 3.04                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 455.00 $\pm$ 2.00         | 8.04 $\pm$ 0.02           | 28.20 $\pm$ 0.10          | 3.26 $\pm$ 0.00           | 2.95 $\pm$ 0.00          
Bellman Ford (ms)         | 2960.00 $\pm$ 40.00       | 7.72 $\pm$ 0.01           | 6.36 $\pm$ 0.01           | 3.86 $\pm$ 0.00           | 6.49 $\pm$ 0.01          
Dijkstra (ms)             | 7440.00 $\pm$ 90.00       | 48.10 $\pm$ 0.30          | 41.00 $\pm$ 0.70          | 37.60 $\pm$ 0.50          | 50.40 $\pm$ 0.40         
Euler (ms)                | 5000.00 $\pm$ 120.00      | 41.50 $\pm$ 1.30          | 112.00 $\pm$ 0.00         | 21.30 $\pm$ 1.00          | 235.00 $\pm$ 3.00        
Midpoint Explicit (ms)    | 10100.00 $\pm$ 100.00     | 80.90 $\pm$ 0.50          | 207.00 $\pm$ 1.00         | 30.10 $\pm$ 0.60          | 468.00 $\pm$ 3.00        
Midpoint Fixed (s)        | 50.10 $\pm$ 0.70          | 0.66 $\pm$ 0.00           | 1.05 $\pm$ 0.01           | 0.10 $\pm$ 0.00           | 2.31 $\pm$ 0.01          
RK4 (ms)                  | 24400.00 $\pm$ 300.00     | 202.00 $\pm$ 1.00         | 384.00 $\pm$ 6.00         | 45.90 $\pm$ 0.60          | 755.00 $\pm$ 3.00        
FD - L Convection (ms)    | 3260.00 $\pm$ 30.00       | 4.48 $\pm$ 0.02           | 3.41 $\pm$ 0.19           | 1.71 $\pm$ 0.07           | 2.54 $\pm$ 0.13          
FD - NL Convection (ms)   | 4090.00 $\pm$ 80.00       | 3.51 $\pm$ 0.04           | 3.47 $\pm$ 0.10           | 1.84 $\pm$ 0.08           | 2.61 $\pm$ 0.13          
FD - Poisson (ms)         | 9100.00 $\pm$ 50.00       | 5.69 $\pm$ 0.01           | 9.98 $\pm$ 0.13           | 3.71 $\pm$ 0.01           | 4.90 $\pm$ 0.02          
FD - Laplace (ms)         | 729.00 $\pm$ 86.00        | 238.00 $\pm$ 3.00         | 381.00 $\pm$ 4.00         | 76.80 $\pm$ 2.10          | 419.00 $\pm$ 2.00        
M-D (ms)                  | 19700.00 $\pm$ 300.00     | 53.00 $\pm$ 0.00          | 74.80 $\pm$ 1.50          | 106.00 $\pm$ 0.00         | 110.00 $\pm$ 0.00        

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.8.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.91                      | 0.42                      | 1.45                      | 1.40                     
Bellman Ford              | -                         | 4.12                      | 1.38                      | 2.49                      | 2.54                     
Dijkstra                  | -                         | 3.06                      | 1.45                      | 2.63                      | 2.51                     
Euler                     | -                         | 3.61                      | 2.12                      | 2.42                      | 2.46                     
Midpoint Explicit         | -                         | 4.12                      | 2.75                      | 2.82                      | 2.89                     
Midpoint Fixed            | -                         | 4.67                      | 2.93                      | 2.91                      | 2.99                     
RK4                       | -                         | 5.28                      | 3.29                      | 3.52                      | 3.56                     
FD - L Convection         | -                         | 3.06                      | 1.19                      | 2.42                      | 2.46                     
FD - NL Convection        | -                         | 4.25                      | 1.14                      | 2.44                      | 2.45                     
FD - Poisson              | -                         | 4.13                      | 1.61                      | 2.63                      | 2.61                     
FD - Laplace              | -                         | 8.21                      | 2.97                      | 3.04                      | 3.08                     
M-D                       | -                         | 8.37                      | 3.59                      | 3.57                      | 3.27                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 459.00 $\pm$ 11.00        | 8.25 $\pm$ 0.24           | 28.80 $\pm$ 0.70          | 2.23 $\pm$ 0.05           | 2.34 $\pm$ 0.14          
Bellman Ford (ms)         | 3060.00 $\pm$ 60.00       | 8.51 $\pm$ 0.35           | 7.58 $\pm$ 0.34           | 5.08 $\pm$ 0.15           | 9.34 $\pm$ 0.33          
Dijkstra (ms)             | 8220.00 $\pm$ 550.00      | 41.80 $\pm$ 1.00          | 44.30 $\pm$ 1.00          | 37.10 $\pm$ 1.20          | 55.50 $\pm$ 2.30         
Euler (ms)                | 5370.00 $\pm$ 130.00      | 54.60 $\pm$ 6.50          | 122.00 $\pm$ 7.00         | 26.20 $\pm$ 1.10          | 260.00 $\pm$ 16.00       
Midpoint Explicit (ms)    | 11100.00 $\pm$ 300.00     | 103.00 $\pm$ 5.00         | 238.00 $\pm$ 9.00         | 43.00 $\pm$ 1.80          | 486.00 $\pm$ 8.00        
Midpoint Fixed (s)        | 54.60 $\pm$ 1.50          | 0.74 $\pm$ 0.02           | 1.22 $\pm$ 0.03           | 0.14 $\pm$ 0.00           | 2.39 $\pm$ 0.02          
RK4 (ms)                  | 27100.00 $\pm$ 800.00     | 241.00 $\pm$ 11.00        | 425.00 $\pm$ 9.00         | 58.00 $\pm$ 2.80          | 810.00 $\pm$ 14.00       
FD - L Convection (ms)    | 3360.00 $\pm$ 160.00      | 3.67 $\pm$ 0.19           | 4.05 $\pm$ 0.13           | 2.51 $\pm$ 0.07           | 3.27 $\pm$ 0.31          
FD - NL Convection (ms)   | 4140.00 $\pm$ 100.00      | 4.44 $\pm$ 0.26           | 4.24 $\pm$ 0.12           | 2.61 $\pm$ 0.04           | 3.56 $\pm$ 0.24          
FD - Poisson (ms)         | 9420.00 $\pm$ 120.00      | 12.50 $\pm$ 0.20          | 13.50 $\pm$ 0.60          | 7.40 $\pm$ 0.26           | 9.83 $\pm$ 0.23          
FD - Laplace (ms)         | 1040.00 $\pm$ 20.00       | 352.00 $\pm$ 6.00         | 531.00 $\pm$ 8.00         | 165.00 $\pm$ 4.00         | 474.00 $\pm$ 7.00        
M-D (ms)                  | 20300.00 $\pm$ 500.00     | 69.70 $\pm$ 2.30          | 101.00 $\pm$ 3.00         | 124.00 $\pm$ 3.00         | 131.00 $\pm$ 8.00        

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
