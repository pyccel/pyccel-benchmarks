### Performance Comparison (as of 1.8.0)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 3.19                      | 0.53                      | 1.49                      | 1.41                     
Bellman Ford              | -                         | 4.38                      | 1.51                      | 2.61                      | 2.60                     
Dijkstra                  | -                         | 3.27                      | 1.62                      | 2.80                      | 2.63                     
Euler                     | -                         | 3.89                      | 2.26                      | 2.59                      | 2.65                     
Midpoint Explicit         | -                         | 4.22                      | 3.04                      | 2.89                      | 2.96                     
Midpoint Fixed            | -                         | 4.99                      | 3.19                      | 2.95                      | 3.05                     
RK4                       | -                         | 5.54                      | 3.61                      | 3.75                      | 3.80                     
FD - L Convection         | -                         | 3.28                      | 1.24                      | 2.54                      | 2.55                     
FD - NL Convection        | -                         | 4.14                      | 1.33                      | 2.51                      | 2.53                     
FD - Poisson              | -                         | 4.33                      | 1.80                      | 2.69                      | 2.74                     
FD - Laplace              | -                         | 8.66                      | 3.31                      | 3.24                      | 3.35                     
M-D                       | -                         | 8.85                      | 3.87                      | 3.77                      | 3.38                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 491.00 $\pm$ 18.00        | 8.51 $\pm$ 0.38           | 28.90 $\pm$ 1.70          | 2.23 $\pm$ 0.12           | 2.25 $\pm$ 0.13          
Bellman Ford (ms)         | 3170.00 $\pm$ 40.00       | 6.79 $\pm$ 0.28           | 7.27 $\pm$ 0.31           | 4.92 $\pm$ 0.16           | 9.60 $\pm$ 0.42          
Dijkstra (ms)             | 8260.00 $\pm$ 170.00      | 44.60 $\pm$ 1.90          | 47.40 $\pm$ 2.70          | 40.60 $\pm$ 1.70          | 56.90 $\pm$ 3.20         
Euler (ms)                | 5490.00 $\pm$ 130.00      | 51.30 $\pm$ 7.90          | 122.00 $\pm$ 5.00         | 22.90 $\pm$ 1.30          | 264.00 $\pm$ 10.00       
Midpoint Explicit (ms)    | 11600.00 $\pm$ 600.00     | 89.20 $\pm$ 3.50          | 241.00 $\pm$ 11.00        | 36.70 $\pm$ 3.20          | 521.00 $\pm$ 19.00       
Midpoint Fixed (s)        | 58.50 $\pm$ 3.60          | 0.74 $\pm$ 0.02           | 1.22 $\pm$ 0.07           | 0.12 $\pm$ 0.01           | 2.51 $\pm$ 0.07          
RK4 (ms)                  | 28300.00 $\pm$ 1700.00    | 230.00 $\pm$ 11.00        | 463.00 $\pm$ 15.00        | 48.00 $\pm$ 2.60          | 837.00 $\pm$ 27.00       
FD - L Convection (ms)    | 3590.00 $\pm$ 70.00       | 3.72 $\pm$ 0.14           | 4.57 $\pm$ 0.13           | 3.19 $\pm$ 0.38           | 4.72 $\pm$ 0.56          
FD - NL Convection (ms)   | 4490.00 $\pm$ 70.00       | 4.27 $\pm$ 0.12           | 5.26 $\pm$ 0.69           | 3.24 $\pm$ 0.37           | 5.78 $\pm$ 0.65          
FD - Poisson (ms)         | 9960.00 $\pm$ 400.00      | 9.72 $\pm$ 0.46           | 12.90 $\pm$ 0.50          | 8.44 $\pm$ 0.23           | 11.80 $\pm$ 0.30         
FD - Laplace (ms)         | 1170.00 $\pm$ 20.00       | 334.00 $\pm$ 11.00        | 563.00 $\pm$ 9.00         | 191.00 $\pm$ 4.00         | 558.00 $\pm$ 11.00       
M-D (ms)                  | 21700.00 $\pm$ 400.00     | 61.00 $\pm$ 3.00          | 103.00 $\pm$ 2.00         | 138.00 $\pm$ 3.00         | 143.00 $\pm$ 2.00        
