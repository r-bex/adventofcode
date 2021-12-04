import sys
sys.path.append("../..")
from utils.utils import load_input

def part1(data):
    """Incoming data is list of ints. Want to count every time an entry is higher
    than the previous entry"""
    num_increases = 0
    for i in range(len(data) - 1):
        if data[i+1] > data[i]:
            num_increases += 1
    return num_increases

def part2(data):
    """Compare sums of sliding windows instead of direct list of ints"""
    window_size = 3
    sums = []
    for i in range(len(data) - window_size + 1):
        sums.append(sum(data[i : i + window_size]))
    return part1(sums)


if __name__ == "__main__":
    # run test against provided example
    parsing_func = lambda l: int(l)
    example_input = load_input(path="example.txt", parsing_func = parsing_func)
    real_input = load_input(parsing_func = parsing_func)
    
    # part1
    assert part1(example_input) == 7
    print("part 1: {}".format(part1(real_input)))

    # part2
    assert part2(example_input) == 5
    print("part 2: {}".format(part2(real_input)))
    