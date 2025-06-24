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
Pyccel configurations valid for your machine can be generated using the following command (which may be adapted for another compiler family, see the [pyccel documentation](https://github.com/pyccel/pyccel/blob/master/tutorial/compiler.md)):
```
pyccel --compiler-family llvm --export-compiler-config pyccel_llvm.json
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
Devel branch benchmarks failed on python 3.11!

![Development compilation results](./version_specific_results/devel_performance_310_compilation.svg)
![Development execution results](./version_specific_results/devel_performance_310_execution.svg)
## Python 3.8 results
### Performance Comparison (as of 1.12.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.82                      | 1.93                      | 0.34                      | 1.29                      | 1.26                      | 1.37                      | 1.34                     
Bellman Ford              | -                         | 3.24                      | 3.85                      | 1.24                      | 3.74                      | 4.01                      | 3.85                      | 4.58                     
Dijkstra                  | -                         | 2.24                      | 2.60                      | 1.70                      | 3.83                      | 4.03                      | 3.95                      | 4.69                     
Euler                     | -                         | 2.47                      | 2.92                      | 2.04                      | 3.63                      | 4.00                      | 3.87                      | 4.56                     
Midpoint Explicit         | -                         | 2.82                      | 3.46                      | 3.08                      | 3.85                      | 4.17                      | 3.98                      | 4.65                     
Midpoint Fixed            | -                         | 3.30                      | 3.92                      | 3.38                      | 3.99                      | 4.38                      | 4.03                      | 4.77                     
RK4                       | -                         | 3.46                      | 4.09                      | 3.79                      | 4.35                      | 4.59                      | 4.46                      | 5.11                     
FD - L Convection         | -                         | 2.07                      | 2.60                      | 0.92                      | 3.56                      | 3.84                      | 3.69                      | 4.38                     
FD - NL Convection        | -                         | 2.99                      | 3.44                      | 0.91                      | 3.57                      | 3.90                      | 3.72                      | 4.46                     
FD - Poisson              | -                         | 3.10                      | 3.62                      | 1.35                      | 3.68                      | 3.99                      | 4.91                      | 4.48                     
FD - Laplace              | -                         | 6.13                      | 8.65                      | 3.04                      | 4.02                      | 4.32                      | 4.26                      | 4.95                     
M-D                       | -                         | 5.98                      | 7.55                      | 4.03                      | 4.39                      | 4.49                      | 4.57                      | 5.35                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 384.00 $\pm$ 4.00         | 2.94 $\pm$ 0.02           | 3.06 $\pm$ 0.02           | 10.90 $\pm$ 0.10          | 1.56 $\pm$ 0.00           | 1.56 $\pm$ 0.01           | 9.11 $\pm$ 0.12           | 4.80 $\pm$ 0.01          
Bellman Ford (ms)         | 2000.00 $\pm$ 20.00       | 4.54 $\pm$ 0.08           | 3.19 $\pm$ 0.05           | 3.89 $\pm$ 0.08           | 2.99 $\pm$ 0.02           | 6.19 $\pm$ 0.05           | 4.43 $\pm$ 0.03           | 18.50 $\pm$ 0.30         
Dijkstra (ms)             | 5050.00 $\pm$ 50.00       | 23.80 $\pm$ 0.20          | 16.90 $\pm$ 0.20          | 20.50 $\pm$ 0.40          | 19.70 $\pm$ 0.30          | 31.10 $\pm$ 0.20          | 25.40 $\pm$ 0.30          | 23.10 $\pm$ 0.10         
Euler (ms)                | 3990.00 $\pm$ 40.00       | 29.10 $\pm$ 9.50          | 25.80 $\pm$ 1.40          | 39.30 $\pm$ 1.10          | 15.40 $\pm$ 0.70          | 147.00 $\pm$ 3.00         | 14.30 $\pm$ 0.50          | 129.00 $\pm$ 1.00        
Midpoint Explicit (ms)    | 8130.00 $\pm$ 70.00       | 52.70 $\pm$ 0.40          | 52.10 $\pm$ 1.40          | 82.50 $\pm$ 2.60          | 23.50 $\pm$ 0.50          | 287.00 $\pm$ 3.00         | 16.20 $\pm$ 0.40          | 256.00 $\pm$ 2.00        
Midpoint Fixed (ms)       | 41800.00 $\pm$ 400.00     | 254.00 $\pm$ 1.00         | 92.70 $\pm$ 0.40          | 399.00 $\pm$ 11.00        | 76.70 $\pm$ 0.70          | 1410.00 $\pm$ 10.00       | 61.70 $\pm$ 1.70          | 1250.00 $\pm$ 20.00      
RK4 (ms)                  | 21000.00 $\pm$ 200.00     | 160.00 $\pm$ 4.00         | 36.30 $\pm$ 1.10          | 147.00 $\pm$ 4.00         | 35.40 $\pm$ 0.70          | 496.00 $\pm$ 8.00         | 39.00 $\pm$ 1.90          | 416.00 $\pm$ 4.00        
FD - L Convection (ms)    | 2450.00 $\pm$ 20.00       | 1.55 $\pm$ 0.05           | 1.54 $\pm$ 0.03           | 2.73 $\pm$ 0.05           | 1.56 $\pm$ 0.06           | 1.85 $\pm$ 0.01           | 1.32 $\pm$ 0.01           | 4.19 $\pm$ 0.10          
FD - NL Convection (ms)   | 3020.00 $\pm$ 30.00       | 1.80 $\pm$ 0.02           | 1.72 $\pm$ 0.01           | 2.82 $\pm$ 0.04           | 1.77 $\pm$ 0.10           | 2.20 $\pm$ 0.04           | 1.54 $\pm$ 0.03           | 4.20 $\pm$ 0.03          
FD - Poisson (ms)         | 6450.00 $\pm$ 50.00       | 3.01 $\pm$ 0.03           | 5.72 $\pm$ 0.16           | 7.23 $\pm$ 0.03           | 2.81 $\pm$ 0.07           | 3.86 $\pm$ 0.04           | 2.72 $\pm$ 0.01           | 5.72 $\pm$ 0.02          
FD - Laplace (ms)         | 425.00 $\pm$ 174.00       | 68.80 $\pm$ 0.50          | 151.00 $\pm$ 1.00         | 253.00 $\pm$ 1.00         | 58.70 $\pm$ 0.50          | 286.00 $\pm$ 1.00         | 64.10 $\pm$ 0.70          | 336.00 $\pm$ 2.00        
M-D (ms)                  | 15800.00 $\pm$ 200.00     | 15.30 $\pm$ 0.20          | 53.20 $\pm$ 0.30          | 59.50 $\pm$ 0.30          | 54.10 $\pm$ 0.20          | 59.90 $\pm$ 0.20          | 82.10 $\pm$ 6.80          | 61.70 $\pm$ 0.30         

![Python 3.8 compilation results](./version_specific_results/pypi_performance_38_compilation.svg)
![Python 3.8 execution results](./version_specific_results/pypi_performance_38_execution.svg)
## Python 3.9 results
### Performance Comparison (as of 1.12.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.80                      | 1.93                      | 0.33                      | 1.30                      | 1.25                      | 1.36                      | 1.34                     
Bellman Ford              | -                         | 3.24                      | 3.55                      | 1.11                      | 3.63                      | 3.93                      | 3.74                      | 4.45                     
Dijkstra                  | -                         | 2.18                      | 2.54                      | 1.61                      | 3.71                      | 3.91                      | 3.83                      | 4.48                     
Euler                     | -                         | 2.45                      | 2.88                      | 2.06                      | 3.61                      | 3.90                      | 3.70                      | 4.41                     
Midpoint Explicit         | -                         | 2.81                      | 3.29                      | 3.06                      | 3.93                      | 4.14                      | 3.92                      | 4.62                     
Midpoint Fixed            | -                         | 3.19                      | 3.73                      | 3.29                      | 3.87                      | 4.20                      | 3.99                      | 4.76                     
RK4                       | -                         | 3.46                      | 4.06                      | 3.82                      | 4.33                      | 4.55                      | 4.42                      | 5.10                     
FD - L Convection         | -                         | 2.07                      | 2.55                      | 0.88                      | 3.55                      | 3.85                      | 3.69                      | 4.38                     
FD - NL Convection        | -                         | 2.96                      | 3.44                      | 0.89                      | 3.57                      | 3.86                      | 3.72                      | 4.38                     
FD - Poisson              | -                         | 3.07                      | 3.63                      | 1.36                      | 3.69                      | 4.00                      | 4.94                      | 4.50                     
FD - Laplace              | -                         | 6.17                      | 8.76                      | 3.07                      | 4.02                      | 4.32                      | 4.25                      | 4.88                     
M-D                       | -                         | 6.02                      | 7.59                      | 4.09                      | 4.37                      | 4.49                      | 4.53                      | 5.35                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 333.00 $\pm$ 3.00         | 2.97 $\pm$ 0.03           | 3.06 $\pm$ 0.01           | 10.80 $\pm$ 0.20          | 1.51 $\pm$ 0.00           | 1.56 $\pm$ 0.00           | 7.51 $\pm$ 0.20           | 4.36 $\pm$ 0.00          
Bellman Ford (ms)         | 1920.00 $\pm$ 20.00       | 4.60 $\pm$ 0.02           | 3.19 $\pm$ 0.05           | 3.91 $\pm$ 0.06           | 3.01 $\pm$ 0.02           | 6.08 $\pm$ 0.03           | 4.33 $\pm$ 0.06           | 18.50 $\pm$ 0.40         
Dijkstra (ms)             | 5150.00 $\pm$ 60.00       | 24.90 $\pm$ 0.10          | 16.40 $\pm$ 0.10          | 19.70 $\pm$ 0.20          | 18.10 $\pm$ 0.30          | 30.00 $\pm$ 0.30          | 24.10 $\pm$ 0.20          | 22.40 $\pm$ 0.20         
Euler (ms)                | 3880.00 $\pm$ 30.00       | 25.70 $\pm$ 0.40          | 26.60 $\pm$ 3.60          | 37.50 $\pm$ 0.40          | 15.00 $\pm$ 0.50          | 144.00 $\pm$ 2.00         | 13.80 $\pm$ 0.30          | 128.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 7930.00 $\pm$ 90.00       | 53.10 $\pm$ 0.70          | 52.00 $\pm$ 0.90          | 76.50 $\pm$ 0.50          | 23.50 $\pm$ 0.40          | 284.00 $\pm$ 2.00         | 16.00 $\pm$ 0.40          | 256.00 $\pm$ 5.00        
Midpoint Fixed (ms)       | 40300.00 $\pm$ 300.00     | 253.00 $\pm$ 1.00         | 92.80 $\pm$ 0.50          | 368.00 $\pm$ 2.00         | 75.70 $\pm$ 0.60          | 1420.00 $\pm$ 20.00       | 74.40 $\pm$ 38.60         | 1240.00 $\pm$ 10.00      
RK4 (ms)                  | 20200.00 $\pm$ 100.00     | 160.00 $\pm$ 4.00         | 36.00 $\pm$ 0.80          | 137.00 $\pm$ 1.00         | 35.30 $\pm$ 0.60          | 495.00 $\pm$ 13.00        | 37.20 $\pm$ 0.50          | 414.00 $\pm$ 7.00        
FD - L Convection (ms)    | 2360.00 $\pm$ 10.00       | 1.66 $\pm$ 0.03           | 1.56 $\pm$ 0.02           | 2.74 $\pm$ 0.07           | 1.76 $\pm$ 0.03           | 1.75 $\pm$ 0.11           | 1.54 $\pm$ 0.01           | 4.18 $\pm$ 0.10          
FD - NL Convection (ms)   | 2940.00 $\pm$ 20.00       | 1.58 $\pm$ 0.02           | 1.74 $\pm$ 0.04           | 2.83 $\pm$ 0.03           | 2.07 $\pm$ 0.19           | 2.02 $\pm$ 0.06           | 1.53 $\pm$ 0.01           | 4.19 $\pm$ 0.03          
FD - Poisson (ms)         | 6610.00 $\pm$ 120.00      | 3.18 $\pm$ 0.02           | 5.83 $\pm$ 0.13           | 7.25 $\pm$ 0.06           | 2.83 $\pm$ 0.03           | 3.87 $\pm$ 0.04           | 2.70 $\pm$ 0.02           | 5.71 $\pm$ 0.02          
FD - Laplace (ms)         | 600.00 $\pm$ 14.00        | 69.00 $\pm$ 0.40          | 151.00 $\pm$ 1.00         | 253.00 $\pm$ 1.00         | 63.30 $\pm$ 0.60          | 260.00 $\pm$ 1.00         | 64.20 $\pm$ 0.50          | 322.00 $\pm$ 1.00        
M-D (ms)                  | 15600.00 $\pm$ 100.00     | 15.30 $\pm$ 0.10          | 53.10 $\pm$ 0.20          | 59.60 $\pm$ 0.30          | 54.50 $\pm$ 0.20          | 59.50 $\pm$ 0.20          | 80.00 $\pm$ 0.50          | 60.50 $\pm$ 0.20         

![Python 3.9 compilation results](./version_specific_results/pypi_performance_39_compilation.svg)
![Python 3.9 execution results](./version_specific_results/pypi_performance_39_execution.svg)
## Python 3.10 results
### Performance Comparison (as of 1.12.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.19                      | 2.09                      | 0.33                      | 1.26                      | 1.21                      | 1.32                      | 1.30                     
Bellman Ford              | -                         | 3.31                      | 3.65                      | 1.10                      | 3.60                      | 3.85                      | 3.67                      | 4.38                     
Dijkstra                  | -                         | 2.30                      | 2.68                      | 1.62                      | 3.64                      | 3.88                      | 3.81                      | 4.43                     
Euler                     | -                         | 2.57                      | 3.03                      | 2.06                      | 3.55                      | 3.87                      | 3.66                      | 4.36                     
Midpoint Explicit         | -                         | 2.91                      | 3.45                      | 3.07                      | 3.79                      | 4.15                      | 3.88                      | 4.55                     
Midpoint Fixed            | -                         | 3.28                      | 3.86                      | 3.29                      | 3.84                      | 4.16                      | 3.94                      | 4.64                     
RK4                       | -                         | 3.58                      | 4.18                      | 3.85                      | 4.27                      | 4.55                      | 4.34                      | 5.04                     
FD - L Convection         | -                         | 2.22                      | 2.69                      | 0.89                      | 3.51                      | 3.82                      | 3.58                      | 4.32                     
FD - NL Convection        | -                         | 3.12                      | 3.59                      | 0.91                      | 3.57                      | 3.84                      | 3.68                      | 4.32                     
FD - Poisson              | -                         | 3.21                      | 3.75                      | 1.36                      | 3.65                      | 3.94                      | 4.87                      | 4.44                     
FD - Laplace              | -                         | 6.29                      | 8.89                      | 3.10                      | 3.99                      | 4.25                      | 4.20                      | 4.85                     
M-D                       | -                         | 6.14                      | 7.72                      | 4.12                      | 4.31                      | 4.41                      | 4.46                      | 5.29                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 302.00 $\pm$ 2.00         | 2.90 $\pm$ 0.04           | 3.08 $\pm$ 0.07           | 10.70 $\pm$ 0.30          | 1.56 $\pm$ 0.00           | 1.57 $\pm$ 0.04           | 9.47 $\pm$ 0.24           | 3.95 $\pm$ 0.00          
Bellman Ford (ms)         | 1810.00 $\pm$ 60.00       | 5.27 $\pm$ 0.03           | 3.19 $\pm$ 0.05           | 3.86 $\pm$ 0.06           | 3.00 $\pm$ 0.02           | 6.02 $\pm$ 0.02           | 4.43 $\pm$ 0.01           | 18.70 $\pm$ 0.30         
Dijkstra (ms)             | 4920.00 $\pm$ 40.00       | 24.70 $\pm$ 0.20          | 16.60 $\pm$ 1.50          | 19.10 $\pm$ 0.30          | 18.20 $\pm$ 0.20          | 30.40 $\pm$ 0.20          | 23.20 $\pm$ 0.20          | 22.00 $\pm$ 0.20         
Euler (ms)                | 3890.00 $\pm$ 60.00       | 25.40 $\pm$ 0.40          | 25.50 $\pm$ 1.00          | 37.80 $\pm$ 0.40          | 15.30 $\pm$ 0.40          | 148.00 $\pm$ 9.00         | 13.70 $\pm$ 0.30          | 129.00 $\pm$ 3.00        
Midpoint Explicit (ms)    | 7860.00 $\pm$ 70.00       | 54.70 $\pm$ 4.10          | 51.70 $\pm$ 0.60          | 80.40 $\pm$ 6.10          | 23.70 $\pm$ 1.60          | 284.00 $\pm$ 3.00         | 16.20 $\pm$ 0.80          | 255.00 $\pm$ 2.00        
Midpoint Fixed (ms)       | 40000.00 $\pm$ 200.00     | 254.00 $\pm$ 1.00         | 92.40 $\pm$ 0.30          | 383.00 $\pm$ 4.00         | 75.60 $\pm$ 0.90          | 1410.00 $\pm$ 20.00       | 60.70 $\pm$ 1.30          | 1250.00 $\pm$ 10.00      
RK4 (ms)                  | 20100.00 $\pm$ 200.00     | 160.00 $\pm$ 2.00         | 35.80 $\pm$ 0.90          | 139.00 $\pm$ 2.00         | 35.20 $\pm$ 0.60          | 495.00 $\pm$ 4.00         | 37.20 $\pm$ 0.50          | 412.00 $\pm$ 4.00        
FD - L Convection (ms)    | 2240.00 $\pm$ 20.00       | 1.65 $\pm$ 0.03           | 1.56 $\pm$ 0.03           | 2.77 $\pm$ 0.07           | 1.68 $\pm$ 0.06           | 1.87 $\pm$ 0.03           | 1.33 $\pm$ 0.01           | 4.15 $\pm$ 0.05          
FD - NL Convection (ms)   | 2740.00 $\pm$ 10.00       | 1.79 $\pm$ 0.03           | 1.73 $\pm$ 0.06           | 2.94 $\pm$ 0.12           | 2.03 $\pm$ 0.19           | 2.18 $\pm$ 0.03           | 1.54 $\pm$ 0.04           | 4.15 $\pm$ 0.06          
FD - Poisson (ms)         | 6410.00 $\pm$ 90.00       | 2.99 $\pm$ 0.04           | 5.67 $\pm$ 0.04           | 7.35 $\pm$ 0.24           | 2.83 $\pm$ 0.04           | 3.86 $\pm$ 0.02           | 2.71 $\pm$ 0.02           | 5.73 $\pm$ 0.02          
FD - Laplace (ms)         | 608.00 $\pm$ 15.00        | 67.50 $\pm$ 1.70          | 151.00 $\pm$ 2.00         | 247.00 $\pm$ 1.00         | 60.50 $\pm$ 2.10          | 310.00 $\pm$ 2.00         | 63.90 $\pm$ 0.60          | 327.00 $\pm$ 1.00        
M-D (ms)                  | 15100.00 $\pm$ 100.00     | 15.30 $\pm$ 0.00          | 53.00 $\pm$ 0.20          | 59.50 $\pm$ 0.30          | 54.00 $\pm$ 0.10          | 59.90 $\pm$ 0.30          | 81.10 $\pm$ 0.10          | 62.30 $\pm$ 2.00         

![Python 3.10 compilation results](./version_specific_results/pypi_performance_310_compilation.svg)
![Python 3.10 execution results](./version_specific_results/pypi_performance_310_execution.svg)
## Python 3.11 results
### Performance Comparison (as of 1.12.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.20                      | 2.12                      | 0.29                      | 1.36                      | 1.27                      | 1.42                      | 1.39                     
Bellman Ford              | -                         | 3.35                      | 3.67                      | 1.13                      | 3.69                      | 3.87                      | 3.83                      | 4.48                     
Dijkstra                  | -                         | 2.18                      | 2.55                      | 1.55                      | 3.60                      | 3.82                      | 3.77                      | 4.36                     
Euler                     | -                         | 2.44                      | 2.90                      | 1.95                      | 3.49                      | 3.81                      | 3.60                      | 4.28                     
Midpoint Explicit         | -                         | 2.78                      | 3.26                      | 2.90                      | 3.73                      | 4.05                      | 3.86                      | 4.50                     
Midpoint Fixed            | -                         | 3.12                      | 3.69                      | 3.11                      | 3.78                      | 4.10                      | 3.90                      | 4.58                     
RK4                       | -                         | 3.40                      | 4.01                      | 3.61                      | 4.18                      | 4.44                      | 4.25                      | 4.96                     
FD - L Convection         | -                         | 2.15                      | 2.62                      | 0.84                      | 3.48                      | 3.78                      | 3.62                      | 4.29                     
FD - NL Convection        | -                         | 3.02                      | 3.50                      | 0.83                      | 3.48                      | 3.81                      | 3.66                      | 4.29                     
FD - Poisson              | -                         | 3.07                      | 3.56                      | 1.27                      | 3.61                      | 3.91                      | 4.82                      | 4.40                     
FD - Laplace              | -                         | 6.10                      | 8.65                      | 2.87                      | 3.90                      | 4.20                      | 4.15                      | 4.75                     
M-D                       | -                         | 6.13                      | 7.47                      | 3.98                      | 4.22                      | 4.36                      | 4.38                      | 5.21                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 434.00 $\pm$ 8.00         | 2.90 $\pm$ 0.05           | 3.06 $\pm$ 0.00           | 10.70 $\pm$ 0.30          | 1.56 $\pm$ 0.01           | 1.56 $\pm$ 0.01           | 9.89 $\pm$ 0.57           | 4.39 $\pm$ 0.09          
Bellman Ford (ms)         | 1890.00 $\pm$ 10.00       | 5.27 $\pm$ 0.03           | 3.18 $\pm$ 0.06           | 3.89 $\pm$ 0.16           | 3.01 $\pm$ 0.02           | 6.10 $\pm$ 0.03           | 4.06 $\pm$ 0.04           | 18.70 $\pm$ 0.40         
Dijkstra (ms)             | 4870.00 $\pm$ 80.00       | 23.50 $\pm$ 0.40          | 15.90 $\pm$ 0.10          | 18.90 $\pm$ 0.30          | 17.70 $\pm$ 0.60          | 30.10 $\pm$ 0.20          | 23.40 $\pm$ 0.30          | 21.70 $\pm$ 0.10         
Euler (ms)                | 3850.00 $\pm$ 30.00       | 25.40 $\pm$ 0.50          | 25.40 $\pm$ 1.00          | 37.30 $\pm$ 0.30          | 15.30 $\pm$ 0.70          | 144.00 $\pm$ 2.00         | 13.70 $\pm$ 0.40          | 128.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 7930.00 $\pm$ 130.00      | 52.60 $\pm$ 0.30          | 52.90 $\pm$ 2.20          | 76.90 $\pm$ 1.40          | 23.00 $\pm$ 0.50          | 285.00 $\pm$ 2.00         | 15.90 $\pm$ 0.40          | 253.00 $\pm$ 3.00        
Midpoint Fixed (ms)       | 40200.00 $\pm$ 400.00     | 257.00 $\pm$ 5.00         | 92.60 $\pm$ 1.10          | 367.00 $\pm$ 2.00         | 75.10 $\pm$ 0.50          | 1410.00 $\pm$ 20.00       | 61.40 $\pm$ 2.00          | 1240.00 $\pm$ 20.00      
RK4 (ms)                  | 19800.00 $\pm$ 100.00     | 162.00 $\pm$ 2.00         | 35.50 $\pm$ 0.60          | 137.00 $\pm$ 1.00         | 32.60 $\pm$ 1.00          | 499.00 $\pm$ 14.00        | 37.80 $\pm$ 0.60          | 415.00 $\pm$ 17.00       
FD - L Convection (ms)    | 2220.00 $\pm$ 20.00       | 1.66 $\pm$ 0.05           | 1.56 $\pm$ 0.04           | 2.73 $\pm$ 0.06           | 1.50 $\pm$ 0.05           | 1.74 $\pm$ 0.12           | 1.54 $\pm$ 0.04           | 4.19 $\pm$ 0.03          
FD - NL Convection (ms)   | 2750.00 $\pm$ 20.00       | 1.82 $\pm$ 0.18           | 1.70 $\pm$ 0.07           | 2.84 $\pm$ 0.05           | 1.97 $\pm$ 0.29           | 2.08 $\pm$ 0.12           | 1.53 $\pm$ 0.01           | 4.20 $\pm$ 0.03          
FD - Poisson (ms)         | 6190.00 $\pm$ 110.00      | 3.06 $\pm$ 0.22           | 5.65 $\pm$ 0.03           | 7.23 $\pm$ 0.06           | 2.79 $\pm$ 0.02           | 3.83 $\pm$ 0.02           | 2.67 $\pm$ 0.02           | 5.70 $\pm$ 0.02          
FD - Laplace (ms)         | 594.00 $\pm$ 3.00         | 68.00 $\pm$ 0.70          | 150.00 $\pm$ 1.00         | 246.00 $\pm$ 1.00         | 60.10 $\pm$ 2.10          | 257.00 $\pm$ 2.00         | 63.50 $\pm$ 0.50          | 327.00 $\pm$ 1.00        
M-D (ms)                  | 14900.00 $\pm$ 200.00     | 15.30 $\pm$ 0.10          | 53.20 $\pm$ 0.20          | 59.60 $\pm$ 0.30          | 54.80 $\pm$ 0.20          | 59.60 $\pm$ 0.20          | 80.30 $\pm$ 0.20          | 61.30 $\pm$ 0.20         

![Python 3.11 compilation results](./version_specific_results/pypi_performance_311_compilation.svg)
![Python 3.11 execution results](./version_specific_results/pypi_performance_311_execution.svg)
## Python 3.12 results
### Performance Comparison (as of 1.12.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.95                      | -                         | 0.30                      | 1.39                      | 1.32                      | 1.42                      | 1.40                     
Bellman Ford              | -                         | 3.33                      | -                         | 1.21                      | 3.78                      | 3.97                      | 3.83                      | 4.45                     
Dijkstra                  | -                         | 2.41                      | -                         | 1.74                      | 3.86                      | 3.99                      | 3.92                      | 4.55                     
Euler                     | -                         | 2.54                      | -                         | 2.03                      | 3.63                      | 3.94                      | 3.80                      | 4.43                     
Midpoint Explicit         | -                         | 3.01                      | -                         | 3.15                      | 4.15                      | 4.44                      | 4.24                      | 4.84                     
Midpoint Fixed            | -                         | 3.38                      | -                         | 3.28                      | 4.02                      | 4.47                      | 4.13                      | 4.85                     
RK4                       | -                         | 3.76                      | -                         | 3.85                      | 4.59                      | 5.13                      | 4.85                      | 5.52                     
FD - L Convection         | -                         | 2.44                      | -                         | 0.95                      | 3.83                      | 4.08                      | 3.89                      | 4.64                     
FD - NL Convection        | -                         | 3.22                      | -                         | 0.88                      | 3.75                      | 3.97                      | 3.81                      | 4.44                     
FD - Poisson              | -                         | 3.35                      | -                         | 1.37                      | 3.81                      | 4.16                      | 5.15                      | 4.70                     
FD - Laplace              | -                         | 6.38                      | -                         | 3.19                      | 4.23                      | 4.44                      | 4.40                      | 5.01                     
M-D                       | -                         | 6.47                      | -                         | 4.09                      | 4.62                      | 4.61                      | 4.78                      | 5.46                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 437.00 $\pm$ 8.00         | 2.95 $\pm$ 0.02           | -                         | 10.80 $\pm$ 0.30          | 1.56 $\pm$ 0.01           | 1.61 $\pm$ 0.01           | 10.60 $\pm$ 0.20          | 4.37 $\pm$ 0.01          
Bellman Ford (ms)         | 2530.00 $\pm$ 40.00       | 4.59 $\pm$ 0.01           | -                         | 3.87 $\pm$ 0.07           | 3.01 $\pm$ 0.02           | 5.62 $\pm$ 0.02           | 4.25 $\pm$ 0.05           | 18.60 $\pm$ 0.30         
Dijkstra (ms)             | 6850.00 $\pm$ 40.00       | 26.80 $\pm$ 0.20          | -                         | 20.90 $\pm$ 0.50          | 19.10 $\pm$ 0.70          | 29.40 $\pm$ 0.10          | 23.00 $\pm$ 0.20          | 22.30 $\pm$ 0.40         
Euler (ms)                | 4900.00 $\pm$ 40.00       | 25.40 $\pm$ 0.30          | -                         | 37.80 $\pm$ 0.50          | 15.50 $\pm$ 0.70          | 144.00 $\pm$ 2.00         | 13.80 $\pm$ 0.40          | 128.00 $\pm$ 1.00        
Midpoint Explicit (ms)    | 9820.00 $\pm$ 50.00       | 52.60 $\pm$ 0.40          | -                         | 78.10 $\pm$ 0.60          | 24.40 $\pm$ 1.00          | 285.00 $\pm$ 4.00         | 16.60 $\pm$ 0.60          | 256.00 $\pm$ 3.00        
Midpoint Fixed (ms)       | 48700.00 $\pm$ 400.00     | 254.00 $\pm$ 1.00         | -                         | 387.00 $\pm$ 2.00         | 75.40 $\pm$ 0.70          | 1410.00 $\pm$ 20.00       | 62.60 $\pm$ 3.30          | 1260.00 $\pm$ 30.00      
RK4 (ms)                  | 24500.00 $\pm$ 100.00     | 165.00 $\pm$ 17.00        | -                         | 147.00 $\pm$ 15.00        | 36.40 $\pm$ 0.60          | 498.00 $\pm$ 11.00        | 38.90 $\pm$ 0.30          | 417.00 $\pm$ 14.00       
FD - L Convection (ms)    | 2950.00 $\pm$ 30.00       | 1.63 $\pm$ 0.01           | -                         | 2.73 $\pm$ 0.03           | 1.69 $\pm$ 0.01           | 1.75 $\pm$ 0.13           | 1.53 $\pm$ 0.01           | 4.21 $\pm$ 0.03          
FD - NL Convection (ms)   | 3640.00 $\pm$ 40.00       | 1.81 $\pm$ 0.04           | -                         | 2.83 $\pm$ 0.03           | 1.94 $\pm$ 0.23           | 1.97 $\pm$ 0.01           | 1.40 $\pm$ 0.01           | 4.24 $\pm$ 0.09          
FD - Poisson (ms)         | 8120.00 $\pm$ 110.00      | 2.97 $\pm$ 0.04           | -                         | 7.25 $\pm$ 0.05           | 2.83 $\pm$ 0.03           | 3.82 $\pm$ 0.04           | 2.68 $\pm$ 0.01           | 5.75 $\pm$ 0.14          
FD - Laplace (ms)         | 602.00 $\pm$ 11.00        | 69.60 $\pm$ 1.70          | -                         | 248.00 $\pm$ 1.00         | 62.60 $\pm$ 3.70          | 257.00 $\pm$ 2.00         | 64.20 $\pm$ 1.60          | 329.00 $\pm$ 1.00        
M-D (ms)                  | 18900.00 $\pm$ 100.00     | 15.20 $\pm$ 0.00          | -                         | 60.30 $\pm$ 2.30          | 55.20 $\pm$ 1.90          | 59.80 $\pm$ 0.70          | 81.30 $\pm$ 0.30          | 61.90 $\pm$ 0.50         

![Python 3.12 compilation results](./version_specific_results/pypi_performance_312_compilation.svg)
![Python 3.12 execution results](./version_specific_results/pypi_performance_312_execution.svg)
