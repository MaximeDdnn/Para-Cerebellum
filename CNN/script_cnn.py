#!/usr/bin/env python

import os
import subprocess
import shutil

"""
script  for run the CNN programme avalailable here : http://www.iacl.ece.jhu.edu/index.php/Cerebellum_CNN
"""

simg_path = '/home/dieudonnem/hpc/soft_cerebellum/CNN/cerebellum-parcellation_v2.simg'
input_dir = '/home/dieudonnem/hpc/data/dataset_sence/sub-1/anat'
output_folder = '/cnn'  # output folder is created in the input folder by the cmd_cnn, that's why i move it after in my output_dir
output_dir = '/home/dieudonnem/hpc/out/'
files = os.listdir(input_dir)
files.sort()
print(files)
for mri in files:
    output_folder_name =  mri.split('.')[0] # remove the extension '.nii'
    output_folder = os.path.join(output_dir, output_folder_name)
    cmd_cnn = 'singularity run -B %s:/mnt %s -i /mnt/%s -o /mnt/%s' % (input_dir, simg_path, mri, output_folder)
    subprocess.run(cmd_cnn, shell=True)
shutil.move(os.path.join(input_dir, output_folder), output_dir)


