import math
import numpy as np


def cut_bbox(bbox, nb_cut):
    step_s = int(math.floor(((abs(bbox[1] - bbox[0])) / nb_cut[0])))
    step_c = int(math.floor(((abs(bbox[3] - bbox[2])) / nb_cut[1])))
    step_a = int(math.floor(((abs(bbox[5] - bbox[4])) / nb_cut[2])))

    slices_sag = np.arange(bbox[0], bbox[1], step_s)
    slices_sag = [int(x) for x in slices_sag]

    slices_cor = np.arange(bbox[2], bbox[3], step_c)
    slices_cor = [int(y) for y in slices_cor]

    slices_ax = np.arange(bbox[4], bbox[5], step_a)
    slices_ax = [int(y) for y in slices_ax]
    slices = [slices_sag, slices_cor, slices_ax]
    return slices
