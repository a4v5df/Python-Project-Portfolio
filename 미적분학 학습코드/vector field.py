import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameter t values
t = np.linspace(-1,1, 1000)  # Range of t from 0 to 2*pi
t_1 = np.linspace(-2,2, 1000)
# Define the parametric equations
x = np.cosh(t_1)
y = np.sinh(t_1)
z = np.zeros_like(t_1)
a=5/3+(4/3)*t
b=4/3+(5/3)*t
c=np.zeros_like(t)
# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

# Plot the parametric curve
ax.plot(x, y, z,color='black',alpha=0.7)
ax.plot(a,b,c,color='red')
# Set plot labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


# Show the plot
plt.legend()
plt.show()
