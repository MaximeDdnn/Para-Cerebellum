def crop_slices(list_slices, bbox):
    for idx in range(len(list_slices[0])):
        list_slices[0][idx] = list_slices[0][idx][bbox[4]:bbox[5], bbox[2]:bbox[3]]
    return list_slices
