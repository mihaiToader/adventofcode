from location_ids_distance_1_0 import get_input

LEVEL = '1.1'


def create_appearances_hash(location_ids: list[int]):
    appearances = dict()
    for loc_id in location_ids:
        if not appearances.get(loc_id):
            appearances[loc_id] = 1
        else:
            appearances[loc_id] += 1
    return appearances


def solve():
    input_data = get_input(LEVEL)
    appearances_hash = create_appearances_hash(input_data[1])
    similarity_score = 0
    for loc_id in input_data[0]:
        similarity_score += loc_id * appearances_hash.get(loc_id, 0)
    print(similarity_score)


if __name__ == "__main__":
    solve()
