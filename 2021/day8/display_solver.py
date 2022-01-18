from collections import Counter

from utils import utils

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

TRUE_SEGMENT_TO_DIGIT_MAP = {
    "ABCEFG": 0, # 6 edges
    "CF": 1, # 2 edges
    "ACDEG": 2, # 5 edges
    "ACDFG": 3, # 5 edges
    "BCDF": 4, # 4 edges
    "ABDFG": 5, # 5 edges
    "ABDEFG": 6, # 6 edges
    "ACF": 7, # 3 edges
    "ABCDEFG": 8, # 7 edges
    "ABCDFG": 9 # 6 edges
}

class DisplaySolver:
    """Builds segment map from input signals and then decodes output signals

    Args:
        input_signals (list(str)): the ten scrambled input signals
        debug (bool): whether to print debug statements
    
    Attributes:
        segment_map dict (str -> str): mapping between signal segments and true segments
        solved (bool): whether the mapping has been completely constructed yet
    """
    def __init__(self, input_signals, debug=False):
        if len(input_signals) != 10:
            raise ValueError("DisplaySolver needs 10 input_signals to initialise")
        
        self.input_signals = input_signals
        self.debug = debug

        self.segment_map = {}
        self.solve_map()

    def _is_solved(self):
        """Check whether the map has been completely constructed yet
        
        Every signal segment exists as a key and every true segment exists
        as a value in the segment map. Only checks validity, not correctness.

        Returns:
            boolean - True if segment map has been built completely, False otherwise
        """
        all_keys = all([ss in self.segment_map for ss in SIGNAL_SEGMENT_SET])
        all_values = all([ts in self.segment_map.values() for ts in TRUE_SEGMENT_SET])
        
        if self.debug:
            print(self.segment_map)
            print("All keys present? ", all_keys)
            print("All values present? ", all_values)

        return all_keys and all_values

    def _get_signals_by_length(self, length):
        """Return the subset of the input signals with the given length"""
        return [x for x in self.input_signals if len(x) == length]

    def _get_signals_by_frequency(self, frequency):
        flat_list = utils.flatten_nested_list(self.input_signals)
        frequencies = Counter(flat_list)
        return [char for (char, freq) in frequencies.items() if freq == frequency]

    def _add_mapping(self, signal_segment, true_segment):
        """This is just here to add debug value without repeating 7 times"""
        if self.debug:
            print(f"Adding {signal_segment} -> {true_segment} to segment mapping")
        self.segment_map[signal_segment] = true_segment

    def solve_map(self):
        """Apply logic to generate segment map"""
        if self.debug:
            print(self.input_signals)

        # A is the signal in the 3-length but not 2-length signals
        l3 = self._get_signals_by_length(3)[0] # should just be 1
        l2 = self._get_signals_by_length(2)[0] # should just be 1
        a = set(l3).difference(set(l2)).pop()
        self._add_mapping(a, "A")

        # F is the only segment that is in 9 of the 10 digits
        f = self._get_signals_by_frequency(9)[0]
        self._add_mapping(f, "F")

        # B is the only segment in exactly 6 of the 10 digits
        b = self._get_signals_by_frequency(6)[0]
        self._add_mapping(b, "B")

        # E is the only segment in exactly 4 of the 10 digits
        e = self._get_signals_by_frequency(4)[0]
        self._add_mapping(e, "E")

        # now we know F, C is the one in the length-2 signal that isn't F
        c = set(l2).difference({f}).pop()
        self._add_mapping(c, "C")

        # we can find D because it is the only unknown in the length-4 signal
        l4 = self._get_signals_by_length(4)[0]
        d = [char for char in l4 if char not in self.segment_map][0]
        self._add_mapping(d, "D")

        # this means G is the one left
        g = SIGNAL_SEGMENT_SET.difference(set(self.segment_map.keys())).pop()
        self._add_mapping(g, "G")

    def translate_signals(self, signals_to_decode):
        """Use the solved mapping to decode output signals

        Args:
            signals_to_decode (list(str)): 4 output signals

        Returns:
            list(int): the corresponding 4 digits, decoded
        """
        if not self._is_solved():
            raise Exception(f"""
                Right hand signals cannot be decoded before
                map is solved. Current map: {self.segment_map}
            """)
        
        output_digits = []
        for output_signal in signals_to_decode:
            true_segments = "".join(sorted([self.segment_map[char] for char in output_signal]))
            output_digits.append(TRUE_SEGMENT_TO_DIGIT_MAP[true_segments])

        return output_digits