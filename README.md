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
### Performance Comparison (as of Wed Jul 17 15:26:21 UTC 2024)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.40                      | 2.16                      | 0.34                      | 1.32                      | 1.26                      | 1.39                      | 1.34                     
Bellman Ford              | -                         | 3.51                      | 3.76                      | 1.12                      | 3.68                      | 3.96                      | 3.79                      | 4.43                     
Dijkstra                  | -                         | 2.42                      | 2.71                      | 1.61                      | 3.72                      | 3.96                      | 3.90                      | 4.45                     
Euler                     | -                         | 2.74                      | 3.06                      | 2.06                      | 3.62                      | 3.94                      | 3.76                      | 4.42                     
Midpoint Explicit         | -                         | 3.10                      | 3.51                      | 3.09                      | 3.87                      | 4.18                      | 3.99                      | 4.61                     
Midpoint Fixed            | -                         | 3.52                      | 3.92                      | 3.29                      | 3.91                      | 4.29                      | 4.10                      | 4.71                     
RK4                       | -                         | 3.84                      | 4.21                      | 3.80                      | 4.34                      | 4.62                      | 4.40                      | 5.06                     
FD - L Convection         | -                         | 2.36                      | 2.74                      | 0.88                      | 3.61                      | 3.91                      | 3.78                      | 4.43                     
FD - NL Convection        | -                         | 3.36                      | 3.63                      | 0.90                      | 3.63                      | 3.95                      | 3.77                      | 4.40                     
FD - Poisson              | -                         | 3.50                      | 3.80                      | 1.35                      | 3.74                      | 4.04                      | 5.01                      | 4.51                     
FD - Laplace              | -                         | 6.82                      | 9.05                      | 3.14                      | 4.06                      | 4.37                      | 4.30                      | 4.89                     
M-D                       | -                         | 6.60                      | 7.89                      | 4.11                      | 4.41                      | 4.50                      | 4.61                      | 5.35                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 294.00                    | 3.21                      | 3.03                      | 9.59                      | 1.50                      | 1.50                      | 7.38                      | 3.92                     
Bellman Ford (ms)         | 1850.00                   | 5.22                      | 3.25                      | 3.77                      | 2.99                      | 5.98                      | 4.02                      | 18.60                    
Dijkstra (ms)             | 4940.00                   | 25.00                     | 17.10                     | 19.80                     | 19.00                     | 30.90                     | 24.40                     | 22.80                    
Euler (ms)                | 3980.00                   | 25.80                     | 24.80                     | 37.10                     | 14.60                     | 143.00                    | 13.70                     | 127.00                   
Midpoint Explicit (ms)    | 8130.00                   | 53.10                     | 52.00                     | 77.90                     | 23.70                     | 286.00                    | 15.70                     | 254.00                   
Midpoint Fixed (ms)       | 41600.00                  | 252.00                    | 91.60                     | 369.00                    | 74.60                     | 1390.00                   | 63.50                     | 1230.00                  
RK4 (ms)                  | 20200.00                  | 159.00                    | 34.90                     | 138.00                    | 34.00                     | 486.00                    | 37.60                     | 403.00                   
FD - L Convection (ms)    | 2220.00                   | 1.62                      | 1.49                      | 2.72                      | 1.44                      | 1.84                      | 1.30                      | 4.44                     
FD - NL Convection (ms)   | 2830.00                   | 1.86                      | 1.77                      | 2.83                      | 1.80                      | 1.99                      | 1.40                      | 4.14                     
FD - Poisson (ms)         | 6630.00                   | 2.89                      | 5.56                      | 7.20                      | 2.78                      | 3.86                      | 2.66                      | 5.69                     
FD - Laplace (ms)         | 592.00                    | 68.80                     | 151.00                    | 248.00                    | 62.90                     | 309.00                    | 59.60                     | 320.00                   
M-D (ms)                  | 15000.00                  | 15.20                     | 52.80                     | 59.00                     | 53.90                     | 59.40                     | 79.90                     | 60.70                    

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.8 results
### Performance Comparison (as of 1.12.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.90                      | -                         | 0.34                      | 1.28                      | 1.25                      | 1.36                      | 1.35                     
Bellman Ford              | -                         | 3.34                      | -                         | 1.07                      | 3.63                      | 3.88                      | 3.72                      | 4.35                     
Dijkstra                  | -                         | 2.29                      | -                         | 1.56                      | 3.68                      | 3.91                      | 3.85                      | 4.39                     
Euler                     | -                         | 2.67                      | -                         | 1.99                      | 3.67                      | 3.94                      | 3.73                      | 4.30                     
Midpoint Explicit         | -                         | 3.08                      | -                         | 2.99                      | 3.92                      | 4.18                      | 4.01                      | 4.62                     
Midpoint Fixed            | -                         | 3.39                      | -                         | 3.16                      | 3.93                      | 4.23                      | 4.06                      | 4.65                     
RK4                       | -                         | 3.72                      | -                         | 3.73                      | 4.37                      | 4.62                      | 4.49                      | 5.11                     
FD - L Convection         | -                         | 2.29                      | -                         | 0.89                      | 3.71                      | 3.98                      | 3.90                      | 4.38                     
FD - NL Convection        | -                         | 3.41                      | -                         | 0.92                      | 3.63                      | 3.99                      | 3.83                      | 4.44                     
FD - Poisson              | -                         | 3.43                      | -                         | 1.37                      | 3.80                      | 4.05                      | 4.33                      | 4.49                     
FD - Laplace              | -                         | 6.97                      | -                         | 3.08                      | 4.10                      | 4.47                      | 4.36                      | 4.96                     
M-D                       | -                         | 6.65                      | -                         | 4.16                      | 4.56                      | 4.69                      | 4.76                      | 5.63                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 340.00 $\pm$ 5.00         | 2.96 $\pm$ 0.01           | -                         | 10.70 $\pm$ 0.10          | 1.55 $\pm$ 0.00           | 1.55 $\pm$ 0.00           | 8.83 $\pm$ 0.22           | 4.77 $\pm$ 0.01          
Bellman Ford (ms)         | 1850.00 $\pm$ 20.00       | 4.92 $\pm$ 0.02           | -                         | 3.89 $\pm$ 0.06           | 2.95 $\pm$ 0.03           | 6.09 $\pm$ 0.02           | 4.04 $\pm$ 0.02           | 18.40 $\pm$ 0.20         
Dijkstra (ms)             | 4950.00 $\pm$ 80.00       | 26.70 $\pm$ 0.50          | -                         | 20.00 $\pm$ 0.70          | 19.80 $\pm$ 0.60          | 30.90 $\pm$ 0.60          | 24.40 $\pm$ 0.90          | 22.90 $\pm$ 0.50         
Euler (ms)                | 3970.00 $\pm$ 30.00       | 29.10 $\pm$ 0.40          | -                         | 39.20 $\pm$ 1.50          | 16.10 $\pm$ 0.70          | 145.00 $\pm$ 2.00         | 14.20 $\pm$ 0.40          | 129.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 8220.00 $\pm$ 180.00      | 60.00 $\pm$ 0.80          | -                         | 81.80 $\pm$ 2.90          | 23.60 $\pm$ 0.70          | 283.00 $\pm$ 2.00         | 15.70 $\pm$ 0.40          | 256.00 $\pm$ 1.00        
Midpoint Fixed (ms)       | 41400.00 $\pm$ 400.00     | 255.00 $\pm$ 1.00         | -                         | 392.00 $\pm$ 13.00        | 75.20 $\pm$ 1.30          | 1400.00 $\pm$ 20.00       | 60.60 $\pm$ 1.80          | 1250.00 $\pm$ 20.00      
RK4 (ms)                  | 21000.00 $\pm$ 100.00     | 167.00 $\pm$ 4.00         | -                         | 147.00 $\pm$ 3.00         | 32.40 $\pm$ 0.50          | 492.00 $\pm$ 6.00         | 37.90 $\pm$ 0.60          | 409.00 $\pm$ 2.00        
FD - L Convection (ms)    | 2450.00 $\pm$ 60.00       | 1.44 $\pm$ 0.03           | -                         | 2.71 $\pm$ 0.04           | 1.56 $\pm$ 0.23           | 1.86 $\pm$ 0.02           | 1.32 $\pm$ 0.01           | 3.70 $\pm$ 0.01          
FD - NL Convection (ms)   | 2990.00 $\pm$ 20.00       | 2.01 $\pm$ 0.02           | -                         | 2.82 $\pm$ 0.04           | 1.81 $\pm$ 0.10           | 2.01 $\pm$ 0.01           | 1.40 $\pm$ 0.01           | 3.75 $\pm$ 0.01          
FD - Poisson (ms)         | 6440.00 $\pm$ 60.00       | 3.05 $\pm$ 0.16           | -                         | 7.21 $\pm$ 0.03           | 2.82 $\pm$ 0.01           | 3.81 $\pm$ 0.03           | 2.68 $\pm$ 0.02           | 7.64 $\pm$ 0.03          
FD - Laplace (ms)         | 621.00 $\pm$ 23.00        | 69.40 $\pm$ 0.40          | -                         | 251.00 $\pm$ 1.00         | 60.60 $\pm$ 2.60          | 257.00 $\pm$ 2.00         | 60.80 $\pm$ 1.90          | 328.00 $\pm$ 1.00        
M-D (ms)                  | 16500.00 $\pm$ 100.00     | 15.20 $\pm$ 0.00          | -                         | 59.50 $\pm$ 0.80          | 53.90 $\pm$ 0.30          | 59.20 $\pm$ 0.20          | 78.00 $\pm$ 1.10          | 61.90 $\pm$ 0.40         

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.12.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.95                      | -                         | 0.33                      | 1.29                      | 1.25                      | 1.37                      | 1.38                     
Bellman Ford              | -                         | 3.37                      | -                         | 1.08                      | 3.64                      | 3.91                      | 3.76                      | 4.38                     
Dijkstra                  | -                         | 2.32                      | -                         | 1.58                      | 3.70                      | 3.91                      | 3.87                      | 4.43                     
Euler                     | -                         | 2.66                      | -                         | 2.02                      | 3.61                      | 3.94                      | 3.74                      | 4.37                     
Midpoint Explicit         | -                         | 3.04                      | -                         | 3.01                      | 3.89                      | 4.16                      | 3.98                      | 4.61                     
Midpoint Fixed            | -                         | 3.47                      | -                         | 3.19                      | 3.95                      | 4.28                      | 4.15                      | 4.74                     
RK4                       | -                         | 3.94                      | -                         | 3.82                      | 4.42                      | 4.75                      | 4.55                      | 5.28                     
FD - L Convection         | -                         | 2.39                      | -                         | 0.93                      | 3.70                      | 4.03                      | 3.80                      | 4.41                     
FD - NL Convection        | -                         | 3.45                      | -                         | 0.90                      | 3.67                      | 4.03                      | 3.86                      | 4.49                     
FD - Poisson              | -                         | 3.42                      | -                         | 1.34                      | 3.72                      | 4.02                      | 4.35                      | 4.45                     
FD - Laplace              | -                         | 6.79                      | -                         | 3.08                      | 4.10                      | 4.41                      | 4.32                      | 4.89                     
M-D                       | -                         | 6.48                      | -                         | 4.12                      | 4.47                      | 4.60                      | 4.64                      | 5.47                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 306.00 $\pm$ 7.00         | 2.99 $\pm$ 0.09           | -                         | 10.70 $\pm$ 0.20          | 1.55 $\pm$ 0.00           | 1.55 $\pm$ 0.00           | 8.58 $\pm$ 0.28           | 3.93 $\pm$ 0.01          
Bellman Ford (ms)         | 1920.00 $\pm$ 30.00       | 4.18 $\pm$ 0.02           | -                         | 3.89 $\pm$ 0.10           | 2.98 $\pm$ 0.02           | 6.08 $\pm$ 0.09           | 4.44 $\pm$ 0.07           | 18.30 $\pm$ 0.30         
Dijkstra (ms)             | 4970.00 $\pm$ 30.00       | 25.10 $\pm$ 0.50          | -                         | 19.40 $\pm$ 0.40          | 18.50 $\pm$ 0.30          | 30.80 $\pm$ 0.50          | 24.10 $\pm$ 0.50          | 22.70 $\pm$ 0.40         
Euler (ms)                | 3870.00 $\pm$ 20.00       | 28.50 $\pm$ 0.30          | -                         | 39.50 $\pm$ 1.00          | 15.10 $\pm$ 0.50          | 143.00 $\pm$ 2.00         | 14.30 $\pm$ 0.40          | 130.00 $\pm$ 4.00        
Midpoint Explicit (ms)    | 7960.00 $\pm$ 140.00      | 59.80 $\pm$ 0.40          | -                         | 83.10 $\pm$ 2.90          | 23.30 $\pm$ 0.50          | 283.00 $\pm$ 4.00         | 15.90 $\pm$ 1.00          | 254.00 $\pm$ 3.00        
Midpoint Fixed (ms)       | 40400.00 $\pm$ 200.00     | 256.00 $\pm$ 2.00         | -                         | 389.00 $\pm$ 14.00        | 75.10 $\pm$ 0.60          | 1420.00 $\pm$ 20.00       | 61.70 $\pm$ 3.00          | 1250.00 $\pm$ 20.00      
RK4 (ms)                  | 20100.00 $\pm$ 200.00     | 167.00 $\pm$ 3.00         | -                         | 148.00 $\pm$ 4.00         | 33.00 $\pm$ 0.60          | 490.00 $\pm$ 3.00         | 38.80 $\pm$ 0.80          | 410.00 $\pm$ 3.00        
FD - L Convection (ms)    | 2370.00 $\pm$ 20.00       | 1.65 $\pm$ 0.04           | -                         | 2.72 $\pm$ 0.07           | 1.76 $\pm$ 0.02           | 1.63 $\pm$ 0.02           | 1.52 $\pm$ 0.01           | 3.72 $\pm$ 0.14          
FD - NL Convection (ms)   | 2950.00 $\pm$ 20.00       | 1.84 $\pm$ 0.07           | -                         | 2.84 $\pm$ 0.05           | 1.78 $\pm$ 0.08           | 2.07 $\pm$ 0.12           | 1.40 $\pm$ 0.01           | 3.82 $\pm$ 0.31          
FD - Poisson (ms)         | 6390.00 $\pm$ 50.00       | 3.16 $\pm$ 0.23           | -                         | 7.20 $\pm$ 0.06           | 2.79 $\pm$ 0.04           | 3.85 $\pm$ 0.02           | 2.67 $\pm$ 0.01           | 7.64 $\pm$ 0.03          
FD - Laplace (ms)         | 599.00 $\pm$ 22.00        | 66.70 $\pm$ 1.90          | -                         | 252.00 $\pm$ 2.00         | 63.10 $\pm$ 0.50          | 282.00 $\pm$ 2.00         | 60.50 $\pm$ 0.50          | 323.00 $\pm$ 3.00        
M-D (ms)                  | 15400.00 $\pm$ 100.00     | 15.30 $\pm$ 0.00          | -                         | 59.30 $\pm$ 0.20          | 54.00 $\pm$ 0.10          | 60.40 $\pm$ 2.00          | 79.00 $\pm$ 1.00          | 62.30 $\pm$ 0.50         

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.12.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.34                      | -                         | 0.34                      | 1.26                      | 1.22                      | 1.32                      | 1.32                     
Bellman Ford              | -                         | 3.45                      | -                         | 1.08                      | 3.63                      | 3.83                      | 3.67                      | 4.33                     
Dijkstra                  | -                         | 2.49                      | -                         | 1.57                      | 3.64                      | 3.86                      | 3.80                      | 4.38                     
Euler                     | -                         | 2.75                      | -                         | 2.03                      | 3.56                      | 3.85                      | 3.67                      | 4.30                     
Midpoint Explicit         | -                         | 3.13                      | -                         | 3.01                      | 3.81                      | 4.11                      | 3.92                      | 4.52                     
Midpoint Fixed            | -                         | 3.56                      | -                         | 3.21                      | 3.85                      | 4.20                      | 4.00                      | 4.52                     
RK4                       | -                         | 3.83                      | -                         | 3.77                      | 4.25                      | 4.56                      | 4.40                      | 4.99                     
FD - L Convection         | -                         | 2.38                      | -                         | 0.86                      | 3.51                      | 3.83                      | 3.66                      | 4.27                     
FD - NL Convection        | -                         | 3.37                      | -                         | 0.89                      | 3.52                      | 3.86                      | 3.70                      | 4.27                     
FD - Poisson              | -                         | 3.41                      | -                         | 1.34                      | 3.62                      | 3.93                      | 4.17                      | 4.32                     
FD - Laplace              | -                         | 6.70                      | -                         | 3.06                      | 3.97                      | 4.29                      | 4.21                      | 4.80                     
M-D                       | -                         | 6.44                      | -                         | 4.06                      | 4.32                      | 4.44                      | 4.52                      | 5.23                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 300.00 $\pm$ 3.00         | 3.01 $\pm$ 0.14           | -                         | 10.60 $\pm$ 0.30          | 1.50 $\pm$ 0.00           | 1.50 $\pm$ 0.00           | 8.73 $\pm$ 0.35           | 4.34 $\pm$ 0.01          
Bellman Ford (ms)         | 1910.00 $\pm$ 80.00       | 4.18 $\pm$ 0.02           | -                         | 3.89 $\pm$ 0.06           | 2.98 $\pm$ 0.02           | 6.05 $\pm$ 0.02           | 4.32 $\pm$ 0.07           | 18.40 $\pm$ 0.40         
Dijkstra (ms)             | 4960.00 $\pm$ 40.00       | 23.60 $\pm$ 0.40          | -                         | 19.50 $\pm$ 0.50          | 19.00 $\pm$ 0.40          | 30.00 $\pm$ 0.50          | 23.40 $\pm$ 0.30          | 22.70 $\pm$ 0.40         
Euler (ms)                | 3900.00 $\pm$ 50.00       | 28.70 $\pm$ 0.40          | -                         | 39.30 $\pm$ 1.10          | 15.10 $\pm$ 0.70          | 143.00 $\pm$ 2.00         | 14.40 $\pm$ 0.40          | 128.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 7870.00 $\pm$ 50.00       | 62.10 $\pm$ 8.90          | -                         | 82.30 $\pm$ 2.50          | 22.90 $\pm$ 0.50          | 281.00 $\pm$ 4.00         | 15.60 $\pm$ 0.40          | 253.00 $\pm$ 2.00        
Midpoint Fixed (ms)       | 39900.00 $\pm$ 200.00     | 255.00 $\pm$ 1.00         | -                         | 400.00 $\pm$ 10.00        | 74.80 $\pm$ 0.70          | 1390.00 $\pm$ 10.00       | 61.30 $\pm$ 2.60          | 1240.00 $\pm$ 30.00      
RK4 (ms)                  | 20000.00 $\pm$ 100.00     | 165.00 $\pm$ 3.00         | -                         | 149.00 $\pm$ 10.00        | 32.70 $\pm$ 2.00          | 489.00 $\pm$ 11.00        | 38.50 $\pm$ 1.00          | 408.00 $\pm$ 13.00       
FD - L Convection (ms)    | 2280.00 $\pm$ 20.00       | 1.65 $\pm$ 0.03           | -                         | 2.70 $\pm$ 0.05           | 1.48 $\pm$ 0.11           | 1.77 $\pm$ 0.11           | 1.31 $\pm$ 0.01           | 3.68 $\pm$ 0.01          
FD - NL Convection (ms)   | 2820.00 $\pm$ 20.00       | 1.93 $\pm$ 0.08           | -                         | 2.82 $\pm$ 0.04           | 1.90 $\pm$ 0.17           | 2.04 $\pm$ 0.09           | 1.52 $\pm$ 0.01           | 3.80 $\pm$ 0.05          
FD - Poisson (ms)         | 6560.00 $\pm$ 180.00      | 2.98 $\pm$ 0.06           | -                         | 7.19 $\pm$ 0.03           | 2.81 $\pm$ 0.02           | 3.83 $\pm$ 0.02           | 2.67 $\pm$ 0.01           | 7.77 $\pm$ 0.03          
FD - Laplace (ms)         | 579.00 $\pm$ 7.00         | 65.00 $\pm$ 0.50          | -                         | 245.00 $\pm$ 1.00         | 58.70 $\pm$ 0.40          | 256.00 $\pm$ 0.00         | 60.00 $\pm$ 0.70          | 327.00 $\pm$ 1.00        
M-D (ms)                  | 15400.00 $\pm$ 100.00     | 15.30 $\pm$ 0.20          | -                         | 59.30 $\pm$ 0.20          | 54.10 $\pm$ 0.20          | 59.30 $\pm$ 0.20          | 77.80 $\pm$ 0.10          | 61.60 $\pm$ 0.60         

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.12.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.33                      | -                         | 0.29                      | 1.27                      | 1.21                      | 1.33                      | 1.33                     
Bellman Ford              | -                         | 3.36                      | -                         | 1.09                      | 3.60                      | 3.87                      | 3.75                      | 4.35                     
Dijkstra                  | -                         | 2.36                      | -                         | 1.55                      | 3.68                      | 3.87                      | 3.82                      | 4.41                     
Euler                     | -                         | 2.70                      | -                         | 1.96                      | 3.59                      | 3.88                      | 3.71                      | 4.33                     
Midpoint Explicit         | -                         | 3.07                      | -                         | 2.90                      | 3.82                      | 4.12                      | 3.84                      | 4.55                     
Midpoint Fixed            | -                         | 3.40                      | -                         | 3.10                      | 3.85                      | 4.20                      | 4.00                      | 4.65                     
RK4                       | -                         | 3.76                      | -                         | 3.59                      | 4.27                      | 4.52                      | 4.35                      | 4.96                     
FD - L Convection         | -                         | 2.36                      | -                         | 0.85                      | 3.53                      | 3.86                      | 3.69                      | 4.29                     
FD - NL Convection        | -                         | 3.36                      | -                         | 0.84                      | 3.52                      | 3.86                      | 3.72                      | 4.31                     
FD - Poisson              | -                         | 3.33                      | -                         | 1.28                      | 3.65                      | 3.95                      | 4.22                      | 4.37                     
FD - Laplace              | -                         | 6.59                      | -                         | 2.87                      | 3.98                      | 4.29                      | 4.23                      | 4.79                     
M-D                       | -                         | 6.26                      | -                         | 3.93                      | 4.29                      | 4.41                      | 4.49                      | 5.21                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 458.00 $\pm$ 4.00         | 2.98 $\pm$ 0.07           | -                         | 10.60 $\pm$ 0.30          | 1.55 $\pm$ 0.00           | 1.55 $\pm$ 0.00           | 8.57 $\pm$ 0.31           | 4.34 $\pm$ 0.01          
Bellman Ford (ms)         | 1810.00 $\pm$ 20.00       | 4.19 $\pm$ 0.02           | -                         | 3.83 $\pm$ 0.05           | 2.99 $\pm$ 0.03           | 6.10 $\pm$ 0.01           | 4.31 $\pm$ 0.07           | 18.30 $\pm$ 0.40         
Dijkstra (ms)             | 4850.00 $\pm$ 30.00       | 26.50 $\pm$ 0.40          | -                         | 19.50 $\pm$ 0.40          | 18.50 $\pm$ 0.40          | 30.30 $\pm$ 0.50          | 24.20 $\pm$ 0.20          | 23.10 $\pm$ 1.00         
Euler (ms)                | 3750.00 $\pm$ 40.00       | 28.50 $\pm$ 0.30          | -                         | 38.50 $\pm$ 1.30          | 15.10 $\pm$ 0.50          | 143.00 $\pm$ 3.00         | 14.10 $\pm$ 0.20          | 130.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 7560.00 $\pm$ 60.00       | 59.60 $\pm$ 0.70          | -                         | 73.90 $\pm$ 0.90          | 22.90 $\pm$ 0.40          | 281.00 $\pm$ 2.00         | 15.80 $\pm$ 0.40          | 253.00 $\pm$ 3.00        
Midpoint Fixed (ms)       | 38500.00 $\pm$ 200.00     | 256.00 $\pm$ 2.00         | -                         | 377.00 $\pm$ 2.00         | 75.50 $\pm$ 0.60          | 1410.00 $\pm$ 20.00       | 60.80 $\pm$ 2.20          | 1250.00 $\pm$ 10.00      
RK4 (ms)                  | 19600.00 $\pm$ 200.00     | 167.00 $\pm$ 4.00         | -                         | 158.00 $\pm$ 64.00        | 34.80 $\pm$ 0.70          | 493.00 $\pm$ 13.00        | 38.00 $\pm$ 0.90          | 410.00 $\pm$ 10.00       
FD - L Convection (ms)    | 2210.00 $\pm$ 20.00       | 1.63 $\pm$ 0.01           | -                         | 2.74 $\pm$ 0.07           | 1.55 $\pm$ 0.23           | 1.73 $\pm$ 0.11           | 1.53 $\pm$ 0.06           | 3.68 $\pm$ 0.01          
FD - NL Convection (ms)   | 2770.00 $\pm$ 20.00       | 1.93 $\pm$ 0.10           | -                         | 2.82 $\pm$ 0.05           | 1.99 $\pm$ 0.17           | 2.08 $\pm$ 0.12           | 1.38 $\pm$ 0.01           | 3.75 $\pm$ 0.01          
FD - Poisson (ms)         | 6010.00 $\pm$ 100.00      | 3.06 $\pm$ 0.05           | -                         | 7.21 $\pm$ 0.07           | 2.80 $\pm$ 0.02           | 3.85 $\pm$ 0.02           | 2.71 $\pm$ 0.03           | 7.62 $\pm$ 0.03          
FD - Laplace (ms)         | 586.00 $\pm$ 7.00         | 68.40 $\pm$ 0.40          | -                         | 246.00 $\pm$ 1.00         | 63.80 $\pm$ 1.80          | 309.00 $\pm$ 2.00         | 64.50 $\pm$ 0.50          | 324.00 $\pm$ 8.00        
M-D (ms)                  | 14600.00 $\pm$ 100.00     | 15.20 $\pm$ 0.00          | -                         | 59.70 $\pm$ 0.20          | 54.70 $\pm$ 0.10          | 59.90 $\pm$ 0.20          | 76.80 $\pm$ 0.60          | 61.80 $\pm$ 0.30         

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
## Python 3.12 results
### Performance Comparison (as of 1.12.0)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | -                         | -                         | 0.29                      | 1.35                      | 1.31                      | 1.43                      | 1.43                     
Bellman Ford              | -                         | -                         | -                         | 1.19                      | 3.71                      | 3.97                      | 3.87                      | 4.52                     
Dijkstra                  | -                         | -                         | -                         | 1.60                      | 3.77                      | 3.99                      | 3.93                      | 4.53                     
Euler                     | -                         | -                         | -                         | 2.02                      | 3.67                      | 3.97                      | 3.79                      | 4.43                     
Midpoint Explicit         | -                         | -                         | -                         | 2.95                      | 4.01                      | 4.32                      | 4.10                      | 4.67                     
Midpoint Fixed            | -                         | -                         | -                         | 3.21                      | 4.05                      | 4.37                      | 4.15                      | 4.82                     
RK4                       | -                         | -                         | -                         | 3.63                      | 4.47                      | 4.78                      | 4.60                      | 5.18                     
FD - L Convection         | -                         | -                         | -                         | 0.89                      | 3.63                      | 3.92                      | 3.77                      | 4.39                     
FD - NL Convection        | -                         | -                         | -                         | 0.87                      | 3.64                      | 3.94                      | 3.84                      | 4.41                     
FD - Poisson              | -                         | -                         | -                         | 1.31                      | 3.73                      | 4.04                      | 4.30                      | 4.42                     
FD - Laplace              | -                         | -                         | -                         | 2.90                      | 4.11                      | 4.39                      | 4.31                      | 4.91                     
M-D                       | -                         | -                         | -                         | 3.96                      | 4.53                      | 4.56                      | 4.71                      | 5.47                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 476.00 $\pm$ 28.00        | -                         | -                         | 10.70 $\pm$ 0.20          | 1.55 $\pm$ 0.00           | 1.60 $\pm$ 0.01           | 7.56 $\pm$ 0.13           | 4.37 $\pm$ 0.01          
Bellman Ford (ms)         | 2530.00 $\pm$ 40.00       | -                         | -                         | 3.83 $\pm$ 0.06           | 2.94 $\pm$ 0.02           | 6.06 $\pm$ 0.03           | 4.43 $\pm$ 0.02           | 18.70 $\pm$ 0.30         
Dijkstra (ms)             | 6790.00 $\pm$ 60.00       | -                         | -                         | 19.70 $\pm$ 0.70          | 19.70 $\pm$ 0.50          | 30.10 $\pm$ 0.40          | 24.40 $\pm$ 0.80          | 22.60 $\pm$ 0.40         
Euler (ms)                | 4820.00 $\pm$ 40.00       | -                         | -                         | 37.70 $\pm$ 0.50          | 15.40 $\pm$ 0.70          | 145.00 $\pm$ 2.00         | 14.40 $\pm$ 0.40          | 129.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 9700.00 $\pm$ 40.00       | -                         | -                         | 73.10 $\pm$ 1.50          | 23.70 $\pm$ 0.60          | 284.00 $\pm$ 3.00         | 15.90 $\pm$ 0.90          | 262.00 $\pm$ 13.00       
Midpoint Fixed (s)        | 48.30 $\pm$ 0.30          | -                         | -                         | 0.37 $\pm$ 0.00           | 0.08 $\pm$ 0.00           | 1.40 $\pm$ 0.02           | 0.06 $\pm$ 0.00           | 1.25 $\pm$ 0.02          
RK4 (ms)                  | 24300.00 $\pm$ 200.00     | -                         | -                         | 144.00 $\pm$ 17.00        | 34.20 $\pm$ 0.60          | 496.00 $\pm$ 13.00        | 38.20 $\pm$ 0.50          | 407.00 $\pm$ 2.00        
FD - L Convection (ms)    | 2880.00 $\pm$ 50.00       | -                         | -                         | 2.71 $\pm$ 0.04           | 1.55 $\pm$ 0.08           | 1.61 $\pm$ 0.01           | 1.51 $\pm$ 0.00           | 3.70 $\pm$ 0.01          
FD - NL Convection (ms)   | 3620.00 $\pm$ 100.00      | -                         | -                         | 2.90 $\pm$ 0.11           | 2.08 $\pm$ 0.19           | 2.05 $\pm$ 0.09           | 1.52 $\pm$ 0.01           | 3.75 $\pm$ 0.01          
FD - Poisson (ms)         | 8160.00 $\pm$ 170.00      | -                         | -                         | 7.20 $\pm$ 0.06           | 2.76 $\pm$ 0.02           | 3.83 $\pm$ 0.01           | 2.66 $\pm$ 0.01           | 7.12 $\pm$ 0.04          
FD - Laplace (ms)         | 604.00 $\pm$ 20.00        | -                         | -                         | 247.00 $\pm$ 1.00         | 59.30 $\pm$ 1.80          | 307.00 $\pm$ 1.00         | 59.80 $\pm$ 0.40          | 334.00 $\pm$ 2.00        
M-D (ms)                  | 18700.00 $\pm$ 100.00     | -                         | -                         | 59.30 $\pm$ 0.10          | 54.60 $\pm$ 0.20          | 59.70 $\pm$ 0.30          | 78.60 $\pm$ 1.20          | 62.10 $\pm$ 0.20         

![Python 3.12 compilation results](./version_specific_results/pypi_performance_312_compilation.svg)
![Python 3.12 execution results](./version_specific_results/pypi_performance_312_execution.svg)
