class Node:
    def __init__(self, value: int):
        self.value = value
        self.previous: Node | None = None
        self.next: Node | None = None

    def __repr__(self):
        return f"Value: {self.value}, Previous: {self.previous.value}, Next: {self.next.value}"

def solution_part1(fname="inputs/day20"):
    with open(fname, "r") as f:
        nodes: list[Node] = []
        node_0: Node | None = None
        for line in f:
            value = int(line)
            if value == 0:
                node_0 = Node(value)
                nodes.append(node_0)
                continue
            nodes.append(Node(value))

        for i in range(len(nodes)):
            nodes[i].previous = nodes[i-1]
            nodes[i].next = nodes[i+1] if i < len(nodes) - 1 else nodes[0]

        for i in range(len(nodes)):
            current_node = nodes[i]
            current_node.previous.next = current_node.next
            current_node.next.previous = current_node.previous

            moves = current_node.value % (len(nodes) - 1)
            for _ in range(moves):
                current_node.next = current_node.next.next

            current_node.previous = current_node.next.previous
            current_node.next.previous = current_node
            current_node.previous.next = current_node

        result = 0
        current = node_0
        for i in range(3000):
            current = current.next
            if i == 999 or i == 1999 or i == 2999:
                result += current.value

        print(result)



def solution_part2(fname="inputs/day20"):
    with open(fname, "r") as f:
        nodes: list[Node] = []
        node_0: Node | None = None
        for line in f:
            value = int(line) * 811589153
            if value == 0:
                node_0 = Node(value)
                nodes.append(node_0)
                continue
            nodes.append(Node(value))

        for i in range(len(nodes)):
            nodes[i].previous = nodes[i-1]
            nodes[i].next = nodes[i+1] if i < len(nodes) - 1 else nodes[0]

        for _ in range(10):
            for i in range(len(nodes)):
                current_node = nodes[i]
                current_node.previous.next = current_node.next
                current_node.next.previous = current_node.previous

                moves = current_node.value % (len(nodes) - 1)
                for _ in range(moves):
                    current_node.next = current_node.next.next

                current_node.previous = current_node.next.previous
                current_node.next.previous = current_node
                current_node.previous.next = current_node

        result = 0
        current = node_0
        for i in range(3000):
            current = current.next
            if i == 999 or i == 1999 or i == 2999:
                result += current.value

        print(result)


solution_part2()
