import sys
sys.path.append("../..")
from utils.utils import load_input

def parse_movement_string(movement_string):
    """Convert direction & magnitude into movement tuple (vector)

    Args:
        movement_string (str): direction & magnitude e.g. 'forward 3', 'up 4'

    Returns:
        (int, int): vector representation of movement
    """
    direction = movement_string.split(" ")[0]
    magnitude = int(movement_string.split(" ")[1])

    if direction == "forward":
        return (magnitude, 0)
    elif direction == "up":
        return (0, -1 * magnitude)
    elif direction == "down":
        return (0, magnitude)
    else:
        raise ValueError(f"Couldn't parse line: {s}")

def part1(data):
    """Track horizontal & depth position of sub & multiply"""
    horizontal_pos, depth_pos = 0, 0
    movements = [parse_movement_string(s) for s in data]
    for (horizontal_delta, depth_delta) in movements:
        horizontal_pos += horizontal_delta
        depth_pos += depth_delta
    return horizontal_pos * depth_pos


def part2(data):
    """As above but depth value is now aim, and actual depth is function of aim
    and horizontal pos"""
    horizontal_pos, aim, depth_pos = 0, 0, 0
    movements = [parse_movement_string(s) for s in data]
    for (horizontal_delta, aim_delta) in movements:
        # check that only one of values is non-zero. This means can do next steps in any order.
        assert bool(horizontal_delta) != bool(aim_delta)

        aim += aim_delta
        horizontal_pos += horizontal_delta
        depth_pos += aim * horizontal_delta # will be no change if horizontal_delta = 0

    return horizontal_pos * depth_pos


if __name__ == "__main__":
    # load example and real input data
    example_input = load_input(path="example.txt")
    real_input = load_input()

    # part 1
    assert part1(example_input) == 150
    print("Part 1: {}".format(part1(real_input)))

    # part2
    assert part2(example_input) == 900
    print("Part 2: {}".format(part2(real_input)))