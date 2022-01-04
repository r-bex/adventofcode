import sys
sys.path.append("../..")
from utils.utils import load_input, flatten_nested_list

class Board:
    def __init__(self, rows):
        # assert all rows are the same length
        assert len(set([len(row) for row in rows])) == 1

        # assert that everything is an int
        assert all([isinstance(val, int) for val in flatten_nested_list(rows)])

        # matrix of tuples (val, called) where val is the board number and
        # called is a boolean integer for whether that number has been called
        self.matrix = [[(num, 0) for num in r] for r in rows]

        self.num_rows = len(rows)
        self.num_cols = len(rows[0])

    def pretty_print(self):
        """Pretty print the board for debugging purposes"""
        def stringify_tuple(t):
            val, called = t
            val_str = " " + str(val) if val < 10 else str(val)
            return f"{val_str}o" if called == 0 else f"{val_str}x"

        print("--------")
        for row in self.matrix:
            print(" ".join([stringify_tuple(t) for t in row]))
        print("---------\n")

    def update(self, number):
        """Update the board state after a called number"""
        for row_ind in range(self.num_rows):
            for col_ind in range(self.num_cols):
                val, _ = self.matrix[row_ind][col_ind]
                if val == number:
                    self.matrix[row_ind][col_ind] = (val, 1)

    def has_won(self):
        """Check if any row or column is completely marked"""
        row_totals = [sum([mkd for (v, mkd) in r]) for r in self.matrix]
        row_win = any([total == self.num_cols for total in row_totals])
        if row_win:
            return row_win

        col_totals = [sum([row[i][1] for row in self.matrix]) for i in range(self.num_cols)]
        col_win = any([total == self.num_rows for total in col_totals])
        return col_win

    def sum_of_unmarked_numbers(self):
        """Sum all the uncalled numbers on the board"""
        return sum([
            val for (val, called)
            in flatten_nested_list(self.matrix)
            if called == 0
        ])

def load_and_prepare_input(all_lines):
    """Load the file as a list of called numbers and set of boards"""
    called_numbers = [int(x) for x in all_lines[0].split(",")]

    boards = []
    current_board = []

    # boards start from line 2 onwards
    for line in all_lines[2:]:
        if len(line) > 1:
            # split the board row line into a list of ints
            line_nums = [int(char) for char in line.split(" ") if len(char) > 0]
            current_board.append(line_nums)
        elif len(current_board):
            # we've hit a new line and need to finish the board before continuing
            boards.append(Board(current_board))
            current_board = []

    # if we've got to the end of the file try to add a final board
    if len(current_board):
        boards.append(Board(current_board))
    
    return called_numbers, boards


def part1(data):
    nums, boards = load_and_prepare_input(data)
    print("Loaded {} boards".format(len(boards)))

    for num in nums:
        for board in boards:
            board.update(num)
            if board.has_won():
                return board.sum_of_unmarked_numbers() * num

    return -1


def part2(data):
    nums, boards = load_and_prepare_input(data)
    print("Loaded {} boards".format(len(boards)))

    for num in nums:
        boards_to_remove = []
        for board in boards:
            board.update(num)
            if board.has_won():
                if len(boards) > 1:
                    boards_to_remove.append(board)
                else:
                    return board.sum_of_unmarked_numbers() * num

        # clean up boards that have already won
        for board in boards_to_remove:
            boards.remove(board)

    return -1


if __name__ == "__main__":
    # load example and real input data
    example_input = load_input(path="example.txt", remove_empty_lines=False)
    real_input = load_input(remove_empty_lines=False)

    # part 1
    assert part1(example_input) == 4512
    print("Part 1: {}".format(part1(real_input)))

    # part2
    assert part2(example_input) == 1924
    print("Part 2: {}".format(part2(real_input)))