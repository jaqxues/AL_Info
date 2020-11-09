from random import randint


def get_random(n, a, b):
    return [randint(a, b) for _ in range(n)]


def selection_sort(li):
    for idx in range(len(li) - 1):
        smallest = idx
        for x in range(idx + 1, len(li)):
            if li[x] < li[smallest]:
                smallest = x
        if smallest != idx:
            li[smallest], li[idx] = li[idx], li[smallest]


def partition(li, p, r):
    q = p
    for x in range(p, r):
        if li[x] <= li[r]:
            li[x], li[q] = li[q], li[x]
            q += 1
    li[q], li[r] = li[r], li[q]

    return q


def quicksort(li):
    def _quicksort(p, r):
        if r - p < 1:
            return
        q = partition(li, p, r)
        _quicksort(p, q - 1)
        _quicksort(q, r)

    return _quicksort(0, len(li) - 1)


# Solution given for partition and quicksort implementations
def partition_2(a, g, d):
    p = a[d]
    i, j = g, d - 1
    while True:
        while i <= j and a[i] < p:  # a[i] on the left side?
            i += 1
        while i <= j and a[j] > p:  # a[j] on the right side?
            j -= 1
        if i <= j:
            (a[i], a[j]) = (a[j], a[i])  # put a[i] and a[j] on the correct sides
            i += 1
            j -= 1
        else:  # i and j crossed each other => done
            a[i], a[d] = p, a[i]  # put the pivot in the correct position
            return i  # index of pivot


def quicksort_2(a, g=0, d=None):
    if d is None:
        d = len(a) - 1
    if g >= d:
        # let’s stop
        return
    p = partition_2(a, g, d)
    quicksort_2(a, g, p - 1)  # sublist to the left of the pivot
    quicksort_2(a, p + 1, d)  # sublist to the right of the pivot


if __name__ == '__main__':
    li = get_random(20, 0, 100)
    print(li)
    copy = li[:]
    selection_sort(li)
    quicksort(copy)
    assert copy == li
    print(li)
