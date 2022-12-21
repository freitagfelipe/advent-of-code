from math import floor

monkeys = []
curr_dict = {}

while True:
    try:
        entry = input().strip()

        if entry.startswith("Monkey"):
            continue
        elif entry.startswith("Starting"):
            items = [int(x) for x in entry[16::].split(", ")]

            curr_dict["items"] = items
        elif entry.startswith("Operation"):
            operation = entry[17::]

            curr_dict["operation"] = operation
        elif entry.startswith("Test"):
            divisible_by = entry.split(" ")[3]

            curr_dict["test"] = int(divisible_by)
        elif entry.startswith("If"):
            entry = entry.split(" ")

            curr_dict[entry[1][:-1:]] = int(entry[5])
        elif entry == "":
            monkeys.append(curr_dict)

            curr_dict = {}

            pass
    except EOFError:
        monkeys.append(curr_dict)

        break

def process_operation(operation: str, curr_worry: int) -> int:
    operation = operation.replace("old", str(curr_worry)).split(" ")

    value = 0

    if operation[1] == '+':
        value = int(operation[0]) + int(operation[2])
    else:
        value = int(operation[0]) * int(operation[2])

    return floor(value / 3)


def process_test(value: int, test: int) -> bool:
    if value % test == 0:
        return True

    return False


answer = [0 for _ in range(0, len(monkeys))]

for i in range(0, len(monkeys) * 20):
    j = i % len(monkeys)

    for item in monkeys[j]["items"]:
        new_worry = process_operation(monkeys[j]["operation"], item)
        result = process_test(new_worry, monkeys[j]["test"])

        if result:
            index = monkeys[j]["true"]

            monkeys[index]["items"].append(new_worry)
        else:
            index = monkeys[j]["false"]

            monkeys[index]["items"].append(new_worry)

        answer[j] += 1

    monkeys[j]["items"] = []

answer.sort(reverse=True)

print(answer[0] * answer[1])