def part1(id_ranges):
    invalid_id_sum = 0

    for id_range in id_ranges:
        from_range = int(id_range.split("-")[0])
        to_range = int(id_range.split("-")[1])

        for i in range(from_range, to_range + 1):
            num_str = str(i)

            if len(num_str) % 2 != 0:
                continue

            part1 = num_str[: len(num_str) // 2]
            part2 = num_str[len(num_str) // 2 :]

            if part1 == part2:
                invalid_id_sum += i

    print(f"part 1: {invalid_id_sum}")


def part2(id_ranges):
    def is_repeated(num):
        num_str = str(num)

        for sequence_count in range(2, len(num_str) + 1):
            if len(num_str) % sequence_count != 0:
                continue

            sequence_size = len(num_str) // sequence_count
            skip = False

            for i in range(sequence_size):
                character = num_str[i]

                for j in range(sequence_count):
                    index = j * sequence_size + i
                    if num_str[index] != character:
                        skip = True
                        break

                if skip:
                    break

            if not skip:
                return True

        return False

    invalid_id_sum = 0

    for id_range in id_ranges:
        from_range = int(id_range.split("-")[0])
        to_range = int(id_range.split("-")[1])

        for i in range(from_range, to_range + 1):
            if is_repeated(i):
                invalid_id_sum += i

    print(f"part 2: {invalid_id_sum}")


if __name__ == "__main__":
    with open("inp", "r") as f:
        id_ranges = f.read().split(",")

        part1(id_ranges)
        part2(id_ranges)
