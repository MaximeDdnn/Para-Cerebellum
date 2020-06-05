import matplotlib.pyplot as plt
import numpy as np


def display_mosaic(main_view, list_slices, list_idx):
    nrow = len(list_slices)  # nb view
    nb = [0]*nrow
    for view in range(nrow):
        nb[view] = len(list_slices[view])
    ncol = np.max(nb)+1
    fig = plt.figure(figsize=(20,4))
    for i in range(1, nrow + 1):
        img = main_view[i - 1]
        plt.subplot(nrow, ncol, 1 + (i - 1) * (ncol))
        plt.axis('off')
        plt.imshow(img)
        if i != 3:
            for y in list_idx[i - 1]:
                plt.axhline(y=y, color='red',linewidth=0.5 )
        else:
            for x in list_idx[i - 1]:
                plt.axvline(x=x, color='red',linewidth=1 )
    for view in range(nrow):
        for x in range(1, nb[view] + 1):
            img = list_slices[view][x - 1]
            # rotate the right way
            img = np.rot90(img)
            plt.subplot(nrow, ncol, x + (view * ncol) + 1)
            # str = 'slice %d' % slices[x-1]
            # plt.title(str)
            plt.axis('off')
            plt.subplots_adjust( wspace=0.03)
            plt.imshow(img)
    plt.show()
