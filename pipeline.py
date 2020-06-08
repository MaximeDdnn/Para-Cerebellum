import os
from overlay_own_lut import get_slices
from display import display_mosaic
from get_bbox import get_bbox, get_main_view, get_quick_visual
from cut_bbox import cut_bbox
from crop_slices import crop_slices
from jinja_env import make_report


def pipeline(img_path, img_name, mask_path, lut_path, info_dataset, save_path):

    bbox = get_bbox(mask_path)
    str = 'getbbox done \n sright = %d, sleft = %d, cpost = %d, cant = %d, asup = %d, ainf = %d, ' % (bbox[0], bbox[1], bbox[2], bbox[3], bbox[4], bbox[5])
    print(str)

    # find index of slice according the number of cuts needed
    nb_cut = [5, 5, 2]  # 5 slices sagital, 5 slices coronal, 2 slices axials

    idx_slice = cut_bbox(bbox, nb_cut)  # idx_slice = [[idx_s],[idx_c],[idx_a]]
    print('idx_slice = ', idx_slice)
    # save the desired slices
    list_slices = get_slices(img_path, mask_path, lut_path, idx_slice)

    # zoom around the cerebellum
    marge = 5  # marge around the crop
    list_slices = crop_slices(list_slices, bbox, marge)

    # display and save
    main_view = get_main_view(img_path)
    display_mosaic(main_view, list_slices, idx_slice)
    print('mosaic done and save\n')

    # make pdf report
    quick_visual_path = os.path.join(save_path, 'quick_visual.png')
    get_quick_visual(img_path, quick_visual_path)
    img_recap = info_dataset.loc[info_dataset['name_recale'] == img_name]
    img_recap = img_recap[['name_recale','contrast', 'sequence', 'resolution', 'mouvement', 'mouvement correction','noise','regularisation factor']]
    resultat_suit = os.path.join(save_path,'img1','mosaic.png')
    make_report(img_name, img_recap, quick_visual_path, resultat_suit)
    print('report done and save\n')
