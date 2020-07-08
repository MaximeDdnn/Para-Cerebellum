import os
import nibabel as nib
import numpy as np
from scipy.ndimage import sobel, generic_gradient_magnitude


walk_dir = '/home/dieudonnem/hpc/out/comparaison/suiter_cnn/dataset_sence/sub-1/mask'

for root, subdirs, files in os.walk(walk_dir):
    for name in files:
        # input
        path_input = os.path.join(root, name)
        img = nib.load(path_input)
        data = img.get_fdata()
        print(path_input, '>> load')
        # process
        edge = generic_gradient_magnitude(data, sobel)
        edge[edge < 0.7 * np.max(edge)] = 0 # cleaning
        print(path_input, '>> processed')
        # output
        path_output = path_input.split('mask')[0] + 'edge' + path_input.split('mask')[1]
        os.makedirs(os.path.dirname(path_output), exist_ok
         =True)
        print(path_output, '>> created')
        # saving
        new_img = nib.Nifti1Image(edge, img.affine, img.header)
        nib.save(new_img, path_output)
        print(path_output, '>> save')


