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