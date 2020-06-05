import nibabel as nib
import numpy as np

def get_bbox(mask_path):
    mask = nib.load(mask_path)
    data_mask = mask.get_data()
    nb_slice_sag, nb_slice_axial, nb_slice_cor = data_mask.shape
    list_sum_sag = [0] * nb_slice_sag
    list_sum_axial = [0] * nb_slice_axial
    list_sum_cor = [0] * nb_slice_cor
    for s in range(0, nb_slice_sag):
        list_sum_sag[s] = np.sum(data_mask[s, :, :])
    for c in range(0, nb_slice_cor):
        list_sum_cor[c] = np.sum(data_mask[:, c, :])
    for a in range(0, nb_slice_axial):
        list_sum_axial[a] = np.sum(data_mask[:, :, a])

    # sagital
    slice_sag_right = next(x for x in list_sum_sag if x != 0)
    sright = list_sum_sag.index(slice_sag_right)
    list_sum_sag.reverse()
    slice_sag_left = next(x for x in list_sum_sag if x != 0)
    slice_sag_left = list_sum_sag.index(slice_sag_left)
    sleft = nb_slice_sag - slice_sag_left - 1
    # coronal
    slice_cor_post = next(x for x in list_sum_cor if x != 0)
    cpost = list_sum_cor.index(slice_cor_post)
    list_sum_cor.reverse()
    slice_cor_ant = next(x for x in list_sum_cor if x != 0)
    slice_cor_ant = list_sum_cor.index(slice_cor_ant)
    cant = nb_slice_cor - slice_cor_ant - 1
    # axial
    slice_axial_sup = next(x for x in list_sum_axial if x != 0)
    asup = list_sum_axial.index(slice_axial_sup)
    list_sum_axial.reverse()
    slice_axial_inf = next(x for x in list_sum_axial if x != 0)
    slice_axial_inf = list_sum_axial.index(slice_axial_inf)
    ainf = nb_slice_axial - slice_axial_inf - 1
    bbox = [sright, sleft, cpost, cant, asup, ainf]
    return bbox


def get_main_view(img_path):
    img = nib.load(img_path)
    data = img.get_fdata()
    main_view = [data[:, 100, :], data[110, :, :],data[:, 100, :]]
    return main_view
