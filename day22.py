DIRECTIONS = [">", "v", "<", "^"]

def solution_part1(fname="inputs/day22"):
    with open(fname, "r") as f:
        grid = [line[:-1] for line in f.readlines()]
        instructions = grid.pop()
        grid.pop()
        max_len = max([len(line) for line in grid])
        grid = [line + (" " * (max_len - len(line))) for line in grid]

        position = (0,[i for i in range(len(grid[0])) if grid[0][i] == "."][0])
        facing = ">"

        c_i = 0

        while c_i < len(instructions):
            str_buff = []
            while c_i < len(instructions) and instructions[c_i].isnumeric():
                str_buff.append(instructions[c_i])
                c_i += 1
            num = int("".join(str_buff))
            rot = 0 if c_i == len(instructions) else 1 if instructions[c_i] == "R" else -1
            c_i += 1

            # Move as many steps as possible
            for _ in range(num):
                if facing == ">" or facing == "<":
                    change = 1 if facing == ">" else -1
                    new_position_1 = (position[1] + change) % len(grid[position[0]])
                    while grid[position[0]][new_position_1] == " ":
                        new_position_1 = (new_position_1 + change) % len(grid[position[0]])
                    if grid[position[0]][new_position_1] == "#":
                        break
                    position = (position[0], new_position_1)
                elif facing == "v" or facing == "^":
                    change = 1 if facing == "v" else -1
                    new_position_0 = (position[0] + change) % len(grid)
                    while grid[new_position_0][position[1]] == " ":
                        new_position_0 = (new_position_0 + change) % len(grid)
                    if grid[new_position_0][position[1]] == "#":
                        break
                    position = (new_position_0, position[1])
            # rotate
            facing = DIRECTIONS[(DIRECTIONS.index(facing) + rot) % 4]

        print(1000 * (position[0] + 1) + 4 * (position[1] + 1) + DIRECTIONS.index(facing))

class Node:
    def __init__(self, symbol: str, position: tuple[int, int]):
        self.symbol = symbol
        self.position = position
        # (Node, new direction)
        self.left: tuple[Node, str] = (self, "x")
        self.right: tuple[Node, str] = (self, "x")
        self.up: tuple[Node, str] | None = (self, "x")
        self.down: tuple[Node, str] | None = (self, "x")

def solution_part2(fname="inputs/day22"):
    with open(fname, "r") as f:
        grid = [line[:-1] for line in f.readlines()]
        instructions = grid.pop()
        grid.pop()

        nodes: dict[tuple(int, int), Node] = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in ("#", "."):
                    nodes[(i, j)] = Node(grid[i][j], (i, j))
                    if (i-1, j) in nodes:
                        nodes[(i, j)].up = (nodes[(i-1, j)], "^")
                        nodes[(i-1, j)].down = (nodes[(i, j)], "v")
                    if (i, j-1) in nodes:
                        nodes[(i, j)].left = (nodes[(i, j-1)], "<")
                        nodes[(i, j-1)].right = (nodes[(i, j)], ">")

        # MANUALLY ADD IN THE EDGES OF THE CUBE
        for i in range(50):
            nodes[(50 + i, 50)].left = (nodes[(100, i)], "v")
            nodes[(100, i)].up = (nodes[(50 + i, 50)], ">")

            nodes[(i, 50)].left = (nodes[(149 - i, 0)], ">")
            nodes[(149 - i, 0)].left = (nodes[(i, 50)], ">")

            nodes[(149, 50 + i)].down = (nodes[(150 + i, 49)], "<")
            nodes[(150 + i, 49)].right = (nodes[(149, 50 + i)], "^")

            nodes[(50 + i, 99)].right = (nodes[(49, 100 + i)], "^")
            nodes[(49, 100 + i)].down = (nodes[(50 + i, 99)], "<")

            nodes[(i, 149)].right = (nodes[(149 - i, 99)], "<")
            nodes[(149 - i, 99)].right = (nodes[(i, 149)], "<")

            nodes[(0, 50 + i)].up = (nodes[(150 + i, 0)], ">")
            nodes[((150 + i, 0))].left = (nodes[(0, 50 + i)], "v")

            nodes[(0, 100 + i)].up = (nodes[(199, i)], "^")
            nodes[(199, i)].down = (nodes[(0, 100 + i)], "v")

        current_node = nodes[(0,[i for i in range(len(grid[0])) if grid[0][i] == "."][0])]
        facing = ">"

        c_i = 0
        while c_i < len(instructions):
            str_buff = []
            while c_i < len(instructions) and instructions[c_i].isnumeric():
                str_buff.append(instructions[c_i])
                c_i += 1
            num = int("".join(str_buff))
            rot = 0 if c_i == len(instructions) else 1 if instructions[c_i] == "R" else -1
            c_i += 1

            # Move as many steps as possible
            for _ in range(num):
                new_node, new_facing = current_node.right if facing == ">" else \
                                       current_node.down if facing == "v" else \
                                       current_node.left if facing == "<" else \
                                       current_node.up
                if new_node.symbol == "#":
                    break
                current_node = new_node
                facing = new_facing

            # rotate
            facing = DIRECTIONS[(DIRECTIONS.index(facing) + rot) % 4]

        position = current_node.position
        print(1000 * (position[0] + 1) + 4 * (position[1] + 1) + DIRECTIONS.index(facing))


solution_part2()
