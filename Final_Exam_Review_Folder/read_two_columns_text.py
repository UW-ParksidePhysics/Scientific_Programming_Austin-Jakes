__author__

import numpy as np

def read_two_columns_text(filename: str) -> np.ndarray:
    """
    Reads two columns of data from a text file of arbitrary length.
    Returns the data as an (2, M) ndarray.
    """
    try:
        data = np.genfromtxt(filename)                
        return data
    except OSError as e:
        raise OSError(f"Error reading file: {filename}") from e

if __name__ == "__main__":
    try:
        data = read_two_columns_text('volumes_energies.dat')
        print(f'{data=}, shape={data.shape}')
    except OSError as e:
        print(e)