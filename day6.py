def solution_part1(fname="inputs/day6"):
    with open(fname, "r") as f:
        last_seen_dict: dict[str, int] = {}
        last_seen: list[str] = []
        i: int = 1
        for c in f.readline():
            if len(last_seen) < 3:
                pass
            elif c not in last_seen_dict and all([x == 1 for x in last_seen_dict.values()]):
                print(i)
                return
            else:
                if last_seen_dict[last_seen[0]] == 1:
                    last_seen_dict.pop(last_seen[0])
                else:
                    last_seen_dict[last_seen[0]] -= 1
                last_seen.pop(0)

            last_seen.append(c)
            last_seen_dict[c] = last_seen_dict.get(c, 0) + 1
            i += 1



def solution_part2(fname="inputs/day6"):
    with open(fname, "r") as f:
        last_seen_dict: dict[str, int] = {}
        last_seen: list[str] = []
        i: int = 1
        for c in f.readline():
            if len(last_seen) < 13:
                pass
            elif c not in last_seen_dict and all([x == 1 for x in last_seen_dict.values()]):
                print(i)
                return
            else:
                if last_seen_dict[last_seen[0]] == 1:
                    last_seen_dict.pop(last_seen[0])
                else:
                    last_seen_dict[last_seen[0]] -= 1
                last_seen.pop(0)

            last_seen.append(c)
            last_seen_dict[c] = last_seen_dict.get(c, 0) + 1
            i += 1


solution_part2()
