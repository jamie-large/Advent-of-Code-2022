def solution_part1(fname="inputs/day15"):
    with open(fname, "r") as f:
        TARGET_Y = 2000000

        sensor_map: dict[tuple[int, int], tuple[int, int]] = {}
        y_objects: set[int] = set()
        for line in f:
            spl = line.split()
            sensor_pos = (int(spl[2][2:-1]), int(spl[3][2:-1]))
            closest_beacon = (int(spl[-2][2:-1]), int(spl[-1][2:]))
            sensor_map[sensor_pos] = closest_beacon
            if sensor_pos[1] == TARGET_Y:
                y_objects.add(sensor_pos[0])
            if closest_beacon[1] == TARGET_Y:
                y_objects.add(closest_beacon[0])

        y_positions: set[int] = set()
        for sensor_pos in sensor_map:
            closest_beacon = sensor_map[sensor_pos]
            manhattan_distance = abs(sensor_pos[0] - closest_beacon[0]) + abs(sensor_pos[1] - closest_beacon[1])

            for i in range(sensor_pos[0] - (manhattan_distance - abs(sensor_pos[1] - TARGET_Y)), sensor_pos[0] + (manhattan_distance - abs(sensor_pos[1] - TARGET_Y)) + 1):
                y_positions.add(i)

        for x in y_objects:
            y_positions.remove(x)

        print(len(y_positions))

def solution_part2(fname="inputs/day15"):
    with open(fname, "r") as f:
        B = 4000000

        shapes: dict[tuple[int, int], int] = {}

        for line in f:
            spl = line.split()
            sensor_pos = (int(spl[2][2:-1]), int(spl[3][2:-1]))
            closest_beacon = (int(spl[-2][2:-1]), int(spl[-1][2:]))
            shapes[sensor_pos] = abs(sensor_pos[0] - closest_beacon[0]) + abs(sensor_pos[1] - closest_beacon[1])

        # Check range at each height
        for y in range(B + 1):
            if y % 100000 == 0:
                print(f"y = {y}")
            # Initially, there are none
            x_ranges: list[tuple[int, int]] = []
            for sensor_pos in shapes:
                manhattan_distance = shapes[sensor_pos]
                # The range of where y values are
                x_range = (max(sensor_pos[0] - (manhattan_distance - abs(sensor_pos[1] - y)), 0),
                           min(sensor_pos[0] + (manhattan_distance - abs(sensor_pos[1] - y)), B))
                if x_range[1] < 0 or x_range[0] > B or x_range[0] > x_range[1]:
                    continue
                i = 0
                while i < len(x_ranges):
                    current_range = x_ranges[i]
                    # If it intersects, update
                    if (x_range[0] >= current_range[0] - 1 and x_range[0] <= current_range[1] + 1) or \
                       (x_range[1] >= current_range[0] - 1 and x_range[1] <= current_range[1] + 1) or \
                       (current_range[1] >= x_range[0] - 1 and current_range[1] <= x_range[1] + 1) or \
                       (current_range[0] >= x_range[0] - 1 and current_range[0] <= x_range[1] + 1):
                        x_range = (min(x_range[0], current_range[0]), max(x_range[1], current_range[1]))
                        x_ranges.pop(i)
                    else:
                        i += 1
                if x_range == (0, B):
                    break
                x_ranges.append(x_range)
            else:
                x_val = x_ranges[0][1] + 1 if x_ranges[0][1] < B else x_ranges[1][1] + 1
                print(x_val * 4000000 + y)
                return

solution_part2()
