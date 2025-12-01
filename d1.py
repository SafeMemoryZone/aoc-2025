directions = {"L": -1, "R": 1}


def part1(instructions):
    dial_value = 50
    zero_count = 0

    for inst in instructions:
        direction = directions[inst[0]]
        count = int(inst[1:])

        dial_value += count * direction
        dial_value %= 100

        if dial_value == 0:
            zero_count += 1

    print(f"part 1: {zero_count}")


def part2(instructions):
    dial_value = 50
    zero_count = 0

    for inst in instructions:
        direction = directions[inst[0]]
        count = int(inst[1:])

        for _ in range(count):
            if dial_value == 0:
                zero_count += 1

            dial_value += direction
            dial_value %= 100

    print(f"part 2: {zero_count}")


with open("inp", "r") as f:
    instructions = f.read().split()
    part1(instructions)
    part2(instructions)
