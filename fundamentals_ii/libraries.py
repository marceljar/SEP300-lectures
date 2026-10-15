import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y = np.square(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y)
plt.title("Squares of Numbers")
plt.xlabel("Number")
plt.ylabel("Square")
plt.savefig("squares_plot.png", dpi=300)
plt.close()
