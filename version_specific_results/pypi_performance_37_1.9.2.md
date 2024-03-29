### Performance Comparison (as of 1.9.2)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.43                      | 0.45                      | 1.50                      | 1.41                     
Bellman Ford              | -                         | 4.00                      | 1.42                      | 2.57                      | 2.51                     
Dijkstra                  | -                         | 3.14                      | 1.61                      | 2.75                      | 2.63                     
Euler                     | -                         | 3.58                      | 2.21                      | 2.52                      | 2.51                     
Midpoint Explicit         | -                         | 4.15                      | 3.03                      | 2.99                      | 2.94                     
Midpoint Fixed            | -                         | 4.77                      | 3.47                      | 3.05                      | 3.13                     
RK4                       | -                         | 5.40                      | 3.90                      | 3.73                      | 3.75                     
FD - L Convection         | -                         | 3.00                      | 1.30                      | 2.48                      | 2.60                     
FD - NL Convection        | -                         | 3.85                      | 1.32                      | 2.52                      | 2.60                     
FD - Poisson              | -                         | 4.19                      | 1.89                      | 2.68                      | 2.75                     
FD - Laplace              | -                         | 8.45                      | 3.57                      | 3.31                      | 3.27                     
M-D                       | -                         | 8.73                      | 4.02                      | 3.86                      | 3.53                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 571.00 $\pm$ 18.00        | 8.80 $\pm$ 0.30           | 32.80 $\pm$ 1.10          | 2.27 $\pm$ 0.14           | 2.24 $\pm$ 0.08          
Bellman Ford (ms)         | 3100.00 $\pm$ 80.00       | 8.34 $\pm$ 0.44           | 11.60 $\pm$ 0.60          | 5.15 $\pm$ 0.16           | 9.63 $\pm$ 0.31          
Dijkstra (ms)             | 8680.00 $\pm$ 180.00      | 45.20 $\pm$ 1.70          | 46.80 $\pm$ 1.60          | 39.30 $\pm$ 1.40          | 57.00 $\pm$ 2.00         
Euler (ms)                | 6500.00 $\pm$ 190.00      | 55.30 $\pm$ 2.80          | 105.00 $\pm$ 7.00         | 27.80 $\pm$ 1.50          | 263.00 $\pm$ 7.00        
Midpoint Explicit (ms)    | 13200.00 $\pm$ 200.00     | 105.00 $\pm$ 5.00         | 267.00 $\pm$ 11.00        | 43.60 $\pm$ 1.90          | 520.00 $\pm$ 15.00       
Midpoint Fixed (s)        | 67.10 $\pm$ 1.10          | 0.78 $\pm$ 0.03           | 1.48 $\pm$ 0.04           | 0.15 $\pm$ 0.01           | 2.57 $\pm$ 0.04          
RK4 (ms)                  | 30400.00 $\pm$ 500.00     | 259.00 $\pm$ 8.00         | 539.00 $\pm$ 21.00        | 58.30 $\pm$ 2.30          | 856.00 $\pm$ 15.00       
FD - L Convection (ms)    | 3500.00 $\pm$ 80.00       | 3.70 $\pm$ 0.14           | 18.40 $\pm$ 1.00          | 2.24 $\pm$ 0.06           | 3.62 $\pm$ 0.06          
FD - NL Convection (ms)   | 4860.00 $\pm$ 40.00       | 4.48 $\pm$ 0.15           | 17.30 $\pm$ 0.50          | 2.42 $\pm$ 0.10           | 3.58 $\pm$ 0.09          
FD - Poisson (ms)         | 10600.00 $\pm$ 100.00     | 13.30 $\pm$ 0.60          | 24.80 $\pm$ 0.80          | 7.54 $\pm$ 0.16           | 10.10 $\pm$ 0.40         
FD - Laplace (ms)         | 1100.00 $\pm$ 10.00       | 367.00 $\pm$ 6.00         | 552.00 $\pm$ 15.00        | 171.00 $\pm$ 4.00         | 480.00 $\pm$ 5.00        
M-D (ms)                  | 24600.00 $\pm$ 500.00     | 73.00 $\pm$ 2.40          | 107.00 $\pm$ 5.00         | 128.00 $\pm$ 6.00         | 128.00 $\pm$ 2.00        
