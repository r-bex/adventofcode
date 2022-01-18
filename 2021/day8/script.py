from utils import utils

from display_solver import DisplaySolver


def part1(data):
    # input should be list of tuples where tuple[0] is a list of the input
    # signals (10 of them) and tuple[1] is a list of the output signals (4)
    digits_to_count = [1, 4, 7, 8]
    counter = 0
    for input_signals, output_signals in data:
        solver = DisplaySolver(input_signals, debug=False)
        output_digits = solver.translate_signals(output_signals)
        counter += len([d for d in output_digits if d in digits_to_count])
    return counter

def part2(data):
    output_sum = 0
    for input_signals, output_signals in data:
        solver = DisplaySolver(input_signals, debug=False)
        output_digits = solver.translate_signals(output_signals)
        output_sum += int("".join([str(d) for d in output_digits]))
    return output_sum

def parse_line(l):
    """Take a full line and split into intput & output signals"""
    left, right = l.split(" | ")
    left_signals = left.split(" ")
    right_signals = right.split(" ")
    return left_signals, right_signals

if __name__ == "__main__":
    # load example and real input data
    example_input = utils.load_input(path="example.txt", parsing_func=parse_line)
    real_input = utils.load_input(parsing_func=parse_line)

    # part 1
    assert part1(example_input) == 26
    print("Part 1: {}".format(part1(real_input)))

    # part2
    assert part2(example_input) == 61229
    print("Part 2: {}".format(part2(real_input)))