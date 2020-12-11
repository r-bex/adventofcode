import sys
sys.path.append("..")
from utils.utils import load_input

FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

apply_direction = lambda coord, direction: (coord[0] + direction[0], coord[1] + direction[1])


def is_direction_occupied(grid, coord, direction, immediate_only):
    """Check whether the nearest seat in a given direction is occupied

        Args:
            grid (list(list(int)): the seat layout as a 2d array
            coord (int, int): the reference coordinate/seat
            direction (int, int): the direction to check, as row & column deltas
            immediate_only (bool): if True, only consider space immediately adjacent.
                If False, consider nearest seat in direction, if it exists.

        Returns:
            bool - whether the nearest seat from the coord in the given direction
                is occupied or not 
    """
    num_rows = len(grid)
    num_cols = len(grid[0])

    in_bounds = True
    while in_bounds:
        (new_row, new_col) = apply_direction(coord, direction)
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            if grid[new_row][new_col] == OCCUPIED:
                return True
            
            if grid[new_row][new_col] == EMPTY:
                return False

            if immediate_only:
                return False
            
            coord = (new_row, new_col)
        else:
            # have reached edge of bounds
            in_bounds = False
    return False


def calculate_next_state(current_state, num_occupied_neighbours, occupation_tolerance):
    """Use current state and neighbour states to calculate new state according to rules

        Args:
            current_state (str): either '.', 'L' or '#'
            num_occupied_neighbours (int): number of adjacent occupied seats
            occupation_tolerance (int): if at least this many adjacent seats are
                occupied the current state will flip from occupied to empty

        Returns:
            str: the next state of the current position, either '.', 'L' or '#'
    """
    if current_state == EMPTY and num_occupied_neighbours == 0:
        return OCCUPIED
    elif current_state == OCCUPIED and num_occupied_neighbours >= occupation_tolerance:
        return EMPTY
    else:
        return current_state


def iterate(grid, occupation_tolerance, immediate_only):
    """Take the current grid state, apply iteration rules and return new grid state

        Args:
            grid (list(list(string)): the current grid state, as a 2D array of strings
            occupation_tolerance (int): if at least this many adjacent seats are
                occupied the current state will flip from occupied to empty
            immediate_only (bool): whether to consider only immediately adjacent spaces,
                seats or otherwise (True), or to consider nearest seats by direction (False)

        Returns:
            list(list(string)): the next grid state
            bool: whether the new grid is different to the incoming grid
    """    
    new_grid = []
    for row_index, row in enumerate(grid):
        new_row = []
        for column_index, current_state in enumerate(row):
            num_occupied_directions = [
                is_direction_occupied(grid, (row_index, column_index), dirn, immediate_only) for dirn in DIRECTIONS
            ].count(True)
            new_row.append(calculate_next_state(current_state, num_occupied_directions, occupation_tolerance))
        new_grid.append(new_row)
    
    return (new_grid, new_grid == grid)


def count_occupied_seats_after_iterations(initial_grid, occupation_tolerance, immediate_only):
    """Iterate grid by rules and count total occupied seats once stabilised

        Args:
            initial_grid (list(list(int))): the seat grid as a 2d array
            occupation_tolerance (int): if at least this many seats adjacent to an
                occupied seat are also occupied, the seat will become empty
            immediate_only (bool): whether to consider only immediately adjacent spaces,
                seats or otherwise (True), or to consider nearest seats by direction (False)

        Returns:
            int - the total occupied seats once grid has stabilised
    """
    iterate_grid = True
    grid = initial_grid

    while iterate_grid:
        grid, grid_changed = iterate(grid, occupation_tolerance, immediate_only)
        if grid_changed:
            iterate_grid = False

    return sum([row.count(OCCUPIED) for row in grid])


def part1(initial_grid):
    # iterate based only on immediate neighbours
    return count_occupied_seats_after_iterations(initial_grid, occupation_tolerance=4, immediate_only=True)

def part2(initial_grid):
    # iterate based on nearest visible seats
    return count_occupied_seats_after_iterations(initial_grid, occupation_tolerance=5, immediate_only=False)


if __name__ == "__main__":
    # run test against provided example
    example_input = load_input(path="example.txt")
    assert part1(example_input) == 37
    assert part2(example_input) == 26

    # run against real data
    values = load_input()
    print("Part 1: {}".format(part1(values)))
    print("Part 2: {}".format(part2(values)))
