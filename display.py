import matplotlib.pyplot as plt


def display_mosaic(list_slices, slices):
    nb_img = len(list_slices)
    rows = 2

    for x in range(1,nb_img+1):
        img = list_slices[x-1]
        plt.subplot(rows, 5, x)
        str = 'slice %d' % slices[x-1]
        plt.title(str)
        plt.axis('off')
        plt.imshow(img)
    plt.show()