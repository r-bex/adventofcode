import sys
sys.path.append("../..")
from utils.utils import load_input

import math
from itertools import combinations

TARGET_NUMBER = 2020


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
    test_values = load_input(path="example.txt", parsing_func=parse_line_func)
    assert part1(test_values) == 514579

    # test against real data
    input_values = load_input(parsing_func=parse_line_func)
    print("part 1: {}".format(part1(input_values)))
    print("part 2: {}".format(part2(input_values)))
