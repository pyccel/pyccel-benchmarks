### Performance Comparison (as of 1.7.2)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.80                      | 0.33                      | 1.39                      | 1.31                     
Bellman Ford              | -                         | 3.14                      | 1.08                      | 2.27                      | 2.22                     
Dijkstra                  | -                         | 2.34                      | 1.20                      | 2.32                      | 2.24                     
Euler                     | -                         | 2.74                      | 1.66                      | 2.22                      | 2.26                     
Midpoint Explicit         | -                         | 3.18                      | 2.35                      | 2.60                      | 2.60                     
Midpoint Fixed            | -                         | 3.87                      | 2.68                      | 2.61                      | 2.66                     
RK4                       | -                         | 4.20                      | 2.99                      | 3.18                      | 3.17                     
FD - L Convection         | -                         | 2.48                      | 0.96                      | 2.21                      | 2.22                     
FD - NL Convection        | -                         | 3.20                      | 1.00                      | 2.19                      | 2.21                     
FD - Poisson              | -                         | 3.87                      | 1.43                      | 2.39                      | 2.37                     
FD - Laplace              | -                         | 7.90                      | 2.77                      | 2.81                      | 2.88                     
M-D                       | -                         | 6.83                      | 3.27                      | 3.21                      | 3.00                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 478.00 $\pm$ 3.00         | 9.74 $\pm$ 0.02           | 32.30 $\pm$ 0.30          | 3.14 $\pm$ 0.00           | 3.28 $\pm$ 0.00          
Bellman Ford (ms)         | 2610.00 $\pm$ 70.00       | 6.46 $\pm$ 0.01           | 10.50 $\pm$ 0.00          | 4.45 $\pm$ 0.00           | 6.57 $\pm$ 0.00          
Dijkstra (ms)             | 6870.00 $\pm$ 20.00       | 37.90 $\pm$ 0.40          | 32.10 $\pm$ 0.60          | 29.60 $\pm$ 0.50          | 47.50 $\pm$ 0.50         
Euler (ms)                | 4640.00 $\pm$ 30.00       | 36.80 $\pm$ 0.50          | 125.00 $\pm$ 1.00         | 17.10 $\pm$ 0.40          | 201.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 9430.00 $\pm$ 60.00       | 73.70 $\pm$ 0.70          | 318.00 $\pm$ 7.00         | 29.10 $\pm$ 0.70          | 400.00 $\pm$ 4.00        
Midpoint Fixed (s)        | 48.50 $\pm$ 0.60          | 0.63 $\pm$ 0.02           | 1.75 $\pm$ 0.01           | 0.10 $\pm$ 0.00           | 1.97 $\pm$ 0.01          
RK4 (ms)                  | 23800.00 $\pm$ 300.00     | 219.00 $\pm$ 1.00         | 638.00 $\pm$ 8.00         | 33.70 $\pm$ 0.60          | 526.00 $\pm$ 17.00       
FD - L Convection (ms)    | 3130.00 $\pm$ 50.00       | 4.92 $\pm$ 0.00           | 13.80 $\pm$ 0.10          | 2.64 $\pm$ 0.13           | 2.93 $\pm$ 0.06          
FD - NL Convection (ms)   | 3840.00 $\pm$ 50.00       | 4.13 $\pm$ 0.01           | 14.80 $\pm$ 0.10          | 2.47 $\pm$ 0.06           | 2.93 $\pm$ 0.05          
FD - Poisson (ms)         | 8090.00 $\pm$ 30.00       | 6.43 $\pm$ 0.00           | 18.90 $\pm$ 0.00          | 4.28 $\pm$ 0.01           | 5.30 $\pm$ 0.01          
FD - Laplace (ms)         | 683.00 $\pm$ 4.00         | 226.00 $\pm$ 0.00         | 397.00 $\pm$ 3.00         | 81.70 $\pm$ 0.50          | 365.00 $\pm$ 1.00        
M-D (ms)                  | 20400.00 $\pm$ 300.00     | 65.70 $\pm$ 1.10          | 91.30 $\pm$ 0.80          | 120.00 $\pm$ 0.00         | 121.00 $\pm$ 0.00        
