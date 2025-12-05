def parse_input(lines):
    ranges = []
    foods = []

    for line in lines:
        parts = list(map(int, line.split("-")))

        if len(parts) == 2:
            ranges.append([parts[0], parts[1]])
        else:
            foods.append(parts[0])

    return ranges, foods


def part1(lines):
    ranges, foods = parse_input(lines)
    count = 0

    for food in foods:
        for r in ranges:
            if food <= r[1] and food >= r[0]:
                count += 1
                break

    print(f"part 1: {count}")


def part2(lines):
    ranges, _ = parse_input(lines)
    ranges.sort(key=lambda x: x[0])

    patched_ranges = []

    for r in ranges:
        found_range_to_extend = False

        for idx, pr in enumerate(patched_ranges):
            pr_start, pr_end = pr[0], pr[1]
            r_start, r_end = r[0], r[1]

            if r_start >= pr_start and r_start <= pr_end:
                # we need to extend this range
                patched_ranges[idx][1] = max(patched_ranges[idx][1], r_end)
                found_range_to_extend = True
                break

        if not found_range_to_extend:
            patched_ranges.append(r)

    count = 0

    for pr in patched_ranges:
        count += pr[1] - pr[0] + 1

    print(f"part 2: {count}")


if __name__ == "__main__":
    with open("inp", "r") as f:
        lines = f.read().split()

        part1(lines)
        part2(lines)
