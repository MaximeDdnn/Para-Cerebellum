
#!/usr/bin/env python3
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from functions import show_slices
from nilearn import plotting as plot
from save_slice import get_slices
from display import display_mosaic
from get_bbox import get_bbox
import math

img_path = '/home/maxime/hpc/data/dataset_sence/data/images_recale/Folder_r01_sub-testanat_T1w/r01_sub-testanat_T1w.nii'
mask_path = '/home/maxime/hpc/data/dataset_sence/data/images_recale/Folder_r01_sub-testanat_T1w/iw_Lobules-SUIT_u_a_r01_sub-testanat_T1w_seg1.nii'
lut_path = '/home/maxime/hpc/data/dataset_sence/data/images_recale/lut_perso_suit.csv'

mask=nib.load(mask_path)
data_mask=mask.get_data()
plt.figure()
plt.imshow(data_mask[100:,:,:])
plt.show()
np.rot90(data_mask,k=1,axes=(1,2))
plt.figure()
plt.imshow(data_mask[100:,:,:])
plt.show()


smin, smax, cmin, cmax, amin, amax = get_bbox(mask_path)

print(smin, smax, cmin, cmax, amin, amax)


pas_s = int(math.floor(((smax - smin)/5)))
pas_c = int(math.floor(((cmax - cmin)/5)))
slices_sag = np.arange(smin, smax, pas_s)
slices_sag = [int(x) for x in slices_sag]

slices_cor = np.arange(cmin, cmax, pas_c)
slices_cor = [int(y) for y in slices_cor]
print(slices_cor)
print(slices_sag)

#slices_sag = [150,151]
#slices_cor = [80,81]

list_slices_sag, list_slices_cor = get_slices(img_path, mask_path, lut_path, slices_sag,slices_cor)
display_mosaic(list_slices_sag, slices_sag)
display_mosaic(list_slices_cor, slices_cor)










