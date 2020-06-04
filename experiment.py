import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from overlay_own_lut import get_slices
from display import display_mosaic
from get_bbox import get_bbox
import math

img_path = '/home/dieudonnem/hpc/data/dataset_sence/Folder_r01_sub-testanat_T1w/r01_sub-testanat_T1w.nii'
mask_path = '/home/dieudonnem/hpc/data/dataset_sence/Folder_r01_sub-testanat_T1w/iw_Lobules-SUIT_u_a_r01_sub-testanat_T1w_seg1.nii'
lut_path = 'lut_perso.csv'


img = nib.load(img_path)
data = img.get_fdata()
data2 = np.rot90(data,1,(1,2))

sag = data[100, :, :]
axial = data[:, 100, :]
cor = data[:, :, 100]




sag2 = data2[100, :, :]
axial2 = data2[:, 100, :]
cor2 = data2[:, :, 100]


plt.figure()
plt.subplot(2,3,1)
plt.imshow(sag)
plt.subplot(2,3,2)
plt.imshow(axial)
plt.subplot(2,3,3)
plt.imshow(cor)
plt.subplot(2,3,4)
plt.imshow(sag2)
plt.subplot(2,3,5)
plt.imshow(axial2)
plt.subplot(2,3,6)
plt.imshow(cor2)

plt.show()
