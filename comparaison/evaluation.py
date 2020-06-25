import nibabel as nib
import numpy as np
import os
from scipy.ndimage import sobel, generic_gradient_magnitude


# CNN
soft = 'CNN'
input = '/home/dieudonnem/hpc/out/CNN/dataset_sence/sub-1/evaluation/in'
save_dir = '/home/dieudonnem/hpc/out/CNN/dataset_sence/sub-1/evaluation/out'
list_img = os.listdir(input)
list_img.sort()

# label
# 0 : bg
# 12 : CM
# 33 : R I-III
# 36 : L I-III
# 43 : R IV
# 46 : L IV
# 53 : R V
# 56 : L V
# 60 : R VI
# 63 : V VI
# 66 : L VI
# 70 : V VII
# 73 : R CRI
# 74 : R CRII
# 75 : R VIIB
# 76 : L CRI
# 77 : L CRII
# 78 : L VIIB
# 80 : V VIII
# 83 : R VIIIA
# 84 : R VIIIB
# 86 : L VIIIA
# 87 : L VIIIB
# 90 : V IX
# 93 : R IX
# 96 : L IX
# 100 : V X
# 103 : R X
# 106 : L X


def draw_fissure(list_img):
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


draw_fissure(list_img)

