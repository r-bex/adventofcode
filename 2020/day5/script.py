import sys
sys.path.append("../..")
from utils.utils import load_input


def decode_alphabetic_binary(code_string, pos_char):
    # turn e.g. FFBBFBB into a number using base 2 maths
    reversed_code = code_string[::-1] # so that char indexes align with value of position
    position_values = [
        int(char == pos_char) * 2**char_index for char_index, char in enumerate(reversed_code)
    ]
    return sum(position_values)


def resolve_seat_id(raw_code):
    # split the raw code into row and column components
    # turn these to numbers and combine to get the seat ID
    row_number = decode_alphabetic_binary(raw_code[:-3], "B")
    column_number = decode_alphabetic_binary(raw_code[-3:], "R")
    return row_number * 8 + column_number


def part1(bp_codes):
    # return the maximum seat ID found by combining row and col numbers
    seat_ids = [resolve_seat_id(bp_code) for bp_code in bp_codes]
    return max(seat_ids)


def part2(bp_codes):
    # order the seat IDs and find the consecutive pair where the jump between them is 2
    sorted_seat_ids = sorted([resolve_seat_id(bp_code) for bp_code in bp_codes])
    jumps = [sorted_seat_ids[i] - sorted_seat_ids[i - 1] for i in range(1, len(sorted_seat_ids))]
    missing_seat_id = sorted_seat_ids[jumps.index(2)] + 1
    return missing_seat_id


if __name__ == "__main__":
    # run test against provided example
    example_input = load_input(path="example.txt")
    assert part1(example_input) == 820

    # run against real data
    values = load_input()
    print("part 1: {}".format(part1(values)))
    print("part 2: {}".format(part2(values)))

    assert part1(values) == 826
    assert part2(values) == 678