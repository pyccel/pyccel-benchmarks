### Performance Comparison (as of 1.10.0)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.98                      | 0.39                      | 1.22                      | 1.18                     
Bellman Ford              | -                         | 3.33                      | 1.22                      | 2.18                      | 2.13                     
Dijkstra                  | -                         | 2.55                      | 1.35                      | 2.25                      | 2.16                     
Euler                     | -                         | 2.93                      | 1.81                      | 2.11                      | 2.14                     
Midpoint Explicit         | -                         | 3.33                      | 2.54                      | 2.48                      | 2.50                     
Midpoint Fixed            | -                         | 3.83                      | 2.69                      | 2.51                      | 2.55                     
RK4                       | -                         | 4.24                      | 3.01                      | 3.08                      | 3.07                     
FD - L Convection         | -                         | 2.36                      | 0.96                      | 2.05                      | 2.07                     
FD - NL Convection        | -                         | 3.09                      | 1.03                      | 2.09                      | 2.13                     
FD - Poisson              | -                         | 3.39                      | 1.49                      | 2.25                      | 2.27                     
FD - Laplace              | -                         | 6.72                      | 2.87                      | 2.68                      | 2.73                     
M-D                       | -                         | 6.98                      | 3.38                      | 3.20                      | 2.94                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 402.00 $\pm$ 1.00         | 9.90 $\pm$ 0.03           | 27.50 $\pm$ 0.80          | 3.20 $\pm$ 0.00           | 3.26 $\pm$ 0.00          
Bellman Ford (ms)         | 2600.00 $\pm$ 10.00       | 6.73 $\pm$ 0.00           | 6.34 $\pm$ 0.02           | 4.45 $\pm$ 0.00           | 6.57 $\pm$ 0.01          
Dijkstra (ms)             | 6880.00 $\pm$ 20.00       | 39.40 $\pm$ 0.40          | 34.10 $\pm$ 0.70          | 31.60 $\pm$ 1.70          | 49.10 $\pm$ 0.70         
Euler (ms)                | 4930.00 $\pm$ 80.00       | 41.50 $\pm$ 11.00         | 108.00 $\pm$ 0.00         | 18.80 $\pm$ 0.90          | 205.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 10100.00 $\pm$ 200.00     | 76.10 $\pm$ 0.40          | 214.00 $\pm$ 9.00         | 29.00 $\pm$ 0.60          | 404.00 $\pm$ 5.00        
Midpoint Fixed (s)        | 50.70 $\pm$ 0.30          | 0.60 $\pm$ 0.01           | 1.09 $\pm$ 0.02           | 0.10 $\pm$ 0.00           | 2.01 $\pm$ 0.08          
RK4 (ms)                  | 25300.00 $\pm$ 200.00     | 218.00 $\pm$ 1.00         | 411.00 $\pm$ 10.00        | 42.40 $\pm$ 2.60          | 671.00 $\pm$ 9.00        
FD - L Convection (ms)    | 3080.00 $\pm$ 20.00       | 2.81 $\pm$ 0.00           | 3.19 $\pm$ 0.15           | 1.63 $\pm$ 0.02           | 2.48 $\pm$ 0.06          
FD - NL Convection (ms)   | 3870.00 $\pm$ 10.00       | 3.08 $\pm$ 0.00           | 3.36 $\pm$ 0.06           | 1.64 $\pm$ 0.01           | 2.53 $\pm$ 0.00          
FD - Poisson (ms)         | 8920.00 $\pm$ 220.00      | 5.78 $\pm$ 0.00           | 10.20 $\pm$ 0.30          | 4.20 $\pm$ 0.01           | 5.30 $\pm$ 0.01          
FD - Laplace (ms)         | 731.00 $\pm$ 5.00         | 251.00 $\pm$ 1.00         | 390.00 $\pm$ 5.00         | 78.50 $\pm$ 1.60          | 316.00 $\pm$ 2.00        
M-D (ms)                  | 20800.00 $\pm$ 100.00     | 65.20 $\pm$ 0.00          | 79.50 $\pm$ 1.40          | 120.00 $\pm$ 0.00         | 122.00 $\pm$ 0.00        