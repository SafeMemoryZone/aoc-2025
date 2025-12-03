def part1(battery_banks):
    joltage_sum = 0

    for bank in battery_banks:
        joltage_arr = list(map(int, list(bank)))

        first_num = max(joltage_arr[:-1])
        second_num = max(joltage_arr[joltage_arr.index(first_num) + 1 :])
        joltage_sum += first_num * 10 + second_num

    print(f"part 1: {joltage_sum}")


def part2(battery_banks):
    joltage_sum = 0

    for bank in battery_banks:
        joltage_arr = list(map(int, list(bank)))

        built_num_str = ""
        next_idx = 0

        while len(built_num_str) != 12:
            additional_free_space = (
                len(joltage_arr) - next_idx - (12 - len(built_num_str))
            )
            highest_num = 0
            highest_idx = 0

            for i in range(next_idx, next_idx + additional_free_space + 1):
                if joltage_arr[i] > highest_num:
                    highest_num = joltage_arr[i]
                    highest_idx = i

            next_idx = highest_idx + 1
            built_num_str += str(highest_num)

        joltage_sum += int(built_num_str)

    print(f"part 2: {joltage_sum}")


if __name__ == "__main__":
    with open("inp", "r") as f:
        battery_banks = f.read().split()

        part1(battery_banks)
        part2(battery_banks)
