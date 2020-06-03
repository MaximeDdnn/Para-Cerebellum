import nibabel as nib
import numpy as np

def get_bbox(mask_path):
    mask = nib.load(mask_path)
    data_mask = mask.get_data()
    np.rot90(data_mask,k=1,axes=(1,2))
    print(data_mask.shape)
    nb_slice_sag, nb_slice_cor, nb_slice_axial = data_mask.shape
    list_sum_sag = [0] * nb_slice_sag
    list_sum_cor = [0] * nb_slice_cor
    list_sum_axial = [0] * nb_slice_axial
    for i in range(0, nb_slice_sag):
        list_sum_sag[i] = np.sum(data_mask[i, :, :])
    for j in range(0, nb_slice_cor):
        list_sum_cor[j] = np.sum(data_mask[:, j, :])
    for k in range(0, nb_slice_axial):
        list_sum_axial[k] = np.sum(data_mask[:, :, k])
    # sagital
    slice_sag_right = next(x for x in list_sum_sag if x != 0)
    list_sum_sag.reverse()
    slice_sag_left = next(x for x in list_sum_sag if x != 0)
    slice_sag_left = nb_slice_sag - slice_sag_left
    # coronal
    slice_cor_ant = next(x for x in list_sum_cor if x != 0)
    list_sum_cor.reverse()
    slice_cor_post = next(x for x in list_sum_cor if x != 0)
    slice_cor_post = nb_slice_cor - slice_cor_post
    # axial
    slice_axial_sup = next(x for x in list_sum_axial if x != 0)
    list_sum_axial.reverse()
    slice_axial_inf = next(x for x in list_sum_axial if x != 0)
    slice_axial_inf = nb_slice_axial - slice_axial_inf
    return slice_sag_right, slice_sag_left, slice_cor_ant, slice_cor_post, slice_axial_sup, slice_axial_inf
