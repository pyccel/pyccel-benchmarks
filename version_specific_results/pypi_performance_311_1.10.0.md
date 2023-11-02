### Performance Comparison (as of 1.10.0)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.58                      | 0.35                      | 1.39                      | 1.30                     
Bellman Ford              | -                         | 3.64                      | 1.22                      | 2.34                      | 2.25                     
Dijkstra                  | -                         | 2.82                      | 1.36                      | 2.43                      | 2.37                     
Euler                     | -                         | 3.14                      | 1.77                      | 2.27                      | 2.27                     
Midpoint Explicit         | -                         | 3.55                      | 2.39                      | 2.60                      | 2.65                     
Midpoint Fixed            | -                         | 4.25                      | 2.64                      | 2.71                      | 2.73                     
RK4                       | -                         | 4.69                      | 2.91                      | 3.20                      | 3.18                     
FD - L Convection         | -                         | 2.66                      | 0.99                      | 2.17                      | 2.22                     
FD - NL Convection        | -                         | 3.53                      | 1.01                      | 2.26                      | 2.28                     
FD - Poisson              | -                         | 3.73                      | 1.47                      | 2.35                      | 2.42                     
FD - Laplace              | -                         | 7.39                      | 2.75                      | 2.79                      | 2.87                     
M-D                       | -                         | 7.45                      | 3.27                      | 3.26                      | 3.08                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 550.00 $\pm$ 25.00        | 8.04 $\pm$ 0.03           | 28.10 $\pm$ 0.20          | 2.98 $\pm$ 0.01           | 3.31 $\pm$ 0.01          
Bellman Ford (ms)         | 2880.00 $\pm$ 20.00       | 7.72 $\pm$ 0.01           | 6.36 $\pm$ 0.01           | 3.85 $\pm$ 0.00           | 6.49 $\pm$ 0.01          
Dijkstra (ms)             | 7250.00 $\pm$ 50.00       | 46.90 $\pm$ 0.40          | 40.80 $\pm$ 1.00          | 36.40 $\pm$ 0.70          | 50.90 $\pm$ 0.90         
Euler (ms)                | 4580.00 $\pm$ 120.00      | 41.20 $\pm$ 0.40          | 111.00 $\pm$ 1.00         | 19.50 $\pm$ 0.60          | 241.00 $\pm$ 3.00        
Midpoint Explicit (ms)    | 9370.00 $\pm$ 170.00      | 85.30 $\pm$ 0.70          | 207.00 $\pm$ 1.00         | 29.70 $\pm$ 0.70          | 479.00 $\pm$ 2.00        
Midpoint Fixed (s)        | 45.70 $\pm$ 0.40          | 0.67 $\pm$ 0.00           | 1.05 $\pm$ 0.02           | 0.10 $\pm$ 0.01           | 2.38 $\pm$ 0.02          
RK4 (ms)                  | 23100.00 $\pm$ 200.00     | 199.00 $\pm$ 1.00         | 383.00 $\pm$ 1.00         | 46.10 $\pm$ 0.90          | 776.00 $\pm$ 5.00        
FD - L Convection (ms)    | 2990.00 $\pm$ 40.00       | 2.87 $\pm$ 0.02           | 3.29 $\pm$ 0.09           | 1.77 $\pm$ 0.01           | 2.57 $\pm$ 0.22          
FD - NL Convection (ms)   | 3720.00 $\pm$ 30.00       | 3.36 $\pm$ 0.02           | 3.49 $\pm$ 0.14           | 1.81 $\pm$ 0.03           | 2.61 $\pm$ 0.09          
FD - Poisson (ms)         | 8590.00 $\pm$ 80.00       | 5.69 $\pm$ 0.00           | 9.76 $\pm$ 0.02           | 3.74 $\pm$ 0.02           | 4.93 $\pm$ 0.02          
FD - Laplace (ms)         | 779.00 $\pm$ 4.00         | 234.00 $\pm$ 1.00         | 384.00 $\pm$ 4.00         | 76.00 $\pm$ 1.30          | 417.00 $\pm$ 2.00        
M-D (ms)                  | 18500.00 $\pm$ 400.00     | 52.90 $\pm$ 0.00          | 74.10 $\pm$ 0.60          | 106.00 $\pm$ 0.00         | 110.00 $\pm$ 0.00        