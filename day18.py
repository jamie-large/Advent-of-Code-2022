def solution_part1(fname="inputs/day18"):
    with open(fname, "r") as f:
        cube_positions: set[tuple[int, int, int]] = set()
        for line in f:
            cube_positions.add(tuple([int(x) for x in line.split(",")]))

        result = 0
        for x, y, z in cube_positions:
            neighbor_offsets = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
            neighbors = [(x+i, y+j, z+k) for (i, j, k) in neighbor_offsets]
            for n in neighbors:
                if n not in cube_positions:
                    result += 1
        print(result)


def solution_part2(fname="inputs/day18"):
    with open(fname, "r") as f:
        cube_positions: set[tuple[int, int, int]] = set()
        maxes = [0, 0, 0]
        mins = [0, 0, 0]
        for line in f:
            coordinates = [int(x) for x in line.split(",")]
            cube_positions.add(tuple(coordinates))
            maxes = [max(maxes[i], coordinates[i] + 1) for i in range(3)]
            mins = [min(mins[i], coordinates[i] - 1) for i in range(3)]

        queue: list[tuple[int, int, int]] = [tuple(mins)]
        dont_process: set[tuple[int, int, int]] = set(queue)
        result = 0

        while len(queue) > 0:
            x, y, z = queue.pop(0)
            neighbor_offsets = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
            neighbors = [(x+i, y+j, z+k) for (i, j, k) in neighbor_offsets]
            for n in neighbors:
                if n in cube_positions:
                    result += 1
                elif n not in dont_process and all(n[i] >= mins[i] and n[i] <= maxes[i] for i in range(3)):
                    dont_process.add(n)
                    queue.append(n)
        print(result)

solution_part2()
