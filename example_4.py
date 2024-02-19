sentence = "Hello, world!"

print(sentence[2])

print(sentence[-2])

print(sentence[:5])

print(sentence[:-2])

for i in range(0, len(sentence), 2):
    print(sentence[i], end="")

print()

for i in range(1, len(sentence), 2):
    print(sentence[i], end="")

print()

for i in range(len(sentence)-1, -1, -1):
    print(sentence[i], end="")

print()


for i in range(len(sentence)-1, -1, -2):
    print(sentence[i], end="")

print()

print(len(sentence))
