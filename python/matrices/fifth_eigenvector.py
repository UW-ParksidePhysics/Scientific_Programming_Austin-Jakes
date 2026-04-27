import numpy as np


main_diag = 2 * np.ones(5)
off_diag = -1 * np.ones(4)

matrix = np.diag(main_diag, k=0) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
print(f'{matrix}')
