def solution_part1(fname: str = "inputs/day2"):
    with open(fname, "r") as f:
        total = 0
        for line in f:
            opp, you = line.split()
            if you == "X":
                total += 1 if opp == "B" else 4 if opp == "A" else 7
            elif you == "Y":
                total += 2 if opp == "C" else 5 if opp == "B" else 8
            elif you == "Z":
                total += 3 if opp == "A" else 6 if opp == "C" else 9
        print(total)


def solution_part2(fname: str = "inputs/day2"):
    with open(fname, "r") as f:
        total = 0
        for line in f:
            opp, res = line.split()
            if opp == "A":
                total += 3 if res == "X" else 4 if res == "Y" else 8
            elif opp == "B":
                total += 1 if res == "X" else 5 if res == "Y" else 9
            elif opp == "C":
                total += 2 if res == "X" else 6 if res == "Y" else 7
        print(total)

solution_part2()
