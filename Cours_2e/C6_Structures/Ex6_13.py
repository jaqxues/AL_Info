import string


def nb_digits(str1):
    counter = 0
    for digit in string.digits:
        counter += str1.count(digit)
    return counter


def count_digits(str1):
    nb = []
    for digit in string.digits:
        nb.append(str1.count(digit))
    return nb
