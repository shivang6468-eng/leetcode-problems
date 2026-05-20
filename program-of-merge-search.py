def sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])

    sort_list = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sort_list.append(left[i])
            i += 1
        else:
            sort_list.append(right[j])
            j += 1
    sort_list.extend(left[i:])
    sort_list.extend(right[j:])

    return sort_list
