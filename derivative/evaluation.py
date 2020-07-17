import nibabel as nib
import numpy as np
import os
from scipy.ndimage import sobel, generic_gradient_magnitude


def save_edge(list_img):
    for img in list_img:
        mri = nib.load(os.path.join(input, img))
        data = mri.get_fdata()
        label = np.unique(data)
        print(len(np.unique(data)))
        for lab in label:
            # select area with specified label
            area = np.zeros(data.shape)
            area[data == lab] = lab
            # find edge of the area
            edge = generic_gradient_magnitude(area, sobel)
            print(np.min(edge), np.max(edge))
            # clean edge
            edge[edge < 0.5 * np.max(edge)] = 0
            new_img = nib.Nifti1Image(edge, mri.affine, mri.header)
            # saving
            name = soft + '_lab-' + str(int(lab))
            folder_out = img.split('.')
            folder_out = folder_out[0]
            if not os.path.exists(os.path.join(save_dir, folder_out)):
                os.mkdir(os.path.join(save_dir, folder_out))
            nib.save(new_img, os.path.join(save_dir, folder_out, name))




