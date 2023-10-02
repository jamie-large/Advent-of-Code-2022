def solution_part1(fname="inputs/day25"):
    with open(fname, "r") as f:
        total_sum = 0
        for line in f:
            total_sum += snafu_to_decimal(line[:-1])
        print(decimal_to_snafu(total_sum))

def snafu_to_decimal(n: str) -> int:
    result = 0
    for i in range(len(n)):
        c = n[len(n) - 1 - i]
        c_val = int(c) if c in ("0", "1", "2") else -1 if c == "-" else -2
        result += c_val * (5 ** i)
    return result

def decimal_to_snafu(n: int) -> str:
    result = []
    val = n
    inc = False
    while val != 0:
        mod = val % 5
        if mod in (0, 1):
            result.append(str(mod + 1) if inc else str(mod))
            inc = False
        elif mod == 2:
            if inc:
                result.append("=")
            else:
                result.append("2")
        elif mod == 3:
            if inc:
                result.append("-")
            else:
                result.append("=")
            inc = True
        elif mod == 4:
            if inc:
                result.append("0")
            else:
                result.append("-")
            inc = True
        val = int(val / 5)
    if inc:
        result.append("1")
    result.reverse()
    return "".join(result)

def solution_part2(fname="inputs/day25"):
    with open(fname, "r") as f:
        pass

solution_part1()
