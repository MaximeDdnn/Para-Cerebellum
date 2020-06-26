import nibabel as nib
import numpy as np
import os
from scipy.ndimage import sobel, generic_gradient_magnitude

# suiter
# soft = 'suiter'
# input = '/home/dieudonnem/hpc/out/suiter/dataset_sence/sub-1/evaluation/in'
# save_dir = '/home/dieudonnem/hpc/out/suiter/dataset_sence/sub-1/evaluation/out'
# list_img = os.listdir(input)
# list_img.sort()

# suit
soft = 'suit'
input = '/home/dieudonnem/hpc/out/suit/dataset_sence/sub-1/evaluation/in'
save_dir = '/home/dieudonnem/hpc/out/suit/dataset_sence/sub-1/evaluation/out'
list_img = os.listdir(input)
list_img.sort()

# label Suit/er
# 0 : bg
# 1 : CM
# 2 : R I-III
# 3 : L I-III
# 4 : R IV
# 5 : L IV
# 6 : R V
# 7 : L V
# 8 : R VI
# 9 : V VI
# 10 : L VI
# 11 : V VII
# 12 : R CRI
# 13 : R CRII
# 14 : R VIIB
# 15 : L CRI
# 16 : L CRII
# 17 : L VIIB
# 18 : V VIII
# 19 : R VIIIA
# 20 : R VIIIB
# 21 : L VIIIA
# 22 : L VIIIB
# 23 : V IX
# 24 : R IX
# 25 : L IX
# 26 : V X
# 27 : L X
# 28 : R X
# 29 : L dentate
# 30 : R dentate
# 31 : L inter
# 32 : R inter
# 33 : L fas
# 34 : R fas

# CNN
# soft = 'CNN'
# input = '/home/dieudonnem/hpc/out/CNN/dataset_sence/sub-1/evaluation/in'
# save_dir = '/home/dieudonnem/hpc/out/CNN/dataset_sence/sub-1/evaluation/out'
# list_img = os.listdir(input)
# list_img.sort()
# label CNN
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

