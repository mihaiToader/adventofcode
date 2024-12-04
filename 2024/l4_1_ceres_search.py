from l4_0_ceres_search import get_input, is_in_puzzle_row, is_in_puzzle_column

LEVEL = '4.2.1'


DIAGONALS = [
    [[-1, -1], [1, 1]],
    [[-1, 1], [1, -1]],
]


def find_xmas(puzzle, row, col):
    for diagonal in DIAGONALS:
        coordinates_1_row = row + diagonal[0][0]
        coordinates_1_col = col + diagonal[0][1]
        coordinates_2_row = row + diagonal[1][0]
        coordinates_2_col = col + diagonal[1][1]

        if not is_in_puzzle_row(puzzle, coordinates_1_row) or not is_in_puzzle_row(puzzle, coordinates_2_row) or not is_in_puzzle_column(puzzle, coordinates_2_col) or not is_in_puzzle_column(puzzle, coordinates_1_col):
            return False

        if puzzle[coordinates_1_row][coordinates_1_col] == 'M' and puzzle[coordinates_2_row][coordinates_2_col] == 'S':
            continue

        if puzzle[coordinates_1_row][coordinates_1_col] == 'S' and puzzle[coordinates_2_row][coordinates_2_col] == 'M':
            continue

        return False
    return True


def solve():
    puzzle = get_input(LEVEL)

    rows = len(puzzle)
    columns = len(puzzle[0])
    total_words = 0
    for row in range(0, rows):
        for col in range(0, columns):
            if puzzle[row][col] == 'A' and find_xmas(puzzle, row, col):
                total_words += 1

    print(total_words)


if __name__ == "__main__":
    solve()
