file_lines = []


def parseInput():
    numbers = []
    ops = []

    for line in file_lines:
        if line == "":
            continue

        parsed_line = line.split()

        if parsed_line[0].isdigit():
            numbers.append(list(map(int, parsed_line)))
        else:
            ops = parsed_line

    return numbers, ops


def part1():
    numbers, ops = parseInput()
    result_sum = 0

    for idx, op in enumerate(ops):
        result = 0 if op == "+" else 1

        for i in range(len(numbers)):
            num = numbers[i][idx]
            if op == "+":
                result += num
            else:
                result *= num

        result_sum += result

    print(f"part 1: {result_sum}")


def part2():
    _, ops = parseInput()
    col_idx = 0
    result_sum = 0

    for op in ops:
        result = 0 if op == "+" else 1

        while col_idx < len(file_lines[0]):
            num = ""
            move_to_next_op = True

            for row_idx in range(len(file_lines)):
                c = file_lines[row_idx][col_idx]
                if not c.isdigit():
                    continue
                move_to_next_op = False
                num += c

            col_idx += 1

            if move_to_next_op:
                break

            if op == "+":
                result += int(num)
            else:
                result *= int(num)

        result_sum += result

    print(f"part 2: {result_sum}")


if __name__ == "__main__":
    with open("inp", "r") as f:
        file_lines = f.read().split("\n")
        if file_lines[-1] == "":
            file_lines.pop(-1)

        part1()
        part2()
