import matplotlib.pyplot as plt
import numpy as np
from random_funcs import *
from alter_funcs import *

WIDTH = 50
HEIGHT = 50

# note (0,0) is top left of image
out_image = np.zeros((HEIGHT,WIDTH))

for _ in range(5):
    position = random_point(out_image)
    size = random_size(out_image)
    linear_square(out_image, position, size)

imgplot = plt.imshow(out_image, cmap='gray',vmin=0,vmax=255)

if __name__ == "__main__":
    # print the matrix of numbers that make up the image
    print(out_image)
    # show the image
    plt.show()