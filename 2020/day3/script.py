import math


def load_input(parsing_func, path="data.txt"):
    """Load lines from the specified file and apply parsing_func linewise

        Args:
            parsing_func (str -> T): a function that takes a string as input
            path (str): the input data file location. Default = "data.txt"

        Returns:
            list(T): a list of the files contents after applying the parsing function
    """
    with open(path, 'r') as f:
        lines = f.readlines()
    f.close()
    non_empty = [l for l in lines if len(l.replace("\n", "")) > 0]
    return list(map(parsing_func, non_empty))


def count_trees_on_slope(data_rows, horizontal_velocity, vertical_velocity):
    # data_rows is 2d array e.g. [['#', '.', '.'], ['#', '#', '.']]
    # slope_dir is dictionary of velocity in horizontal & vertical dirs
    row_length = len(data_rows[0])

    current_row = 0
    current_position = 0

    tree_count = 0
    while current_row < len(data_rows):
        # check if tree in current position
        if data_rows[current_row][current_position] == '#':
            tree_count += 1

        # update position
        current_row += vertical_velocity
        current_position = (current_position +
                            horizontal_velocity) % row_length
    return tree_count


if __name__ == "__main__":
    parse_line = lambda l: list(l.replace("\n", ""))

    # run test against provided example
    example_input = load_input(parse_line, path="example.txt")
    assert count_trees_on_slope(example_input,
                                horizontal_velocity=3,
                                vertical_velocity=1) == 7

    # load real data
    terrain = load_input(parse_line)

    # part 1 - slope = 3 right, down 1
    part1_solution = count_trees_on_slope(terrain,
                                          horizontal_velocity=3,
                                          vertical_velocity=1)
    print("part 1: {}".format(part1_solution))

    # part 2 - many slopes
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    slope_counts = [
        count_trees_on_slope(terrain,
                             horizontal_velocity=hv,
                             vertical_velocity=vv) for (hv, vv) in slopes
    ]
    part2_solution = math.prod(slope_counts)
    print("part 2: {}".format(part2_solution))
