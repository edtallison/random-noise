import matplotlib.pyplot as plt
import numpy as np
from random_funcs import *
from alter_funcs import *

size = (50, 50)

# note (0,0) is top left of image
out_image = np.zeros(size)

for _ in range(10):
    position = random_point(size)
    radius = random_radius(size)
    linear_square(out_image, size, position, radius)

imgplot = plt.imshow(out_image, cmap='gray',vmin=0,vmax=255)

if __name__ == "__main__":
    # print the matrix of numbers that make up the image
    print(out_image)
    # show the image
    plt.show()