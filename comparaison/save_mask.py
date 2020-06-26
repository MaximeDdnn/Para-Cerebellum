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
            if not os.path.exists(os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1', 'derivative', 'mask')):
                os.mkdir(os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1', 'derivative', 'mask'))
            if not os.path.exists(os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1', 'derivative', 'mask', folder)):
                os.mkdir(os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1', 'derivative', 'mask', folder))
            set_name = soft_select.get(soft)[0]
            name = set_name.get(lab)
            print(name)
            nib.save(mask, os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1', 'derivative', 'mask', folder, name))


for soft in ['suiter']:
    input_dir = os.path.join('/home/dieudonnem/hpc/out/', soft, 'dataset_sence/sub-1/out_soft')
    save_mask(input_dir, soft)

def dice(img1, img2):
    coef = (2 * (np.logical_and(img1,img2)) / np.logical_or(img1,img2))
    return coef

