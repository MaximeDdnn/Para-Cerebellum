from derivative.postprocessing import create_mask, merge_mask, create_edge
from derivative.statistique import dice_matrix, split_dice_matrix, exl
from derivative.labels import label_suiter_cnn, label_cnn, label_suit, label_suiter, soft_select

#  Main file to create derivative in each soft subfolders once output are already stored


softs = ['suit', 'suiter', 'cnn']
vs_softs = [['suit','cnn'],['suiter','cnn']]

# 1.mask
for soft in softs:
    create_mask(soft)

# 2.mask merged
for vs_soft in vs_softs:
    merge_mask(vs_soft)

# 3.edge
for vs_soft in vs_softs:
    create_edge(vs_soft)

# 4. dice
for vs_soft in vs_softs:
    dice_matrix(vs_soft)
for vs_soft in vs_softs:
    split_dice_matrix(vs_soft)
for vs_soft in vs_softs:
    dicevsrec(vs_soft)

# 5. display




