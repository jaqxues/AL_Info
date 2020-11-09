# Given solution
def partition(a, g, d):
    if d - g >= 2:  # 3 éléments non confondus, qu'on va trier
        x, y, z = a[g], a[(g + d) // 2], a[d]  # exercice 2.9
        if x < y:
            x, y = y, x
        if z > y:  # mod 21/10/2019
            if z > x:
                x, y, z = z, x, y
            else:
                y, z = z, y
        a[g], a[d], a[(g + d) // 2] = x, y, z  # maintenant a[d] contient la médiane
    p = a[d]
    i, j = g, d - 1
    while True:
        while i <= j and a[i] < p:  # a[i] déjà du bon côté ?
            i += 1
        while i <= j and a[j] > p:  # a[j] déjà du bon côté ?
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]  # placer a[i] et a[j] du bon côté
            i += 1
            j -= 1
        else:  # i et j se sont croisés => toute la liste a déjà été analysée
            a[i], a[d] = p, a[i]  # placer le pivot au bon endroit
            return i  # renvoyer l'indice du pivot


def quicksort(a, g=0, d=None):
    if d is None:
        d = len(a) - 1
    if g >= d:  # condition d'arrêt
        return
    p = partition(a, g, d)
    quicksort(a, g, p - 1)  # sous-liste à gauche du pivot
    quicksort(a, p + 1, d)  # sous-liste à droite du pivot
