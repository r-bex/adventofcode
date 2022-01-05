from enum import Enum, auto

# """
#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg
# """

# the letter that appears in the 3- but not the 2- is the top bar, A

TRUE_SEGMENT_SET = set("ABCDEFG")
SIGNAL_SEGMENT_SET = set("abcdefg")

DIGIT_TS_MAP = {
    0: set("abcefg"), # 6
    1: set("cf"), # 2
    2: set("acdeg"), # 5
    3: set("acdfg"), # 5
    4: set("bcdf"), # 4
    5: set("abdfg"), # 5
    6: set("abdefg"), # 6
    7: set("acf"), # 3
    8: set("abcdefg"), # 7
    9: set("abcdfg") # 6
}

class Digit:
    def __init__(self, true_segments=None, signal_segments=None):
        self.true_segments = true_segments
        self.signal_segments = signal_segments
        self.solved = self._is_solved()

    def _is_solved(self):
        return self.true_segments is not None and len(self.true_segments) == len(self.signal_segments)


# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe

def parse_line(l):
    left, right = l.split(" | ")
    