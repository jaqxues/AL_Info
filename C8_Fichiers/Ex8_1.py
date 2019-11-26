filename = input("Enter filename: ")

lines = 0
words = 0

with open(filename, "r") as file:
    line = file.readline()
    while line != "":
        line += 1
        words += len(line.split(" "))

print(words, "words in", lines, "lines of file", filename)
