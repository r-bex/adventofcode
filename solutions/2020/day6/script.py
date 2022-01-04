import sys
sys.path.append("../..")
from utils.utils import load_input, chunk_lines_by_blanks


def part1(all_lines):
    # sum of number of unique answers per group
    group_counts = 0
    grouped_answers = chunk_lines_by_blanks(all_lines)
    for group_answers in grouped_answers:
        distinct_answers = set("".join(group_answers))
        group_counts += len(distinct_answers)
    return group_counts

def count_common_answers(answers):
    # takes all group's answers like ['abc', 'bc', 'bde']
    # returns number of letters appearing in all answers
    concat_answer = "".join(answers)
    unique_answers = set(list(concat_answer))
    answer_occurrences = list(map(concat_answer.count, unique_answers))
    return answer_occurrences.count(len(answers))

def part2(all_lines):
    # sum of number of answers given by all of group
    group_counts = 0
    grouped_answers = chunk_lines_by_blanks(all_lines)
    for group_answers in grouped_answers:
        group_counts += count_common_answers(group_answers)
    return group_counts


if __name__ == "__main__":
    # run test against provided example
    example_input = load_input(path="example.txt", remove_empty_lines=False)
    assert part1(example_input) == 11

    # run against real data
    lines = load_input(remove_empty_lines=False)
    print("part 1: {}".format(part1(lines)))
    print("part 2: {}".format(part2(lines)))
