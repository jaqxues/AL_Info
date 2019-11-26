def get_polynomial(d=None):
    if d is None:
        d = int(input('Enter degree of polynomial: '))
    """
    :param d: [Optional] Given degree
    :return: polynomial in form of a list
    """
    poly = []
    for i in range(d, -1, -1):
        value = float(input(f'Enter coefficient x^({i}): '))
        if value.is_integer():
            value = int(value)
        assert i != d or value != 0
        poly.append(value)
    return poly


def format_polynomial(poly):
    formatted = ''
    first_term = True
    degree = len(poly) - 1

    for p in range(0, degree + 1):
        current = poly[p]
        if current == 0:
            continue

        current_degree = degree - p
        if current_degree > 1:
            coefficient = f'x^{current_degree}'
        elif current_degree == 1:
            coefficient = 'x'
        else:
            coefficient = ''

        sign = '- ' if current < 0 else '+ '
        if first_term and sign == '+ ':
            sign = ''
        first_term = False

        number = abs(current)
        # Removes .0 if number is integer (ignore if already converted to int)
        if number is not int or number.is_integer():
            number = int(number)
        if number == 1 and p != degree:
            number = ''
        else:
            number = str(number)

        formatted += sign + str(number) + coefficient + ('' if current_degree == 0 else ' ')
    return formatted


# Prevents from running when imported in other file. Imported in other exercises to reuse code.
if __name__ == '__main__':
    print(format_polynomial(get_polynomial()))
