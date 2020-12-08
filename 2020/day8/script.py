import sys
sys.path.append("..")
from utils.utils import load_input

from copy import deepcopy


def parse_line_to_instruction(line):
    # turn file line e.g. 'acc +31' into instruction tuple ("acc", 31)
    line = line.replace("\n", "")
    [cmd, num] = line.split(" ")
    return (cmd, int(num))


def execute(command, current_acc, current_line):
    """Use the provided command to update accumulator and next line to be processed

        Args:
            command (tup(str, int))) - single instruction, e.g. ("jmp", 3)
            current_acc (int) - the current accumulator value
            current_line (int) - the index of the line currently being processed

        Returns:
            int - the new accumulator total
            int - the index of the line that should be processed next
    """
    (cmd, num) = command
    acc_diff = num if cmd == "acc" else 0
    line_diff = num if cmd == "jmp" else 1
    return (current_acc + acc_diff, current_line + line_diff)


def run_commands(commands):
    """Execute given instructions and return final accumulator

        NB. if instructions contain loop, final accumulator is value
        reached before any instruction would repeat. If not, final 
        accumulator is value reached when the final instruction is run.

        Args:
            commands (list(str, int)): sequence of instructions, 
                e.g. [("jmp", 3), ("nop", 0)]

        Returns:
            int - the final accumulator value
            bool - whether the process exited successfully (via last line)
    """
    invocations = [0 for cmd in commands]
    acc = 0
    exe_line = 0
    exited_successfully = False
    while invocations[exe_line] < 1:
        invocations[exe_line] += 1
        acc, exe_line = execute(commands[exe_line], acc, exe_line)
        if exe_line == len(commands):
            exited_successfully = True
            break
    return (acc, exited_successfully)


def part1(commands):
    # use cyclic instructions to find acc value before repeats
    acc, _ = run_commands(commands)
    return acc


def part2(commands):
    # modify single commands until program exits successfully - return acc
    jump_or_nop = [(cmd, num, i) for i, (cmd, num) in enumerate(commands) if cmd in ["nop", "jmp"]]
    for (current_cmd, num, line_index) in jump_or_nop:
        new_commands = deepcopy(commands)
        new_commands[line_index] = ("jmp" if current_cmd == "nop" else "nop", num)
        acc, successful_exit = run_commands(new_commands)
        if successful_exit:
            return acc
    return None


if __name__ == "__main__":
    # run test against provided example
    example_instructions = load_input(path="example.txt", parsing_func=parse_line_to_instruction)
    assert part1(example_instructions) == 5
    assert part2(example_instructions) == 8

    # run against real data
    real_instructions = load_input(parsing_func=parse_line_to_instruction)
    print("part 1: {}".format(part1(real_instructions)))
    print("part 2: {}".format(part2(real_instructions)))
