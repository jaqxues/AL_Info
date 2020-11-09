def selection_sort_rec(li, idx=0):
    if idx == len(li) - 1:
        return

    # p = min(enumerate(li), key=lambda x: x[1])[0]
    p = idx
    for j in range(idx + 1, len(li)):
        if li[j] < li[p]:
            p = j
    if p > idx:
        li[p], li[idx] = li[idx], li[p]
    selection_sort_rec(li, idx + 1)
