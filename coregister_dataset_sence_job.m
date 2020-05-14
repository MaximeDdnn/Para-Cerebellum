%-----------------------------------------------------------------------
% Job saved on 14-May-2020 11:51:54 by cfg_util (rev $Rev: 7345 $)
% spm SPM - SPM12 (7771)
% cfg_basicio BasicIO - Unknown
%-----------------------------------------------------------------------
matlabbatch{1}.spm.spatial.coreg.estwrite.ref = {'/home/maxime/hpc/data/dataset_sence/data/09_sub-testanat2_acq-0p8mm_rec-uniden8000_T1w.nii,1'};
matlabbatch{1}.spm.spatial.coreg.estwrite.source = {'/home/maxime/hpc/data/dataset_sence/data/08_sub-testanat2_acq-0p8mm_rec-uniden4000_T1w.nii,1'};
%%
matlabbatch{1}.spm.spatial.coreg.estwrite.other = {
                                                   '/home/maxime/hpc/data/dataset_sence/data/01_sub-testanat_T1w.nii,1'
                                                   '/home/maxime/hpc/data/dataset_sence/data/02_sub-testanat_acq-MEMPRAGE_T1w.nii,1'
                                                   '/home/maxime/hpc/data/dataset_sence/data/03_sub-testanat2_acq-0p8mm_T1w.nii,1'
                                                   '/home/maxime/hpc/data/dataset_sence/data/04_sub-testanat2_acq-MEMPRAGEnomotion_T1w.nii,1'
                                                   '/home/maxime/hpc/data/dataset_sence/data/05_sub-testanat2_acq-MEMPRAGEmotion_T1w.nii,1'
                                                   '/home/maxime/hpc/data/dataset_sence/data/06_sub-testanat_acq-1mm_rec-uniden8000_T1w.nii,1'
                                                   '/home/maxime/hpc/data/dataset_sence/data/07_sub-testanat_acq-1mm_rec-mp2rage_T1w.nii,1'
                                                   '/home/maxime/hpc/data/dataset_sence/data/10_sub-testanat2_acq-0p8mm_rec-mp2rage_T1w.nii,1'
                                                   '/home/maxime/hpc/data/dataset_sence/data/14_sub-testanat_acq-vNav_T2w.nii,1'
                                                   '/home/maxime/hpc/data/dataset_sence/data/15_sub-testanat_T2w.nii,1'
                                                   '/home/maxime/hpc/data/dataset_sence/data/16_sub-testanat2_acq-vNav_T2w.nii,1'
                                                   '/home/maxime/hpc/data/dataset_sence/data/17_sub-testanat2_T2w.nii,1'
                                                   '/home/maxime/hpc/data/dataset_sence/data/18_sub-testanat_acq-1mm_rec-mp2rage_T1map.nii,1'
                                                   '/home/maxime/hpc/data/dataset_sence/data/19_sub-testanat2_acq-0p8mm_T1map.nii,1'
                                                   };
%%
matlabbatch{1}.spm.spatial.coreg.estwrite.eoptions.cost_fun = 'nmi';
matlabbatch{1}.spm.spatial.coreg.estwrite.eoptions.sep = [4 2];
matlabbatch{1}.spm.spatial.coreg.estwrite.eoptions.tol = [0.02 0.02 0.02 0.001 0.001 0.001 0.01 0.01 0.01 0.001 0.001 0.001];
matlabbatch{1}.spm.spatial.coreg.estwrite.eoptions.fwhm = [7 7];
matlabbatch{1}.spm.spatial.coreg.estwrite.roptions.interp = 4;
matlabbatch{1}.spm.spatial.coreg.estwrite.roptions.wrap = [0 0 0];
matlabbatch{1}.spm.spatial.coreg.estwrite.roptions.mask = 0;
matlabbatch{1}.spm.spatial.coreg.estwrite.roptions.prefix = 'r';
