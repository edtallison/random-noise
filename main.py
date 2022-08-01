import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

test_image = np.zeros((50,50))

for i in range(len(test_image)):
    for j in range(len(test_image[i])):
        test_image[i,j] += (i+j)*4

imgplot = plt.imshow(test_image, cmap='gray',vmin=0,vmax=255)

print(test_image)

plt.show()