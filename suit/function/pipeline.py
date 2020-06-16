import os
from suit.function.overlay_own_lut import get_slices
from suit.function.display import save_slice_visual, save_slice
from suit.function.get_bbox import get_bbox, get_main_view
from suit.function.crop_slices import crop_slices


def pipeline(input_dir, folder, lut_path, idx_slice, out_dir):
    """
    :param input_dir:  your input directory where input folder are stored
    :param folder: the name of the folder with the SUIT output
    :param lut_path: the lut you want apply to the Suit segmentation mask overlayed on your MRI image
    :param idx_slice: [[idx_sagittal_slices],[idx_coronal_slices],[idx_axial_slices]] : the index of slices you want to save
    :param out_dir: output dir where you want to save png file of your slices
    :return:  out_dir ___ Folder_img1 ___ sagittal ___sliceX.png
                                     |            |___ ...
                                     |___ coronal ___sliceX.png
                                     |           |___...
                                     |___ axial ___slice89.png
                                     |         |___. ..
                                     |___ view ___ sagittal.png
                                                |___ coronal.png
                                                |___ axial.png
    the ouptput "/view" is an image of the cerebellum with line added on it that show the selected slices
    """
    # get img and mask path
    img_name = folder.split('_', 1)
    img_name = img_name[1]
    mask_name = 'iw_Lobules-SUIT_u_a_' + img_name + '_seg1' + '.nii'
    img_name = img_name + '.nii'
    img_path = os.path.join(input_dir, folder, img_name)
    mask_path = os.path.join(input_dir, folder, mask_name)

    # figure out which slices are good to save for segmentation evaluation.
    bbox = get_bbox(mask_path)
    str = 'getbbox done \n sright = %d, sleft = %d, cpost = %d, cant = %d, asup = %d, ainf = %d, ' % (bbox[0], bbox[1], bbox[2], bbox[3], bbox[4], bbox[5])
    print(str)

    # save the desired slices
    list_slices = get_slices(img_path, mask_path, lut_path, idx_slice, lut_flag=True)

    # zoom around the cerebellum
    marge = 5  # marge around the crop
    list_slices = crop_slices(list_slices, bbox, marge)
    print('les slices sont enregistrées dans une liste')
    # display and save
    out_file = os.path.join(out_dir, folder)
    main_view = get_main_view(img_path)
    save_slice_visual(main_view, out_file, idx_slice)
    save_slice(idx_slice,list_slices, out_file)
    print('visual and slices sauvegardées dans le dossier \n')


