import matplotlib.pyplot as plt
import sys
sys.path.append("..\<data_visual>")
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()