questionInputFile = open("input.txt", "r")
questionInput = questionInputFile.read()
questionInputFile.close()

lines = questionInput.split("\n")

answer = 0

for line in lines:
    line  = line.split("x")
    numbers = [int(line[0]), int(line[1]), int(line[2])]

    numbers.sort()

    answer += numbers[0] * numbers[1] * numbers[2] + numbers[0] * 2 + numbers[1] * 2

print(answer)