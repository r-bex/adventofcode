from utils.utils import load_input

from display_solver import DisplaySolver

def part1(data):
    return -1


def part2(data):
    return -1

def parse_line(l):
    """blah"""
    left, right = l.split(" | ")
    left_signals = left.split(" ")
    right_signals = right.split(" ")
    return left_signals, right_signals

if __name__ == "__main__":
    # load example and real input data
    example_input = load_input(path="example.txt")
    real_input = load_input()

    # part 1
    assert part1(example_input) == ???
    print("Part 1: {}".format(part1(real_input)))

    # part2
    # assert part2(example_input) == ???
    # print("Part 2: {}".format(part2(real_input)))