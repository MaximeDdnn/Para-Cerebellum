#!/usr/bin/env python3
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from overlay_own_lut import get_slices
from display import display_mosaic
from get_bbox import get_bbox, get_main_view
from cut_bbox import cut_bbox
from crop_slices import crop_slices

# load
img_path = '/home/dieudonnem/hpc/data/dataset_sence/Folder_r01_sub-testanat_T1w/r01_sub-testanat_T1w.nii'
mask_path = '/home/dieudonnem/hpc/data/dataset_sence/Folder_r01_sub-testanat_T1w/iw_Lobules-SUIT_u_a_r01_sub-testanat_T1w_seg1.nii'
lut_path = 'lut_perso.csv'

# get 3Dbbox around cerebellum
bbox = get_bbox(mask_path)
str = 'getbbox done \n sright = %d, sleft = %d, cpost = %d, cant = %d, asup = %d, ainf = %d, ' %(bbox[0],bbox[1],bbox[2],bbox[3],bbox[4],bbox[5])
print(str)

# find index of slice according the number of cuts needed
nb_cut = [10, 10, 2] # 5 slices sagital, 5 slices coronal, 2 slices axials
print(nb_cut[0],nb_cut[1],nb_cut[2])
idx_slice = cut_bbox(bbox, nb_cut) # idx_slice = [[idx_s],[idx_c],[idx_a]]
print('idx_slice = ', idx_slice)
# save the desired slices
list_slices = get_slices(img_path, mask_path, lut_path, idx_slice)

# zoom around the cerebellum
marge = 5 # marge around the crop
list_slices = crop_slices(list_slices, bbox, marge)

# display
main_view = get_main_view(img_path)
display_mosaic(main_view,list_slices,idx_slice)











