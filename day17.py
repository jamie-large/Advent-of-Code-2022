class Rock:
    def __init__(self, type: int):
        self.type = type

    # Given position of bottom left corner, determine whether it can move in the grid
    def can_move(self, direction: str, grid: list[list[str]], position: tuple[int, int]):
        x, y = position
        # @@@@
        if self.type == 0:
            if direction == ">":
                return x <= 2 and grid[y][x+4] == "."
            elif direction == "<":
                return x > 0 and grid[y][x-1] == "."
            else:
                return y > 0 and all(grid[y-1][i] == "." for i in range(x, x+4))
        # .@.
        # @@@
        # .@.
        elif self.type == 1:
            if direction == ">":
                return x <= 3 and grid[y][x+2] == "." and grid[y+1][x+3] == "." and grid[y+2][x+2] == "."
            elif direction == "<":
                return x > 0 and grid[y][x] == "." and grid[y+1][x-1] == "." and grid[y+2][x] == "."
            else:
                return y > 0 and grid[y][x] == "." and grid[y-1][x+1] == "." and grid[y][x+2] == "."
        # ..@
        # ..@
        # @@@
        elif self.type == 2:
            if direction == ">":
                return x <= 3 and all(grid[i][x+3] == "." for i in range(y, y+3))
            elif direction == "<":
                return x > 0 and grid[y][x-1] == "." and grid[y+1][x+1] == "." and grid[y+2][x+1] == "."
            else:
                return y > 0 and all(grid[y-1][i] == "." for i in range(x, x+3))
        # @
        # @
        # @
        # @
        elif self.type == 3:
            if direction == ">":
                return x <= 5 and all(grid[i][x+1] == "." for i in range(y, y+4))
            elif direction == "<":
                return x > 0 and all(grid[i][x-1] == "." for i in range(y, y+4))
            else:
                return y > 0 and grid[y-1][x] == "."
        # @@
        # @@
        elif self.type == 4:
            if direction == ">":
                return x <= 4 and all(grid[i][x+2] == "." for i in range(y, y+2))
            elif direction == "<":
                return x > 0 and all(grid[i][x-1] == "." for i in range(y, y+2))
            else:
                return y > 0 and all(grid[y-1][i] == "." for i in range(x, x+2))

    # Given position of bottom left corner, draws it onto the grid, returns max height of rocks on grid
    def draw(self, grid: list[list[str]], position: tuple[int, int]):
        x, y = position
        max_height = 0
        if self.type == 0:
            max_height = max(max_height, y)
            for i in range(x, x+4):
                grid[y][i] = "#"
        elif self.type == 1:
            max_height = max(max_height, y+2)
            grid[y][x+1] = "#"
            for i in range(x, x+3):
                grid[y+1][i] = "#"
            grid[y+2][x+1] = "#"
        elif self.type == 2:
            max_height = max(max_height, y+2)
            for i in range(x, x+3):
                grid[y][i] = "#"
            grid[y+1][x+2] = "#"
            grid[y+2][x+2] = "#"
        elif self.type == 3:
            max_height = max(max_height, y+3)
            for i in range(y, y+4):
                grid[i][x] = "#"
        elif self.type == 4:
            print(f"DRAWING AT {(x, y)}")
            max_height = max(max_height, y+1)
            for i in range(x, x+2):
                for j in range(y, y+2):
                    grid[j][i] = "#"
        return max_height

    def draw_2(self, grid: list[list[str]], position: tuple[int, int], max_heights: list[int]):
        x, y = position
        if self.type == 0:
            for i in range(x, x+4):
                grid[y][i] = "#"
                max_heights[i] = max(max_heights[i], y)
        elif self.type == 1:
            grid[y][x+1] = "#"
            for i in range(x, x+3):
                grid[y+1][i] = "#"
            grid[y+2][x+1] = "#"
            max_heights[x] = max(max_heights[x], y+1)
            max_heights[x+1] = max(max_heights[x+1], y+2)
            max_heights[x+2] = max(max_heights[x+2], y+1)
        elif self.type == 2:
            for i in range(x, x + 3):
                grid[y][i] = "#"
            grid[y+1][x+2] = "#"
            grid[y+2][x+2] = "#"
            max_heights[x] = max(max_heights[x], y)
            max_heights[x+1] = max(max_heights[x+1], y)
            max_heights[x+2] = max(max_heights[x+2], y+2)
        elif self.type == 3:
            for i in range(y, y + 4):
                grid[i][x] = "#"
            max_heights[x] = max(max_heights[x], y+3)
        elif self.type == 4:
            for i in range(x, x+2):
                for j in range(y, y+2):
                    grid[j][i] = "#"
                max_heights[i] = max(max_heights[i], y+1)
        return max_heights

def solution_part1(fname="inputs/day17"):
    with open(fname, "r") as f:
        directions = f.readline()[:-1]
        direction_i = 0
        rocks = [Rock(i) for i in range(5)]
        rock_i = 0

        grid = [["." for _ in range(7)] for _ in range(7)]
        max_height = -1

        for _ in range(2022):
            rock = rocks[rock_i]
            rock_i = (rock_i + 1) % len(rocks)
            position = (2, max_height + 4)

            while position[1] + 4 > len(grid):
                grid.append(["." for _ in range(7)])

            while True:
                direction = directions[direction_i]
                direction_i = (direction_i + 1) % len(directions)
                # try to move right/left
                if rock.can_move(direction, grid, position):
                    position = (position[0] + (1 if direction == ">" else -1), position[1])
                # try to move down
                if rock.can_move("d", grid, position):
                    position = (position[0], position[1] - 1)
                else:
                    break

            max_height = max(max_height, rock.draw(grid, position))

            # for i in range(len(grid) - 1, -1, -1):
            #     print("|" + "".join(grid[i]) + "|")
            # print("---------")
            # print()
        print(max_height + 1)

def solution_part2(fname="inputs/day17"):
    with open(fname, "r") as f:
        NUM_TURNS = 1000000000000
        directions = f.readline()[:-1]
        direction_i = 0
        rocks = [Rock(i) for i in range(5)]
        rock_i = 0

        grid = [["." for _ in range(7)] for _ in range(7)]
        max_heights = [-1, -1, -1, -1, -1, -1, -1]
        max_height = -1

        # repeat until find a repeating sequence, figure out how much height it gains/how many steps it took
        # dict of tuple of (bottom relative heights, direction_i, rock_i) to tuple of (turn #, max_height)
        states: dict[tuple[tuple[int, int, int, int, int, int, int], int, int], tuple[int, int]] = {}
        turn = 0

        while True:
            min_height = min(max_heights)
            relative_heights = tuple([x - min_height for x in max_heights])

            if turn == NUM_TURNS:
                print(max_height + 1)
                return

            if (relative_heights, direction_i, rock_i) in states:
                # figure out how much it increased and how many turns it took
                original_turn, original_height = states[(relative_heights, direction_i, rock_i)]
                turn_increase = turn - original_turn
                height_increase = max_height - original_height
                # figure out how many times this is going to happen
                turns_remaining = NUM_TURNS - turn
                num_repeats = int(turns_remaining / turn_increase)

                # figure out the offset
                turn_offset = turns_remaining % turn_increase
                for x in states:
                    if states[x][0] == original_turn + turn_offset:
                        # Return final height
                        # Height to reach repeating state + (n_repeats * height per repeat) + height to reach final turn + 1
                        print(max_height + (num_repeats * height_increase) + states[x][1] - original_height + 1)
                        return

            states[(relative_heights, direction_i, rock_i)] = (turn, max_height)

            rock = rocks[rock_i]
            rock_i = (rock_i + 1) % len(rocks)
            position = (2, max_height + 4)

            while position[1] + 4 > len(grid):
                grid.append(["." for _ in range(7)])

            while True:
                direction = directions[direction_i]
                direction_i = (direction_i + 1) % len(directions)
                # try to move right/left
                if rock.can_move(direction, grid, position):
                    position = (position[0] + (1 if direction == ">" else -1), position[1])
                # try to move down
                if rock.can_move("d", grid, position):
                    position = (position[0], position[1] - 1)
                else:
                    break

            max_heights = rock.draw_2(grid, position, max_heights)
            max_height = max(max_heights)

            # for i in range(len(grid) - 1, -1, -1):
            #     print("|" + "".join(grid[i]) + "|")
            # print("---------")
            # print()

            turn += 1



solution_part2("inputs/test")
