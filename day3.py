def solution_part1(fname="inputs/day3"):
    with open(fname, "r") as f:
        result = 0
        for line in f:
            seen: set[str] = set()
            dups: set[str] = set()
            for i in range(len(line)):
                if i < (len(line) - 1) / 2:
                    seen.add(line[i])
                elif line[i] in seen:
                    dups.add(line[i])
            for c in dups:
                result += ord(c) - ord("a") + 1 if c.islower() else ord(c) - ord("A") + 27
        print(result)

def solution_part2(fname="inputs/day3"):
    with open(fname, "r") as f:
        result = 0
        i = 0
        seen = set()
        for line in f:
            if i == 0:
                seen = set()
                for c in line[:-1]:
                    seen.add(c)
            elif i == 1:
                double_seen = set()
                for c in line[:-1]:
                    if c in seen:
                        double_seen.add(c)
                seen = double_seen
            elif i == 2:
                for c in line[:-1]:
                    if c in seen:
                        result += ord(c) - ord("a") + 1 if c.islower() else ord(c) - ord("A") + 27
                        break

            i = (i + 1) % 3
        print(result)

solution_part2()
