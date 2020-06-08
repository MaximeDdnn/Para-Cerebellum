#!/usr/bin/env python3
import os
import pandas as pd
from pipeline import pipeline


def main():
    # initialisation input
    dir_path = '/home/dieudonnem/hpc/data/dataset_sence/'
    img_folder = 'Folder_r01_sub-testanat_T1w'
    img_name = 'r01_sub-testanat_T1w.nii'
    img_path = os.path.join(dir_path, img_folder, img_name)
    mask_name = 'iw_Lobules-SUIT_u_a_r01_sub-testanat_T1w_seg1.nii'
    mask_path = os.path.join(dir_path, img_folder, mask_name)
    lut_path = 'lut_perso.csv'
    info_dataset = pd.read_csv('recap_dataset_sence.csv')
    #initialisation output
    save_path = '/home/dieudonnem/hpc/out/suit/dataset_sence/'

    # pipeline
    pipeline(img_path, img_name, mask_path, lut_path, info_dataset, save_path)


if __name__ == "__main__":
    main()









