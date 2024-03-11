### Performance Comparison (as of 1.11.2)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.53                      | 2.39                      | 0.34                      | 1.29                      | 1.22                      | 1.36                      | 1.38                     
Bellman Ford              | -                         | 3.70                      | 3.94                      | 1.12                      | 2.44                      | 2.69                      | 2.58                      | 3.39                     
Dijkstra                  | -                         | 2.53                      | 2.91                      | 1.62                      | 2.49                      | 2.65                      | 2.64                      | 3.44                     
Euler                     | -                         | 3.01                      | 3.49                      | 2.07                      | 2.44                      | 2.70                      | 2.56                      | 3.36                     
Midpoint Explicit         | -                         | 3.47                      | 3.95                      | 3.18                      | 2.78                      | 2.90                      | 2.78                      | 3.63                     
Midpoint Fixed            | -                         | 3.69                      | 4.53                      | 3.31                      | 2.70                      | 3.04                      | 2.88                      | 3.84                     
RK4                       | -                         | 4.07                      | 4.82                      | 3.94                      | 3.24                      | 3.31                      | 3.25                      | 4.26                     
FD - L Convection         | -                         | 2.45                      | 2.89                      | 0.91                      | 2.39                      | 2.53                      | 2.49                      | 3.32                     
FD - NL Convection        | -                         | 3.53                      | 3.92                      | 0.93                      | 2.41                      | 2.56                      | 2.55                      | 3.32                     
FD - Poisson              | -                         | 3.55                      | 4.09                      | 1.40                      | 2.53                      | 2.68                      | 3.02                      | 3.41                     
FD - Laplace              | -                         | 7.03                      | 9.02                      | 3.11                      | 2.78                      | 3.07                      | 3.18                      | 4.06                     
M-D                       | -                         | 6.91                      | 8.01                      | 4.15                      | 3.16                      | 3.20                      | 3.32                      | 4.35                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 315.00 $\pm$ 4.00         | 2.99 $\pm$ 0.11           | 3.47 $\pm$ 0.01           | 10.70 $\pm$ 0.20          | 1.50 $\pm$ 0.01           | 1.50 $\pm$ 0.00           | 9.21 $\pm$ 0.11           | 3.93 $\pm$ 0.01          
Bellman Ford (ms)         | 1780.00 $\pm$ 20.00       | 4.18 $\pm$ 0.03           | 3.26 $\pm$ 0.06           | 3.84 $\pm$ 0.07           | 3.02 $\pm$ 0.04           | 6.05 $\pm$ 0.03           | 4.28 $\pm$ 0.09           | 18.70 $\pm$ 0.20         
Dijkstra (ms)             | 4940.00 $\pm$ 50.00       | 23.90 $\pm$ 0.50          | 17.70 $\pm$ 0.60          | 21.70 $\pm$ 1.10          | 20.60 $\pm$ 0.50          | 31.70 $\pm$ 0.50          | 24.80 $\pm$ 0.70          | 23.70 $\pm$ 0.30         
Euler (ms)                | 3960.00 $\pm$ 40.00       | 29.40 $\pm$ 0.40          | 29.10 $\pm$ 0.40          | 39.70 $\pm$ 1.30          | 16.10 $\pm$ 0.50          | 146.00 $\pm$ 3.00         | 15.10 $\pm$ 0.50          | 129.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 7970.00 $\pm$ 40.00       | 59.80 $\pm$ 0.30          | 57.20 $\pm$ 0.70          | 81.80 $\pm$ 2.40          | 23.60 $\pm$ 0.70          | 284.00 $\pm$ 8.00         | 16.20 $\pm$ 0.40          | 256.00 $\pm$ 6.00        
Midpoint Fixed (ms)       | 40600.00 $\pm$ 200.00     | 258.00 $\pm$ 1.00         | 63.70 $\pm$ 0.40          | 434.00 $\pm$ 157.00       | 75.70 $\pm$ 0.70          | 1420.00 $\pm$ 20.00       | 61.00 $\pm$ 1.90          | 1260.00 $\pm$ 30.00      
RK4 (ms)                  | 20100.00 $\pm$ 100.00     | 162.00 $\pm$ 3.00         | 38.80 $\pm$ 0.60          | 162.00 $\pm$ 51.00        | 33.60 $\pm$ 0.50          | 489.00 $\pm$ 4.00         | 38.50 $\pm$ 0.60          | 418.00 $\pm$ 14.00       
FD - L Convection (ms)    | 2290.00 $\pm$ 20.00       | 1.67 $\pm$ 0.07           | 1.58 $\pm$ 0.02           | 2.73 $\pm$ 0.05           | 1.54 $\pm$ 0.11           | 1.71 $\pm$ 0.11           | 1.51 $\pm$ 0.01           | 3.70 $\pm$ 0.01          
FD - NL Convection (ms)   | 2840.00 $\pm$ 20.00       | 1.87 $\pm$ 0.06           | 1.83 $\pm$ 0.04           | 2.85 $\pm$ 0.10           | 2.04 $\pm$ 0.17           | 2.13 $\pm$ 0.08           | 1.40 $\pm$ 0.01           | 3.76 $\pm$ 0.08          
FD - Poisson (ms)         | 6480.00 $\pm$ 100.00      | 3.02 $\pm$ 0.05           | 2.71 $\pm$ 0.05           | 7.22 $\pm$ 0.04           | 2.79 $\pm$ 0.01           | 3.80 $\pm$ 0.03           | 2.70 $\pm$ 0.05           | 8.95 $\pm$ 0.03          
FD - Laplace (ms)         | 602.00 $\pm$ 15.00        | 68.50 $\pm$ 0.40          | 152.00 $\pm$ 1.00         | 246.00 $\pm$ 1.00         | 62.80 $\pm$ 0.50          | 259.00 $\pm$ 1.00         | 64.00 $\pm$ 0.60          | 306.00 $\pm$ 1.00        
M-D (ms)                  | 15200.00 $\pm$ 100.00     | 15.20 $\pm$ 0.00          | 52.00 $\pm$ 0.20          | 59.80 $\pm$ 1.30          | 54.20 $\pm$ 0.10          | 59.50 $\pm$ 0.30          | 69.20 $\pm$ 0.60          | 60.40 $\pm$ 0.50         