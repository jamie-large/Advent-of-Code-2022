from functools import cmp_to_key
import json

def solution_part1(fname="inputs/day13"):
    with open(fname, "r") as f:
        skip: str = "A"
        i = 1
        result = 0
        while skip:
            first: list[list | int] = json.loads(f.readline())
            second: list[list | int] = json.loads(f.readline())
            skip = f.readline()

            if compare(first, second) == -1:
                result += i

            i += 1
        print(result)


def compare(first: list[list | int], second: list[list | int]):
    first_i = 0
    second_i = 0
    while first_i < len(first) and second_i < len(second):
        left = first[first_i]
        right = second[second_i]
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return -1
            if left > right:
                return 1
        elif isinstance(left, int):
            test = compare([left], right)
            if test != 0:
                return test
        elif isinstance(right, int):
            test = compare(left, [right])
            if test != 0:
                return test
        else:
            test = compare(left, right)
            if test != 0:
                return test
        first_i += 1
        second_i += 1
    # left ran out of items first
    if second_i < len(second):
        return -1
    if first_i < len(first):
        return 1

    return 0

def solution_part2(fname="inputs/day13"):
    with open(fname, "r") as f:
        skip: str = "A"
        all_lists = [[[2]], [[6]]]
        while skip:
            first: list[list | int] = json.loads(f.readline())
            second: list[list | int] = json.loads(f.readline())
            skip = f.readline()

            all_lists.append(first)
            all_lists.append(second)

        sorted_lists = sorted(all_lists, key=cmp_to_key(compare))

        result = 1
        for i in range(len(sorted_lists)):
            if sorted_lists[i] == [[2]]:
                result = i + 1
            if sorted_lists[i] == [[6]]:
                print(result * (i+1))
                return



solution_part2()
