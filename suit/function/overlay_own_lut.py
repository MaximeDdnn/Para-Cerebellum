import numpy as np
import nibabel as nib
import cv2
import pandas as pd


def gt_slice_dim0(arr, x):
    return arr[x, :, :]


def gt_slice_dim1(arr, x):
    return arr[:, x, :]


def gt_slice_dim2(arr, x):
    return arr[:, :, x]


switcher = {
    0: gt_slice_dim0,
    1: gt_slice_dim1,
    2: gt_slice_dim2
}

def get_slices(img_path, mask_path, lut_path, slices, lut_flag):
    """
    :param img_path: path of your original MRI image
    :param mask_path: path of the mask you want overlay on your original MRI image
    :param lut_path: path of the lut for the mask
    :param slices: [[idx_sagittal_slices],[idx_coronal_slices],[idx_axial_slices]] : the index of slices you want to save
    :param lut_flag: boolean, if True : return your image with mask overlay, if false, return just your original image
    :return: list_slice : a list of list of images [[sagittal slices],[coronal slices ],[axial slices]]
    """
    # load image and mask
    img = nib.load(img_path)
    mask = nib.load(mask_path)
    data_img = img.get_data()
    data_mask = mask.get_data()

    nview = len(slices)
    list_slices = [0]*nview
    for view in range(nview):
        list_slices[view] = [0]*len(slices[view])

    # loop
    for view in range(nview):
        sl = slices[view]
        list_sl = list_slices[view]
        idx_list_slices = 0
        for num_slice in sl:
            func = switcher.get(view)
            data_imgslice = func(data_img, num_slice)
            data_maskslice = func(data_mask, num_slice)

            # Data are normalized because cv2 maps {0,1} to {0,255}
            # e.g any value greater than 1 is equal to 255
            data_norm_imgslice = (data_imgslice - np.min(data_imgslice)) / (np.max(data_imgslice) - np.min(data_imgslice))
            data_norm_imgslice = np.concatenate(
                (data_norm_imgslice[:, :, None], data_norm_imgslice[:, :, None], data_norm_imgslice[:, :, None]), 2)

            if lut_flag:
                # build lut
                lut = pd.read_csv(lut_path)
                RGB = pd.DataFrame.to_numpy(lut[['Red', 'Green', 'Blue']])

                # apply lut
                data_maskslice_R = np.zeros(data_maskslice.shape)
                data_maskslice_G = np.zeros(data_maskslice.shape)
                data_maskslice_B = np.zeros(data_maskslice.shape)

                for label in range(1, 35):
                    data_maskslice_R[data_maskslice == label] = RGB[label - 1, 0]
                    data_maskslice_G[data_maskslice == label] = RGB[label - 1, 1]
                    data_maskslice_B[data_maskslice == label] = RGB[label - 1, 2]

                data_maskslice_RGB = np.concatenate(
                    (data_maskslice_R[:, :, None], data_maskslice_G[:, :, None], data_maskslice_B[:, :, None]), 2)
                data_norm_maskslice_RGB = (data_maskslice_RGB - np.min(data_maskslice_RGB)) / (
                        np.max(data_maskslice_RGB) - np.min(data_maskslice_RGB))

                # overlay
                alpha = 0.6
                beta = 1 - alpha
                img_overlay = cv2.addWeighted(data_norm_imgslice, alpha, data_norm_maskslice_RGB, beta, 0.0)

                # stock in list_slices
                list_sl[idx_list_slices] = img_overlay
                idx_list_slices = idx_list_slices + 1
            else:
                list_sl[idx_list_slices] = data_norm_imgslice
                idx_list_slices = idx_list_slices + 1

            # display
            #cv2.imshow("sagital view", img_overlay)
            #cv2.waitKey(0)
        list_slices[view] = list_sl

    return list_slices
