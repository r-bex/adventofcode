import sys
import timeit
sys.path.append("../..")
from utils.utils import load_input, time_execution

# dts - days_to_spawn

# rules for iterating sequence
# - each item in the sequence describes the dts value of a single lanternfish
# - each iteration is moving a day forward in time
# - if dts > 0 then the lanternfish is not yet due to spawn a new baby
# - if dts = 0 then it is spawning day, and a new baby lanternfish is added to the end of the sequence
# - after spawning, it will be DAYS_BETWEEN_SPAWN days until the parent fish can spawn again
# - new baby lanternfishes require DAYS_TO_MATURE additional days before they can start spawning


DAYS_BETWEEN_SPAWN = 7
DAYS_TO_MATURE = 2

# -- Method 1: iterate the sequence forward 1 day at a time --

def iterate_dts_list(dts_values, num_iterations=1, debug=False):
    """Iterate a DTS sequence 1 day forward according to the rules above

    Args:
        dts_values (list(int)): sequence of DTS values, one per lanternfish
        num_iterations (int): the number of iterations to simulate. Default = 1
        debug (bool): if True, print intermediate sequences. Default = False

    Returns:
        list(int): the lanternfish DTS sequence 1 day later
    """
    seq = dts_values
    if debug:
        print(f"0: {seq}")

    for i in range(num_iterations):
        next_seq = []
        new_additions = []
        for dts in seq:
            if dts > 0:
                next_seq.append(dts - 1)
            else:
                next_seq.append(DAYS_BETWEEN_SPAWN - 1)
                new_additions.append(DAYS_BETWEEN_SPAWN + DAYS_TO_MATURE - 1)
        seq = next_seq + new_additions
        if debug:
            print(f"{i + 1}: {seq}")
    return seq

def count_future_population_method1(starting_seq, num_iterations, debug=False):
    """Calculate the population after X iterations using iteration method"""
    seq_after_iterations = iterate_dts_list(starting_seq, num_iterations)
    return len(seq_after_iterations)

# -- Method 2: recursively count a fish's children -- 

def generate_baby_dates(current_date, max_date, current_dts):
    """Calculate a lanternfish's future spawning dates/iterations"""
    if current_date + current_dts > max_date:
        return []
    else:
        baby_dates = [current_date + current_dts]
        while baby_dates[-1] + DAYS_BETWEEN_SPAWN <= max_date:
            baby_dates.append(baby_dates[-1] + DAYS_BETWEEN_SPAWN)
        return baby_dates

def count_all_future_children(date, max_date, current_dts, debug=False):
    """Recursively count all of a lanternfish's children within a timespan
    
    Args:
        date (int): the current iteration counter
        max_date (int): the number of iterations to run to in total
        current_dts (int): the current DTS value of the lanternfish
        debug (bool): if True, print out helpful things. Default = False

    Returns:
        int - the total future children this lanternfish will produce,
            directly or indirectly
    """
    if debug:
        print("***")
        print(f"Date: {date}/{max_date} - current DTS = {current_dts}")

    if date + current_dts > max_date:
        if debug:
            print("Not having children")
            print("------")
        return 1
    else:
        spawn_dates = generate_baby_dates(date, max_date, current_dts)
        if debug:
            print(f"Will spawn on dates: {spawn_dates}")
            print("Calculating children...")
        return 1 + sum([count_all_future_children(
            sd, max_date, DAYS_BETWEEN_SPAWN + DAYS_TO_MATURE
        ) for sd in spawn_dates])

def count_future_population_method2(starting_seq, num_iterations, debug=False):
    """Calculate the population after X iterations using recursion method"""
    return sum([
        count_all_future_children(1, num_iterations, dts, debug=debug) for dts in starting_seq
    ])

if __name__ == "__main__":
    # load example and real input data
    parse_line = lambda l: [int(char) for char in l.split(",")]
    example_input = load_input(path="example.txt", parsing_func=parse_line)[0]
    real_input = load_input(parsing_func=parse_line)[0]

    # part 1
    time_execution(1, count_future_population_method2, *(example_input, 256), **{})
    #assert count_future_population_method1(example_input, 80) == 5934 # 7.3ms
    #assert count_future_population_method2(example_input, 80) == 5934 # 4.2ms
    #print("Part 1 method 1: {}".format(count_future_population_method1(real_input, 80))) # 337ms
    #print("Part 1 method 2: {}".format(count_future_population_method2(real_input, 80))) # 175ms

    # part 2
    #assert count_future_population_method1(example_input, 256) == 26984457539 # not finished after 60s
    #assert count_future_population_method2(example_input, 256) == 26984457539 # not tried yet
    #print("Part 2 method 1: {}".format(count_future_population_method1(real_input, 256))) # not finished after 60s
    # print("Part 2 method 2: {}".format(count_future_population_method2(real_input, 256))) # not finished after 60s
