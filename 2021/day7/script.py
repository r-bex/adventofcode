import sys
sys.path.append("../..")
from utils.utils import load_input

def calculate_minimum_fuel_to_align_crabs(starting_positions, fuel_cost_func=lambda x: x):
    """Calculate the cheapest crab alignment cost given crab positions
    
    Args:
        starting_positions (list(int)): initial horizontal positions of all crabs
        fuel_cost_func (func): function that takes steps required to align and
            returns cost of fuel required to take these steps

    Returns:
        int: the minimum fuel cost required to align all crabs over the same point
    """
    possible_positions = range(min(starting_positions), max(starting_positions) + 1)
    fuel_costs = [
        sum([fuel_cost_func(abs(candidate_posn - crab_posn)) for crab_posn in starting_positions])
        for candidate_posn in possible_positions
    ]
    return min(fuel_costs)

def part1(horizontal_positions):
    return calculate_minimum_fuel_to_align_crabs(horizontal_positions)


def part2(horizontal_positions):
    sum_up_to_n = lambda n: (n * (n + 1)) / 2
    return calculate_minimum_fuel_to_align_crabs(horizontal_positions, fuel_cost_func=sum_up_to_n)


if __name__ == "__main__":
    # load example and real input data
    parse_positions = lambda line: [int(char) for char in line.split(",")]
    example_input = load_input(path="example.txt", parsing_func=parse_positions)[0]
    real_input = load_input(parsing_func=parse_positions)[0]

    # part 1
    assert part1(example_input) == 37
    print("Part 1: {}".format(part1(real_input)))

    # part2
    assert part2(example_input) == 168
    print("Part 2: {}".format(part2(real_input)))