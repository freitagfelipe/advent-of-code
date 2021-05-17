questionInputFile = open("input.txt", "r")
questionInput = questionInputFile.read()
questionInputFile.close()

answer = 1
coordinates = [[[0, 0]], [[0,0]]]
verticalMove = [0, 0]
horizontalMove = [0, 0]
shift = 0


for character in questionInput:
    verify = 1

    if character == "<":
        horizontalMove[shift] -= 1
    elif character == ">":
        horizontalMove[shift] += 1
    elif character == "^":
        verticalMove[shift] += 1
    elif character == "v":
        verticalMove[shift] -= 1

    position = [horizontalMove[shift], verticalMove[shift]]

    for coordinate in coordinates[0]:
        if coordinate[0] == position[0] and coordinate[1] == position[1]:
            verify = 0
            break

    for coordinate in coordinates[1]:
        if coordinate[0] == position[0] and coordinate[1] == position[1]:
            verify = 0
            break

    if verify:
        answer += 1
        coordinates[shift].append(position)
    
    if shift:
        shift = 0
    else:
        shift = 1

print(answer)