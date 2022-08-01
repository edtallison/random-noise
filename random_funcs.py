import numpy.random as random

def random_point(size):

    height, width = size

    y = random.random_integers(0, height)
    x = random.random_integers(0, width)

    position = (y, x)

    return position

def random_radius(size):

    height, width = size

    max_radius = int(min(height, width) / 4)
    min_radius = 5

    size = random.random_integers(min_radius, max_radius)

    return size