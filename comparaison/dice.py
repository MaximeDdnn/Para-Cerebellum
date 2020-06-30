import numpy as np
import nibabel as nib
import os
import matplotlib.pyplot as plt
from comparaison.label import label_suit, label_suiter


def get_dice(img1, img2):
    """
    :param img1: numpy array reprensting a binary mask with same dimension of img2
    :param img2: nulpy array reprensenting binary mask with same dimension of img1
    :return: Dice coefficient between img1 and 2
    """

    dice = (2 * np.sum(np.logical_and(img1, img2))) / (np.sum(img1) + np.sum(img2))
    return dice


# main
nb_label = 35
dataset = 'dataset_sence'
sub_id = 'sub-1'

out_path = '/home/dieudonnem/hpc/out'

suiter_path = os.path.join(out_path, 'suiter')
suiter_mask_path = os.path.join(suiter_path, dataset, sub_id, 'derivative', 'mask')

suit_path = os.path.join(out_path, 'suit')
suit_mask_path = os.path.join(suit_path, dataset, sub_id, 'derivative', 'mask')

list_img = os.listdir(suiter_mask_path)
list_img.sort()
print(list_img)

list_label = list(label_suit.keys())  # ist_label is the same for suit and suiter

# for img in list_img:
#     print('>>', img)
#     dice_matrix = np.zeros((nb_label, nb_label))
#     # loop to fill dice_matrix
#     for label_1 in list_label:
#         for label_2 in list_label:
#             print('\t', label_1, label_2, '\n')
#             # data_1 : suit mask
#             mask_1 = label_suit.get(label_1) + '.nii'
#             mri_1 = nib.load(os.path.join(suit_mask_path, img, mask_1))
#             data_1 = mri_1.get_fdata()
#             # data_2 : suiter mask
#             mask_2 = label_suit.get(label_2) + '.nii'
#             mri_2 = nib.load(os.path.join(suiter_mask_path, img, mask_2))
#             data_2 = mri_2.get_fdata()
#             # fill dice_matrix
#             dice_matrix[label_1][label_2] = get_dice(data_1, data_2)
#     save_dir = os.path.join(out_path, 'comparaison', 'suit_suiter', dataset, sub_id, img)
#     if not os.path.exists(save_dir):
#         os.mkdir(save_dir)
#     np.save(os.path.join(save_dir,'dice_matrix'), dice_matrix)
#     print('\t dice_matric for %s save \n' %img )

# display


# for img in list_img:
#     dice_matrix = np.load(os.path.join(out_path, 'comparaison', 'suit_suiter', dataset, sub_id, img, 'dice_matrix.npy'))
#     plt.imshow(dice_matrix)
#     plt.title(img)
#     plt.show()


list_label_name = list(label_suit.values())
list_label_name_suit = ["suiter " + x for x in list_label_name]
list_label_name_suiter = ["suit " + x for x in list_label_name]


for img in list_img:
    fig, ax = plt.subplots()
    dice_matrix = np.load(os.path.join(out_path, 'comparaison', 'suit_suiter', dataset, sub_id, img, 'dice_matrix.npy'))
    im = ax.imshow(dice_matrix)
    ax.set_xticks(np.arange(len(list_label_name_suit)))
    ax.set_yticks(np.arange(len(list_label_name_suiter)))
    ax.set_xticklabels(list_label_name_suit)
    ax.set_yticklabels(list_label_name_suiter)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", fontsize = "x-small")
    plt.setp(ax.get_yticklabels(), fontsize="x-small")
    for i in range(len(list_label_name)):
        for j in range(len(list_label_name)):
            text = ax.text(j, i, round(dice_matrix[i, j],2), ha="center", va="center", color="w", fontsize = "xx-small")
    ax.set_title(img)
    fig.tight_layout()
    plt.show()
