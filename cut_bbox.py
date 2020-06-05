import math
import numpy as np


def cut_bbox(bbox, nb_cut):
    nview = len(nb_cut)
    step = [0]*nview
    slices = [0]*nview
    for view in range(nview):
        step[view] = int(math.floor(((abs(bbox[view*2 + 1] - bbox[view*2])) / nb_cut[view])))
        slices[view] = np.arange(bbox[2*view], bbox[2*view + 1], step[view])
        slices[view] = [int(x) for x in slices[view]]
    return slices
