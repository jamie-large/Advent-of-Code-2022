Blizzard = dict[tuple[int, int], list[str]]

def solution_part1(fname="inputs/day24"):
    with open(fname, "r") as f:
        grid = [line[:-1] for line in f.readlines()]
        dimensions = (len(grid), len(grid[0]))
        num_states = (dimensions[0] - 2) * (dimensions[1] - 2)
        blizzards_at_time: dict[int, Blizzard] = { 0: dict() }
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                if grid[i][j] != ".":
                    blizzards_at_time[0][(i, j)] = [grid[i][j]]

        queue: list[int, int, int] = [(0, 1, 0)]
        dont_process: set[tuple[int, int, int]] = set(queue)

        BLANK_GRID = ["#." + "#" * (dimensions[1] - 2)] + ["#" + "." * (dimensions[1] - 2) + "#" for _ in range(dimensions[0] - 2)] + ["#" * (dimensions[1] - 2) + ".#"]
        BLANK_GRID = [[c for c in line] for line in BLANK_GRID]

        while len(queue) > 0:
            row, col, time = queue.pop(0)
            modded_time = (time + 1) % num_states

            if modded_time not in blizzards_at_time:
                blizzards_at_time[modded_time] = make_next_blizzard(blizzards_at_time[time % num_states], dimensions)

            next_blizzard = blizzards_at_time[modded_time]

            # If they can move down into the end, we've won
            if (row + 1, col) == (dimensions[0] - 1, dimensions[1] - 2):
                print(time + 1)
                return

            # If they can remain in place
            if (row, col) not in next_blizzard and (row, col, modded_time) not in dont_process:
                queue.append((row, col, time + 1))
                dont_process.add((row, col, modded_time))
            # If they can move down
            if row < dimensions[0] - 2 and (row + 1, col) not in next_blizzard and (row + 1, col, modded_time) not in dont_process:
                queue.append((row + 1, col, time + 1))
                dont_process.add((row + 1, col, modded_time))

            if (row, col) == (0, 1):
                continue

            # If they can move right
            if col < dimensions[1] - 2 and (row, col + 1) not in next_blizzard and (row, col + 1, modded_time) not in dont_process:
                queue.append((row, col + 1, time + 1))
                dont_process.add((row, col + 1, modded_time))
            # If they can move up
            if row > 1 and (row - 1, col) not in next_blizzard and (row - 1, col, modded_time) not in dont_process:
                queue.append((row - 1, col, time + 1))
                dont_process.add((row - 1, col, modded_time))
            # If they can move left
            if col > 1 and (row, col - 1) not in next_blizzard and (row, col - 1, modded_time) not in dont_process:
                queue.append((row, col - 1, time + 1))
                dont_process.add((row, col - 1, modded_time))

def make_next_blizzard(b: Blizzard, dimensions: tuple[int, int]) -> Blizzard:
    next_blizzard: Blizzard = dict()
    for row, col in b:
        for wind in b[(row, col)]:
            new_pos = (row, col)
            if wind == ">":
                new_pos = (row, col + 1 if col < dimensions[1] - 2 else 1)
            elif wind == "<":
                new_pos = (row, col - 1 if col > 1 else dimensions[1] - 2)
            elif wind == "v":
                new_pos = (row + 1 if row < dimensions[0] - 2 else 1, col)
            elif wind == "^":
                new_pos = (row - 1 if row > 1 else dimensions[0] - 2, col)

            if new_pos not in next_blizzard:
                next_blizzard[new_pos] = []
            next_blizzard[new_pos].append(wind)
    return next_blizzard


def solution_part2(fname="inputs/day24"):
    with open(fname, "r") as f:
        grid = [line[:-1] for line in f.readlines()]
        dimensions = (len(grid), len(grid[0]))
        num_states = (dimensions[0] - 2) * (dimensions[1] - 2)
        blizzards_at_time: dict[int, Blizzard] = { 0: dict() }
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                if grid[i][j] != ".":
                    blizzards_at_time[0][(i, j)] = [grid[i][j]]

        queue: list[int, int, int] = [(0, 1, 0)]
        dont_process: set[tuple[int, int, int]] = set(queue)
        stage = 0

        BLANK_GRID = ["#." + "#" * (dimensions[1] - 2)] + ["#" + "." * (dimensions[1] - 2) + "#" for _ in range(dimensions[0] - 2)] + ["#" * (dimensions[1] - 2) + ".#"]
        BLANK_GRID = [[c for c in line] for line in BLANK_GRID]

        while len(queue) > 0:
            row, col, time = queue.pop(0)
            modded_time = (time + 1) % num_states

            if modded_time not in blizzards_at_time:
                blizzards_at_time[modded_time] = make_next_blizzard(blizzards_at_time[time % num_states], dimensions)

            next_blizzard = blizzards_at_time[modded_time]

            # If they can move down into the end, increase the stage
            if (row + 1, col) == (dimensions[0] - 1, dimensions[1] - 2):
                if stage == 0:
                    stage += 1
                    queue = [(dimensions[0] - 1, dimensions[1] - 2, time + 1)]
                    dont_process = set([(dimensions[0] - 1, dimensions[1] - 2, modded_time)])
                    continue
                elif stage == 2:
                    print(time + 1)
                    return

            # If they can move up into the start and are in the proper stage, increase the stage
            if (row - 1, col) == (0, 1) and stage == 1:
                stage += 1
                queue = [(0, 1, time + 1)]
                dont_process = set([(0, 1, modded_time)])
                continue

            # If they can remain in place
            if (row, col) not in next_blizzard and (row, col, modded_time) not in dont_process:
                queue.append((row, col, time + 1))
                dont_process.add((row, col, modded_time))
            # If they can move down
            if row < dimensions[0] - 2 and (row + 1, col) not in next_blizzard and (row + 1, col, modded_time) not in dont_process:
                queue.append((row + 1, col, time + 1))
                dont_process.add((row + 1, col, modded_time))

            if (row, col) == (0, 1):
                continue
            # If they can move right
            if col < dimensions[1] - 2 and (row, col + 1) not in next_blizzard and (row, col + 1, modded_time) not in dont_process:
                queue.append((row, col + 1, time + 1))
                dont_process.add((row, col + 1, modded_time))
            # If they can move up
            if row > 1 and (row - 1, col) not in next_blizzard and (row - 1, col, modded_time) not in dont_process:
                queue.append((row - 1, col, time + 1))
                dont_process.add((row - 1, col, modded_time))

            if (row, col) == (dimensions[0] - 1, dimensions[1] - 2):
                continue
            # If they can move left
            if col > 1 and (row, col - 1) not in next_blizzard and (row, col - 1, modded_time) not in dont_process:
                queue.append((row, col - 1, time + 1))
                dont_process.add((row, col - 1, modded_time))

solution_part2()
