import numpy as np

def linear_square(image, position, size):
    # add single linear square noise to image
    #
    # Inputs:
    # image: 2x2 np array
    # position: (y, x) tuple
    # size: int (radius from position)

    image[position] = 255