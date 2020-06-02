#!/usr/bin/env python3
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from functions import show_slices
from nilearn import plotting as plot
from save_slice import get_slices
from display import display_mosaic

img_path = '/home/maxime/hpc/data/dataset_sence/data/images_recale/Folder_r01_sub-testanat_T1w/r01_sub-testanat_T1w.nii'
mask_path = '/home/maxime/hpc/data/dataset_sence/data/images_recale/Folder_r01_sub-testanat_T1w/iw_Lobules-SUIT_u_a_r01_sub-testanat_T1w_seg1.nii'
lut_path = '/home/maxime/hpc/data/dataset_sence/data/images_recale/lut_perso_suit.csv'


slices = [50,89,100,150,160]

list_slices = get_slices(img_path,slices,mask_path,lut_path)
display_mosaic(list_slices,slices)






