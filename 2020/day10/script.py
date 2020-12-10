import sys
sys.path.append("..")
from utils.utils import load_input, sliding_windows_across_list

from copy import deepcopy
import math

def prep_sequence(loose_adapters, device_jump=3):
    """Turn looes adapters into ordered list from socket to device joltage

        Args:
            loose_adapters (list(int)): available adaptors excluding device
            device_jump (int): the additional joltage of the device

        Returns:
            list(int): ordered sequence of all joltage outputs
    """
    device_joltage = max(loose_adapters) + device_jump
    adapters = sorted(loose_adapters)
    all_adapters = [0] + adapters + [device_joltage]
    return all_adapters

def is_sequence_valid(adapters, max_jump=3):
    """Check if an ordered sequence of adaptors is valid

        Args:
            adapters (list(int)): an ordered list of adapter joltages
            max_jump (int): the maximum allowed interval between 
                consecutive joltages
        
        Returns:
            bool - whether all sequence items are at most max_jump
                away from their preceding item
    """
    jumps = [adapters[i] - adapters[i-1] for i in range(1, len(adapters))]
    return all([j >= 1 and j <= max_jump for j in jumps])

def part1(adapters):
    # multiply number of 1 jumps by number of 3 jumps in valid sequence
    # that uses all adapters
    adapters = prep_sequence(adapters)
    if is_sequence_valid(adapters):
        jumps = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]
        return jumps.count(1) * jumps.count(3)
    else:
        return -1


def test_single_removals(adapters):
    """Return valid subsets of list after removing single element

        NB: this doesn't count all valid subsets, only those created by
            removing a single element from the provided list.

        Args:
            adapters (list(int)): the bounded adapters to find subsets of

        Returns:
            list(list(int)): valid subsets of the complete list provided
    """
    valid_combos = []
    for adap in adapters[1:-1]:
        minus_adap = deepcopy(adapters)
        minus_adap.remove(adap)
        if is_sequence_valid(minus_adap):
            valid_combos.append(minus_adap)
    return valid_combos


def count_valid_subsets_between_anchors(adapters):
    """Given a sequence of adapters bounded by anchors, count all possible subsets

        Works by removing elements one by one and checking validity of what is left.
        If valid, the reduced-by-1 list 'survives' into the next iteration of things
        to be reduced. Runs until there are no more valid sequences to reduce & test.

        Args:
            adapters (list(int)): the full adapter sequence to explore

        Returns:
            int - the number of ordered subsets of the provided list that are
                still valid sequences
    """
    valid_subsets = []
    # check if original entire sequence is valid, before reducing it
    if is_sequence_valid(adapters):
        valid_subsets.append(adapters)

    # for tracking valid subsets we could further reduce and test
    working_subsets = [sorted(adapters)]

    while len(working_subsets) > 0:
        next_iteration_working_subsets = []
        for subset_to_reduce in working_subsets:
            for surviving_subset in test_single_removals(subset_to_reduce):
                if surviving_subset not in valid_subsets:
                    valid_subsets.append(surviving_subset)
                if surviving_subset not in next_iteration_working_subsets:
                    next_iteration_working_subsets.append(surviving_subset)
        working_subsets = next_iteration_working_subsets
    return len(valid_subsets)


def part2(adapters, max_jump=3):
    adapters = prep_sequence(adapters)

    # store indices of adapters you can't remove without breaking condition
    anchor_indices = [0] # start with first index - socket
    for (lower, middle, upper) in sliding_windows_across_list(adapters, window_size=3, as_tuples=True):
        if upper - lower > max_jump:
            anchor_indices.append(adapters.index(middle))
    anchor_indices.append(len(adapters) - 1) # add final index (device adapter)

    # use anchor indices to build sublists that we will count optimisations of
    sublists = []
    anchor_index_pairs = sliding_windows_across_list(anchor_indices, window_size=2, as_tuples=True)
    for (lower_anchor_index, upper_anchor_index) in anchor_index_pairs:
        # if not adjacent in list, then create sublist
        if upper_anchor_index - lower_anchor_index > 1:
            sublists.append(adapters[lower_anchor_index : upper_anchor_index + 1])

    # for each sublist, calculate possible valid subsets contained & return total
    sublist_combos = [count_valid_subsets_between_anchors(sublist) for sublist in sublists]
    return math.prod(sublist_combos)


if __name__ == "__main__":
    parse_func = lambda l: int(l.replace("\n", ""))
    # run test against provided example
    example1_adapters = load_input(path="example1.txt", parsing_func=parse_func)
    assert part1(example1_adapters) == 35
    assert part2(example1_adapters) == 8

    example2_adapters = load_input(path="example2.txt", parsing_func=parse_func)
    assert part1(example2_adapters) == 220
    assert part2(example2_adapters) == 19208

    # run against real data
    real_adapters = load_input(parsing_func=parse_func)
    print("part 1: {}".format(part1(real_adapters)))
    print("part 2: {}".format(part2(real_adapters)))
