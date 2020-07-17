import numpy as np
import nibabel as nib
import os
import matplotlib.pyplot as plt
from derivative.labels import label_suit, label_suiter, label_cnn, label_suiter_cnn
from scipy.ndimage import sobel, generic_gradient_magnitude

def get_dice(img1, img2):
    """
    :param img1: numpy array reprensting a binary mask with same dimension of img2
    :param img2: nulpy array reprensenting binary mask with same dimension of img1
    :return: Dice coefficient between img1 and 2
    """

    dice = (2 * np.sum(np.logical_and(img1, img2))) / (np.sum(img1) + np.sum(img2))
    return dice


def minimize_label(input_dir, softs,  edge_flag=True):
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



def dice_matrix(list_img, soft1, soft2, soft1_mask_path, soft2_mask_path, dict_label):
    """
    :param list_img:
    :param soft1: you must choose between string 'cnn' or 'suit' or 'suiter
    :param soft2: you must choose between string 'cnn' or 'suit' or 'suiter
    :param soft1_mask_path: path like input where are stored mak of the soft1
    :param soft2_mask_path: path like input where are stored mak of the soft2
    :param dict_label:
    :return:
    """
    out_path = '/home/dieudonnem/hpc/out'
    list_label = list(dict_label.keys())
    nb_label = len(list_label)
    for img in list_img:
        print('>>', img)
        dice_matrix = np.zeros((nb_label, nb_label))
        # loop to fill dice_matrix
        for label_1 in list_label:
            for label_2 in list_label:
                print(img, ':', label_1, label_2, '\n')
                # data_1 : soft1 mask
                mask_1 = label_1 + '.nii'
                mri_1 = nib.load(os.path.join(soft1_mask_path, img, mask_1))
                data_1 = mri_1.get_fdata()
                # data_2 : soft2 mask
                mask_2 = label_2 + '.nii'
                mri_2 = nib.load(os.path.join(soft2_mask_path, img, mask_2))
                data_2 = mri_2.get_fdata()
                # fill dice_matrix
                dice_matrix[list_label.index(label_1)][list_label.index(label_2)] = get_dice(data_1, data_2)
        save_dir = os.path.join(out_path, 'derivative', soft1 + '_' + soft2, dataset, sub_id, 'dice_matrix', img)
        os.makedirs(save_dir, exist_ok=True)
        np.save(os.path.join(save_dir, 'dice_matrix'), dice_matrix)
        print('\t dice_matrix for %s save \n' %img )



def split_dice_matrix(dice_matrix, label):
    """
    split the dice matrix that contain all the area of the cerebellum in two smaller dice matrix for a better interpretability.
    it splits into a dice matrix without left areaw and in an other dice matrix without right areas
    :param dice_matrix: dice matrix that contains all the area
    :param label: dict with lab
    :return: dice_matrix_L for left ( and vermis) and dice matric_R for right (and vermis)
    """
    idx_noR = [label.index(x) for x in label if 'R_' not in x]
    idx_noL = [label.index(x) for x in label if 'L_' not in x]
    dice_matrix_R = dice_matrix[idx_noL,:][:,idx_noL]
    dice_matrix_L = dice_matrix[idx_noR, :][:, idx_noR]
    return dice_matrix_L, dice_matrix_R

def displayRL(soft1, soft2, list_label_name_L,list_label_name_R):
    input_dir = os.path.join('/home/dieudonnem/hpc/out/derivative', soft1 + '_' + soft2, 'dataset_sence/sub-1/dice_matrix')
    subfolders = os.listdir(input_dir)
    subfolders.sort()
    for folder in subfolders:
        fig, axs = plt.subplots(1, 2)
        dice_matrix_L = np.load(os.path.join(input_dir, folder, 'dice_matrix_L.npy'))
        im0 = axs[0].imshow(dice_matrix_L)
        axs[0].set_xticks(np.arange(len(list_label_name_L)))
        axs[0].set_yticks(np.arange(len(list_label_name_L)))
        axs[0].set_xticklabels(list_label_name_L)
        axs[0].set_yticklabels(list_label_name_L)
        plt.setp(axs[0].get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", fontsize = "x-small")
        plt.setp(axs[0].get_yticklabels(), fontsize="x-small")
        for i in range(len(list_label_name_L)):
            for j in range(len(list_label_name_L)):
                text = axs[0].text(j, i, round(dice_matrix_L[i, j], 2), ha="center", va="center", color="w", fontsize = "xx-small")
        axs[0].set_title('Left Hemisphere')
        dice_matrix_R = np.load(os.path.join(input_dir, folder, 'dice_matrix_R.npy'))
        im1 = axs[1].imshow(dice_matrix_R)
        axs[1].set_xticks(np.arange(len(list_label_name_R)))
        axs[1].set_yticks(np.arange(len(list_label_name_R)))
        axs[1].set_xticklabels(list_label_name_R)
        axs[1].set_yticklabels(list_label_name_R)
        plt.setp(axs[1].get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", fontsize="x-small")
        plt.setp(axs[1].get_yticklabels(), fontsize="x-small")
        for i in range(len(list_label_name_R)):
            for j in range(len(list_label_name_R)):
                text = axs[1].text(j, i, round(dice_matrix_R[i, j], 2), ha="center", va="center", color="w",
                               fontsize="xx-small")
        axs[1].set_title('Right Hemisphere')
        fig.suptitle(folder)
        fig.tight_layout()
        plt.show()



def display(soft1, soft2, list_label_name_soft1,list_label_name_soft2):
    input_dir = os.path.join('/home/dieudonnem/hpc/out/derivative', soft1 + '_' + soft2, 'dataset_sence/sub-1/dice_matrix')
    subfolders = os.listdir(input_dir)
    subfolders.sort()
    for folder in subfolders:
        fig, ax = plt.subplots()
        dice_matrix = np.load(os.path.join(input_dir, folder, 'dice_matrix.npy'))
        im = ax.imshow(dice_matrix)
        ax.set_xticks(np.arange(len(list_label_name_soft2)))
        ax.set_yticks(np.arange(len(list_label_name_soft1)))
        ax.set_xticklabels(list_label_name_soft2)
        ax.set_yticklabels(list_label_name_soft1)
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", fontsize = "x-small")
        plt.setp(ax.get_yticklabels(), fontsize="x-small")
        for i in range(len(list_label_name)):
            for j in range(len(list_label_name)):
                text = ax.text(j, i, round(dice_matrix[i, j], 2), ha="center", va="center", color="w", fontsize = "xx-small")
        ax.set_title(folder)
        fig.tight_layout()
        plt.show()



def exl(label_R):
    """
    create an excel sheet that sum up dice score for each area ( column ) and each type of record ( row )
    :return:
    """
    input_path = os.path.join('/home/dieudonnem/hpc/out/derivative', 'suit_cnn', 'dataset_sence/sub-1/dice_matrix')
    list_folder = os.listdir(input_path)
    list_dice_matrix = [np.load(os.path.join(input_path, folder, 'dice_matrix_R.npy')) for folder in list_folder]
    dice_rec = np.array([np.diag(x) for x in list_dice_matrix])
    print(type(dice_rec))
    print(dice_rec)
    # display
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(len(list_folder)))
    ax.set_xticklabels(list_folder)
    for folder in range(len(label_R)):
        plt.plot(dice_rec[:, folder], 'o-', label=label_R[folder])
    plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor", fontsize="xx-small")
    plt.legend(loc = 0)
    plt.show()


def comp_rec():
    input_path = '/home/dieudonnem/hpc/out/comparaison/suit_cnn/dataset_sence/sub-1/dice_matrix'
    list_folder = os.listdir(input_path)
    fig, ax = plt.subplots()
    x = np.arange(len(list_folder))
    ax.set_xticks(np.arange(len(x)))
    ax.set_yticks(np.arange(len(list_folder)))
    ax.set_xticklabels(list_folder)
    ax.set_yticklabels(x)
    for a in range(5):
        plt.plot(x+a, 'o-')
    plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor", fontsize="xx-small")
    plt.show()

# main

dataset = 'dataset_sence'
sub_id = 'sub-1'

out_path = '/home/dieudonnem/hpc/out'

suiter_path = os.path.join(out_path, 'suiter')
suiter_mask_path = os.path.join(suiter_path, dataset, sub_id, 'derivative', 'mask')

suit_path = os.path.join(out_path, 'suit')
suit_mask_path = os.path.join(suit_path, dataset, sub_id, 'derivative', 'mask')

list_label = list(label_suit.keys())  # list_label is the same for suit and suiter

suit_path = '/home/dieudonnem/hpc/out/comparaison/suit_cnn/dataset_sence/sub-1/mask/suit/'
suiter_path = '/home/dieudonnem/hpc/out/comparaison/suiter_cnn/dataset_sence/sub-1/mask/suiter/'
cnn_path = '/home/dieudonnem/hpc/out/comparaison/suiter_cnn/dataset_sence/sub-1/mask/cnn/'
list_img = os.listdir(suiter_path)
list_img.sort()

list_label_name = list(label_suiter_cnn.keys())
list_label_name_R = [x for x in list_label_name if 'R_' not in x]
list_label_name_L = [x for x in list_label_name if 'L_' not in x]
list_label_name_suiter = ["suiter " + x for x in list_label_name]
list_label_name_cnn = ["cnn " + x for x in list_label_name]

#for softs in [['suit', 'cnn']]:
    # input_dir = os.path.join('/home/dieudonnem/hpc/out/', softs[0], 'dataset_sence/sub-1/derivative/mask')
    # minimize_label(input_dir, softs)


#save_dice_matrix(list_img, 'suit', 'cnn', suit_path, cnn_path, label_suiter_cnn)
#display('suiter', 'cnn', list_label_name_suiter, list_label_name_cnn)



# input_path = '/home/dieudonnem/hpc/out/derivative/suit_cnn/dataset_sence/sub-1/dice_matrix'
# list_folder = os.listdir(input_path)
# list_folder.sort()
# for folder in list_folder:
#     dice_matrix = np.load(os.path.join(input_path, folder, 'dice_matrix.npy'))
#     dice_matrix_L, dice_matrix_R = split_dice_matrix(dice_matrix, list(label_suiter_cnn.keys()))
#     np.save(os.path.join(input_path, folder, 'dice_matrix_L.npy'), dice_matrix_L,)
#     np.save(os.path.join(input_path, folder, 'dice_matrix_R.npy'), dice_matrix_R)

#displayRL('suit', 'cnn', list_label_name_L, list_label_name_R)

#comp_rec()
exl(list_label_name_R)