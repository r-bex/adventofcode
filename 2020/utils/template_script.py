import sys
sys.path.append("..")
from utils.utils import load_input

def part1(data):
    return -1


def part2(data):
    return -1


if __name__ == "__main__":
    # run test against provided example
    example_input = load_input(path="example.txt")
    assert part1(example_input) == ???

    # run against real data
    values = load_input()
    print("part 1: {}".format(part1(values)))
    print("part 2: {}".format(part2(values)))