from collections import Counter

from utils.utils import load_input, bidirectional_inclusive_range


def draw_grid(point_counter):
    """Utility function for drawing the current grid from a point Counter"""
    num_cols = max([x for (x, _) in point_counter.keys()]) + 1
    num_rows = max([y for (_, y) in point_counter.keys()]) + 1
    print("------------")
    for row_ind in range(0, num_rows):
        chars = []
        for col_ind in range(0, num_cols):
            chars.append(str(point_counter.get((col_ind, row_ind), ".")))
        print("".join(chars))
    print("------------")

def generate_intermediate_points(pos1, pos2, allow_diagonals=False):
    """Return points on horizontal or vertical line defined by start and end
    
    Args:
        pos1 ((int, int)): tuple of (x, y) coordinate defining start of line
        pos2 ((int, int)): tuple of (x, y) coordinate defining end of line
        allow_diagonals (bool): whether to return intermediate points if 
            incoming line is diagonal. Default = False

    Returns:
        list(tuple): the points that fall on the line specified by start and end
    """
    (x1, y1) = pos1
    (x2, y2) = pos2
    if x1 == x2:
        return [(x1, yi) for yi in range(min([y1, y2]), max([y1, y2]) + 1)]
    elif y1 == y2:
        return [(xi, y1) for xi in range(min([x1, x2]), max([x1, x2]) + 1)]
    else:
        if allow_diagonals:
            x_values = bidirectional_inclusive_range(x1, x2)
            y_values = bidirectional_inclusive_range(y1, y2)
            return list(zip(x_values, y_values))
        else:
            return []

def count_grid_hotspots(coord_pairs, allow_diagonals=False, threshold=2, debug=False):
    """Process incoming lines and count resulting grid points above a threshold

    Args:
        coord_pairs (list(tuple, tuple)): the incoming lines defined by start and
            end (x,y) tuple coordinates
        allow_diagonals (bool): whether to draw diagonal lines. Default = False
        threshold (int): the minimum number of lines to have fallen through a point
            for it to be counted in the final count. Default = 2
        debug (bool): if True, draw grid after every new line. Default = False

    Returns:
        int - the number of points on the grid that have had at least a certain
            number of lines fall on it, set by the threshold variable.
    """
    point_counter = Counter()
    for (pos1, pos2) in coord_pairs:
        new_points = generate_intermediate_points(pos1, pos2, allow_diagonals=allow_diagonals)
        point_counter.update(new_points)
        if debug:
            print(f"Drawing {pos1} -> {pos2} = {new_points}")
            draw_grid(point_counter)
    return len([k for k, v in point_counter.items() if v >= threshold])
    
def part1(coord_pairs, debug=False):
    return count_grid_hotspots(coord_pairs, debug=debug)

def part2(coord_pairs, debug=False):
    return count_grid_hotspots(coord_pairs, allow_diagonals=True, debug=debug)

def parse_coord_pairs(line):
    """Parse e.g. '0,3 -> 5,1' to ((0, 3), (5, 1))"""
    pos1, pos2 = line.split(" -> ")
    x1, y1 = pos1.split(",")
    x2, y2 = pos2.split(",")
    return ((int(x1), int(y1)), (int(x2), int(y2)))

if __name__ == "__main__":
    # load example and real input data
    example_input = load_input(path="example.txt", parsing_func=parse_coord_pairs)
    real_input = load_input(parsing_func=parse_coord_pairs)

    # part 1
    assert part1(example_input) == 5
    print("Part 1: {}".format(part1(real_input)))

    # part2
    assert part2(example_input) == 12
    print("Part 2: {}".format(part2(real_input)))