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

# can pin down all edges just from signal lengths/frequencies except D and G
# e.g. the letter that appears in the 3- but not the 2- is the top bar, A

TRUE_SEGMENT_SET = set("ABCDEFG")
SIGNAL_SEGMENT_SET = set("abcdefg")

DIGIT_SEGMENT_MAP = {
    0: set("ABCEFG"), # 6 edges
    1: set("CF"), # 2 edges
    2: set("ACDEG"), # 5 edges
    3: set("ACDFG"), # 5 edges
    4: set("BCDF"), # 4 edges
    5: set("ABDFG"), # 5 edges
    6: set("ABDEFG"), # 6 edges
    7: set("ACF"), # 3 edges
    8: set("ABCDEFG"), # 7 edges
    9: set("ABCDFG") # 6 edges
}

class DisplaySolver:
    def __init__(self, input_signals):
        self.input_signals = input_signals
        self.segment_map = {}
        self.solved = self._is_solved()

def _is_solved(self):
    """Check whether the map has been completely constructed yet
    
    Every signal segment exists as a key and every true segment exists
    as a value in the segment map. Only checks validity, not correctness.

    Returns:
        boolean - True if segment map has been built completely, False otherwise
    """
    # does map contain all edges uniquely
    return False

def solve_map(self, left_signals):
    """Apply logic to generate segment map"""
    # figure out 

def translate_signals(self, signals_to_decode):
    if not self.solved:
        raise Exception("Right hand signals cannot be decoded before map is solved")
    
    # TODO: put decoding here
    pass