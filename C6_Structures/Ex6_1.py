# Using List Comprehension
inputs = [int(input(f"Enter number ({x + 1}): ")) for x in range(5)]

# Or:
# inputs = []
# for x in range(5):
#     inputs.append(int(input(f"Enter number ({x + 1}): ")))

print(inputs)
