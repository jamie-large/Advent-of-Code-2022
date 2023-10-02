class Valve:
    def __init__(self, name: str, flow: int, paths: list[str]):
        self.name = name
        self.flow = flow
        self.paths = paths

    def __repr__(self):
        return f"Valve {self.name}=> flow: {self.flow}, paths: {self.paths}"

def solution_part1(fname="inputs/day16"):
    with open(fname, "r") as f:
        valves: dict[str, Valve] = {}

        for line in f:
            spl = line.split()
            valves[spl[1]] = Valve(spl[1], int(spl[4][5:-1]), [x[:-1] for x in spl[9:-1]] + [spl[-1]])

        min_distances: dict[tuple[str, str], int] = {}

        for v in valves:
            queue: list[tuple(str, int)] = [(v, 0)]
            dont_search: set[str] = set([v])

            while len(queue) > 0:
                current, steps = queue.pop(0)

                min_distances[(v, current)] = min_distances[(current, v)] = steps

                for n in valves[current].paths:
                    if n not in dont_search:
                        queue.append((n, steps + 1))
                        dont_search.add(n)

        final_queue: list[tuple[str, int, dict[str, int]]] = [("AA", 0, {})]

        ending_paths: list[dict[str, int]] = []

        while len(final_queue) > 0:
            name, time, path = final_queue.pop(0)

            found_next = False

            # calculate all the next possible moves
            for v in valves:
                if v != name and v not in path and valves[v].flow > 0 and (name, v) in min_distances:
                    travel_distance = time + min_distances[(name, v)] + 1
                    if travel_distance > 30:
                        continue
                    found_next = True
                    new_path = path.copy()
                    new_path[v] = travel_distance

                    final_queue.append((v, travel_distance, new_path))

            if not found_next:
                ending_paths.append(path)

        best_score = 0
        best_path: dict[str, int] = {}
        for p in ending_paths:
            score = 0
            for v in p:
                score += valves[v].flow * (30 - p[v])
            if score > best_score:
                best_score = score
                best_path = p

        print(best_score)

def solution_part2(fname="inputs/day16"):
    with open(fname, "r") as f:
        valves: dict[str, Valve] = {}

        for line in f:
            spl = line.split()
            valves[spl[1]] = Valve(spl[1], int(spl[4][5:-1]), [x[:-1] for x in spl[9:-1]] + [spl[-1]])

        min_distances: dict[tuple[str, str], int] = {}

        for v in valves:
            queue: list[tuple(str, int)] = [(v, 0)]
            dont_search: set[str] = set([v])

            while len(queue) > 0:
                current, steps = queue.pop(0)

                min_distances[(v, current)] = min_distances[(current, v)] = steps

                for n in valves[current].paths:
                    if n not in dont_search:
                        queue.append((n, steps + 1))
                        dont_search.add(n)

        active_valves = [v for v in valves if valves[v].flow > 0]

        # Figure out all possible paths for 1 agent in 26 minutes

        final_queue: list[tuple[str, int, dict[str, int]]] = [("AA", 0, {})]

        all_paths: list[dict[str, int]] = []

        while len(final_queue) > 0:
            name, time, path = final_queue.pop(0)
            all_paths.append(path)

            for v in active_valves:
                if v != name and v not in path and (name, v) in min_distances:
                    travel_distance = time + min_distances[(name, v)] + 1
                    if travel_distance > 26:
                        continue
                    new_path = path.copy()
                    new_path[v] = travel_distance

                    final_queue.append((v, travel_distance, new_path))

        # Figure out value of the best route through each possible path
        best_paths: dict[str, int] = {}
        path_sets: dict[str, set[str]] = {}
        for p in all_paths:
            path_name = stringify_path(p)
            val = calculate_path_value(p, valves)
            if path_name not in path_sets:
                path_sets[path_name] = set(p.keys())
            if val > best_paths.get(path_name, 0):
                best_paths[path_name] = val

        # Find the best combination of paths
        path_names = list(best_paths.keys())
        result = 0
        for i in range(len(path_names)):
            for j in range(i+1, len(path_names)):
                if intersects(path_sets[path_names[i]], path_sets[path_names[j]]):
                    continue
                val = best_paths[path_names[i]] + best_paths[path_names[j]]
                if val > result:
                    result = val
        print(result)

def stringify_path(path: dict[str, int]):
    nodes = [p for p in path]
    nodes.sort()
    return "".join(nodes)

def calculate_path_value(path: dict[str, int], valves: dict[str, Valve]):
    return sum([valves[v].flow * (26 - path[v]) for v in path])

def intersects(s1: set, s2: set):
    shorter = s1 if len(s1) < len(s2) else s2
    longer = s1 if len(s1) >= len(s2) else s2
    for item in shorter:
        if item in longer:
            return True

    return False

solution_part2()
