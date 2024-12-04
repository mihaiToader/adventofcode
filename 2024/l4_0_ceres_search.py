from input_output import read_level_input

LEVEL = '4.1'


def get_input(level):
    input_data = read_level_input(level)
    return [list(row) for row in input_data]


MOVES = [
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0],
    [-1, -1],
    [-1, 1],
    [1, -1],
    [1, 1]
]


def is_in_puzzle_row(puzzle, row):
    rows = len(puzzle)
    return 0 <= row < rows


def is_in_puzzle_column(puzzle, column):
    columns = len(puzzle[0])
    return 0 <= column < columns


def count_words(puzzle, row, col, word):
    words = 0
    for move in MOVES:
        searched_word = list(word[1:])
        search_row = row
        search_col = col
        while len(searched_word) > 0:
            search_row += move[0]
            search_col += move[1]
            if not is_in_puzzle_row(puzzle, search_row) or not is_in_puzzle_column(puzzle, search_col):
                break
            if puzzle[search_row][search_col] != searched_word[0]:
                break

            searched_word = searched_word[1:]

        if len(searched_word) == 0:
            words += 1

    return words


def solve():
    puzzle = get_input(LEVEL)

    rows = len(puzzle)
    columns = len(puzzle[0])
    total_words = 0
    for row in range(0, rows):
        for col in range(0, columns):
            if puzzle[row][col] == 'X':
                total_words += count_words(puzzle, row, col, 'XMAS')
            if puzzle[row][col] == 'S':
                total_words += count_words(puzzle, row, col, 'SAMX')
    print(total_words / 2)


if __name__ == "__main__":
    solve()
