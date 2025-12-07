def find_start_idx(grid):
    for row in grid:
        x_idx = row.index("S")
        if x_idx != -1:
            return x_idx

    return -1


def part1(grid):
    split_count = 0
    tracked_idxs = {find_start_idx(grid)}

    for row in grid:
        to_remove = set()
        to_add = set()

        for idx in tracked_idxs:
            if row[idx] == "^":
                split_count += 1
                to_remove.add(idx)
                to_add.add(idx - 1)
                to_add.add(idx + 1)

        for i in to_remove:
            tracked_idxs.remove(i)

        for i in to_add:
            tracked_idxs.add(i)

    print(f"part 1: {split_count}")


def part2(grid):
    ways = {find_start_idx(grid): 1}

    for row in grid:
        new_ways = {}

        for idx, count in ways.items():
            if row[idx] == "^":
                new_ways[idx - 1] = new_ways.get(idx - 1, 0) + count
                new_ways[idx + 1] = new_ways.get(idx + 1, 0) + count
            else:
                new_ways[idx] = new_ways.get(idx, 0) + count

        ways = new_ways

    print(f"part 2: {sum(ways.values())}")


if __name__ == "__main__":
    with open("inp", "r") as f:
        grid = f.read().split()

        part1(grid)
        part2(grid)
