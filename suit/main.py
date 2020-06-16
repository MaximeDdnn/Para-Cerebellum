#!/usr/bin/env python3
import os
import pandas as pd
from suit.function.pipeline import pipeline


def main():
    """
    This main function save all the slices you specified of your MRI to make the evaluation of you processing easier.
    The slices are saved in png format in your output directory.
    First This main function create the empty output folders in your output directory.
    And then this main funtion run the pipeline function for store specified slice, overlay segmentation mask of Suit
    crop aroud the cerebellum.

    :parameter

    input : input_dir ___ Folder_img1 ___ img1.nii
                    |                |___ mask1.nii
                    |                |___ ...all proccessing Suit outputs
                    | ___ Folder_img2 ___img2.nii
                    |                |___mask2.nii
                    |                |___ ...all processing Suit outputs
                    |___Folder_imgN ...

    idx_slices = [[idx_sagittal_slices],[idx_coronal_slices],[idx_axial_slices]] : the index of slices you want to save
        note : your can specify only sagitall slices and coronal slices if you want not saved axial slices like [[idx_sagittal_slices],[idx_coronal_slices]]
        output with for exemple idx_slices = [[10,12,14],[50,100],[89]]

    lut_path : .csv file that link a label to a rgb color. There is 34 labels corresponding to the 34 outputs label of suits
    (see : Diedrichsen, J., Balsters, J. H., Flavell, J., Cussans, E., & Ramnani, N. (2009). A probabilistic atlas of the human cerebellum. Neuroimage.46(1), 39-46)

    info_dataset : .csv file that sum up all the caracteristiques of the acquisition of the MRI images. It is use to make automatically a pdf report for each images.

    :returns

    output : out_dir ___ Folder_img1 ___ sagittal ___slice10.png
                    |                  |            |___slice12.png
                    |                  |            |___slice14.png
                    |                  |___ coronal ___slice50.png
                    |                  |           |___slice100.png
                    |                  |___ axial ___slice89.png
                    |                  |___ view ___sagittal.png
                    |                           |___coronal.png
                    |                           |___axial.png
                    | ___ Folder_imgN ___ ...

    the ouptput "/view" is an image of the cerebellum with line added on it that show the selected slices
    """

    # initialisation of the inputs
    input_dir = '/home/dieudonnem/hpc/data/dataset_sence/'
    input_folders = [x for x in os.listdir(input_dir)]
    input_folders.sort()
    input_folders = ['Folder_r04_sub-testanat2_acq-MEMPRAGEnomotion_T1w']
    lut_path = 'doc/lut_perso.csv'
    info_dataset = pd.read_csv('doc/recap_dataset_sence.csv')

    # initialisation output
    out_dir = '/home/dieudonnem/hpc/out/suit/dataset_sence/Folder_r04_sub-testanat2_acq-MEMPRAGEnomotion_T1w'

    # idx_slice is set to compare some slices with the figures available in the Schmahmann1999 paper.
    # "Three-dimensional MRI Atlas of the Human Cerebellum in Proportional Stereotaxic Space" DOI: 10.1006/nimg.1999.0459
    # Schmaahman paper Sagittal images progressing laterally by increment of 10 mm
    # Schmaahman paper Coronal fig 20-25 : images comencint at y=-38 and progressing caudally to y= -88
    idx_slice = [[50, 60, 70, 80, 90, 100], [70, 80, 90, 100, 110, 120]]

    for folder in input_folders:
        if not os.path.exists(os.path.join(out_dir, folder)):
            os.mkdir(os.path.join(out_dir, folder))

    for folder in input_folders:
        pipeline(input_dir, folder, lut_path, idx_slice, out_dir)


if __name__ == "__main__":
    main()









