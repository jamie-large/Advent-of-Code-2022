class CPU:
    def __init__(self):
        self.t = 1
        self.X = 1

    def execute(self, inst: str):
        spl = inst.split()
        if spl[0] == "addx":
            self.X += int(spl[1])
            self.t += 2
        elif spl[0] == "noop":
            self.t += 1
        return self.t

def solution_part1(fname="inputs/day10"):
    with open(fname, "r") as f:
        C = CPU()
        cycle = 0
        previous_x = 1
        next = 20
        result = 0
        for line in f:
            cycle = C.execute(line)
            if cycle > next:
                result += next * previous_x
                next += 40
                if next > 220:
                    break
            previous_x = C.X
        print(result)


def solution_part2(fname="inputs/day10"):
    with open(fname, "r") as f:
        C = CPU()
        drawing: list[list[str]] = [[]]
        previous_x = 1
        cycle = 1
        for line in f:
            previous_cycle = cycle
            cycle = C.execute(line)
            for i in range(previous_cycle, cycle):
                if (i-1) % 40 == 0:
                    drawing.append([])
                drawing[-1].append("#" if abs(previous_x - len(drawing[-1])) <= 1 else ".")
            previous_x = C.X

        for x in drawing:
            print("".join(x))

solution_part2()
