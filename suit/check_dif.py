import numpy as np
import nibabel as nib

img1_path = '/home/dieudonnem/hpc/out/suit/dataset_sence/pred/Folder_r09_sub-testanat2_acq-0p8mm_rec-uniden8000_T1w/iw_Lobules-SUIT_u_a_r09_sub-testanat2_acq-0p8mm_rec-uniden8000_T1w_seg1.nii'
img2path = '/home/dieudonnem/hpc/out/suit/dataset_sence/pred/T1T2/Folder_r09_sub-testanat2_acq-0p8mm_rec-uniden8000_T1w/iw_Lobules-SUIT_u_a_r09_sub-testanat2_acq-0p8mm_rec-uniden8000_T1w_seg1.nii'
img1 = nib.load(img1_path)
img2 = nib.load(img2path)
data1=img1.get_fdata()
data2 = img2.get_fdata()
print(np.sum(data1-data2))