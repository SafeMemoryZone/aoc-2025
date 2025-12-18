import math

distance_list = []


def dist(junction1, junction2):
    return math.sqrt(
        abs(junction1[0] - junction2[0]) ** 2
        + abs(junction1[1] - junction2[1]) ** 2
        + abs(junction1[2] - junction2[2]) ** 2
    )


def get_sorted_distance_list(junctions):
    distance_list = []
    processed_pairs = set()

    for i in range(len(junctions)):
        for j in range(len(junctions)):
            if i == j:
                continue

            if (j, i) in processed_pairs:
                continue

            distance_list.append((i, j, dist(junctions[i], junctions[j])))
            processed_pairs.add((i, j))

    distance_list.sort(key=lambda x: x[2])
    return distance_list


def part1(junctions):
    junction_id_to_circuit_id = dict()
    circuit_id_to_junction_ids = dict()

    for i in range(len(junctions)):
        junction_id_to_circuit_id[i] = i
        circuit_id_to_junction_ids[i] = [i]

    for dp in distance_list[:1000]:
        j1, j2 = dp[0], dp[1]

        j1_circuit_id = junction_id_to_circuit_id[j1]
        j2_circuit_id = junction_id_to_circuit_id[j2]

        if j1_circuit_id == j2_circuit_id:
            continue

        # merge the two circuits

        second_junction_ids = circuit_id_to_junction_ids[j2_circuit_id]
        circuit_id_to_junction_ids[j1_circuit_id] += second_junction_ids
        del circuit_id_to_junction_ids[j2_circuit_id]

        for j in second_junction_ids:
            junction_id_to_circuit_id[j] = j1_circuit_id

    circuit_lengths = [0] * 1000

    for k, v in circuit_id_to_junction_ids.items():
        circuit_lengths[k] = len(v)

    circuit_lengths.sort(reverse=True)
    print(f"part 1: {circuit_lengths[0] * circuit_lengths[1] * circuit_lengths[2]}")


def part2(junctions):
    junction_id_to_circuit_id = dict()
    circuit_id_to_junction_ids = dict()

    for i in range(len(junctions)):
        junction_id_to_circuit_id[i] = i
        circuit_id_to_junction_ids[i] = [i]

    for dp in distance_list:
        j1, j2 = dp[0], dp[1]

        j1_circuit_id = junction_id_to_circuit_id[j1]
        j2_circuit_id = junction_id_to_circuit_id[j2]

        if j1_circuit_id == j2_circuit_id:
            continue

        # merge the two circuits

        second_junction_ids = circuit_id_to_junction_ids[j2_circuit_id]
        circuit_id_to_junction_ids[j1_circuit_id] += second_junction_ids
        del circuit_id_to_junction_ids[j2_circuit_id]

        for j in second_junction_ids:
            junction_id_to_circuit_id[j] = j1_circuit_id

        if len(circuit_id_to_junction_ids) == 1:
            print(f"part 2: {junctions[j1][0] * junctions[j2][0]}")
            return

    print("part 2: no result")


if __name__ == "__main__":
    with open("inp", "r") as f:
        junctions = [tuple(map(int, x.split(","))) for x in f.read().split()]
        distance_list = get_sorted_distance_list(junctions)

        part1(junctions)
        part2(junctions)
