def solution_part1(fname="inputs/day5"):
    with open(fname, "r") as f:
        state = 0
        stacks = []
        for line in f:
            if len(line) == 1:
                state = 1
                for s in stacks:
                    s.pop()
            elif state == 0:
                for i in range(1, len(line), 4):
                    if line[i] != " ":
                        while int(i / 4) >= len(stacks):
                            stacks.append([])
                        stacks[int(i / 4)].append(line[i])
            else:
                spl = line.split()
                n = int(spl[1])
                orig = int(spl[3]) - 1
                dest = int(spl[5]) - 1

                stacks[dest] = stacks[orig][:n][::-1] + stacks[dest]
                stacks[orig] = stacks[orig][n:]
        print("".join([s[0] for s in stacks]))

def solution_part2(fname="inputs/day5"):
    with open(fname, "r") as f:
        state = 0
        stacks = []
        for line in f:
            if len(line) == 1:
                state = 1
                for s in stacks:
                    s.pop()
            elif state == 0:
                for i in range(1, len(line), 4):
                    if line[i] != " ":
                        while int(i / 4) >= len(stacks):
                            stacks.append([])
                        stacks[int(i / 4)].append(line[i])
            else:
                spl = line.split()
                n = int(spl[1])
                orig = int(spl[3]) - 1
                dest = int(spl[5]) - 1

                stacks[dest] = stacks[orig][:n] + stacks[dest]
                stacks[orig] = stacks[orig][n:]
        print("".join([s[0] for s in stacks]))

solution_part2()
