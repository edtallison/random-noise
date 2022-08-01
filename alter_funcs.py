import numpy as np

def stars(image, size, position, rad):
    # add stars to image
    #
    # Inputs:
    # image: 2x2 np array
    # position: (y, x) tuple
    # size: int (radius from position)

    y, x = position
    height, width = size

    bound_l = max(0, x - rad)
    bound_r = min(width, x + rad)
    bound_t = max(0, y - rad)
    bound_b = min(height, y + rad)

    for i in range(rad):
        dist_amount = 10*(rad-i)
        if x+i < bound_r:
            image[y, x+i] += dist_amount
        if x-i > bound_l:
            image[y, x-i] += dist_amount
        if y+i < bound_b:
            image[y+i, x] += dist_amount
        if y-i > bound_t:
            image[y-i, x] += dist_amount

def linear_square(image, size, position, rad):
    # add single linear square noise to image
    #
    # Inputs:
    # image: 2x2 np array
    # position: (y, x) tuple
    # size: int (radius from position)

    y, x = position
    height, width = size

    bound_l = max(0, x - rad)
    bound_r = min(width, x + rad)
    bound_t = max(0, y - rad)
    bound_b = min(height, y + rad)

    for i in range(rad):
        dist_amount = 10*(rad-i)
        if x+i < bound_r:
            image[y, x+i] += dist_amount
        if x-i > bound_l:
            image[y, x-i] += dist_amount
        if y+i < bound_b:
            image[y+i, x] += dist_amount
        if y-i > bound_t:
            image[y-i, x] += dist_amount

        