% Author : maxime.dieudonne@univ_amu.fr
% Date : 15/05/2020
% Tested on Ubuntu18.04.4 LTS, Matlab R2016b, spm12 and the most recent suit version available at this date 
%
% Usage : Run the function in the directory of the dataset you want to process.
% 
% The function segmentation_suit does the folowing steps : 
% 0/ creates a folder for each images and places the image in this folder
% for each images : 
% 1/ isolation of the cerebellum
% 2/ Normalisation using Dartel
% 3/ reslice in SUIT space
% 4/ reslice in native space
% 
% Inputs : 
% pathDataset : the directory where your images to process are stored.
% pathAtlas : the directory where the atlas you want use to segment the cerebellum is stored
% ( in my case : '/home/maxime/hpc/soft/spm12/toolbox/suit/atlasesSUIT/Lobules-SUIT.nii')
% 
% Ouputs : this function creates a folder for each images in your pathDataset.
% Each folder contains : 
% *_seg1*' : Gray Mater mask.                                                   
% *_seg2*' :  White Mater mask.
% c_*_pcereb* :Whole cerebellum mask
% c_*' : Whole cerebllum mask with bounding box
% u_a* :  non linear part of the coregistration
% Affine_* : linear part of the registration      
% wd* : flowfield of deformation
% iw_* : segmentation according the atlas


function segmentation_suit(pathDataset, pathAtlas)

fileList = get_file_list(pathDataset);
create_folder(pathDataset,fileList);                                        % create a folder with the image 
                                                                            % source in the path dataset.

for k=1:length(fileList)
    folderName = strcat('Folder_',fileList(k).name);
    pathFolder = fullfile(pathDataset,folderName);
    img = fullfile(pathFolder,fileList(k).name);
    cd(pathFolder)                                                          % like so, the suit functions generate
                                                                            % the outputs in the appropriate folder.
  
    % step 1 : suit_isolate_seg 
    % inputs step 1                                                         % input is a struct Source with fields
    Source.source = {{img}};                                                % if muliple inputs to impove isolation, 
                                                                            % do {{img1},{img2}}.(T1W and T2W of same subject for exemple)
    Source.maskp = 0.2;                                                     % défaut=0.2 see suit_get_defaults() in the suit project.
    Source.bb = [-76,76; -108,-6;-70,11];                                   % défaut=[-76,76; -108,-6;-70,11]
    Source.keeptempfiles = 0 ;                                              % defaut=0                                                                           
    suit_isolate_seg(Source);
    % outputs step 1                                                        % outputs are matlab structures :
    GM = dir('*_seg1*');                                                    % Gray Mater mask.                                                   
    WM = dir('*_seg2*');                                                    % White Mater mask.
    whole_cereb = dir('c_*_pcereb*');                                       % Whole cerebellum mask
    whole_cereb_box = dir('c_*');                                           % Whole cerebllum mask with bounding box
    fprintf('\n image %d step 1/4 isolation done \n',k);
     
    % step 2 : suit_normalize_dartel
    % inputs step 2                                                         % input is the structure job with field jobND. mri. 
                                                                            % mri is struct with fields gray,whit and isolation.
    mri.gray = {GM.name};
    mri.white = {WM.name};
    mri.isolation = {whole_cereb.name};
    job.subjND = mri;
    suit_normalize_dartel(job)
    %outputs step 2
    TR_no_lin = dir('u_a*');                                                % non linear part of the coregistration
    TR_lin = dir('Affine_*');                                               % linear part of the registration       
    fprintf('\n image %d step 2/4 normalisation done \n',k);
    
    % step 3 : suit_reslice_dartel
    % inputs step 3 
    mri.affineTr = {TR_lin.name};
    mri.flowfield = {TR_no_lin.name};
    mri.resample = {img};
    mri.mask =  {whole_cereb.name};
    job.subj = mri;                                                         
    
    suit_reslice_dartel(job)
    % output step 3 
    mri_suit = dir('wd*');                                                  % flowfield of deformation

    fprintf('\n image %d step 3/4 reslice suit space done \n',k);
    % step 4 suit_reslice_dartel 
    job02.Affine = {TR_lin.name};
    job02.flowfield = {TR_no_lin.name};
    job02.resample = {pathAtlas};
    job02.ref = {img};
    suit_reslice_dartel_inv(job02)

    fprintf('\n image %d step 4/4 reslice native space done \n',k);

    cd(pathDataset)

end
end


function [fileList] = get_file_list(pathDataset)
fileList = dir(fullfile(pathDataset, 'r*.nii'));
end

function create_folder(pathDataset,fileList)
    for k=1:length(fileList)
        nameFile = fileList(k).name;
        nameFolder = strcat('Folder_',nameFile);
        mkdir(fullfile(pathDataset,nameFolder));
        movefile(fullfile(pathDataset,nameFile),fullfile(pathDataset,nameFolder));
    end
end



