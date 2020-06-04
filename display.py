import matplotlib.pyplot as plt
import numpy as np

def display_mosaic(list_slices):
    nb_img = len(list_slices)
    rows = 2

    for x in range(1,nb_img+1):
        img = list_slices[x-1]
        # rotate the right way
        img = np.rot90(img)
        plt.subplot(rows, 5, x)
        #str = 'slice %d' % slices[x-1]
        #plt.title(str)
        plt.axis('off')
        plt.imshow(img)
    plt.show()