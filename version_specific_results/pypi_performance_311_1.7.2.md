### Performance Comparison (as of 1.7.2)
## Compilation time
Algorithm                 | python                    | pythran                   | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.03                      | 1.57                      | 1.50                     
Bellman Ford              | -                         | 3.34                      | 2.45                      | 2.41                     
Dijkstra                  | -                         | 2.53                      | 2.50                      | 2.46                     
Euler                     | -                         | 2.94                      | 2.43                      | 2.48                     
Midpoint Explicit         | -                         | 3.36                      | 2.74                      | 2.80                     
Midpoint Fixed            | -                         | 4.02                      | 2.83                      | 2.86                     
RK4                       | -                         | 4.39                      | 3.30                      | 3.33                     
FD - L Convection         | -                         | 2.67                      | 2.38                      | 2.40                     
FD - NL Convection        | -                         | 3.39                      | 2.38                      | 2.43                     
FD - Poisson              | -                         | 4.06                      | 2.59                      | 2.56                     
FD - Laplace              | -                         | 8.23                      | 2.99                      | 3.03                     
M-D                       | -                         | 7.03                      | 3.32                      | 3.16                     

## Execution time
Algorithm                 | python                    | pythran                   | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 399.00 $\pm$ 3.00         | 9.73 $\pm$ 0.02           | 3.28 $\pm$ 0.00           | 3.26 $\pm$ 0.00          
Bellman Ford (ms)         | 2660.00 $\pm$ 20.00       | 6.46 $\pm$ 0.01           | 4.46 $\pm$ 0.01           | 6.59 $\pm$ 0.01          
Dijkstra (ms)             | 6520.00 $\pm$ 40.00       | 40.90 $\pm$ 2.90          | 31.00 $\pm$ 0.50          | 48.30 $\pm$ 0.40         
Euler (ms)                | 4920.00 $\pm$ 20.00       | 37.60 $\pm$ 0.60          | 19.60 $\pm$ 1.00          | 201.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 9840.00 $\pm$ 80.00       | 73.40 $\pm$ 0.60          | 29.40 $\pm$ 1.10          | 402.00 $\pm$ 10.00       
Midpoint Fixed (s)        | 49.10 $\pm$ 0.30          | 0.63 $\pm$ 0.01           | 0.10 $\pm$ 0.00           | 1.98 $\pm$ 0.03          
RK4 (ms)                  | 24700.00 $\pm$ 300.00     | 220.00 $\pm$ 3.00         | 34.30 $\pm$ 0.70          | 517.00 $\pm$ 7.00        
FD - L Convection (ms)    | 2630.00 $\pm$ 50.00       | 4.92 $\pm$ 0.00           | 2.59 $\pm$ 0.05           | 2.62 $\pm$ 0.13          
FD - NL Convection (ms)   | 3210.00 $\pm$ 20.00       | 4.13 $\pm$ 0.01           | 2.52 $\pm$ 0.01           | 2.64 $\pm$ 0.16          
FD - Poisson (ms)         | 8130.00 $\pm$ 260.00      | 6.36 $\pm$ 0.01           | 4.34 $\pm$ 0.00           | 5.31 $\pm$ 0.01          
FD - Laplace (ms)         | 683.00 $\pm$ 4.00         | 227.00 $\pm$ 0.00         | 81.80 $\pm$ 0.30          | 366.00 $\pm$ 1.00        
M-D (ms)                  | 19800.00 $\pm$ 100.00     | 65.40 $\pm$ 0.20          | 120.00 $\pm$ 0.00         | 127.00 $\pm$ 17.00       