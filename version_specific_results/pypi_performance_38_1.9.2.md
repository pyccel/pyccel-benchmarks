### Performance Comparison (as of 1.9.2)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.75                      | 0.55                      | 1.64                      | 1.59                     
Bellman Ford              | -                         | 4.28                      | 1.58                      | 2.82                      | 2.66                     
Dijkstra                  | -                         | 3.35                      | 1.87                      | 2.92                      | 2.73                     
Euler                     | -                         | 3.89                      | 2.43                      | 2.72                      | 2.69                     
Midpoint Explicit         | -                         | 4.46                      | 3.36                      | 3.30                      | 3.43                     
Midpoint Fixed            | -                         | 5.07                      | 3.59                      | 3.22                      | 3.28                     
RK4                       | -                         | 5.64                      | 3.95                      | 3.92                      | 4.17                     
FD - L Convection         | -                         | 3.19                      | 1.25                      | 2.62                      | 2.79                     
FD - NL Convection        | -                         | 4.27                      | 1.39                      | 2.65                      | 2.72                     
FD - Poisson              | -                         | 4.58                      | 1.98                      | 3.17                      | 3.08                     
FD - Laplace              | -                         | 9.28                      | 3.68                      | 3.53                      | 3.46                     
M-D                       | -                         | 9.14                      | 4.21                      | 4.14                      | 3.79                     

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel_fortran            | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 567.00 $\pm$ 8.00         | 9.69 $\pm$ 0.23           | 32.20 $\pm$ 0.60          | 2.52 $\pm$ 0.08           | 2.59 $\pm$ 0.04          
Bellman Ford (ms)         | 3600.00 $\pm$ 140.00      | 7.41 $\pm$ 0.30           | 7.93 $\pm$ 0.19           | 5.18 $\pm$ 0.14           | 10.00 $\pm$ 0.30         
Dijkstra (ms)             | 9310.00 $\pm$ 340.00      | 48.10 $\pm$ 2.60          | 51.30 $\pm$ 2.30          | 40.90 $\pm$ 1.40          | 60.90 $\pm$ 1.40         
Euler (ms)                | 5820.00 $\pm$ 190.00      | 48.10 $\pm$ 1.10          | 134.00 $\pm$ 3.00         | 25.20 $\pm$ 0.90          | 293.00 $\pm$ 6.00        
Midpoint Explicit (ms)    | 11900.00 $\pm$ 300.00     | 97.00 $\pm$ 3.70          | 276.00 $\pm$ 12.00        | 42.30 $\pm$ 1.00          | 589.00 $\pm$ 19.00       
Midpoint Fixed (s)        | 60.20 $\pm$ 1.30          | 0.77 $\pm$ 0.01           | 1.32 $\pm$ 0.03           | 0.13 $\pm$ 0.00           | 2.82 $\pm$ 0.06          
RK4 (ms)                  | 28500.00 $\pm$ 600.00     | 235.00 $\pm$ 4.00         | 482.00 $\pm$ 17.00        | 53.10 $\pm$ 2.20          | 950.00 $\pm$ 20.00       
FD - L Convection (ms)    | 4230.00 $\pm$ 140.00      | 3.90 $\pm$ 0.09           | 4.79 $\pm$ 0.24           | 3.38 $\pm$ 0.23           | 4.17 $\pm$ 0.14          
FD - NL Convection (ms)   | 5480.00 $\pm$ 210.00      | 4.94 $\pm$ 0.10           | 5.29 $\pm$ 0.62           | 3.83 $\pm$ 0.15           | 5.91 $\pm$ 0.62          
FD - Poisson (ms)         | 10700.00 $\pm$ 300.00     | 10.40 $\pm$ 0.20          | 14.40 $\pm$ 0.50          | 8.64 $\pm$ 0.32           | 12.00 $\pm$ 0.30         
FD - Laplace (ms)         | 1220.00 $\pm$ 10.00       | 359.00 $\pm$ 5.00         | 565.00 $\pm$ 9.00         | 193.00 $\pm$ 3.00         | 563.00 $\pm$ 5.00        
M-D (ms)                  | 23800.00 $\pm$ 800.00     | 67.10 $\pm$ 3.10          | 104.00 $\pm$ 1.00         | 140.00 $\pm$ 3.00         | 145.00 $\pm$ 3.00        
