import numpy.random as random

def random_point(image):
    
    height = len(image)
    width = len(image[0])

    y = random.random_integers(0, height)
    x = random.random_integers(0, width)

    return (y, x)