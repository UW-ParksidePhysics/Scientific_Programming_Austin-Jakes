__author__

import numpy as np
import matplotlib.pyplot as plt

def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):

    shape = square_matrix.shape
    if len(shape) != 2 or shape[0] != shape[1]:
        raise IndexError("Input matrix must be square (M, M).")
    
    M = shape[0]
    if number_of_eigenvectors < 1 or number_of_eigenvectors > M:
        raise IndexError(f"number_of_eigenvectors must be between 1 and {M}.")
        
        eigenvalues, eigenvectors = np.linalg.eig(square_matrix)
        sorted_indices = np.argsort(eigenvalues)
        lowest_k_indices = sorted_indices[:number_of_eigenvectors]
        sorted_eigenvalues = eigenvalues[lowest_k_indices]
        sorted_eigenvectors = eigenvectors[:, lowest_k_indices]
        
    return sorted_eigenvalues, sorted_eigenvectors

    if __name__ == "__main__":
    test_matrix = np.array([[2, -1], [-1, 2]])
    k = 2
    
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(test_matrix, k)
    
    print("Eigenvalues:", eigenvalues) 
    print("Eigenvectors (normalized):\n", eigenvectors)
    plt.show()
