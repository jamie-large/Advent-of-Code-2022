def solution_part1(fname="inputs/day12"):
    with open(fname, "r") as f:
        grid = [[c for c in line[:-1]] for line in f.readlines()]
        starting_pos = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == "S"][0]
        ending_pos = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == "E"][0]
        grid[starting_pos[0]][starting_pos[1]] = "a"
        grid[ending_pos[0]][ending_pos[1]] = "z"
        grid = [[ord(c) for c in x] for x in grid]

        visited = set()
        pending = set([starting_pos])
        queue = [(starting_pos, 0)]
        while len(queue) > 0:
            current_pos, steps = queue.pop(0)
            pending.remove(current_pos)
            visited.add(current_pos)
            neighbors = [(current_pos[0] + i, current_pos[1] + j) for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)] \
                         if current_pos[0] + i >= 0 and current_pos[0] + i < len(grid) and current_pos[1] + j >= 0 and current_pos[1] + j < len(grid[i])]
            for n in neighbors:
                if n not in visited and n not in pending and grid[n[0]][n[1]] - grid[current_pos[0]][current_pos[1]] <= 1:
                    if n == ending_pos:
                        print(steps + 1)
                        return
                    queue.append((n, steps + 1))
                    pending.add(n)


def solution_part2(fname="inputs/day12"):
    with open(fname, "r") as f:
        grid = [[c for c in line[:-1]] for line in f.readlines()]
        starting_pos = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == "S"][0]
        ending_pos = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == "E"][0]
        grid[starting_pos[0]][starting_pos[1]] = "a"
        grid[ending_pos[0]][ending_pos[1]] = "z"
        grid = [[ord(c) for c in x] for x in grid]

        visited = set()
        pending = set([ending_pos])
        queue = [(ending_pos, 0)]
        while len(queue) > 0:
            current_pos, steps = queue.pop(0)
            pending.remove(current_pos)
            visited.add(current_pos)
            neighbors = [(current_pos[0] + i, current_pos[1] + j) for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)] \
                         if current_pos[0] + i >= 0 and current_pos[0] + i < len(grid) and current_pos[1] + j >= 0 and current_pos[1] + j < len(grid[i])]
            for n in neighbors:
                if n not in visited and n not in pending and grid[current_pos[0]][current_pos[1]] - grid[n[0]][n[1]] <= 1:
                    if grid[n[0]][n[1]] == ord("a"):
                        print(steps + 1)
                        return
                    queue.append((n, steps + 1))
                    pending.add(n)

solution_part2()
