import matplotlib.pyplot as plt
import numpy as np

#Radius 
Zaviye = np.linspace(0, 2 * np.pi, 100)
Radius = 5

#X and Y
X = Radius * np.cos(Zaviye)
Y = Radius * np.sin(Zaviye)
plt.figure(figsize=(10, 10))
plt.plot(X, Y)
plt.gca().set_aspect('equal', adjustable='box')  


plt.title('Circle Draw')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
