def solution_part1(fname="inputs/day9"):
    with open(fname, "r") as f:
        head_pos = (0, 0)
        tail_pos = (0, 0)
        tail_positions = set([tail_pos])
        for line in f:
            [direction, steps] = line.split()
            steps = int(steps)
            if direction == "R":
                for _ in range(1, steps + 1):
                    head_pos = (head_pos[0] + 1, head_pos[1])
                    if head_pos[0] - tail_pos[0] > 1:
                        tail_pos = (head_pos[0] - 1, head_pos[1])
                    tail_positions.add(tail_pos)
            elif direction == "L":
                for _ in range(1, steps + 1):
                    head_pos = (head_pos[0] - 1, head_pos[1])
                    if tail_pos[0] - head_pos[0] > 1:
                        tail_pos = (head_pos[0] + 1, head_pos[1])
                    tail_positions.add(tail_pos)
            elif direction == "U":
                for _ in range(1, steps + 1):
                    head_pos = (head_pos[0], head_pos[1] + 1)
                    if head_pos[1] - tail_pos[1] > 1:
                        tail_pos = (head_pos[0], head_pos[1] - 1)
                    tail_positions.add(tail_pos)
            elif direction == "D":
                for _ in range(1, steps + 1):
                    head_pos = (head_pos[0], head_pos[1] - 1)
                    if tail_pos[1] - head_pos[1] > 1:
                        tail_pos = (head_pos[0], head_pos[1] + 1)
                    tail_positions.add(tail_pos)
        print(len(tail_positions))

def solution_part2(fname="inputs/day9"):
    with open(fname, "r") as f:
        rope_positions = [(0, 0)] * 10
        tail_positions = set([(0, 0)])
        for line in f:
            [direction, steps] = line.split()
            steps = int(steps)
            for _ in range(1, steps + 1):
                if direction == "R":
                    rope_positions[0] = (rope_positions[0][0] + 1, rope_positions[0][1])
                elif direction == "L":
                    rope_positions[0] = (rope_positions[0][0] - 1, rope_positions[0][1])
                elif direction == "U":
                    rope_positions[0] = (rope_positions[0][0], rope_positions[0][1] + 1)
                elif direction == "D":
                    rope_positions[0] = (rope_positions[0][0], rope_positions[0][1] - 1)
                for i in range(1, len(rope_positions)):
                    x, y  = rope_positions[i]
                    if abs(rope_positions[i][0] - rope_positions[i-1][0]) > 1 and abs(rope_positions[i][1] - rope_positions[i-1][1]) > 1:
                        x = rope_positions[i][0] + (1 if rope_positions[i][0] < rope_positions[i-1][0] else -1)
                        y = rope_positions[i][1] + (1 if rope_positions[i][1] < rope_positions[i-1][1] else -1)
                        rope_positions[i] = (x, y)
                    elif abs(rope_positions[i][0] - rope_positions[i-1][0]) > 1:
                        x = rope_positions[i][0] + (1 if rope_positions[i][0] < rope_positions[i-1][0] else -1)
                        y = rope_positions[i-1][1]
                        rope_positions[i] = (x, y)
                    elif abs(rope_positions[i][1] - rope_positions[i-1][1]) > 1:
                        x = rope_positions[i-1][0]
                        y = rope_positions[i][1] + (1 if rope_positions[i][1] < rope_positions[i-1][1] else -1)
                        rope_positions[i] = (x, y)
                    else:
                        break
                tail_positions.add(rope_positions[-1])
        print(len(tail_positions))

solution_part2()
