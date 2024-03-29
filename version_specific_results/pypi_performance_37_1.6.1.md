### Performance Comparison (as of 1.6.1)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.44                      | 0.35                      | 1.25                      | 1.14                     
Bellman Ford              | -                         | 2.70                      | 1.01                      | 1.83                      | 1.73                     
Dijkstra                  | -                         | 2.79                      | 1.36                      | 1.94                      | -                        
Euler                     | -                         | 3.33                      | 1.40                      | 1.87                      | 1.80                     
Midpoint Explicit         | -                         | 4.25                      | 2.13                      | 2.23                      | 2.15                     
Midpoint Fixed            | -                         | 5.11                      | 2.42                      | 2.27                      | 2.24                     
RK4                       | -                         | 5.09                      | 2.51                      | 2.65                      | -                        
FD - L Convection         | -                         | 2.41                      | 0.33                      | 1.71                      | 1.73                     
FD - NL Convection        | -                         | 2.45                      | 0.33                      | 1.75                      | 1.76                     
FD - Poisson              | -                         | 7.95                      | 0.80                      | 1.87                      | 1.82                     
FD - Laplace              | -                         | 13.27                     | 1.85                      | 2.31                      | -                        
M-D                       | -                         | -                         | 5.51                      | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 475.00 $\pm$ 9.00         | 22.00 $\pm$ 0.20          | 32.40 $\pm$ 0.20          | 14.30 $\pm$ 0.00          | 13.60 $\pm$ 0.00         
Bellman Ford (ns)         | 70700.00 $\pm$ 200.00     | 369.00 $\pm$ 1.00         | 540.00 $\pm$ 12.00        | 223.00 $\pm$ 3.00         | 478.00 $\pm$ 4.00        
Dijkstra (ns)             | 33900.00 $\pm$ 300.00     | 371.00 $\pm$ 2.00         | 354.00 $\pm$ 5.00         | 256.00 $\pm$ 1.00         | -                        
Euler (ms)                | 58.90 $\pm$ 0.40          | 0.51 $\pm$ 0.01           | 1.28 $\pm$ 0.02           | 0.14 $\pm$ 0.01           | 2.68 $\pm$ 0.03          
Midpoint Explicit (ms)    | 119.00 $\pm$ 1.00         | 1.20 $\pm$ 0.02           | 3.18 $\pm$ 0.07           | 0.18 $\pm$ 0.01           | 4.82 $\pm$ 0.02          
Midpoint Fixed (ms)       | 590.00 $\pm$ 3.00         | 7.93 $\pm$ 0.08           | 17.50 $\pm$ 0.20          | 0.60 $\pm$ 0.02           | 21.40 $\pm$ 0.20         
RK4 (ms)                  | 278.00 $\pm$ 2.00         | 1.86 $\pm$ 0.01           | 6.37 $\pm$ 0.07           | 0.64 $\pm$ 0.02           | -                        
FD - L Convection (ms)    | 2000.00 $\pm$ 20.00       | 1.66 $\pm$ 0.00           | 9.13 $\pm$ 0.12           | 1.71 $\pm$ 0.00           | 1.50 $\pm$ 0.00          
FD - NL Convection (ms)   | 3030.00 $\pm$ 100.00      | 1.82 $\pm$ 0.01           | 9.44 $\pm$ 0.16           | 1.62 $\pm$ 0.01           | 1.56 $\pm$ 0.00          
FD - Poisson (ms)         | 4370.00 $\pm$ 20.00       | 2.29 $\pm$ 0.01           | 10.90 $\pm$ 0.10          | 3.87 $\pm$ 0.00           | 2.01 $\pm$ 0.00          
FD - Laplace (\textmu s)  | 51.50 $\pm$ 0.40          | 2.43 $\pm$ 0.01           | 8.85 $\pm$ 0.08           | 2.19 $\pm$ 0.01           | -                        
M-D (s)                   | 59.30 $\pm$ 0.50          | -                         | 0.23 $\pm$ 0.00           | -                         | -                        
