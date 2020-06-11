import matplotlib.pyplot as plt
import numpy as np
import os
import nibabel as nib


def save_slice(list_idx, list_slice, out_dir):
    out_folder = ['sagital', 'coronal', 'axial']
    nbview = len(list_slice)
    for view in range(nbview):
        for idx, slice in enumerate(list_slice[view]):
            name_fig = '%d.png' % list_idx[view][idx]
            plt.figure()
            slice = np.rot90(slice)
            plt.imshow(slice)
            if not os.path.exists(os.path.join(out_dir, out_folder[view])):
                os.mkdir(os.path.join(out_dir, out_folder[view]))
            plt.title('%s %d'%(out_folder[view],list_idx[view][idx]))
            plt.savefig(os.path.join(out_dir, out_folder[view], name_fig))
            plt.close()


def save_slice_visual(main_view, out_dir, list_idx):
    out_folder = 'visual'
    name_fig = ['sagital.png', 'coronal.png','axial.png']
    nbview = len(list_idx)
    for view in range(nbview):
        plt.figure()
        plt.imshow(main_view[view])
        if view != 2:
            for y in list_idx[view]:
                plt.axhline(y=y, color='red', linewidth=0.5)
        else:
            for x in list_idx[view]:
                plt.axvline(x=x, color='red', linewidth=0.5)
        if not os.path.exists(os.path.join(out_dir, out_folder)):
            os.mkdir(os.path.join(out_dir, out_folder))
        main_view[view] = np.rot90(main_view[view])
        plt.savefig(os.path.join(out_dir, out_folder, name_fig[view]))
        plt.close()


# def display_mosaic(main_view, list_slices, list_idx):
#     ncol = len(list_slices)  # nb view
#     nb = [0]*ncol
#     for view in range(ncol):
#         nb[view] = len(list_slices[view])
#     nrow = np.max(nb)+1
#     plt.figure()
#     for i in range(1, ncol + 1):
#         img = main_view[i - 1]
#         plt.subplot(nrow, ncol, i)
#         plt.axis('off')
#         plt.imshow(img)
#         if i != 3:
#             for y in list_idx[i - 1]:
#                 plt.axhline(y=y, color='red', linewidth=0.5 )
#         else:
#             for x in list_idx[i - 1]:
#                 plt.axvline(x=x, color='red', linewidth=1 )
#     for view in range(ncol):
#         for x in range(1, nb[view] + 1):
#             img = list_slices[view][x - 1]
#             # rotate the right way
#             img = np.rot90(img)
#             plt.subplot(nrow, ncol, ((x*ncol)+1)+view)
#             str = 'slice %d' % list_idx[view][x-1]
#             plt.title(str)
#             plt.axis('off')
#             #plt.subplots_adjust( wspace=0.03)
#             plt.imshow(img)
#     plt.show()




