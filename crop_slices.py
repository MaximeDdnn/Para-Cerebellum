def crop_slices(list_slices, bbox, marge):
    nview = len(list_slices)
    for view in range(nview):
        # crop sagital
        if view == 0:
            for idx in range(len(list_slices[0])):
                list_slices[0][idx] = list_slices[0][idx][bbox[2] - marge:bbox[3] + marge, bbox[4] - marge:bbox[5] + marge]
            # crop coronal
        if view == 1:
            for idx in range(len(list_slices[1])):
                list_slices[1][idx] = list_slices[1][idx][bbox[0] - marge:bbox[1] + marge, bbox[4] - marge:bbox[5] + marge]
        # crop axial
        if view == 2:
            for idx in range(len(list_slices[2])):
                list_slices[2][idx] = list_slices[2][idx][bbox[0] - marge:bbox[1] + marge, bbox[2] - marge:bbox[3] + marge]
    return list_slices
