import nibabel as nib
import numpy as np
import os
from comparaison.label import label_cnn, label_suit, label_suiter


soft_select = {
    'cnn': [label_cnn, 'r'],
    'suit': [label_suit, 'iw'],
    'suiter': [label_suiter, 'rs']
}


def save_mask(input_dir, soft):
    """
    :param input_dir: folder input where there are the folder img
    :param soft: you must chose between the stings 'cnn' or 'suit' or 'suiter'
    :return: all the mask coresponding to all output label of the specified soft hpc>>out>>'soft'>>dataset_sence>>
                sub-1>>derivative>>mask>>'img_folder'  >> all the mask
    """
    print(soft_select.get(soft))
    list_folder = os.listdir(input_dir)
    for folder in list_folder:
        pref = soft_select.get(soft)[1]
        img = [x for x in os.listdir(os.path.join(input_dir, folder)) if x.startswith(pref)]
        img = img[0]
        mri = nib.load(os.path.join(input_dir, folder, img))
        data = mri.get_fdata()
        label = np.unique(data)
        for lab in label:
            mask = np.zeros(data.shape)
            mask[data == lab] = 1
            mask = nib.Nifti1Image(mask, mri.affine, mri.header)
            os.makedirs(os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1', 'derivative', 'mask', folder), exist_ok=True)
            set_name = soft_select.get(soft)[0]
            name = set_name.get(lab)
            nib.save(mask, os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1', 'derivative', 'mask', folder, name))
            print(folder, '>>', name, 'saved')

for soft in ['suiter', 'suit']:
    input_dir = os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1/original')
    save_mask(input_dir, soft)


