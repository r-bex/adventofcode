BLANK_LINE = ""

def load_input(path="data.txt",
               remove_empty_lines=True,
               parsing_func=lambda l: l.replace("\n", "")):
    """Load lines from the specified file and apply parsing_func linewise

        Args:
            parsing_func (str -> T): a function that takes a string as input
            path (str): the input data file location. Default = "data.txt"

        Returns:
            list(T): a list of the files contents after applying the parsing function
    """
    with open(path, 'r') as f:
        lines = f.readlines()
    f.close()

    if remove_empty_lines:
        lines = [l for l in lines if len(l.replace("\n", "")) > 0]

    if parsing_func:
        return list(map(parsing_func, lines))
    else:
        return lines

def chunk_lines_by_blanks(lines):
    """Take list of lines (strings) and use empty ones to split into groups

        Args:
            list(str): lines of the input file
        
        Returns:
            list(list(str)): split into groups
    """
    # remove start or end blank lines
    if lines[0] == BLANK_LINE:
        lines = lines[1:]
    if lines[-1] == BLANK_LINE:
        lines = lines[:-1]

    chunks = []
    while BLANK_LINE in lines:
        blank_index = lines.index(BLANK_LINE)
        chunks.append(lines[0:blank_index])
        lines = lines[blank_index + 1:]
    chunks.append(lines) # add remainder without blank lines in
    return chunks

def sliding_windows_across_list(l, window_size=2, as_tuples=False):
    """Return list of window-size slices spanning list l

        Args:
            l (list(T)): the list to be windowed
            window_size (int): the desired window size
            as_tuples (bool): if True, windows returned as tuples

        Returns:
            list(list(T)): a list of rolling windows of size
                window_size across list l. Unless as_tuples in which
                case list of tuples
    """
    if window_size > len(l):
        raise ValueError("Window size should be smaller than list")
    
    windows = [
        l[window_start:window_start+window_size]
        for window_start in range(0, len(l) - window_size + 1)
    ]
    if as_tuples:
        windows = [tuple(w) for w in windows]

    return windows
