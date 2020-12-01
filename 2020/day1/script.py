import math
from itertools import combinations

TARGET_NUMBER = 2020


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


def get_multiple_of_components(values, combination_size=2):
    for combo in combinations(values, combination_size):
        if sum(combo) == TARGET_NUMBER:
            return math.prod(combo)
    return 0


def part1(values):
    # halfway_number = math.ceil(TARGET_NUMBER)
    # for i in range(halfway_number + 1):
    #     if i in values and (TARGET_NUMBER - i) in values:
    #         return i * (TARGET_NUMBER - i)
    # return 0
    return get_multiple_of_components(values)


def part2(values):
    return get_multiple_of_components(values, combination_size=3)


if __name__ == "__main__":
    parse_line_func = lambda l: int(l.replace("\n", ""))

    # test against example
    test_values = load_input(parse_line_func, path="example.txt")
    assert part1(test_values) == 514579

    # test against real data
    input_values = load_input(parse_line_func)
    print("part 1: {}".format(part1(input_values)))
    print("part 2: {}".format(part2(input_values)))
