import sys
sys.path.append("..")
from utils.utils import load_input

def check_sum_condition(num, prev_nums):
    # two nums in prev_nums need to sum to num, otherwise False
    for prev_num in prev_nums:
        diff = num - prev_num
        if diff in prev_nums:
            return True
    return False

def part1(data, preamble_length=25):
    # find first number that breaks preamble sum condition
    nums = list(map(lambda s: int(s), data))
    starting_index = preamble_length
    for i in range(starting_index, len(nums)):
        if not check_sum_condition(nums[i], nums[i - preamble_length:i]):
            return nums[i]
    return -1

def check_windows(sl, window_size, target):
    # check rolling windows of given size for sum to target condition
    print("Checking for window size {}".format(window_size))
    num_windows = len(sl) - window_size
    for window_start in range(0, num_windows):
        window = sl[window_start:window_start+window_size]
        if sum(window) == target:
            return window
    return []


def part2(data, target_num):
    # add min and max of contiguous subset that sums to target number
    print("Target num = {}".format(target_num))
    nums = list(map(lambda s: int(s), data))
    found = False
    window_size = min([target_num, len(nums)])
    while not found and window_size > 1:
        window_results = check_windows(nums, window_size, target_num)
        if len(window_results) > 0:
            found = True
            return min(window_results) + max(window_results)
        else:
            window_size -= 1
    return None


if __name__ == "__main__":
    # run test against provided example
    example_input = load_input(path="example.txt")
    assert part1(example_input, preamble_length=5) == 127
    assert part2(example_input, 127) == 62

    # run against real data
    values = load_input()
    invalid_value = part1(values)
    print("part 1: {}".format(invalid_value))
    print("part 2: {}".format(part2(values, invalid_value)))
