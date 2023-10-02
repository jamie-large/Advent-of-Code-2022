class Node:
    def __init__(self, name: str, parent, size: int = -1):
        self.name: str = name
        self.parent: Node = parent
        self.size: int = size
        self.children: dict[str, Node] = {}
        self.files: list[Node] = []

def solution_part1(fname="inputs/day7"):
    with open(fname, "r") as f:
        tree: Node = Node("/", None)
        current_dir: Node = tree
        for line in f:
            if line[0] == "$":
                sp = line[1:].split()
                if sp[0] == "ls":
                    continue
                elif sp[0] == "cd":
                    if sp[1] == "/":
                        current_dir = tree
                    elif sp[1] == "..":
                        current_dir = current_dir.parent if current_dir.name != "/" else tree
                    else:
                        if sp[1] not in current_dir.children:
                            current_dir.children[sp[1]] = Node(sp[1], current_dir)
                        current_dir = current_dir.children[sp[1]]
            else:
                [size, name] = line.split()
                if size == "dir":
                    if name not in current_dir.children:
                        current_dir.children[name] = Node(name, current_dir)
                else:
                    current_dir.files.append(Node(name, current_dir, int(size)))

        calculate_size(tree)
        print(find_solution(tree))

def calculate_size(current: Node):
    if current.size > -1:
        return current.size
    s = 0
    for f in current.files:
        s += f.size
    for c in current.children:
        s += calculate_size(current.children[c])
    current.size = s
    return s

def find_solution(current: Node):
    s = current.size if current.size <= 100000 else 0
    for c in current.children:
        s += find_solution(current.children[c])
    return s

def printer(current: Node, depth = 0):
    print(f"{'  ' * depth} dir {current.name}: {current.size}")
    for d in current.children:
        printer(current.children[d], depth + 1)
    for f in current.files:
        print(f"{'  ' * (depth + 1)} file {f.name}: {f.size}")

def solution_part2(fname="inputs/day7"):
    with open(fname, "r") as f:
        tree: Node = Node("/", None)
        current_dir: Node = tree
        for line in f:
            if line[0] == "$":
                sp = line[1:].split()
                if sp[0] == "ls":
                    continue
                elif sp[0] == "cd":
                    if sp[1] == "/":
                        current_dir = tree
                    elif sp[1] == "..":
                        current_dir = current_dir.parent if current_dir.name != "/" else tree
                    else:
                        if sp[1] not in current_dir.children:
                            current_dir.children[sp[1]] = Node(sp[1], current_dir)
                        current_dir = current_dir.children[sp[1]]
            else:
                [size, name] = line.split()
                if size == "dir":
                    if name not in current_dir.children:
                        current_dir.children[name] = Node(name, current_dir)
                else:
                    current_dir.files.append(Node(name, current_dir, int(size)))

        calculate_size(tree)
        print(find_solution_2(tree, 30000000 - (70000000 - tree.size), 300000000))

def find_solution_2(current: Node, target: int, current_best: int):
    sol = current.size if current.size < current_best and current.size >= target else current_best
    for c in current.children:
        c_val = find_solution_2(current.children[c], target, sol)
        sol = c_val if c_val < current_best and c_val >= target else sol
    return sol


solution_part2()
