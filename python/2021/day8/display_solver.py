from collections import Counter

from utils import utils

#   0:      1:      2:      3:      4:      5:      6:      7:      8:      9:
#  aaaa    ....    aaaa    aaaa    ....    aaaa    aaaa    aaaa    aaaa    aaaa
# b    c  .    c  .    c  .    c  b    c  b    .  b    .  .    c  b    c  b    c
# b    c  .    c  .    c  .    c  b    c  b    .  b    .  .    c  b    c  b    c
#  ....    ....    dddd    dddd    dddd    dddd    dddd    ....    dddd    dddd
# e    f  .    f  e    .  .    f  .    f  .    f  e    f  .    f  e    f  .    f
# e    f  .    f  e    .  .    f  .    f  .    f  e    f  .    f  e    f  .    f
#  gggg    ....    gggg    gggg    ....    gggg    gggg    ....    gggg    gggg

# ---- TERMINOLOGY -----
# Display = a sequence of 4 digits/signals
# Signal = a combination of segments, representing a digit. e.g. 'gde' or 'ACF'
# Segment = an edge in the digit representation, e.g. the top bar 'A'
# Signal segments = the "scrambled" incoming segments e.g. 'gde' for 7
# True segments = the true position of the edge in the digit e.g. 'ACF' for 7
# If no scrambling was happening, it'd be a -> A, b -> B and so on

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
    """Builds segment map from input signals and then decodes display signals

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

        # this dictionary will store a map from signal segment to true segment
        self.segment_map = {}
        self._solve_map()

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
            print("All expected keys present? ", all_keys)
            print("All expected values present? ", all_values)

        return all_keys and all_values

    def _get_signals_by_length(self, length):
        """Return the subset of the input signals with with length X"""
        return [s for s in self.input_signals if len(s) == length]

    def _get_signal_segments_by_frequency(self, frequency):
        """Return the signal segments that appear X times across all input signals"""
        flat_list = utils.flatten_nested_list(self.input_signals)
        frequencies = Counter(flat_list)
        return [char for (char, freq) in frequencies.items() if freq == frequency]

    def _add_mapping(self, signal_segment, true_segment):
        """This function is just to add debug option without repeating 7 times"""
        if self.debug:
            print(f"Adding {signal_segment} -> {true_segment} to segment mapping")
        self.segment_map[signal_segment] = true_segment

    def _solve_map(self):
        """Apply logic to decode input signals and build map"""
        if self.debug:
            print(self.input_signals)

        # A is the segment in the 3-length but not 2-length signals
        l3 = self._get_signals_by_length(3)[0]
        l2 = self._get_signals_by_length(2)[0]
        a = set(l3).difference(set(l2)).pop()
        self._add_mapping(a, "A")

        # F is the only segment that is in 9 of the 10 digits
        f = self._get_signal_segments_by_frequency(9)[0]
        self._add_mapping(f, "F")

        # B is the only segment in exactly 6 of the 10 digits
        b = self._get_signal_segments_by_frequency(6)[0]
        self._add_mapping(b, "B")

        # E is the only segment in exactly 4 of the 10 digits
        e = self._get_signal_segments_by_frequency(4)[0]
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

    def translate_signals(self, display_signals):
        """Use the solved mapping to decode display signals

        Args:
            display_signals (list(str)): 4 signals that require decoding

        Returns:
            list(int): the corresponding 4 digits, decoded
        """
        if not self._is_solved():
            raise Exception(f"""
                Right hand signals cannot be decoded before
                map is solved. Current map: {self.segment_map}
            """)
        
        display_digits = []
        for display_signal in display_signals:
            true_segments = "".join(sorted([self.segment_map[char] for char in display_signal]))
            display_digits.append(TRUE_SEGMENT_TO_DIGIT_MAP[true_segments])

        return display_digits