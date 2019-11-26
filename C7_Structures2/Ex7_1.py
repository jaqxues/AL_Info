from random import randint


def get_or_gen_matrix(i, j=-1):
    """
    Generates or gets from input a matrix of i * j
    :param i: Nb of columns (None for input)
    :param j: Nb of rows (-1 if result should be square matrix, None for input)
    :return: Matrix by i*j (either random values or user-defined
    """
    if i is None:
        i = int(input("Enter i: "))
    if j is -1:
        j = i
    elif j is None:
        j = int(input("Enter j: "))

    assert 2 <= i and 2 <= j
    return [[randint(-100, 100) for _ in range(i)] for _ in range(j)]


def determinant(_matrix):
    _n = len(_matrix)
    if _n < 4:
        value = 0
        for x in range(_n):
            tmp = 1
            for y in range(_n):
                tmp *= _matrix[y][(x + y) % _n]
            value += tmp
        for x in range(_n):
            tmp = 1
            for y in range(_n):
                tmp *= _matrix[y][(x - y) % _n]
            value -= tmp
    else:
        value = 0
        for row in range(_n):
            sign = (-1) ** (row % 2)
            value += sign * _matrix[0][row] * determinant(generate_submatrix(_matrix, 0, row))
    return value


def generate_submatrix(_matrix, i, j):
    """
    :param _matrix: Matrix (rests unchanged, deep copy
    :param i: Column to remove
    :param j: Row to remove
    :return: Matrix where column j and row i have been deleted
    """
    copy = _matrix[:i][:] + _matrix[i + 1:][:]
    for y in range(len(copy)):
        index = y if y < i else y + 1
        copy[y] = _matrix[index][:j] + _matrix[index][j + 1:]
    return copy


def format_matrix(_matrix, delimiter='\n\t', prefix=None):
    if prefix is None:
        prefix = delimiter
    return prefix + delimiter.join(map(str, _matrix))


if __name__ == '__main__':
    matrix = get_or_gen_matrix(None)
    print("Matrix: ", format_matrix(matrix))
    print("Determinant: ", determinant(matrix))
