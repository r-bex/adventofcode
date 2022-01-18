from utils import utils

from display_solver import DisplaySolver


def part1(data):
    """Decode the displays and count the number of times digits appear

    Args:
        data (list(tuple)): list of input & display signal pairs. Tuple[0]
            is list of ten input signals. Tuple[1] is list of 4 display
            signals, which form the display to be decoded.

    Returns:
        int - the number of times certain digits appear in the decoded
            displays.
    """
    digits_to_count = [1, 4, 7, 8]
    counter = 0
    for input_signals, display_signals in data:
        solver = DisplaySolver(input_signals, debug=False)
        display_digits = solver.translate_signals(display_signals)
        counter += len([d for d in display_digits if d in digits_to_count])
    return counter

def part2(data):
    """Decode the displays and sum all the resulting digits

    Args:
        data (list(tuple)): list of input & display signal pairs. Tuple[0]
            is list of ten input signals. Tuple[1] is list of 4 display
            signals, which form the display to be decoded.

    Returns:
        int - the sum of all the digits in the decoded displays
    """
    display_digit_sum = 0
    for input_signals, display_signals in data:
        solver = DisplaySolver(input_signals, debug=False)
        display_digits = solver.translate_signals(display_signals)
        display_digit_sum += int("".join([str(d) for d in display_digits]))
    return display_digit_sum

def parse_line(line):
    """Take a full line and split into intput & output signals

    Args:
        line (str): the raw line from the file

    Returns:
        list, list: input and output signals respectively
    """
    left, right = line.split(" | ")
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