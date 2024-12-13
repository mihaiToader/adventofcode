import copy

from l11_1_plutonian_pebbles import get_input, transform_stone

LEVEL = '11.0'


def add_to_blinks_map(stones_map, new_stones):
    pass


def get_from_blinks_map(blinks_map, stone):
    stone_value = stone['stone']
    blinks = stone['blinks']
    stone_blinks = blinks_map.get(stone_value)
    if not stone_blinks:
        return None
    return stone_blinks.get(blinks)


def get_new_stones(stone):
    stones = []
    new_stone = copy.deepcopy(stone)
    for i in range(new_stone['blinks']):
        new_stones = transform_stone(new_stone['stone'])
        if len(new_stones) > 1:
            stones.append(dict(blinks=new_stone['blinks'] - i - 1, stone=new_stones[1]))
        print(new_stones[0], '->', stones)
        new_stone['stone'] = new_stones[0]
    return stones


def solve():
    stones = get_input(LEVEL)
    blinks = 75
    stones_map = {}
    stack = [dict(blinks=blinks, stone=stone) for stone in stones]
    count = 0
    while len(stack) > 0:
        if count % 10000000 == 0:
            print(count)
        stone = stack.pop()
        count += 1
        new_stones = get_new_stones(stone)
        return
        stack += new_stones

    print(count)


if __name__ == "__main__":
    solve()
