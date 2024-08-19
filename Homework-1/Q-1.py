#CL 603 - Optimization
#Homework 1 - Problem 1
#Priyam Nayak
#214026014


import numpy as np # Import the numpy library and assign it the name 'np'
import matplotlib.pyplot as plt # Import the matplotlib.pyplot module and assign it the name 'plt'


x = np.linspace(0,30,600) # Create an array of 600 evenly spaced values from 0 to 30
fx = -0.1*x/((1+0.1*x)*(1+0.05*x)) # Calculate the function values fx for each x, using the given mathematical expression

plt.plot(x,fx,label=r'$f(x) = \frac{-0.1x}{(1+0.1x)(1+0.05x)}$') # Create a line plot of fx against x
plt.title("Question-1 Plot") # Set the title of the plot
plt.xlabel("x") # Set the label for the x-axis
plt.ylabel("f(x)") # Set the label for the y-axis
plt.legend() #Create legend
plt.savefig('Q1_Plot.png', dpi=300, bbox_inches='tight') #Save the plot as png file
plt.show() # Display the plot