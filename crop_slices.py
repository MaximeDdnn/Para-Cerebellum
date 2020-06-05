def crop_slices(list_slices, bbox, marge):
    #crop sagital
    for idx in range(len(list_slices[0])):
        list_slices[0][idx] = list_slices[0][idx][bbox[2]-marge:bbox[3]+marge, bbox[4]-marge:bbox[5]+marge]
    # crop coronal
    for idx in range(len(list_slices[1])):
        list_slices[1][idx] = list_slices[1][idx][ bbox[0]-marge:bbox[1]+marge,bbox[4]-marge:bbox[5]+marge]
    # crop axial
    for idx in range(len(list_slices[2])):
        list_slices[2][idx] = list_slices[2][idx][bbox[0]-marge:bbox[1]+marge, bbox[2]-marge:bbox[3]+marge]
    return list_slices
