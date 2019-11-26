from random import randint

values = [randint(1, 100) for x in range(20)]
print(values)
print('Min Value:', min(values))
print('Max Value:', max(values))
value_sum = sum(values)
print('Sum:', value_sum)
print('Average', value_sum / len(values))
