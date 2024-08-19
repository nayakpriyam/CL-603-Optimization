#CL 603 - Optimization
#Homework 1 - Problem 5
#Priyam Nayak
#214026014

import numpy as np # Import the numpy library and assign it the alias 'np'

def to_ut(A): #Function to convert a symmetric matrix A to its upper triangular form using Gaussian elimination.
    A = A.astype(float)  # Ensure the matrix is treated as floating-point
    n = A.shape[0]  # Get the number of rows (and columns) in the matrix
    for i in range(n):
        # Perform row elimination to create zeros below the diagonal
        for j in range(i + 1, n):
            if A[i, i] == 0:  # If the pivot element is zero, skip to avoid division by zero
                continue
            factor = A[j, i] / A[i, i]  # Calculate the factor for row elimination
            A[j, i:] -= factor * A[i, i:]  # Subtract the factor times the pivot row from the current row
    return A

def cons_dm(utm): # Function to construct a diagonal matrix from the pivot elements of the upper triangular matrix.
    n = utm.shape[0]  # Get the number of rows (and columns)
    dm = np.zeros((n, n))  # Initialize an n x n zero matrix
    # Extract the diagonal elements (pivot elements) and place them in the diagonal matrix
    for i in range(n):
        dm[i, i] = utm[i, i]
    return dm

def check_def(dm): # Function to check the definiteness of a matrix based on its pivot elements
    pivots = np.diag(dm)  # Extract the diagonal elements (pivot elements)
    if all(p > 0 for p in pivots):
        return "Positive definite"
    elif all(p < 0 for p in pivots):
        return "Negative definite"
    elif all(p >= 0 for p in pivots):
        return "Positive semi-definite"
    elif all(p <= 0 for p in pivots):
        return "Negative semi-definite"
    else:
        return "Indefinite"

# Hessian matrix from Q4
Hessian = np.array([[-22, 12],
                    [12, 26]])

utm = to_ut(Hessian.copy()) # Convert to upper triangular matrix
dm = cons_dm(utm) # Construct diagonal matrix using the pivot elements
definiteness = check_def(dm) # Check definiteness based on the diagonal matrix

with open("Q5_Result.txt", "w") as file:
    file.write("Hessian Matrix:\n")
    file.write(np.array2string(Hessian, separator=', ') +"\n")
    file.write(f"is {definiteness}\n")

print("Hessian Matrix from Q4:")
print(Hessian)
print(f"is {definiteness}")