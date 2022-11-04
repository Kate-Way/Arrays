import bisect

def merge_sorted_arrays(arr, arr2):
    for i in range(len(arr2)):
        bisect.insort(arr, arr2[i])

    return arr


# test
arr = [1, 4, 7, 9, 10, 12]
arr2 = [3, 5, 6, 12, 26]
print(merge_sorted_arrays(arr,arr2))
# [1, 3, 4, 5, 6, 7, 9, 10, 12, 12, 26]