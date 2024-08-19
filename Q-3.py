#CL 603 - Optimization
#Homework 1 - Problem 3
#Priyam Nayak
#214026014

import numpy as np # Import the numpy library and assign it the name 'np'
import matplotlib.pyplot as plt # Import the matplotlib.pyplot module and assign it the name 'plt'

# Define the function
def f(x1, x2):
    return (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2

# Generate the grid of values
x1 = np.linspace(-6, 6, 1000) # Create an array of 1000 evenly spaced values from -6 to 6 for x1
x2 = np.linspace(-6, 6, 1000) # Create an array of 1000 evenly spaced values from -6 to 6 for x1
X1, X2 = np.meshgrid(x1, x2) # Create a meshgrid from x1 and x2 for plotting
Z = f(X1, X2) # Compute the function values over the grid

# Plot the contour
plt.figure(figsize=(8, 6)) # Create a new figure with a specific size
contour = plt.contour(X1, X2, Z, levels=50, cmap='viridis') # Plot the contour with 50 levels and 'viridis' colormap
plt.clabel(contour, inline=True, fontsize=8, fmt="%.1f")  # Display function values along contours
plt.title('Q-3 Contour Plot') # Set the title of the plot
plt.xlabel('x1') # Set the label for the x-axis
plt.ylabel('x2') # Set the label for the y-axis
#plt.legend() #Create legend
plt.savefig('Q3_Plot.png', dpi=300, bbox_inches='tight') #Save the plot as png file
plt.show() # Display the plot
