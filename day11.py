class Monkey:
    def __init__(self):
        self.items: list[int] = []
        self.operation: tuple[str] = ()
        self.test: int = 0
        self.true_monkey: int = 0
        self.false_monkey: int = 0

    def __repr__(self):
        return f"Items: {self.items}, Op: {self.operation}, Test: {self.test}, True: {self.true_monkey}, False: {self.false_monkey}"


def solution_part1(fname="inputs/day11"):
    with open(fname, "r") as f:
        monkeys: list[Monkey] = []
        for line in f:
            if len(line) == 1:
                continue
            spl = line.split()
            if spl[0] == "Monkey":
                monkeys.append(Monkey())
            elif spl[0] == "Starting":
                monkeys[-1].items = [int(x[:-1]) for x in spl[2:-1]] + [int(spl[-1])]
            elif spl[0] == "Operation:":
                monkeys[-1].operation = (spl[-2], int(spl[-1]) if spl[-1] != "old" else spl[-1])
            elif spl[0] == "Test:":
                monkeys[-1].test = int(spl[-1])
            elif spl[1] == "true:":
                monkeys[-1].true_monkey = int(spl[-1])
            elif spl[1] == "false:":
                monkeys[-1].false_monkey = int(spl[-1])

        inspections = [0 for _ in range(len(monkeys))]
        for _ in range(20):
            for i in range(len(monkeys)):
                m = monkeys[i]
                # print(f"Monkey {i}:")
                while len(m.items) > 0:
                    item = m.items.pop(0)
                    # print(f"  Monkey inspects an item with a worry level of {item}")
                    inspections[i] += 1
                    val: int = item if m.operation[1] == "old" else m.operation[1]
                    if m.operation[0] == "+":
                        item += val
                    elif m.operation[0] == "*":
                        item *= val
                    # print(f"    Worry level is multiplied by {val} to {item}")
                    item = int(item / 3)
                    # print(f"    Monkey gets bored with item. Worry level is divided by {3} to {item}")
                    if item % m.test == 0:
                        # print(f"    Current worry level is divisible by {m.test}")
                        monkeys[m.true_monkey].items.append(item)
                        # print(f"    Item with worry level {item} is thrown to monkey {m.true_monkey}")
                    else:
                        # print(f"    Current worry level is not divisible by {m.test}")
                        monkeys[m.false_monkey].items.append(item)
                        # print(f"    Item with worry level {item} is thrown to monkey {m.false_monkey}")

        inspections.sort(reverse=True)
        print(inspections[0] * inspections[1])


def solution_part2(fname="inputs/day11"):
    with open(fname, "r") as f:
        monkeys: list[Monkey] = []
        for line in f:
            if len(line) == 1:
                continue
            spl = line.split()
            if spl[0] == "Monkey":
                monkeys.append(Monkey())
            elif spl[0] == "Starting":
                monkeys[-1].items = [int(x[:-1]) for x in spl[2:-1]] + [int(spl[-1])]
            elif spl[0] == "Operation:":
                monkeys[-1].operation = (spl[-2], int(spl[-1]) if spl[-1] != "old" else spl[-1])
            elif spl[0] == "Test:":
                monkeys[-1].test = int(spl[-1])
            elif spl[1] == "true:":
                monkeys[-1].true_monkey = int(spl[-1])
            elif spl[1] == "false:":
                monkeys[-1].false_monkey = int(spl[-1])

        MOD_VALUE = 1
        for m in monkeys:
            MOD_VALUE *= m.test
        inspections = [0 for _ in range(len(monkeys))]
        for _ in range(10000):
            for i in range(len(monkeys)):
                m = monkeys[i]
                # print(f"Monkey {i}:")
                while len(m.items) > 0:
                    item = m.items.pop(0)
                    # print(f"  Monkey inspects an item with a worry level of {item}")
                    inspections[i] += 1
                    val: int = item if m.operation[1] == "old" else m.operation[1]
                    if m.operation[0] == "+":
                        item += val
                    elif m.operation[0] == "*":
                        item *= val
                    # print(f"    Worry level is multiplied by {val} to {item}")
                    item = item % MOD_VALUE
                    # print(f"    Monkey gets bored with item. Worry level is taken by mod {MOD_VALUE} to {item}")
                    if item % m.test == 0:
                        # print(f"    Current worry level is divisible by {m.test}")
                        monkeys[m.true_monkey].items.append(item)
                        # print(f"    Item with worry level {item} is thrown to monkey {m.true_monkey}")
                    else:
                        # print(f"    Current worry level is not divisible by {m.test}")
                        monkeys[m.false_monkey].items.append(item)
                        # print(f"    Item with worry level {item} is thrown to monkey {m.false_monkey}")

        inspections.sort(reverse=True)
        print(inspections[0] * inspections[1])

solution_part2()
