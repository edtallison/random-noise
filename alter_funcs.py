import numpy as np

def linear_square(image, position, size):
    # add single linear square noise to image
    #
    # Inputs:
    # image: 2x2 np array
    # position: (y, x) tuple
    # size: int (radius from position)

    y, x = position

    for i in range(size):
        if x+i < len(image[0]):
            image[y, x+i] += (255-10*i)