import sys
sys.path.append("../..")
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

def invert_one_to_many_dict(dct):
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
        

def count_outermost_bags(pc_dict, bag_colour="shiny gold"):
    """Count the unique bag colours that could contain the target bag_colour

        Args:
            pc_dict (dict): parent-child mappings of bag requirements
            bag_colour (str): the bag colour to calculate outermost options for

        Returns:
            int - the number of bag_colours that could contain the target bag_colour
    """
    just_colours = {
        parent: [
            colour for (count, colour) in children_with_counts
        ] for parent, children_with_counts in pc_dict.items()
    }
    cp_dict = invert_one_to_many_dict(just_colours)
    unresolved_parents = cp_dict[bag_colour]
    final_parents = []
    while len(unresolved_parents):
        for unp in unresolved_parents:
            unresolved_parents.remove(unp)

            if unp not in final_parents:
                final_parents.append(unp)

            if unp in cp_dict and len(cp_dict[unp]):
                unresolved_parents.extend(cp_dict[unp])
    return len(final_parents)

def get_inner_count(pc_dct, bag_colour='shiny gold'):
    """Recursively count all the bags contained in a bag of the target colour

        Args:
            pc_dct (dict): parent-child mappings of bag requirements
            bag_colour (str): the bag colour to sum the contents of

        Returns:
            int - the total inner contents of the specified bag colour
    """
    if bag_colour not in pc_dct or len(pc_dct[bag_colour]) == 0:
        contents = 0
    else:
        contents = sum([
            inner_num + inner_num * get_inner_count(pc_dct, inner_colour)
                for (inner_num, inner_colour) in pc_dct[bag_colour]
        ])
    return contents

if __name__ == "__main__":
    # run test against provided example
    example_pt1_input = dict(load_input(path="example_part1.txt", parsing_func=parse_line_to_bag_mapping))
    assert count_outermost_bags(example_pt1_input) == 4

    # run part 2 against its own example
    example_pt2_input = dict(load_input(path="example_part2.txt", parsing_func=parse_line_to_bag_mapping))
    assert get_inner_count(example_pt2_input) == 126

    # run against real data
    real_dict = dict(load_input(parsing_func=parse_line_to_bag_mapping))
    print("part 1: {}".format(count_outermost_bags(real_dict)))
    print("part 2: {}".format(get_inner_count(real_dict)))