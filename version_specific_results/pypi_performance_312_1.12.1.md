### Performance Comparison (as of 1.12.1)
## Compilation time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 1.95                      | -                         | 0.30                      | 1.39                      | 1.32                      | 1.42                      | 1.40                     
Bellman Ford              | -                         | 3.33                      | -                         | 1.21                      | 3.78                      | 3.97                      | 3.83                      | 4.45                     
Dijkstra                  | -                         | 2.41                      | -                         | 1.74                      | 3.86                      | 3.99                      | 3.92                      | 4.55                     
Euler                     | -                         | 2.54                      | -                         | 2.03                      | 3.63                      | 3.94                      | 3.80                      | 4.43                     
Midpoint Explicit         | -                         | 3.01                      | -                         | 3.15                      | 4.15                      | 4.44                      | 4.24                      | 4.84                     
Midpoint Fixed            | -                         | 3.38                      | -                         | 3.28                      | 4.02                      | 4.47                      | 4.13                      | 4.85                     
RK4                       | -                         | 3.76                      | -                         | 3.85                      | 4.59                      | 5.13                      | 4.85                      | 5.52                     
FD - L Convection         | -                         | 2.44                      | -                         | 0.95                      | 3.83                      | 4.08                      | 3.89                      | 4.64                     
FD - NL Convection        | -                         | 3.22                      | -                         | 0.88                      | 3.75                      | 3.97                      | 3.81                      | 4.44                     
FD - Poisson              | -                         | 3.35                      | -                         | 1.37                      | 3.81                      | 4.16                      | 5.15                      | 4.70                     
FD - Laplace              | -                         | 6.38                      | -                         | 3.19                      | 4.23                      | 4.44                      | 4.40                      | 5.01                     
M-D                       | -                         | 6.47                      | -                         | 4.09                      | 4.62                      | 4.61                      | 4.78                      | 5.46                     

## Execution time
Algorithm                 | python                    | pythran_gnu               | pythran_intel             | numba                     | pyccel_fortran_gnu        | pyccel_c_gnu              | pyccel_fortran_intel      | pyccel_c_intel           
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 437.00 $\pm$ 8.00         | 2.95 $\pm$ 0.02           | -                         | 10.80 $\pm$ 0.30          | 1.56 $\pm$ 0.01           | 1.61 $\pm$ 0.01           | 10.60 $\pm$ 0.20          | 4.37 $\pm$ 0.01          
Bellman Ford (ms)         | 2530.00 $\pm$ 40.00       | 4.59 $\pm$ 0.01           | -                         | 3.87 $\pm$ 0.07           | 3.01 $\pm$ 0.02           | 5.62 $\pm$ 0.02           | 4.25 $\pm$ 0.05           | 18.60 $\pm$ 0.30         
Dijkstra (ms)             | 6850.00 $\pm$ 40.00       | 26.80 $\pm$ 0.20          | -                         | 20.90 $\pm$ 0.50          | 19.10 $\pm$ 0.70          | 29.40 $\pm$ 0.10          | 23.00 $\pm$ 0.20          | 22.30 $\pm$ 0.40         
Euler (ms)                | 4900.00 $\pm$ 40.00       | 25.40 $\pm$ 0.30          | -                         | 37.80 $\pm$ 0.50          | 15.50 $\pm$ 0.70          | 144.00 $\pm$ 2.00         | 13.80 $\pm$ 0.40          | 128.00 $\pm$ 1.00        
Midpoint Explicit (ms)    | 9820.00 $\pm$ 50.00       | 52.60 $\pm$ 0.40          | -                         | 78.10 $\pm$ 0.60          | 24.40 $\pm$ 1.00          | 285.00 $\pm$ 4.00         | 16.60 $\pm$ 0.60          | 256.00 $\pm$ 3.00        
Midpoint Fixed (ms)       | 48700.00 $\pm$ 400.00     | 254.00 $\pm$ 1.00         | -                         | 387.00 $\pm$ 2.00         | 75.40 $\pm$ 0.70          | 1410.00 $\pm$ 20.00       | 62.60 $\pm$ 3.30          | 1260.00 $\pm$ 30.00      
RK4 (ms)                  | 24500.00 $\pm$ 100.00     | 165.00 $\pm$ 17.00        | -                         | 147.00 $\pm$ 15.00        | 36.40 $\pm$ 0.60          | 498.00 $\pm$ 11.00        | 38.90 $\pm$ 0.30          | 417.00 $\pm$ 14.00       
FD - L Convection (ms)    | 2950.00 $\pm$ 30.00       | 1.63 $\pm$ 0.01           | -                         | 2.73 $\pm$ 0.03           | 1.69 $\pm$ 0.01           | 1.75 $\pm$ 0.13           | 1.53 $\pm$ 0.01           | 4.21 $\pm$ 0.03          
FD - NL Convection (ms)   | 3640.00 $\pm$ 40.00       | 1.81 $\pm$ 0.04           | -                         | 2.83 $\pm$ 0.03           | 1.94 $\pm$ 0.23           | 1.97 $\pm$ 0.01           | 1.40 $\pm$ 0.01           | 4.24 $\pm$ 0.09          
FD - Poisson (ms)         | 8120.00 $\pm$ 110.00      | 2.97 $\pm$ 0.04           | -                         | 7.25 $\pm$ 0.05           | 2.83 $\pm$ 0.03           | 3.82 $\pm$ 0.04           | 2.68 $\pm$ 0.01           | 5.75 $\pm$ 0.14          
FD - Laplace (ms)         | 602.00 $\pm$ 11.00        | 69.60 $\pm$ 1.70          | -                         | 248.00 $\pm$ 1.00         | 62.60 $\pm$ 3.70          | 257.00 $\pm$ 2.00         | 64.20 $\pm$ 1.60          | 329.00 $\pm$ 1.00        
M-D (ms)                  | 18900.00 $\pm$ 100.00     | 15.20 $\pm$ 0.00          | -                         | 60.30 $\pm$ 2.30          | 55.20 $\pm$ 1.90          | 59.80 $\pm$ 0.70          | 81.30 $\pm$ 0.30          | 61.90 $\pm$ 0.50         