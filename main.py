import matplotlib.pyplot as plt
import numpy as np
from random_funcs import *

WIDTH = 50
HEIGHT = 50

# note (0,0) is top left of image
out_image = np.zeros((HEIGHT,WIDTH))

for _ in range(5):
    test_point = random_point(out_image)
    print(test_point)
    out_image[test_point] = 255

imgplot = plt.imshow(out_image, cmap='gray',vmin=0,vmax=255)

if __name__ == "__main__":
    # print the matrix of numbers that make up the image
    print(out_image)
    # show the image
    plt.show()