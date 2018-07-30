def binary_search(arr, key):
    left = -1
    right = len(arr)
    while right > left + 1:
        middle = (left + right) // 2
        if arr[middle] > key:
            right = middle
        else:
            left = middle
    return left >= 0 and arr[left] == key


def upper_bound(arr, key):
    left = -1
    right = len(arr)
    while right > left + 1:
        middle = (left + right) // 2
        if arr[middle] > key:
            right = middle
        else:
            left = middle
    return right


def lower_bound(arr, key):
    left = -1
    right = len(arr)
    while right > left + 1:
        middle = (left + right) // 2
        if arr[middle] >= key:
            right = middle
        else:
            left = middle
    return right