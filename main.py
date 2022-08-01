import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

test_image = np.zeros((50,50))

for i in range(len(test_image)):
    for j in range(len(test_image[i])):
        test_image[i,j] += (i+j)

imgplot = plt.imshow(test_image)

print(test_image)

plt.show()