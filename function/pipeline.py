import os
from function.overlay_own_lut import get_slices
from function.display import save_slice_visual, save_slice
from function.get_bbox import get_bbox, get_main_view
from function.cut_bbox import cut_bbox
from function.crop_slices import crop_slices
from function.jinja_env import make_report


def pipeline(dir_path, folder, lut_path, info_dataset, idx_slice, out_dir):
    # get img and mask path
    img_name = folder.split('_', 1)
    img_name = img_name[1]
    mask_name = 'iw_Lobules-SUIT_u_a_' + img_name + '_seg1' + '.nii'
    img_name = img_name + '.nii'
    img_path = os.path.join(dir_path, folder, img_name)
    mask_path = os.path.join(dir_path, folder, mask_name)

    # figure out which slices are good to save for segmentation evaluation.
    bbox = get_bbox(mask_path)
    str = 'getbbox done \n sright = %d, sleft = %d, cpost = %d, cant = %d, asup = %d, ainf = %d, ' % (bbox[0], bbox[1], bbox[2], bbox[3], bbox[4], bbox[5])
    print(str)

    # # find index of slice according the number of cuts needed
    # nb_cut = [5,5,2]  # 5 slices sagital, 5 slices coronal, 2 slices axials
    # idx_slice = cut_bbox(bbox, nb_cut)  # idx_slice = [[idx_s],[idx_c],[idx_a]]
    # print('idx_slice = ', idx_slice)

    # save the desired slices
    list_slices = get_slices(img_path, mask_path, lut_path, idx_slice)

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

    # make pdf report
    # img_recap = info_dataset.loc[info_dataset['name_recale'] == img_name]
    # img_recap = img_recap[['contrast', 'sequence', 'resolution', 'mouvement', 'mouvement correction','noise','regularisation factor']]
    #
    # make_report(img_name, img_recap, out_dir)
    # print('report done and save\n')
