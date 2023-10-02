from math import ceil
# (Ore)-> ore, (ore)-> clay, (ore, clay)-> obsidian, (ore, obsidian)-> geode
Recipe = tuple[int, int, int, int, int, int]
# Ore, Clay, Obsidian, Geode
Materials = Robots = tuple[int, int, int, int]

def calculate_best(recipe: Recipe, total_time: int):
    result: int = 0
    stack: list[tuple[Materials, Robots, int]] = [((0,0,0,0), (1,0,0,0), 0)]

    while len(stack) > 0:
        materials, robots, minute = stack.pop(-1)

        # Calculate maximum possible geodes it could produce
        max_possible = materials[3]
        for i in range(minute + 1, total_time + 1):
            max_possible += (robots[3] + i - minute - 1)
        if max_possible <= result:
            continue

        result = max(result, materials[3] + (total_time - minute) * robots[3])

        if minute == total_time:
            continue

        # Buy an ore robot if possible
        time_remaining = (0 if materials[0] >= recipe[0] else ceil((recipe[0] - materials[0]) / robots[0])) + 1
        if minute + time_remaining <= total_time:
            new_materials = [materials[i] + robots[i] * time_remaining for i in range(4)]
            new_materials[0] -= recipe[0]
            new_robots = (robots[0] + 1,) + robots[1:]
            stack.append((tuple(new_materials), new_robots, minute + time_remaining))

        # Buy a clay robot if possible
        time_remaining = (0 if materials[0] >= recipe[1] else ceil((recipe[1] - materials[0]) / robots[0])) + 1
        if minute + time_remaining <= total_time:
            new_materials = [materials[i] + robots[i] * time_remaining for i in range(4)]
            new_materials[0] -= recipe[1]
            new_robots = (robots[0], robots[1] + 1) + robots[2:]
            stack.append((tuple(new_materials), new_robots, minute + time_remaining))

        # Buy an obsidian robot if possible
        if robots[1] > 0:
            time_remaining = max(
                                 0 if materials[0] >= recipe[2] else ceil((recipe[2] - materials[0]) / robots[0]),
                                 0 if materials[1] >= recipe[3] else ceil((recipe[3] - materials[1]) / robots[1])
                                ) + 1
            if minute + time_remaining <= total_time:
                new_materials = [materials[i] + robots[i] * time_remaining for i in range(4)]
                new_materials[0] -= recipe[2]
                new_materials[1] -= recipe[3]
                new_robots = robots[:2] + (robots[2] + 1, robots[3])
                stack.append((tuple(new_materials), new_robots, minute + time_remaining))

        # Buy a geode robot if possible
        if robots[2] > 0:
            time_remaining = max(
                                 0 if materials[0] >= recipe[4] else ceil((recipe[4] - materials[0]) / robots[0]),
                                 0 if materials[2] >= recipe[5] else ceil((recipe[5] - materials[2]) / robots[2])
                                ) + 1
            if minute + time_remaining <= total_time:
                new_materials = [materials[i] + robots[i] * time_remaining for i in range(4)]
                new_materials[0] -= recipe[4]
                new_materials[2] -= recipe[5]
                new_robots = robots[:3] + (robots[3] + 1,)
                stack.append((tuple(new_materials), new_robots, minute + time_remaining))
    return result


def solution_part1(fname="inputs/day19"):
    with open(fname, "r") as f:
        # (ore)-> ore, (ore)-> clay, (ore, clay)-> obsidian, (ore, obsidian)-> geode
        recipes: list[Recipe] = []
        for line in f:
            recipes.append(tuple([int(word) for word in line.split() if word.isnumeric()]))

        result = 0
        for N in range(len(recipes)):
            result += calculate_best(recipes[N], 24) * (N + 1)
        print(result)

def solution_part2(fname="inputs/day19"):
    with open(fname, "r") as f:
        # (ore)-> ore, (ore)-> clay, (ore, clay)-> obsidian, (ore, obsidian)-> geode
        recipes: list[Recipe] = []
        for line in f:
            recipes.append(tuple([int(word) for word in line.split() if word.isnumeric()]))

        recipes = recipes[:3]

        result = 1
        for recipe in recipes:
            result *= calculate_best(recipe, 32)

        print(result)


solution_part2()
