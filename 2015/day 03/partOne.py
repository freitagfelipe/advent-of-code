questionInputFile = open("input.txt", "r")
questionInput = questionInputFile.read()
questionInputFile.close()

answer = 1
coordinates = [[0, 0]]
verticalMove = 0
horizontalMove = 0

for character in questionInput:
    verify = 1

    if character == "<":
        horizontalMove -= 1
    elif character == ">":
        horizontalMove += 1
    elif character == "^":
        verticalMove += 1
    elif character == "v":
        verticalMove -= 1

    position = [horizontalMove, verticalMove]

    for coordinate in coordinates:
        if coordinate[0] == position[0] and coordinate[1] == position[1]:
            verify = 0
            break

    if verify:
        answer += 1
        coordinates.append(position)

print(answer)