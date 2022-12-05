from math import ceil

first_line = input()
how_many_columns = ceil(len(first_line) / 4)

valid_columns = [x for x in range(1, how_many_columns * 4 - 2, 4)]
stacks = [[] for _ in range(0, how_many_columns)]

def formatter(str):
    for [i, column] in enumerate(valid_columns):
        if str[column] != " ":
            stacks[i].append(str[column])

formatter(first_line)

while True:
    line = input()

    if line[1] == "1":
        break

    formatter(line)

input()

while True:
    try:
        [_, how_many_times, _, from_col, _, to_col] = input().split(" ")

        how_many_times = int(how_many_times)
        from_col = int(from_col) - 1
        to_col = int(to_col) - 1

        aux = stacks[from_col][0:how_many_times]
        
        aux.reverse()
        aux.extend(stacks[to_col])

        stacks[to_col] = aux
        stacks[from_col] = stacks[from_col][how_many_times::]
    except EOFError:
        break

for stack in stacks:
    if len(stack) != 0:
        print(stack[0], end="")

print()