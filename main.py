
#!/usr/bin/env python3
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

sleft, sright, asup, ainf, cpost, cant = get_bbox(mask_path)

str = 'getbbox done \n sleft = %d, sright = %d, asup = %d, ainf = %d, cpost = %d, cant = %d' %(sleft, sright, asup, ainf, cpost, cant)
print(str)

step_s = int(math.floor(((sright - sleft)/10)))
step_c = int(math.floor(((cant - cpost)/5)))
step_a = int(math.floor(((ainf-asup)/3)))

slices_sag = np.arange(sleft, sright, step_s)
slices_sag = [int(x) for x in slices_sag]

slices_cor = np.arange(cpost, cant, step_c)
slices_cor = [int(y) for y in slices_cor]

list_slices = get_slices(img_path, mask_path, lut_path, slices_sag, slices_cor, [100,101])


display_mosaic(list_slices[0], slices_sag)
display_mosaic(list_slices[1], slices_cor)










