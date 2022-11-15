### Performance Comparison (as of Tue Nov 15 21:50:40 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.51                      | 1.27                      | 1.15                     
Bellman Ford              | -                         | 2.83                      | 1.83                      | 1.74                     
Dijkstra                  | -                         | 2.84                      | 1.90                      | -                        
Euler                     | -                         | 3.36                      | 1.85                      | 1.78                     
Midpoint Explicit         | -                         | 4.13                      | 2.15                      | 2.07                     
Midpoint Fixed            | -                         | 4.95                      | 2.21                      | 2.17                     
RK4                       | -                         | 5.02                      | 2.56                      | -                        
FD - L Convection         | -                         | 2.51                      | 1.70                      | 1.70                     
FD - NL Convection        | -                         | 2.52                      | 1.70                      | 1.71                     
FD - Poisson              | -                         | 7.85                      | 1.83                      | 1.80                     
FD - Laplace              | -                         | 12.72                     | 2.33                      | -                        
M-D                       | -                         | -                         | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran                   | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 413.00 $\pm$ 2.00         | 22.00 $\pm$ 0.20          | 13.20 $\pm$ 0.00          | 14.30 $\pm$ 0.00         
Bellman Ford (ns)         | 56300.00 $\pm$ 200.00     | 368.00 $\pm$ 1.00         | 224.00 $\pm$ 2.00         | 471.00 $\pm$ 4.00        
Dijkstra (ns)             | 27700.00 $\pm$ 100.00     | 361.00 $\pm$ 4.00         | 255.00 $\pm$ 1.00         | -                        
Euler (\textmu s)         | 49100.00 $\pm$ 300.00     | 486.00 $\pm$ 11.00        | 143.00 $\pm$ 5.00         | 2670.00 $\pm$ 10.00      
Midpoint Explicit (ms)    | 98.40 $\pm$ 0.60          | 1.18 $\pm$ 0.02           | 0.18 $\pm$ 0.00           | 4.83 $\pm$ 0.06          
Midpoint Fixed (ms)       | 496.00 $\pm$ 2.00         | 7.40 $\pm$ 0.06           | 0.63 $\pm$ 0.01           | 21.30 $\pm$ 0.20         
RK4 (ms)                  | 249.00 $\pm$ 1.00         | 1.85 $\pm$ 0.01           | 0.64 $\pm$ 0.03           | -                        
FD - L Convection (ms)    | 1960.00 $\pm$ 10.00       | 1.80 $\pm$ 0.11           | 1.86 $\pm$ 0.00           | 1.80 $\pm$ 0.02          
FD - NL Convection (ms)   | 2460.00 $\pm$ 10.00       | 2.16 $\pm$ 0.01           | 1.63 $\pm$ 0.00           | 1.58 $\pm$ 0.00          
FD - Poisson (ms)         | 4210.00 $\pm$ 30.00       | 2.28 $\pm$ 0.00           | 3.87 $\pm$ 0.01           | 2.01 $\pm$ 0.01          
FD - Laplace (\textmu s)  | 54.70 $\pm$ 3.40          | 2.41 $\pm$ 0.02           | 2.27 $\pm$ 0.05           | -                        
M-D (s)                   | 50.10 $\pm$ 0.20          | -                         | -                         | -                        
