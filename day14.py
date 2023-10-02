def solution_part1(fname="inputs/day14"):
    with open(fname, "r") as f:
        grid = {}
        for line in f:
            points = [[int(x) for x in p.split(",")] for p in line.split("->")]
            for i in range(1, len(points)):
                for j in range(min(points[i-1][0], points[i][0]), max(points[i-1][0], points[i][0]) + 1):
                    for k in range(min(points[i-1][1], points[i][1]), max(points[i-1][1], points[i][1]) + 1):
                        grid[(j, k)] = "#"
        max_y = max([p[1] for p in grid])

        sand_dispensed = 0
        while True:
            sand_pos = (500, 0)
            while True:
                if sand_pos[1] > max_y:
                    print(sand_dispensed)
                    return
                elif (sand_pos[0], sand_pos[1] + 1) not in grid:
                    sand_pos = (sand_pos[0], sand_pos[1] + 1)
                elif (sand_pos[0] - 1, sand_pos[1] + 1) not in grid:
                    sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)
                elif (sand_pos[0] + 1, sand_pos[1] + 1) not in grid:
                    sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
                else:
                    grid[sand_pos] = "o"
                    break
            sand_dispensed += 1

def solution_part2(fname="inputs/day14"):
    with open(fname, "r") as f:
        grid = {}
        for line in f:
            points = [[int(x) for x in p.split(",")] for p in line.split("->")]
            for i in range(1, len(points)):
                for j in range(min(points[i-1][0], points[i][0]), max(points[i-1][0], points[i][0]) + 1):
                    for k in range(min(points[i-1][1], points[i][1]), max(points[i-1][1], points[i][1]) + 1):
                        grid[(j, k)] = "#"
        max_y = max([p[1] for p in grid])

        sand_dispensed = 0
        while True:
            sand_pos = (500, 0)
            while True:
                if sand_pos[1] == max_y + 1:
                    grid[sand_pos] = "o"
                    break
                elif (sand_pos[0], sand_pos[1] + 1) not in grid:
                    sand_pos = (sand_pos[0], sand_pos[1] + 1)
                elif (sand_pos[0] - 1, sand_pos[1] + 1) not in grid:
                    sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)
                elif (sand_pos[0] + 1, sand_pos[1] + 1) not in grid:
                    sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
                elif sand_pos == (500, 0):
                    print(sand_dispensed + 1)
                    return
                else:
                    grid[sand_pos] = "o"
                    break

            sand_dispensed += 1

solution_part2()
