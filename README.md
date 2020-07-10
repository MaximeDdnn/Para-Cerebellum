# Para-Cerebellum


## Output folders organisation :

original : The subfolder "original" contains the outputs generated by the soft. Files are not renamed.
derivative : The subfolder "derivative" contains the outputs post-processed by Para-Cerebellum useful for result visualisation. The files inside are renamed and                organised the same way for all the derivative subfolder. Subfolder inside Derivative are "mask", "edge", "dice", "visual".

mask: the subfolder "mask" contains all the binary mask of all the label proposed by the soft. It contains subfolder "self" that contain the binary mask of the         original labels proposed by the soft and "vs$an_other_soft$" subfolder that contains the binary mask fused between two softs.
      for exemple suit proposed three labels for the vermis VII instead of cnn that proposed only one label for vermis VII, that's why the subfolder vsnn contains       only the label V_VII.nii.  
      suit
        self
          V_CrusI.nii
          V_CrusII.nii
          V_VIIb.nii
        vscnn
          V_VII.nii
edge: Same as the mask subfolder, edge is divided in "self" subfolder and other "vs_an_other_soft" subfolders. Each contains the edge of each binary file of mask       subfolders
dice: The subfolder "dice" contains dice matrix that compare the dice score. 
visual: The subfolder "visual" is an additional subfolder that contains additional screen.

Here is a recap of the output organisation 

* suiter
      * dataset
            * sub-i
                  * original
                        * T1w.nii
                  * derivative
                        * mask
                        * self
                              * T1w
                                    * label.nii
                        * vscnn
                        * vsceres
                  * edge
                        * self
                              * T1w
                                    edge.nii
                        vscnn
                        vsceres
                  dice
                        vscnn
                              dice_matrix
                                    dice_matrix.npy
                                    dice_matrix_R.npy
                                    dice_matrix_L.npy
                                    rec
                              dicevsrec.fig
                        vsceres
                        visual       
suit
cnn
ceres


main_pipeline_segmentation_suit show you an exemple to run the function pipeline_segmentation_suit.
You need to run Matlab and spm before be able to run pipeline_segmentation_suit.


Work in progress : Plot MRI overlayed with your own-lut segmentation mask

![mosaic](https://user-images.githubusercontent.com/62238305/83866292-e245a680-a727-11ea-9819-52d25429305b.png)

Suit, Suiter, CNN and Ceres are tools for cerebelum lobule segmentation. 
Para-Cerebellum allows you to make easier the evaluation and comparaison of this four softs.

