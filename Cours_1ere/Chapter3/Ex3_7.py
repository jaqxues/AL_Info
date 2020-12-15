from stack import Stack


def check(expr):
    s = Stack()
    groups = {m1: m2 for m1, m2 in ("()", "''", "{}", "[]", '""')}
    for c in expr:
        if c in groups:
            s.push(c)
        elif c in groups.values():
            if s.is_empty():
                print('Empty Stack, unmatched', c)
                return False
            elif c != groups[s.pop()]:
                print(c, 'in bad position')
                return False
    return s.is_empty()


print(check("{({([][][])})()}"))
print(check("( ) ( ) [ ] { } "))
print(check("([{([{}()]())}[]])"))
print(check("[ {    ] } "))
print(check("(()))"))
print(check("{[}[]}"))

print(check("2*[3+4*(5-x)**2-y]/sin(3)"))
