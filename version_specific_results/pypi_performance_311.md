### Performance Comparison (as of Wed Nov 16 11:46:10 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.65                      | 1.31                      | 1.18                     
Bellman Ford              | -                         | 2.91                      | 1.89                      | 1.76                     
Dijkstra                  | -                         | 2.89                      | 1.94                      | -                        
Euler                     | -                         | 3.44                      | 1.88                      | 1.82                     
Midpoint Explicit         | -                         | 4.28                      | 2.19                      | 2.13                     
Midpoint Fixed            | -                         | 5.05                      | 2.25                      | 2.21                     
RK4                       | -                         | 5.08                      | 2.59                      | -                        
FD - L Convection         | -                         | 2.59                      | 1.74                      | 1.73                     
FD - NL Convection        | -                         | 2.59                      | 1.73                      | 1.73                     
FD - Poisson              | -                         | 7.94                      | 1.85                      | 1.80                     
FD - Laplace              | -                         | 13.02                     | 2.33                      | -                        
M-D                       | -                         | -                         | -                         | -                        

## Execution time
Algorithm                 | python                    | pythran                   | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 415.00 $\pm$ 2.00         | 22.00 $\pm$ 0.20          | 14.30 $\pm$ 0.00          | 14.30 $\pm$ 0.00         
Bellman Ford (ns)         | 56500.00 $\pm$ 200.00     | 368.00 $\pm$ 1.00         | 218.00 $\pm$ 2.00         | 473.00 $\pm$ 5.00        
Dijkstra (ns)             | 27800.00 $\pm$ 100.00     | 361.00 $\pm$ 2.00         | 256.00 $\pm$ 1.00         | -                        
Euler (\textmu s)         | 49000.00 $\pm$ 200.00     | 483.00 $\pm$ 8.00         | 145.00 $\pm$ 7.00         | 2680.00 $\pm$ 30.00      
Midpoint Explicit (ms)    | 98.30 $\pm$ 0.50          | 1.17 $\pm$ 0.02           | 0.18 $\pm$ 0.00           | 4.79 $\pm$ 0.02          
Midpoint Fixed (ms)       | 496.00 $\pm$ 3.00         | 7.42 $\pm$ 0.19           | 0.59 $\pm$ 0.00           | 21.20 $\pm$ 0.10         
RK4 (ms)                  | 250.00 $\pm$ 1.00         | 1.85 $\pm$ 0.01           | 0.64 $\pm$ 0.02           | -                        
FD - L Convection (ms)    | 1970.00 $\pm$ 10.00       | 1.80 $\pm$ 0.11           | 1.86 $\pm$ 0.00           | 1.80 $\pm$ 0.01          
FD - NL Convection (ms)   | 2460.00 $\pm$ 20.00       | 2.16 $\pm$ 0.01           | 1.64 $\pm$ 0.02           | 1.58 $\pm$ 0.00          
FD - Poisson (ms)         | 4220.00 $\pm$ 40.00       | 2.29 $\pm$ 0.01           | 3.87 $\pm$ 0.00           | 2.01 $\pm$ 0.05          
FD - Laplace (\textmu s)  | 53.90 $\pm$ 0.40          | 2.41 $\pm$ 0.01           | 2.32 $\pm$ 0.05           | -                        
M-D (s)                   | 50.20 $\pm$ 0.30          | -                         | -                         | -                        
