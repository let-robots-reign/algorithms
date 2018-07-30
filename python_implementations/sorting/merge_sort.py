def merge(a, b):
    """
    Merge two lists using two pointers
    """
    i = 0
    j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:] + b[j:]
    return result


def merge_sort(a):
    """
    Recursive division of a list
    """
    if len(a) > 1:
        return merge_sort(merge(a[:len(a) // 2], a[len(a) // 2:]))
    else:
        return a