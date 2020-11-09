value = int(input('Value: '))

if value >= 0:
    abs_value = value
else:
    abs_value = -value

# Or using the 'Ternary Operator'
abs_value = value if value >= 0 else -value

print('Absolute Value:', abs_value)
