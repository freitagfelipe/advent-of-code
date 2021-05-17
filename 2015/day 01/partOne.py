questionInputFile = open("input.txt", "r")
questionInput = questionInputFile.read()
questionInputFile.close()

answer = 0

for character in questionInput:
    if character == "(":
        answer += 1
    else:
        answer -= 1

print(answer)