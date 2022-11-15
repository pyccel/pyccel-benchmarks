### Performance Comparison (as of Tue Nov 15 18:16:30 UTC 2022)
## Compilation time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann                 | -                         | 2.36                      | 0.35                      | 1.23                      | 1.12                     
Bellman Ford              | -                         | 2.65                      | 0.97                      | 1.77                      | 1.71                     
Dijkstra                  | -                         | 2.74                      | 1.31                      | 1.90                      | -                        

## Execution time
Algorithm                 | python                    | pythran                   | numba                     | pyccel                    | pyccel_c                 
------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------
Ackermann (ms)            | 444.00 $\pm$ 4.00         | 22.00 $\pm$ 0.20          | 32.30 $\pm$ 0.20          | 14.30 $\pm$ 0.00          | 13.60 $\pm$ 0.00         
Bellman Ford (ns)         | 68800.00 $\pm$ 1900.00    | 369.00 $\pm$ 2.00         | 536.00 $\pm$ 5.00         | 235.00 $\pm$ 2.00         | 476.00 $\pm$ 5.00        
Dijkstra (ns)             | 35100.00 $\pm$ 400.00     | 370.00 $\pm$ 4.00         | 353.00 $\pm$ 3.00         | 256.00 $\pm$ 1.00         | -                        