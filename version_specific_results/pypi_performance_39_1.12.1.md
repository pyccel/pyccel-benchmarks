### Performance Comparison (as of 1.12.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.80                      | 1.93                      | 0.33                      | 1.30                      | 1.25                      | 1.36                      | 1.34                     
Bellman Ford              | -                         | 3.24                      | 3.55                      | 1.11                      | 3.63                      | 3.93                      | 3.74                      | 4.45                     
Dijkstra                  | -                         | 2.18                      | 2.54                      | 1.61                      | 3.71                      | 3.91                      | 3.83                      | 4.48                     
Euler                     | -                         | 2.45                      | 2.88                      | 2.06                      | 3.61                      | 3.90                      | 3.70                      | 4.41                     
Midpoint Explicit         | -                         | 2.81                      | 3.29                      | 3.06                      | 3.93                      | 4.14                      | 3.92                      | 4.62                     
Midpoint Fixed            | -                         | 3.19                      | 3.73                      | 3.29                      | 3.87                      | 4.20                      | 3.99                      | 4.76                     
RK4                       | -                         | 3.46                      | 4.06                      | 3.82                      | 4.33                      | 4.55                      | 4.42                      | 5.10                     
FD - L Convection         | -                         | 2.07                      | 2.55                      | 0.88                      | 3.55                      | 3.85                      | 3.69                      | 4.38                     
FD - NL Convection        | -                         | 2.96                      | 3.44                      | 0.89                      | 3.57                      | 3.86                      | 3.72                      | 4.38                     
FD - Poisson              | -                         | 3.07                      | 3.63                      | 1.36                      | 3.69                      | 4.00                      | 4.94                      | 4.50                     
FD - Laplace              | -                         | 6.17                      | 8.76                      | 3.07                      | 4.02                      | 4.32                      | 4.25                      | 4.88                     
M-D                       | -                         | 6.02                      | 7.59                      | 4.09                      | 4.37                      | 4.49                      | 4.53                      | 5.35                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 333.00 $\pm$ 3.00         | 2.97 $\pm$ 0.03           | 3.06 $\pm$ 0.01           | 10.80 $\pm$ 0.20          | 1.51 $\pm$ 0.00           | 1.56 $\pm$ 0.00           | 7.51 $\pm$ 0.20           | 4.36 $\pm$ 0.00          
Bellman Ford (ms)         | 1920.00 $\pm$ 20.00       | 4.60 $\pm$ 0.02           | 3.19 $\pm$ 0.05           | 3.91 $\pm$ 0.06           | 3.01 $\pm$ 0.02           | 6.08 $\pm$ 0.03           | 4.33 $\pm$ 0.06           | 18.50 $\pm$ 0.40         
Dijkstra (ms)             | 5150.00 $\pm$ 60.00       | 24.90 $\pm$ 0.10          | 16.40 $\pm$ 0.10          | 19.70 $\pm$ 0.20          | 18.10 $\pm$ 0.30          | 30.00 $\pm$ 0.30          | 24.10 $\pm$ 0.20          | 22.40 $\pm$ 0.20         
Euler (ms)                | 3880.00 $\pm$ 30.00       | 25.70 $\pm$ 0.40          | 26.60 $\pm$ 3.60          | 37.50 $\pm$ 0.40          | 15.00 $\pm$ 0.50          | 144.00 $\pm$ 2.00         | 13.80 $\pm$ 0.30          | 128.00 $\pm$ 2.00        
Midpoint Explicit (ms)    | 7930.00 $\pm$ 90.00       | 53.10 $\pm$ 0.70          | 52.00 $\pm$ 0.90          | 76.50 $\pm$ 0.50          | 23.50 $\pm$ 0.40          | 284.00 $\pm$ 2.00         | 16.00 $\pm$ 0.40          | 256.00 $\pm$ 5.00        
Midpoint Fixed (ms)       | 40300.00 $\pm$ 300.00     | 253.00 $\pm$ 1.00         | 92.80 $\pm$ 0.50          | 368.00 $\pm$ 2.00         | 75.70 $\pm$ 0.60          | 1420.00 $\pm$ 20.00       | 74.40 $\pm$ 38.60         | 1240.00 $\pm$ 10.00      
RK4 (ms)                  | 20200.00 $\pm$ 100.00     | 160.00 $\pm$ 4.00         | 36.00 $\pm$ 0.80          | 137.00 $\pm$ 1.00         | 35.30 $\pm$ 0.60          | 495.00 $\pm$ 13.00        | 37.20 $\pm$ 0.50          | 414.00 $\pm$ 7.00        
FD - L Convection (ms)    | 2360.00 $\pm$ 10.00       | 1.66 $\pm$ 0.03           | 1.56 $\pm$ 0.02           | 2.74 $\pm$ 0.07           | 1.76 $\pm$ 0.03           | 1.75 $\pm$ 0.11           | 1.54 $\pm$ 0.01           | 4.18 $\pm$ 0.10          
FD - NL Convection (ms)   | 2940.00 $\pm$ 20.00       | 1.58 $\pm$ 0.02           | 1.74 $\pm$ 0.04           | 2.83 $\pm$ 0.03           | 2.07 $\pm$ 0.19           | 2.02 $\pm$ 0.06           | 1.53 $\pm$ 0.01           | 4.19 $\pm$ 0.03          
FD - Poisson (ms)         | 6610.00 $\pm$ 120.00      | 3.18 $\pm$ 0.02           | 5.83 $\pm$ 0.13           | 7.25 $\pm$ 0.06           | 2.83 $\pm$ 0.03           | 3.87 $\pm$ 0.04           | 2.70 $\pm$ 0.02           | 5.71 $\pm$ 0.02          
FD - Laplace (ms)         | 600.00 $\pm$ 14.00        | 69.00 $\pm$ 0.40          | 151.00 $\pm$ 1.00         | 253.00 $\pm$ 1.00         | 63.30 $\pm$ 0.60          | 260.00 $\pm$ 1.00         | 64.20 $\pm$ 0.50          | 322.00 $\pm$ 1.00        
M-D (ms)                  | 15600.00 $\pm$ 100.00     | 15.30 $\pm$ 0.10          | 53.10 $\pm$ 0.20          | 59.60 $\pm$ 0.30          | 54.50 $\pm$ 0.20          | 59.50 $\pm$ 0.20          | 80.00 $\pm$ 0.50          | 60.50 $\pm$ 0.20         