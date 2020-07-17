import nibabel as nib
import numpy as np
import os
from scipy.ndimage import sobel, generic_gradient_magnitude
from derivative.labels import label_cnn, label_suit, label_suiter




def create_mask(input_dir, soft, mask_flag=True, edge_flag=True):
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

def merge_mask(input_dir, softs,  edge_flag=True):
    """
    :param input_dir: input folder where to find saved mask with save_mask function
    :param softs: [soft1, soft2] ex: ['cnn','suit'] or ['cnn', suiter']
    :return:
    """
    list_folder = os.listdir(input_dir)
    list_folder.sort()
    for img in list_folder:
        for label in label_suiter_cnn:
                lab_suiter = label_suiter_cnn.get(label)[0]
                path_suiter = [os.path.join(out_path, softs[0], dataset, sub_id, 'derivative', 'mask', img, x+'.nii') for x in lab_suiter]
                mask_suiter = [nib.load(x) for x in path_suiter]
                data_suiter = [x.get_fdata() for x in mask_suiter]
                new_mask_suiter = sum(data_suiter)
                new_mask_suiter = nib.Nifti1Image(new_mask_suiter, mask_suiter[0].affine, mask_suiter[0].header)
                os.makedirs(os.path.join('/home/dieudonnem/hpc/out/derivative/',softs[0] + '_' + softs[1], 'dataset_sence', 'sub-1', 'mask', softs[0], img), exist_ok=True)
                nib.save(new_mask_suiter, os.path.join('/home/dieudonnem/hpc/out/derivative/', softs[0] + '_' + softs[1], 'dataset_sence', 'sub-1', 'mask', softs[0], img, label + '.nii'))
                print(img, '>>', softs[0], '>>', label, 'common mask saved')
                lab_cnn = label_suiter_cnn.get(label)[1]
                path_cnn = [os.path.join(out_path, softs[1], dataset, sub_id, 'derivative', 'mask', img, x + '.nii') for x in lab_cnn]
                mask_cnn = [nib.load(x) for x in path_cnn]
                data_cnn = [x.get_fdata() for x in mask_cnn]
                new_mask_cnn = sum(data_cnn)
                new_mask_cnn = nib.Nifti1Image(new_mask_cnn, mask_cnn[0].affine, mask_cnn[0].header)
                os.makedirs(os.path.join('/home/dieudonnem/hpc/out/derivative/', softs[0] + '_' + softs[1],'dataset_sence/sub-1/mask/cnn', img), exist_ok=True)
                nib.save(new_mask_cnn, os.path.join('/home/dieudonnem/hpc/out/derivative', softs[0] + '_' + softs[1], 'dataset_sence/sub-1/mask/',softs[1],img, label + '.nii'))
                print(img, '>>', softs[1], '>>', label, 'common mask saved')


def save_edge(list_img):
    for img in list_img:
        mri = nib.load(os.path.join(input, img))
        data = mri.get_fdata()
        label = np.unique(data)
        print(len(np.unique(data)))
        for lab in label:
            # select area with specified label
            area = np.zeros(data.shape)
            area[data == lab] = lab
            # find edge of the area
            edge = generic_gradient_magnitude(area, sobel)
            print(np.min(edge), np.max(edge))
            # clean edge
            edge[edge < 0.5 * np.max(edge)] = 0
            new_img = nib.Nifti1Image(edge, mri.affine, mri.header)
            # saving
            name = soft + '_lab-' + str(int(lab))
            folder_out = img.split('.')
            folder_out = folder_out[0]
            if not os.path.exists(os.path.join(save_dir, folder_out)):
                os.mkdir(os.path.join(save_dir, folder_out))
            nib.save(new_img, os.path.join(save_dir, folder_out, name))




def edge_mask():
    mri = '/home/dieudonnem/hpc/out/derivative/suiter_cnn/dataset_sence/sub-1/mask/suiter/r04_sub-testanat_acq-0p8mm_rec-MEMPRAGEnomotion_T1w/L_CrusI.nii'
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





