def solution_part1(fname="inputs/day8"):
    with open(fname, "r") as f:
        grid: list[list[int]] = [[int(c) for c in line[:-1]] for line in f.readlines()]
        visible: list[list[bool]] = [[False for _ in range(len(x))] for x in grid]
        for i in range(len(grid)):
            visible[0][i] = True
            visible[-1][i] = True
            visible[i][0] = True
            visible[i][-1] = True

        # Find the ones visible to the left/right
        for i in range(1, len(grid) - 1):
            current_max = grid[i][0]
            for j in range(1, len(grid[i]) - 1):
                if grid[i][j] > current_max:
                    visible[i][j] = True
                    current_max = grid[i][j]
                if current_max == 9:
                    break

            current_max = grid[i][-1]
            for j in range(len(grid[i]) - 1, 0, -1):
                if grid[i][j] > current_max:
                    visible[i][j] = True
                    current_max = grid[i][j]
                if current_max == 9:
                    break

        # find the ones visible to the top/bottom
        for j in range(1, len(grid[0]) - 1):
            current_max = grid[0][j]
            for i in range(1, len(grid) - 1):
                if grid[i][j] > current_max:
                    visible[i][j] = True
                    current_max = grid[i][j]
                if current_max == 9:
                    break

            current_max = grid[-1][j]
            for i in range(len(grid) - 1, 0, -1):
                if grid[i][j] > current_max:
                    visible[i][j] = True
                    current_max = grid[i][j]
                if current_max == 9:
                    break

        print(sum([sum(x) for x in visible]))

def solution_part2(fname="inputs/day8"):
    with open(fname, "r") as f:
        grid: list[list[int]] = [[int(c) for c in line[:-1]] for line in f.readlines()]
        visible_to_left: list[list[int]] = [[0 for _ in range(len(x))] for x in grid]
        visible_to_right: list[list[int]] = [[0 for _ in range(len(x))] for x in grid]
        visible_above: list[list[int]] = [[0 for _ in range(len(x))] for x in grid]
        visible_below: list[list[int]] = [[0 for _ in range(len(x))] for x in grid]

        # calculate to left/right
        for i in range(len(grid)):
            for j in range(1, len(grid[i])):
                if grid[i][j] <= grid[i][j-1]:
                    visible_to_left[i][j] = 1
                else:
                    visible_to_left[i][j] = visible_to_left[i][j-1] + 1
                    k = j - visible_to_left[i][j]
                    while k > 0 and grid[i][j] > grid[i][k]:
                        visible_to_left[i][j] += visible_to_left[i][k]
                        k -= visible_to_left[i][k]

            for j in range(len(grid[i]) - 2, -1, -1):
                if grid[i][j] <= grid[i][j+1]:
                    visible_to_right[i][j] = 1
                else:
                    visible_to_right[i][j] = visible_to_right[i][j+1] + 1
                    k = j + visible_to_right[i][j]
                    while k < len(grid[i]) - 1 and grid[i][j] > grid[i][k]:
                        visible_to_right[i][j] += visible_to_right[i][k]
                        k += visible_to_right[i][k]

        # calculate above/below
        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                if grid[i][j] <= grid[i-1][j]:
                    visible_above[i][j] = 1
                else:
                    visible_above[i][j] = visible_above[i-1][j] + 1
                    k = i - visible_above[i][j]
                    while k > 0 and grid[i][j] > grid[k][j]:
                        visible_above[i][j] += visible_above[k][j]
                        k -= visible_above[k][j]

            for i in range(len(grid) - 2, -1, -1):
                if grid[i][j] <= grid[i+1][j]:
                    visible_below[i][j] = 1
                else:
                    visible_below[i][j] = visible_below[i+1][j] + 1
                    k = i + visible_below[i][j]
                    while k < len(grid) - 1 and grid[i][j] > grid[k][j]:
                        visible_below[i][j] += visible_below[k][j]
                        k += visible_below[k][j]

        print(max([visible_to_left[i][j] * visible_to_right[i][j] * visible_above[i][j] * visible_below[i][j] for j in range(len(grid[i])) for i in range(len(grid))]))

solution_part2()
