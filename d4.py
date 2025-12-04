# not the most efficient solution for part 2! There are better ones but this one was very quick to implement.

offsets = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def get_removable_papers(grid):
    removable = []

    for y_idx, row in enumerate(grid):
        for x_idx in range(len(row)):
            if grid[y_idx][x_idx] != "@":
                continue

            neighbour_count = 0

            for x_off, y_off in offsets:
                new_x = x_idx + x_off
                new_y = y_idx + y_off

                if new_x < 0 or new_x >= len(row) or new_y < 0 or new_y >= len(grid):
                    continue

                if grid[new_y][new_x] == "@":
                    neighbour_count += 1

            if neighbour_count < 4:
                removable.append((x_idx, y_idx))

    return removable


def part1(grid):
    count = len(get_removable_papers(grid))

    print(f"part 1: {count}")


def part2(lines):
    splitted_lines = [list(row[:]) for row in lines]

    removable = get_removable_papers(splitted_lines)
    removed_count = 0

    while len(removable) != 0:
        for x_idx, y_idx in removable:
            splitted_lines[y_idx][x_idx] = "."

        removed_count += len(removable)
        removable = get_removable_papers(splitted_lines)

    print(f"part 2: {removed_count}")


if __name__ == "__main__":
    with open("inp", "r") as f:
        grid = f.read().split()

        part1(grid)
        part2(grid)
