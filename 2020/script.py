def load_input(parsing_func, path="data.txt"):
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
    non_empty = [l for l in lines if len(l.replace("\n", "")) > 0]
    return list(map(parsing_func, non_empty))


def part1(???):
    return ???


def part2(???):
    return ???


if __name__ == "__main__":
    parse_line = ???

    # run test against provided example
    example_input = load_input(parse_line, path="example.txt")
    assert example_input == ???

    # run against real data
    values = load_input(parse_line)
    print("part 1: {}".format(part1(values)))
    print("part 2: {}".format(part2(values)))