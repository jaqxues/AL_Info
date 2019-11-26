from random import randint

a, b = randint(10, 20), randint(10, 20)

correct_answers = 0

# Sum
if int(input(f"{a} + {b} = ")) == a + b:
    print("Correct Answer!")
    correct_answers += 1
else:
    print(f"Wrong Answer (correct: {a + b})")

# Difference
if int(input(f"{a} - {b} = ")) == a - b:
    print("Correct Answer!")
    correct_answers += 1
else:
    print(f"Wrong Answer (correct: {a - b})")

# Product
if int(input(f"{a} * {b} = ")) == a * b:
    print("Correct Answer!")
    correct_answers += 1
else:
    print(f"Wrong Answer (correct: {a * b})")

# Integer Division
if int(input(f"{a} // {b} = ")) == a // b:
    print("Correct Answer!")
    correct_answers += 1
else:
    print(f"Wrong Answer (correct: {a // b})")

# \n -> new line
# \t -> 4 spaces (1 Tab)
print("======\n\nResult:\n\tCorrect Answers:", correct_answers, "- Wrong Answers:", 4 - correct_answers)
