import sys
sys.path.append("..")
from utils.utils import load_input


def resolve_seat_id(l):
    # turn e.g. FFBBFBBLRR into two binary parts 0011011 and 011
    # turn these to ints and then combine to get the seat ID
    row_code = "".join(["0" if c == 'F' else "1" for c in l[:-3]])
    row_number = int(row_code, 2)

    column_code = "".join(["0" if c == 'L' else "1" for c in l[-3:]])
    column_number = int(column_code, 2)

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