ans = 0

while True:
    try:
        [first, second] = [x.split("-") for x in input().split(",")]

        first = [int(x) for x in first]
        second = [int(x) for x in second]

        if second[0] <= first[0] <= second[1] or second[0] <= first[1] <= second[1]:
            ans += 1
        elif first[0] <= second[0] <= first[1] or first[0] <= second[1] <= first[1]:
            ans += 1
    except EOFError:
        break

print(ans)