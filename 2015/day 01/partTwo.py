questionInputFile = open("input.txt", "r")
questionInput = questionInputFile.read()
questionInputFile.close()

index = 1
floor = 0

for character in questionInput:
    if character == "(":
        floor += 1
    else:
        floor -= 1

    if floor == -1:
        print(index)
        break
    else:
        index += 1