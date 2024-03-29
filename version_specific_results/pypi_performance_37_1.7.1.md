### Performance Comparison (as of 1.7.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.06                      | 0.38                      | 1.60                      | 1.48                     
Bellman Ford              | -                         | 2.69                      | 1.04                      | 2.49                      | 2.42                     
Dijkstra                  | -                         | 2.78                      | 1.39                      | 2.58                      | 2.52                     
Euler                     | -                         | 3.26                      | 1.46                      | 2.49                      | 2.48                     
Midpoint Explicit         | -                         | 3.79                      | 2.27                      | 2.83                      | 2.85                     
Midpoint Fixed            | -                         | 4.54                      | 2.59                      | 2.90                      | 2.94                     
RK4                       | -                         | 4.60                      | 2.64                      | 3.53                      | 3.46                     
FD - L Convection         | -                         | 2.42                      | 0.34                      | 2.33                      | 2.40                     
FD - NL Convection        | -                         | 2.43                      | 0.34                      | 2.34                      | 2.42                     
FD - Poisson              | -                         | 6.87                      | 0.83                      | 2.49                      | 2.48                     
FD - Laplace              | -                         | 10.45                     | 2.56                      | 3.14                      | -                        
M-D                       | -                         | -                         | 5.91                      | 3.72                      | 3.44                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 512.00 $\pm$ 14.00        | 4.00 $\pm$ 0.08           | 19.70 $\pm$ 0.70          | 2.30 $\pm$ 0.05           | 2.57 $\pm$ 0.06          
Bellman Ford (ns)         | 68600.00 $\pm$ 1800.00    | 398.00 $\pm$ 11.00        | 588.00 $\pm$ 18.00        | 241.00 $\pm$ 7.00         | 534.00 $\pm$ 14.00       
Dijkstra (ns)             | 36300.00 $\pm$ 1100.00    | 349.00 $\pm$ 10.00        | 407.00 $\pm$ 12.00        | 306.00 $\pm$ 9.00         | 523.00 $\pm$ 15.00       
Euler (ms)                | 59.50 $\pm$ 2.60          | 0.76 $\pm$ 0.02           | 1.21 $\pm$ 0.04           | 0.14 $\pm$ 0.00           | 3.26 $\pm$ 0.10          
Midpoint Explicit (ms)    | 121.00 $\pm$ 3.00         | 1.70 $\pm$ 0.04           | 3.13 $\pm$ 0.13           | 0.24 $\pm$ 0.01           | 5.80 $\pm$ 0.14          
Midpoint Fixed (ms)       | 608.00 $\pm$ 16.00        | 10.40 $\pm$ 0.80          | 17.30 $\pm$ 0.50          | 1.03 $\pm$ 0.03           | 25.70 $\pm$ 0.70         
RK4 (ms)                  | 279.00 $\pm$ 9.00         | 2.36 $\pm$ 0.05           | 6.22 $\pm$ 0.19           | 0.29 $\pm$ 0.01           | 6.90 $\pm$ 0.22          
FD - L Convection (ms)    | 2390.00 $\pm$ 50.00       | 2.48 $\pm$ 0.07           | 10.20 $\pm$ 0.20          | 1.64 $\pm$ 0.04           | 1.87 $\pm$ 0.06          
FD - NL Convection (ms)   | 3400.00 $\pm$ 50.00       | 3.76 $\pm$ 0.14           | 10.10 $\pm$ 0.20          | 1.73 $\pm$ 0.05           | 1.82 $\pm$ 0.04          
FD - Poisson (ms)         | 5000.00 $\pm$ 60.00       | 3.46 $\pm$ 0.07           | 11.30 $\pm$ 0.20          | 4.29 $\pm$ 0.12           | 1.90 $\pm$ 0.04          
FD - Laplace (ms)         | 568.00 $\pm$ 15.00        | 324.00 $\pm$ 9.00         | 623.00 $\pm$ 12.00        | 117.00 $\pm$ 3.00         | -                        
M-D (ms)                  | 57000.00 $\pm$ 1200.00    | -                         | 246.00 $\pm$ 7.00         | 304.00 $\pm$ 16.00        | 297.00 $\pm$ 9.00        
