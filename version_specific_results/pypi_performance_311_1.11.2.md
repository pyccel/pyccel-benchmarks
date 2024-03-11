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