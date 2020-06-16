#!/usr/bin/env python

import os
import subprocess


simg_path = '/home/dieudonnem/hpc/soft_cerebellum/CNN/cerebellum-parcellation_v2.simg'
input_dir = '/home/dieudonnem/hpc/data/dataset_sence'
output_dir = '/home/dieudonnem/hpc/out/CNN'
files = os.listdir(input_dir)
files.sort()
print(files)
for mri in files:
    output_folder_name = 'folder_' + mri.split('.')[0] # remove the extension '.nii'
    output_folder = os.path.join(output_dir, output_folder_name)
    cmd_cnn = 'singularity run -B %s:/mnt %s -i /mnt/%s -o /mnt/%s' % (input_dir, simg_path, mri, output_folder)
    subprocess.run(cmd_cnn, shell=True)

