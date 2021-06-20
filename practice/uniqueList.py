def unique_list(lst):
    unique_nms = []

    for num in lst:
        if num not in unique_nms:
            unique_nms.append(num) 
    
    return unique_nms