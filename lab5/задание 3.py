import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from mpl_toolkits.mplot3d import Axes3D # type: ignore

#1
x = np.linspace(-100, 100, 100)
y = np.linspace(-100, 100, 100)
x, y = np.meshgrid(x, y)
z = np.power(x, 0.25) + np.power(y, 0.25)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

#2
x = np.linspace(-100, 100, 100)
y = np.linspace(-100, 100, 100)
x, y = np.meshgrid(x, y)
z = x**2 - y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='coolwarm')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

#3
x = np.linspace(-100, 100, 100)
y = np.linspace(-100, 100, 100)
x, y = np.meshgrid(x, y)
z = 2*x + 3*y

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='plasma')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

#4
x = np.linspace(-100, 100, 100)
y = np.linspace(-100, 100, 100)
x, y = np.meshgrid(x, y)
z = x**2 + y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='cividis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

#5
x = np.linspace(-100, 100, 100)
y = np.linspace(-100, 100, 100)
x, y = np.meshgrid(x, y)
z = 2 + 2*x + 2*y - x**2 - y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='cividis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()