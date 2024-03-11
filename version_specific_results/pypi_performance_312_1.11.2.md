### Performance Comparison (as of 1.11.2)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | -                         | -                         | 0.31                      | 1.38                      | 1.35                      | 1.46                      | 1.43                     
Bellman Ford              | -                         | -                         | -                         | 1.27                      | 2.52                      | 2.72                      | 2.66                      | 3.60                     
Dijkstra                  | -                         | -                         | -                         | 1.66                      | 2.63                      | 2.73                      | 2.76                      | 3.59                     
Euler                     | -                         | -                         | -                         | 2.09                      | 2.50                      | 2.74                      | 2.62                      | 3.49                     
Midpoint Explicit         | -                         | -                         | -                         | 3.05                      | 2.78                      | 3.02                      | 2.91                      | 3.77                     
Midpoint Fixed            | -                         | -                         | -                         | 3.30                      | 2.93                      | 3.14                      | 3.03                      | 3.89                     
RK4                       | -                         | -                         | -                         | 3.79                      | 3.33                      | 3.55                      | 3.50                      | 4.34                     
FD - L Convection         | -                         | -                         | -                         | 0.93                      | 2.47                      | 2.68                      | 2.67                      | 3.48                     
FD - NL Convection        | -                         | -                         | -                         | 0.91                      | 2.47                      | 2.72                      | 2.65                      | 3.47                     
FD - Poisson              | -                         | -                         | -                         | 1.38                      | 2.63                      | 2.84                      | 3.19                      | 3.56                     
FD - Laplace              | -                         | -                         | -                         | 3.07                      | 3.06                      | 3.26                      | 3.30                      | 4.18                     
M-D                       | -                         | -                         | -                         | 4.10                      | 3.40                      | 3.37                      | 3.63                      | 4.54                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 471.00 $\pm$ 5.00         | -                         | -                         | 10.70 $\pm$ 0.30          | 1.55 $\pm$ 0.00           | 1.62 $\pm$ 0.10           | 8.32 $\pm$ 0.38           | 4.36 $\pm$ 0.01          
Bellman Ford (ms)         | 2550.00 $\pm$ 40.00       | -                         | -                         | 3.88 $\pm$ 0.07           | 2.96 $\pm$ 0.02           | 5.95 $\pm$ 0.03           | 4.39 $\pm$ 0.02           | 18.20 $\pm$ 0.30         
Dijkstra (ms)             | 6930.00 $\pm$ 40.00       | -                         | -                         | 20.50 $\pm$ 0.60          | 19.40 $\pm$ 0.40          | 30.90 $\pm$ 0.60          | 24.70 $\pm$ 0.40          | 22.70 $\pm$ 0.40         
Euler (ms)                | 4780.00 $\pm$ 30.00       | -                         | -                         | 37.60 $\pm$ 0.30          | 15.30 $\pm$ 0.30          | 144.00 $\pm$ 1.00         | 14.90 $\pm$ 0.50          | 131.00 $\pm$ 3.00        
Midpoint Explicit (ms)    | 9600.00 $\pm$ 60.00       | -                         | -                         | 75.70 $\pm$ 5.40          | 23.60 $\pm$ 0.50          | 284.00 $\pm$ 2.00         | 16.50 $\pm$ 1.20          | 253.00 $\pm$ 1.00        
Midpoint Fixed (s)        | 47.80 $\pm$ 0.20          | -                         | -                         | 0.38 $\pm$ 0.01           | 0.08 $\pm$ 0.00           | 1.40 $\pm$ 0.01           | 0.06 $\pm$ 0.01           | 1.25 $\pm$ 0.01          
RK4 (ms)                  | 24100.00 $\pm$ 200.00     | -                         | -                         | 144.00 $\pm$ 11.00        | 33.90 $\pm$ 0.80          | 496.00 $\pm$ 8.00         | 38.70 $\pm$ 1.80          | 409.00 $\pm$ 1.00        
FD - L Convection (ms)    | 2890.00 $\pm$ 40.00       | -                         | -                         | 2.70 $\pm$ 0.05           | 1.56 $\pm$ 0.10           | 1.73 $\pm$ 0.12           | 1.32 $\pm$ 0.01           | 3.70 $\pm$ 0.01          
FD - NL Convection (ms)   | 3570.00 $\pm$ 30.00       | -                         | -                         | 2.84 $\pm$ 0.06           | 1.84 $\pm$ 0.03           | 2.06 $\pm$ 0.08           | 1.54 $\pm$ 0.01           | 3.74 $\pm$ 0.01          
FD - Poisson (ms)         | 8130.00 $\pm$ 120.00      | -                         | -                         | 7.38 $\pm$ 0.54           | 2.78 $\pm$ 0.01           | 3.80 $\pm$ 0.03           | 2.69 $\pm$ 0.01           | 8.94 $\pm$ 0.02          
FD - Laplace (ms)         | 605.00 $\pm$ 9.00         | -                         | -                         | 246.00 $\pm$ 1.00         | 64.00 $\pm$ 1.40          | 260.00 $\pm$ 1.00         | 61.60 $\pm$ 2.60          | 308.00 $\pm$ 12.00       
M-D (ms)                  | 18400.00 $\pm$ 200.00     | -                         | -                         | 59.10 $\pm$ 0.30          | 57.60 $\pm$ 4.50          | 59.90 $\pm$ 1.20          | 71.70 $\pm$ 1.70          | 62.80 $\pm$ 1.70         