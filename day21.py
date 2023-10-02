def solution_part1(fname="inputs/day21"):
    with open(fname, "r") as f:
        unsolved: dict[str, tuple[str, str, str]] = {}
        solved: dict[str, int] = {}
        for line in f:
            spl = line.split()
            if len(spl) == 2:
                solved[spl[0][:-1]] = int(spl[1])
            elif spl[1] in solved and spl[3] in solved:
                if spl[2] == "+":
                    solved[spl[0][:-1]] = solved[spl[1]] + solved[spl[3]]
                elif spl[2] == "-":
                    solved[spl[0][:-1]] = solved[spl[1]] - solved[spl[3]]
                elif spl[2] == "*":
                    solved[spl[0][:-1]] = solved[spl[1]] * solved[spl[3]]
                elif spl[2] == "/":
                    solved[spl[0][:-1]] = int(solved[spl[1]] / solved[spl[3]])
            else:
                unsolved[spl[0][:-1]] = (spl[1], spl[2], spl[3])

        while "root" in unsolved:
            solved_this_time: set[str] = set()
            for s in unsolved:
                recipe = unsolved[s]
                if (recipe[0] in solved or recipe[0] in solved_this_time) and (recipe[2] in solved or recipe[2] in solved_this_time):
                    solved_this_time.add(s)
                    if recipe[1] == "+":
                        solved[s] = solved[recipe[0]] + solved[recipe[2]]
                    elif recipe[1] == "-":
                        solved[s] = solved[recipe[0]] - solved[recipe[2]]
                    elif recipe[1] == "*":
                        solved[s] = solved[recipe[0]] * solved[recipe[2]]
                    elif recipe[1] == "/":
                        solved[s] = int(solved[recipe[0]] / solved[recipe[2]])
            for s in solved_this_time:
                unsolved.pop(s)

        print(solved["root"])

def solution_part2(fname="inputs/day21"):
    with open(fname, "r") as f:
        unsolved: dict[str, tuple[str, str, str]] = {}
        solved: dict[str, int] = {}
        for line in f:
            spl = line.split()
            if spl[0][:-1] == "humn":
                continue
            elif len(spl) == 2:
                solved[spl[0][:-1]] = int(spl[1])
            elif spl[1] in solved and spl[3] in solved:
                if spl[2] == "+":
                    solved[spl[0][:-1]] = solved[spl[1]] + solved[spl[3]]
                elif spl[2] == "-":
                    solved[spl[0][:-1]] = solved[spl[1]] - solved[spl[3]]
                elif spl[2] == "*":
                    solved[spl[0][:-1]] = solved[spl[1]] * solved[spl[3]]
                elif spl[2] == "/":
                    solved[spl[0][:-1]] = int(solved[spl[1]] / solved[spl[3]])
            else:
                unsolved[spl[0][:-1]] = (spl[1], spl[2], spl[3])
        unsolved["root"] = (unsolved["root"][0], "=", unsolved["root"][2])

        solved_this_time: set[str] = set(["temp"])
        while len(solved_this_time) > 0:
            solved_this_time = set()
            for s in unsolved:
                recipe = unsolved[s]
                if (recipe[0] in solved or recipe[0] in solved_this_time) and (recipe[2] in solved or recipe[2] in solved_this_time):
                    solved_this_time.add(s)
                    if recipe[1] == "+":
                        solved[s] = solved[recipe[0]] + solved[recipe[2]]
                    elif recipe[1] == "-":
                        solved[s] = solved[recipe[0]] - solved[recipe[2]]
                    elif recipe[1] == "*":
                        solved[s] = solved[recipe[0]] * solved[recipe[2]]
                    elif recipe[1] == "/":
                        solved[s] = int(solved[recipe[0]] / solved[recipe[2]])
            for s in solved_this_time:
                unsolved.pop(s)

        exp = find_expression(unsolved["root"], solved, unsolved)
        print(solve_equation(exp[0], exp[2]))

def find_expression(exp: tuple[str, str, str], solved: dict[str, int], unsolved: dict[str, tuple[str, str, str]]):
    result = []
    if exp[0] == "humn":
        result.append(exp[0])
    elif exp[0] in solved:
        result.append(solved[exp[0]])
    else:
        result.append(find_expression(unsolved[exp[0]], solved, unsolved))

    result.append(exp[1])

    if exp[2] == "humn":
        result.append(exp[2])
    elif exp[2] in solved:
        result.append(solved[exp[2]])
    else:
        result.append(find_expression(unsolved[exp[2]], solved, unsolved))

    return tuple(result)

def solve_equation(exp: tuple[tuple | int | str, str, tuple | int | str], number: int):
    while exp != "humn":
        if exp[1] == "+":
            number = number - (exp[0] if isinstance(exp[0], int) else exp[2])
            exp = (exp[2] if isinstance(exp[0], int) else exp[0])
        elif exp[1] == "*":
            number = int(number / (exp[0] if isinstance(exp[0], int) else exp[2]))
            exp = (exp[2] if isinstance(exp[0], int) else exp[0])
        elif exp[1] == "-":
            if isinstance(exp[0], int):
                number = exp[0] - number
                exp = exp[2]
            else:
                number = number + exp[2]
                exp = exp[0]
        elif exp[1] == "/":
            number = number * exp[2]
            exp = exp[0]

    return number

solution_part2()
