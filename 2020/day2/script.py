import sys
sys.path.append("../..")
from utils.utils import load_input

import re


def parse_input(l):
    # if line is '1-3 g: abcdef' return ('1', '3', 'g', 'abcdef')
    pattern = re.compile(r"(\d+)-(\d+) (.): (.+)")
    matching_groups = pattern.search(l.replace("\n", ""))
    return matching_groups.groups()


def part1(password_data):
    num_valid_passwords = 0
    for (min_occ, max_occ, letter, pwd) in password_data:
        num_letter = len([c for c in pwd if c == letter])
        if num_letter >= int(min_occ) and num_letter <= int(max_occ):
            num_valid_passwords += 1
    return num_valid_passwords


def part2(password_data):
    num_valid_passwords = 0
    for (pos1, pos2, letter, pwd) in password_data:
        ind1_valid = pwd[int(pos1) - 1] == letter
        ind2_valid = pwd[int(pos2) - 1] == letter
        if ind1_valid != ind2_valid:  #xor
            num_valid_passwords += 1
    return num_valid_passwords


if __name__ == "__main__":
    # run test against provided example
    example_input = load_input(path="example.txt", parsing_func=parse_input)
    assert part1(example_input) == 2
    assert part2(example_input) == 1

    # run against real data
    values = load_input(parsing_func=parse_input)
    print("part 1: {}".format(part1(values)))
    print("part 2: {}".format(part2(values)))