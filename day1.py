def solution_part1(fname: str = "inputs/day1"):
    with open(fname, "r") as f:
        max_cals: int = 0
        current_cals: int = 0
        for line in [*f.readlines(), "\n"]:
            if len(line) == 1:
                if current_cals > max_cals:
                    max_cals = current_cals
                current_cals = 0
            else:
                current_cals += int(line)
        print(max_cals)

def solution_part2(fname: str = "inputs/day1"):
    with open(fname, "r") as f:
        max_cals: list[int] = [0, 0, 0]
        current_cals: int = 0
        for line in [*f.readlines(), "\n"]:
            if len(line) == 1:
                if current_cals > max_cals[0]:
                    max_cals[2] = max_cals[1]
                    max_cals[1] = max_cals[0]
                    max_cals[0] = current_cals
                elif current_cals > max_cals[1]:
                    max_cals[2] = max_cals[1]
                    max_cals[1] = current_cals
                elif current_cals > max_cals[2]:
                    max_cals[2] = current_cals
                current_cals = 0
            else:
                current_cals += int(line)

        print(sum(max_cals))

solution_part2("inputs/test")
solution_part2()

