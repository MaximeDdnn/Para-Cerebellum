import nibabel as nib
import numpy as np
import os
from scipy.ndimage import sobel, generic_gradient_magnitude
from comparaison.label import label_cnn, label_suit, label_suiter
from skimage.measure import find_contours
import matplotlib.pyplot as plt


soft_select = {
    'cnn': [label_cnn, 'r'],
    'suit': [label_suit, 'iw'],
    'suiter': [label_suiter, 'rs']
}


def save_mask(input_dir, soft, mask_flag=True, edge_flag=True):
    """
    :param input_dir: folder input where there are the folder img
    :param soft: you must chose between the stings 'cnn' or 'suit' or 'suiter'
    :param mask_flag : Boolean input. set it to True if you want mask saving
    :param edge_flag : Boolean input. set it to True if you want edge saving
    :return: all the mask coresponding to all output label of the specified soft hpc>>out>>'soft'>>dataset_sence>>
                sub-1>>derivative>>mask>>'img_folder'  >> all the mask
    """
    print(soft_select.get(soft))
    list_folder = os.listdir(input_dir)
    list_folder.sort()
    for folder in list_folder:
        pref = soft_select.get(soft)[1]
        img = [x for x in os.listdir(os.path.join(input_dir, folder)) if x.startswith(pref)]
        img = img[0]
        mri = nib.load(os.path.join(input_dir, folder, img))
        data = mri.get_fdata()
        label = np.unique(data)
        for lab in label:
            if mask_flag:
                ### mask
                mask = np.zeros(data.shape)
                mask[data == lab] = 1
                mask = nib.Nifti1Image(mask, mri.affine, mri.header)
                # save mask
                os.makedirs(os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1', 'derivative', 'mask', folder), exist_ok=True)
                set_name = soft_select.get(soft)[0]
                name = set_name.get(lab)
                nib.save(mask, os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1', 'derivative', 'mask', folder, name))
                print(soft, '>>', folder, '>>', name, 'mask saved')
            if edge_flag:
                ### edge
                # select area with specified label
                area = np.zeros(data.shape)
                area[data == lab] = lab
                # find edge of the area
                edge = generic_gradient_magnitude(area, sobel)
                # clean edge
                edge[edge < 0.5 * np.max(edge)] = 0
                new_img = nib.Nifti1Image(edge, mri.affine, mri.header)
                # save edge
                os.makedirs(os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1', 'derivative', 'edge', folder), exist_ok=True)
                set_name = soft_select.get(soft)[0]
                name = set_name.get(lab)
                nib.save(new_img, os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1', 'derivative', 'edge', folder, name))
                print(soft, '>>', folder, '>>', name, 'edge saved')




def edge_mask():
    mri = '/home/dieudonnem/hpc/out/comparaison/suiter_cnn/dataset_sence/sub-1/mask/suiter/r04_sub-testanat_acq-0p8mm_rec-MEMPRAGEnomotion_T1w/L_CrusI.nii'
    img = nib.load(mri)
    data = img.get_fdata()
    edge = generic_gradient_magnitude(data, sobel)
    # clean edge
    edge[edge < 0.7 * np.max(edge)] = 0
    new_img = nib.Nifti1Image(edge, img.affine, img.header)
    # save edge
    os.makedirs(os.path.join('/home/dieudonnem/hpc/out/', 'yolo'), exist_ok=True)
    nib.save(new_img, os.path.join('/home/dieudonnem/hpc/out/', 'yolo', 'name'))
    print('edge saved')

edge_mask()

# for soft in ['cnn', 'suiter', 'suit']:
#     input_dir = os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1/original')
#     save_mask(input_dir, soft, mask_flag=False)


