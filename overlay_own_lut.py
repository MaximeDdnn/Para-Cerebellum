# it's a script, the proper function is not written yet.
# input : 
# original image
# mask segmentation you want to overlay
# your personal lut
# output : image and mask overlay

import numpy as np
import nibabel as nib
import cv2
import pandas as pd

# load path
frame = 100
fname_t1 = '/home/maxime/hpc/data/dataset_sence/data/images_recale/Folder_r01_sub-testanat_T1w/r01_sub-testanat_T1w.nii'
fname_seg = '/home/maxime/hpc/data/dataset_sence/data/images_recale/Folder_r01_sub-testanat_T1w/iw_Lobules-SUIT_u_a_r01_sub-testanat_T1w_seg1.nii'
myLut = '/home/maxime/hpc/data/dataset_sence/data/images_recale/lut_perso_suit.csv'

# load data
img = nib.load(fname_t1)
seg = nib.load(fname_seg)
data = img.get_data()
dataseg = seg.get_data()
img50 = data[frame, :, :]
seg50 = dataseg[frame, :, :]

# Data are normalized because cv2 maps {0,1} to {0,255}
# e.g any value greater than 1 is equal to 255
img50N = (img50 - np.min(img50)) / (np.max(img50) - np.min(img50))
img50N = np.concatenate((img50N[:, :, None], img50N[:, :, None], img50N[:, :, None]),2)

# build lut
lut = pd.read_csv(myLut)
RGB = pd.DataFrame.to_numpy(lut[['Red','Green','Blue']])

# apply lut
seg50_R = np.zeros(seg50.shape)
seg50_G = np.zeros(seg50.shape)
seg50_B = np.zeros(seg50.shape)

for label in range(1,35):
    seg50_R[seg50 == label] = RGB[label-1, 0]
    seg50_G[seg50 == label] = RGB[label-1, 1]
    seg50_B[seg50 == label] = RGB[label-1, 2]

seg50_RGB = np.concatenate((seg50_R[:, :, None], seg50_G[:, :, None], seg50_B[:, :, None]), 2)
seg50N = (seg50_RGB - np.min(seg50_RGB)) / (np.max(seg50_RGB) - np.min(seg50_RGB))

# overlay
alpha = 0.5
beta = 1-alpha
dst = cv2.addWeighted(img50N, alpha, seg50N, beta, 0.0)

#display
cv2.imshow("seg", dst)
cv2.waitKey(0)
