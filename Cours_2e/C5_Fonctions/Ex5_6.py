def add_one_sec(h, m, s):
    assert 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
    return f'{h} {m} {s}'
