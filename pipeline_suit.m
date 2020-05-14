%% IMAGE INPUT

img = 'sub-testanat2_acq-0p8mm_rec-uniden8000_T1w.nii';
[path_img,name_img,ext_img] = fileparts(img);

%% ISOLATION

% Les images d'entrée doivent être spécifiées dans un cell
% {{image1},...,{imageN}}
% l'identifiant des valeurs par défaut ('isolate_seg.*)est définie dans la fonction
% suit_defaults.m
Source.source = {{img}};
Source.maskp = suit_get_defaults('isolate_seg.maskp'); % défaut=0.2
Source.bb = suit_get_defaults('isolate_seg.bb'); % défaut=[-76,76; -108,-6;-70,11]
Source.keeptempfiles = suit_get_defaults('isolate_seg.keeptempfiles'); % defaut=0
suit_isolate_seg(Source);

%% OUTPUT ISOLATION

GM = dir('*_seg1*');
WM = dir('*_seg2*');
whole_cereb = dir('c_*_pcereb*');
whole_cereb_box = dir('c_*');

fprintf('step 1/4 isolation done');
%% NORMALISATION USING DARTEL
mri_01.gray = {GM.name};
mri_01.white = {WM.name};
mri_01.isolation = {whole_cereb.name};
job.subjND = mri_01;
suit_normalize_dartel(job)

%% OUTPUT NORMALISATION 
TR_no_lin = dir('u_a*');
TR_lin = dir('Affine_*');

fprintf('step 2/4 normalisation done');
%% RESLICE IN SUIT SPACE
mri_01.affineTr = {TR_lin.name};
mri_01.flowfield = {TR_no_lin.name};
mri_01.resample = {img};
mri_01.mask =  {whole_cereb.name};
job.subj = mri_01;
suit_reslice_dartel(job)

%% OUTPUT RESLICE IN SUIT SPACE
mri_suit = dir('wd*');

fprintf('step 3/4 reslice suit space done');
%% RESLICE INTO NATIVE SPACE
job02.Affine = {TR_lin.name};
job02.flowfield = {TR_no_lin.name};
job02.resample = {'/home/maxime/hpc/soft/spm12/toolbox/suit/atlasesSUIT/Lobules-SUIT.nii'};
job02.ref = {img};
suit_reslice_dartel_inv(job02)
fprintf('step 4/4 reslice native space done');

