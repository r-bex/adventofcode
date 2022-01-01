import datetime as dt

BLANK_LINE = ""

def load_input(path="data.txt",
                remove_newlines=True,
                remove_empty_lines=True,
                parsing_func=lambda l: str(l)):
    """Load lines from the specified file and apply parsing_func linewise

        Args:
            path (str): the input data file location. Default = "data.txt"
            remove_newlines (bool): whether to trim the "\n"s from the end of each line. Default = True.
            remove_empty_lines (bool): whether to skip empty lines in input file. Default = True.
            parsing_func (str -> T): a function that takes a string as input
            
        Returns:
            list(T): a list of the files contents after applying the parsing function
    """
    with open(path, 'r') as f:
        lines = f.readlines()
    f.close()

    if remove_newlines:
        lines = [l.replace("\n", "") for l in lines]

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

def flatten_nested_list(nl):
    """Flatten a nested list into a single list

    NB: will only flatten one layer deep, not recursively

    Args:
        nl (list(list)): a list of lists

    Returns:
        list: a single flattened list
    """

    return [item for l in nl for item in l]

def bidirectional_inclusive_range(start, end):
    """Generate inclusive range as list, increasing or decreasing

    Examples: (7,9) -> [7, 8, 9] and (9, 7) -> [9, 8, 7]
    
    Args:
        start (int): the start of the range
        end (int): the end of the range

    Returns:
        list(int): list of numbers in inclusive range
    """
    if end > start:
        return list(range(start, end + 1))
    else:
        return list(range(start, end - 1, -1))

def time_execution(n_measurements, func, *args, **kwargs):
    """Time function call with args provided and print stats

    NB: timeit does this better but is fiddly to use in scripts

    Args:
        n_measurements (int): the number of measurements to take
        func (function): the function to call
        *args (tuple of args): arguments to pass to this function
        **kwargs (dict of kwargs): key word arguments to pass to this function

    Returns:
        None
    """
    times_microseconds = []
    for i in range(n_measurements):
        time_before = dt.datetime.now()
        func(*args, **kwargs)
        time_after = dt.datetime.now()
        times_microseconds.append((time_after - time_before).microseconds)
    print(f"Min: {min(times_microseconds)} us")
    print(f"Min: {max(times_microseconds)} us")
    print(f"Mean: {sum(times_microseconds)/len(times_microseconds)} us")

