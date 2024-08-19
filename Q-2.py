#CL 603 - Optimization
#Homework 1 - Problem 2
#Priyam Nayak
#214026014

import numpy as np # Import the numpy library and assign it the name 'np'
import matplotlib.pyplot as plt # Import the matplotlib.pyplot module and assign it the name 'plt'

x = np.linspace(-5,5,1000) # Create an array of 1000 evenly spaced values from -5 to 5
fx = np.cos(x)**2 + 0.1*x # Calculate the function values fx for each x, using the given mathematical expression

plt.plot(x,fx,label=r'$f(x)=\cos^2(x)+0.1x$') # Create the plot of fx against x
plt.title("Question-2 Plot") # Set the title of the plot
plt.xlabel("x") # Set the label for the x-axis
plt.ylabel("f(x)") # Set the label for the y-axis
plt.legend() #Create legend
plt.savefig('Q2_Plot.png', dpi=300, bbox_inches='tight') #Save the plot as png file
plt.show() # Display the plot