def contains_it(li, n):
    for idx, i in enumerate(li):
        if i == n:
            return idx
    return -1


def contains_rec(li, n, idx=0):
    if idx >= len(li):
        return -1
    if li[idx] == n:
        return idx
    return contains_rec(li, n, idx + 1)


def get_indices_it(li, n):
    # Using List Comprehension
    # return [idx for idx, i in enumerate(li) if i == n]
    indices = []
    for idx, i in enumerate(li):
        if i == n:
            indices.append(idx)
    return indices


def get_indices_rec(li, n):
    # To avoid having an `indices` parameter that we have to check for every recursive step invocation, having a local
    # function to handle the creation of the list of indices better
    def _contains_rec(li, n, idx, indices):
        if idx == len(li):
            return indices
        if li[idx] == n:
            indices.append(idx)
        return _contains_rec(li, n, idx + 1, indices)

    return _contains_rec(li, n, 0, [])


def binary_search_it(li, el):
    start, end = 0, len(li)
    while start <= end:
        mid = (start + end) // 2
        if el < li[mid]:
            end = mid - 1
        elif el > li[mid]:
            start = mid + 1
        else:
            return mid
    return -1


'''
Two possibilities for recursive binary search:
* By modifying the start and end indices
* By modifying the list itself (less efficient)
'''


def binary_search_rec(li, el):
    # Avoid having initialization overhead for each invocation by using local functions
    def _binary_search_rec(li, el, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2

        if el < li[mid]:
            return _binary_search_rec(li, el, start, mid - 1)
        elif el > li[mid]:
            return _binary_search_rec(li, el, mid + 1, end)
        return mid

    return _binary_search_rec(li, el, 0, len(li))


def binary_search_rec_2(li, el):
    if len(li) == 0:
        return -1
    mid = len(li) // 2
    if li[mid] < el:
        return mid + 1 + binary_search_rec_2(li[mid + 1:], el)
    elif li[mid] > el:
        return binary_search_rec_2(li[:mid], el)
    return mid
