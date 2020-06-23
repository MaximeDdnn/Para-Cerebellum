import nibabel as nib
import numpy as np
import os
from scipy.ndimage import sobel, generic_gradient_magnitude


out_dir = '/home/dieudonnem/hpc/out'

soft = ['suit', 'suiter']
dataset =  'dataset_sence'
sub = 'sub-1'
folder = ['Folder_r09_sub-testanat2_acq-0p8mm_rec-uniden8000_T1w', 'r09_sub-testanat2_acq-0p8mm_rec-uniden8000_T1w']

# suiter
img_suit = os.path.join(out_dir, soft[0], dataset, sub, folder[0], 'iw_Lobules-SUIT_u_a_r09_sub-testanat2_acq-0p8mm_rec-uniden8000_T1w_seg1.nii')
# suit
img_suiter = os.path.join(out_dir, soft[1], dataset, sub, folder[1], 'ro_wCBS_SUIT.nii')

save_dir = '/home/dieudonnem/hpc/out/comparaison'
img = [img_suit, img_suiter]
label = np.arange(35)

def draw_fissure(img,label):
    # init seg, data, edge
    print(len(img))
    seg = [0]*len(img)
    data = [0]*len(img)

    for i in range(len(img)):
        seg[i] = nib.load(img[i])
        data[i] = seg[i].get_fdata()
    print(data[1].shape,data[0].shape)

    # process
    for i in range(len(img)):
        for lab in label:
            # select area with specified label
            area = np.zeros(data[i].shape)
            print(np.min(data[i]), np.max(data[i]))
            print(np.min(area), np.max(area))
            area[data[i] == lab] = lab
            # find edge of the area
            edge = generic_gradient_magnitude(area, sobel)
            print(np.min(edge), np.max(edge))
            # clean edge
            edge[edge < 0.5 * np.max(edge)] = 0
            new_img = nib.Nifti1Image(edge, seg[i].affine, seg[i].header)
            name = soft[i] + '_lab_' + str(lab)
            nib.save(new_img, os.path.join(save_dir, name))


draw_fissure(img, label)

