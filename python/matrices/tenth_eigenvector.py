import numpy as np


main_diagonal = 2 * np.ones(10)
off_diagonal = -1 * np.ones(9)

matrix = np.diag(main_diagonal, k=0) + np.diag(off_diagonal, k=1) + np.diag(off_diagonal, k=-1)
print(f'{matrix}')
