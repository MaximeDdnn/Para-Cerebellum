from nipype.algorithms.metrics import Similarity
import os

# https://nipype.readthedocs.io/en/latest/api/generated/nipype.algorithms.metrics.html


dir = '/home/dieudonnem/hpc/out/'
data = 'dataset_sence'
sub = 'sub-1'
folder = 'folder_r04_sub-testanat2_acq-MEMPRAGEnomotion_T1w'
similarity = Similarity()
similarity.inputs.volume1 = os.path.join(dir, 'CNN', data, sub, folder, 'r04_sub-testanat2_acq-MEMPRAGEnomotion_T1w_n4_mni_seg_post_inverse.nii')
similarity.inputs.volume2 = os.path.join(dir, 'suiter', data, sub, folder, 'r04_rs_ro_wCBS_SUIT.nii')

similarity.inputs.metric = 'cr'
res = similarity.run()

print(res.outputs)