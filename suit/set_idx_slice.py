from suit.function.display import display_mosaic
from suit.function.overlay_own_lut import get_slices
from suit.function.get_bbox import get_bbox, get_main_view
from suit.function.cut_bbox import cut_bbox
from suit.function.crop_slices import crop_slices


dir_path = '/home/dieudonnem/hpc/data/dataset_sence/'
# a priori best image
img_path = '/home/dieudonnem/hpc/data/dataset_sence/Folder_r09_sub-testanat2_acq-0p8mm_rec-uniden8000_T1w/r09_sub-testanat2_acq-0p8mm_rec-uniden8000_T1w.nii'
mask_path = '/home/dieudonnem/hpc/data/dataset_sence/Folder_r09_sub-testanat2_acq-0p8mm_rec-uniden8000_T1w/iw_Lobules-SUIT_u_a_r09_sub-testanat2_acq-0p8mm_rec-uniden8000_T1w_seg1.nii'
lut_path = 'doc/lut_perso.csv'

# get bbox
bbox = get_bbox(mask_path)
    # stdout
str = 'getbbox done \n sright = %d, sleft = %d, cpost = %d, cant = %d, asup = %d, ainf = %d, ' % (
bbox[0], bbox[1], bbox[2], bbox[3], bbox[4], bbox[5])
print(str)

nb_cut = [11,6]
idx_slice = cut_bbox(bbox, nb_cut)  # idx_slice = [[idx_s],[idx_c],[idx_a]]
print('idx_slice = ', idx_slice)

# Schmaahman paper Sagittal images progressing laterally by increment of 10 mm
idx_slice[0] = [50, 60, 70, 80, 90, 100]

# Schmaahman paper Coronal fig 20-25 : images comencint at y=-38 and progressing caudally to y= -88
idx_slice[1] = [70, 80, 90, 100, 110, 120]


# get the desired slices
list_slices = get_slices(img_path, mask_path, lut_path, idx_slice)

# zoom around the cerebellum
marge = 5  # marge around the crop
list_slices = crop_slices(list_slices, bbox, marge)

#display
main_view = get_main_view(img_path)
display_mosaic(main_view, list_slices, idx_slice )




