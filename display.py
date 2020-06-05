import matplotlib.pyplot as plt
import numpy as np

def display_mosaic(main_view,list_slices):
    nb_rows = len(list_slices) # nb view
    nb_s = len(list_slices[0]) # nb slice sagital
    nb_c = len(list_slices[1]) # nb slice coronal
    nb_a = len(list_slices[2]) # nb slice axial
    nb_col = max(nb_s, nb_c, nb_a) + 1
    nb = [nb_s, nb_c, nb_a]
    plt.figure()
    for i in range(1, nb_rows+1):
        img = main_view[i-1]
        img = np.rot90(img)
        plt.subplot(nb_rows, nb_col, 1 + (i-1)*(nb_col))
        plt.axis('off')
        plt.imshow(img)
    for view in [0, 1, 2]:
        for x in range(1, nb[view] + 1):
            img = list_slices[view][x-1]
            # rotate the right way
            img = np.rot90(img)
            plt.subplot(nb_rows, nb_col, x+ (view*nb_col) +1)
            #str = 'slice %d' % slices[x-1]
            #plt.title(str)
            plt.axis('off')
            plt.imshow(img)
    plt.show()