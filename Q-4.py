#CL 603 - Optimization
#Homework 1 - Problem 4
#Priyam Nayak
#214026014

import numpy as np # Import the numpy library and assign it the name 'np'

# Define the function
def f(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

# Gradient calculation using the center difference method
def gradient(f, x, h=1e-5):
    grad = np.zeros_like(x)  # Initialize the gradient vector with zeros, same shape as x
    for i in range(len(x)):  # Loop over each variable in x
        x_f = x.copy()  # Create a copy of x to modify for forward difference
        x_b = x.copy()  # Create a copy of x to modify for backward difference
        x_f[i] += h  # Increment the i-th variable by h for forward difference
        x_b[i] -= h  # Decrement the i-th variable by h for backward difference
        grad[i] = (f(x_f) - f(x_b)) / (2 * h)  # Compute the central difference for the i-th variable
    return grad  # Return the gradient vector


# Hessian using center difference method
def hessian(f, x, h=1e-5):
    n = len(x)  # Determine the number of variables in x
    hess = np.zeros((n, n))  # Initialize the Hessian matrix with zeros, shape (n, n)
    for i in range(n):  # Loop over each row index of the Hessian matrix
        for j in range(n):  # Loop over each column index of the Hessian matrix
            x_ijpp = x.copy()  # Create a copy of x to modify for both i and j incremented
            x_ijpp[i] += h
            x_ijpp[j] += h
            x_ijnp = x.copy()  # Create a copy of x to modify for i decremented and j incremented
            x_ijnp[i] -= h
            x_ijnp[j] += h
            x_ijpn = x.copy()  # Create a copy of x to modify for i incremented and j decremented
            x_ijpn[i] += h
            x_ijpn[j] -= h
            x_ijnn = x.copy()  # Create a copy of x to modify for both i and j decremented
            x_ijnn[i] -= h
            x_ijnn[j] -= h
            hess[i, j] = (f(x_ijpp) - f(x_ijnp) - f(x_ijpn) + f(x_ijnn)) / (4 * h**2)  # Compute the second partial derivative for f with respect to x_i and x_j
    return hess  # Return the Hessian matrix

    

x = np.array([1.0, 2.0]) # Test at point (1, 2)
grad_f = gradient(f, x)
hess_f = hessian(f, x)
#np.savetxt('Q4_Result.txt', grad_f, fmt='%.6f', header='Gradient Matrix:', comments='')
# Write results to a text file with rounded integers
with open("Q4_Result.txt", "w") as file:
    file.write("Gradient at (1, 2):\n")
    file.write(np.array2string(np.round(grad_f).astype(int), separator=', '))
    file.write("\n\nHessian at (1, 2):\n")
    file.write(np.array2string(hess_f, separator=', '))

print("Gradient at (1, 2):", np.round(grad_f).astype(int))
print("Hessian at (1, 2):\n", hess_f)