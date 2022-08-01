import numpy.random as random

def random_point(image):

    height = len(image)
    width = len(image[0])

    y = random.random_integers(0, height)
    x = random.random_integers(0, width)

    return (y, x)

def random_size(image):
    # size measured as radius in pixels

    height = len(image)
    width = len(image[0])

    max_size = min(height, width) / 2
    min_size = 5

    size = random.random_integers(min_size, max_size)

    return size