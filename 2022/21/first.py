monkey_dict = {}

while True:
    try:
        entry = input().split(" ")

        name = entry[0][:-1:]

        if len(entry) == 2:
            solution = int(entry[1])

            monkey_dict[name] = {"solution": solution, "problem": None, "dependencies": None}
        else:
            monkey_dict[name] = {"solution": None, "problem": " ".join(entry[1::]), "dependencies": [entry[1], entry[3]]}
    except EOFError:
        break

def calculate_solution(first_solution: int, second_solution: int, problem: str) -> int:
    [_, op, _] = problem.split(" ")

    if op == '+':
        return first_solution + second_solution
    elif op == '*':
        return first_solution * second_solution
    elif op == '-':
        return first_solution - second_solution

    return first_solution // second_solution
    

def get_solution(key: str):
    if monkey_dict[key]["solution"]:
        return

    [first_dependency, second_dependency] = monkey_dict[key]["dependencies"]

    first_solution, second_solution = monkey_dict[first_dependency]["solution"], monkey_dict[second_dependency]["solution"]

    if first_solution and second_solution:
        monkey_dict[key]["solution"] = calculate_solution(first_solution, second_solution, monkey_dict[key]["problem"])


while monkey_dict["root"]["solution"] == None:
    for key in monkey_dict:
        get_solution(key)

print(monkey_dict["root"]["solution"])