import sys
sys.path.append("..")
from utils.utils import load_input

from functools import reduce
import re

COLOURED_BAGS_PATTERN = r"(\d+) ([a-z]{1}[a-z ]*) bags?"

def parse_line_to_bag_mapping(line):
    """Turn line from file into parent -> child bag mapping

        Args:
            line (str): the file line, e.g. 'bright white bags contain 1 shiny gold bag.'
        
        Returns:
            (str, list(str, str)) e.g. ('bright white', [1, 'shiny gold'])
    """
    line = line.replace("\n", "").replace(".", "")
    [parent_colour, child_text] = line.split(" bags contain ")
    if child_text == "no other bags":
        return (parent_colour, [])
    else:
        child_colours_with_counts = [
            (int(count_str), colour) for (count_str, colour) in re.findall(COLOURED_BAGS_PATTERN, child_text)
        ]
        return (parent_colour, child_colours_with_counts)

def reverse_dict(dct):
    """Invert dictionary of 1-to-many parent-children mappings

        e.g. {1: ['a', 'b']} -> {'a': 1, 'b': 1}

        Args:
            dct (dict): dictionary where value is a list of items

        Returns:
            dict
    """
    inverted_dct = {}
    unique_children = set(reduce(lambda l, r: l + r, list(dct.values())))
    for target_child in unique_children:
        parents = []
        for parent, children in dct.items():
            if target_child in children:
                parents.append(parent)
        inverted_dct[target_child] = parents
    return inverted_dct
        

def part1(pc_dict, target_colour="shiny gold"):
    # find outermost bags
    just_colours = {
        parent: [
            colour for (count, colour) in children_with_counts
        ] for parent, children_with_counts in pc_dict.items()
    }
    cp_dict = reverse_dict(just_colours)
    unresolved_parents = cp_dict[target_colour]
    final_parents = []
    while len(unresolved_parents):
        for unp in unresolved_parents:
            unresolved_parents.remove(unp)

            if unp not in final_parents:
                final_parents.append(unp)

            if unp in cp_dict and len(cp_dict[unp]):
                unresolved_parents.extend(cp_dict[unp])
    return len(final_parents)

def get_inner_count(dct, bag_colour, num_of_these_bags):
    # get total bags contained in bag plus itself - recursive
    if bag_colour not in dct or len(dct[bag_colour]) == 0:
        inner_count = 0
    else:
        inner_count = sum([
            get_inner_count(dct, inner_colour, inner_num) for (inner_num, inner_colour) in dct[bag_colour]
        ])
    return num_of_these_bags + num_of_these_bags * inner_count

def part2(pc_dict, target_colour='shiny gold'):
    # count all bags INSIDE target colour (so minus 1 after)
    total_including_outer = get_inner_count(pc_dict, target_colour, 1)
    return total_including_outer - 1

if __name__ == "__main__":
    # run test against provided example
    example_pt1_input = load_input(path="example_part1.txt", parsing_func=parse_line_to_bag_mapping)
    example_pt1_dict = {parent: children for (parent, children) in example_pt1_input}
    assert part1(example_pt1_dict) == 4

    example_pt2_input = load_input(path="example_part2.txt", parsing_func=parse_line_to_bag_mapping)
    example_pt2_dict = {parent: children for (parent, children) in example_pt2_input}
    assert part2(example_pt2_dict) == 126

    # run against real data
    values = load_input(parsing_func=parse_line_to_bag_mapping)
    value_dict = {parent: children for (parent, children) in values}
    print("part 1: {}".format(part1(value_dict)))
    print("part 2: {}".format(part2(value_dict)))