ROMAN = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]


def to_roman(_n):
    result = []
    for (arabic, roman) in ROMAN:
        (factor, _n) = divmod(_n, arabic)
        result.append(roman * factor)
        if _n == 0:
            break
    return ''.join(result)


def to_arabic(_n):
    tmp = _n
    result = 0
    for (arabic, roman) in ROMAN:
        while tmp.startswith(roman):
            result += arabic
            tmp = tmp[len(roman):]
        if not tmp:
            break
    else:
        raise Exception('Not a valid number')

    assert to_roman(result) == _n
    return result


print(to_roman(2000))
a_n = int(input('Enter arabic: '))
print(to_roman(a_n))
r_n = input('Enter roman: ')
print(to_arabic(r_n))
