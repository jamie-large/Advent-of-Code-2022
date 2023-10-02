# NORTH, SOUTH, WEST, EAST
NEIGHBOR_INDICES = [(2, 4, 7), (0, 3, 5), (0, 1, 2), (5, 6, 7)]
CHANGES = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def solution_part1(fname="inputs/day23"):
    with open(fname, "r") as f:
        grid = f.readlines()
        elf_positions: set[tuple[int, int]] = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "#":
                    elf_positions.add((j, len(grid) - i - 1))

        for N in range(10):
            # proposed dest, origin
            proposed_moves: dict[tuple[int, int], tuple[int, int]] = {}
            rejected_moves: set[tuple[int, int]] = set()

            for x, y in elf_positions:
                # SW, W, NW, S, N, SE, E, NE
                neighbors = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
                # Don't move if they have no neighbors
                if all(n not in elf_positions for n in neighbors):
                    continue

                proposed_dest = (0, 0)
                # Check to the first direction
                if all(neighbors[i] not in elf_positions for i in NEIGHBOR_INDICES[N % 4]):
                    proposed_dest = (x + CHANGES[N % 4][0], y + CHANGES[N % 4][1])
                # Check to the second direction
                elif all(neighbors[i] not in elf_positions for i in NEIGHBOR_INDICES[(N + 1) % 4]):
                    proposed_dest = (x + CHANGES[(N + 1) % 4][0], y + CHANGES[(N + 1) % 4][1])
                # Check to the third direction
                elif all(neighbors[i] not in elf_positions for i in NEIGHBOR_INDICES[(N + 2) % 4]):
                    proposed_dest = (x + CHANGES[(N + 2) % 4][0], y + CHANGES[(N + 2) % 4][1])
                # Check to the fourth direction
                elif all(neighbors[i] not in elf_positions for i in NEIGHBOR_INDICES[(N + 3) % 4]):
                    proposed_dest = (x + CHANGES[(N + 3) % 4][0], y + CHANGES[(N + 3) % 4][1])
                else:
                    continue

                if proposed_dest in rejected_moves:
                    continue
                elif proposed_dest in proposed_moves:
                    rejected_moves.add(proposed_dest)
                    proposed_moves.pop(proposed_dest)
                else:
                    proposed_moves[proposed_dest] = (x, y)

            for d in proposed_moves:
                o = proposed_moves[d]
                elf_positions.remove(o)
                elf_positions.add(d)


        maxes = [-9999, -9999]
        mins = [9999, 9999]

        for x, y in elf_positions:
            maxes[0] = max(maxes[0], x)
            maxes[1] = max(maxes[1], y)
            mins[0] = min(mins[0], x)
            mins[1] = min(mins[1], y)

        AREA = (maxes[0] - mins[0] + 1) * (maxes[1] - mins[1] + 1)
        print(AREA - len(elf_positions))


def solution_part2(fname="inputs/day23"):
    with open(fname, "r") as f:
        grid = f.readlines()
        elf_positions: set[tuple[int, int]] = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "#":
                    elf_positions.add((j, len(grid) - i - 1))

        N = 0
        while True:
            # proposed dest, origin
            proposed_moves: dict[tuple[int, int], tuple[int, int]] = {}
            rejected_moves: set[tuple[int, int]] = set()

            for x, y in elf_positions:
                # SW, W, NW, S, N, SE, E, NE
                neighbors = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
                # Don't move if they have no neighbors
                if all(n not in elf_positions for n in neighbors):
                    continue

                proposed_dest = (0, 0)
                # Check to the first direction
                if all(neighbors[i] not in elf_positions for i in NEIGHBOR_INDICES[N % 4]):
                    proposed_dest = (x + CHANGES[N % 4][0], y + CHANGES[N % 4][1])
                # Check to the second direction
                elif all(neighbors[i] not in elf_positions for i in NEIGHBOR_INDICES[(N + 1) % 4]):
                    proposed_dest = (x + CHANGES[(N + 1) % 4][0], y + CHANGES[(N + 1) % 4][1])
                # Check to the third direction
                elif all(neighbors[i] not in elf_positions for i in NEIGHBOR_INDICES[(N + 2) % 4]):
                    proposed_dest = (x + CHANGES[(N + 2) % 4][0], y + CHANGES[(N + 2) % 4][1])
                # Check to the fourth direction
                elif all(neighbors[i] not in elf_positions for i in NEIGHBOR_INDICES[(N + 3) % 4]):
                    proposed_dest = (x + CHANGES[(N + 3) % 4][0], y + CHANGES[(N + 3) % 4][1])
                else:
                    continue

                if proposed_dest in rejected_moves:
                    continue
                elif proposed_dest in proposed_moves:
                    rejected_moves.add(proposed_dest)
                    proposed_moves.pop(proposed_dest)
                else:
                    proposed_moves[proposed_dest] = (x, y)

            if len(proposed_moves) == 0:
                print(N + 1)
                return

            for d in proposed_moves:
                o = proposed_moves[d]
                elf_positions.remove(o)
                elf_positions.add(d)

            N += 1

solution_part2()
