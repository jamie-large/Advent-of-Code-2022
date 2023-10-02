def solution_part1(fname="inputs/day4"):
    with open(fname, "r") as f:
        result = 0
        for line in f:
            [[a, b], [c, d]] = [[int(c) for c in ass.split("-")] for ass in line.split(",")]
            if (a >= c and b <= d) or (c >= a and d <= b):
                result += 1
        print(result)

def solution_part2(fname="inputs/day4"):
    with open(fname, "r") as f:
        result = 0
        for line in f:
            [[a, b], [c, d]] = [[int(c) for c in ass.split("-")] for ass in line.split(",")]
            if (a >= c and a <= d) or (b >= c and b <= d) or (c >= a and c <= b) or (d >= a and d <= b):
                result += 1
        print(result)

solution_part2()
