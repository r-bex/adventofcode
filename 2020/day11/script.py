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


def is_nearest_seat_in_direction_occupied(grid, coord, direction):
    """Check whether the nearest seat in a given direction is occupied

        Args:
            grid (list(list(int)): the seat layout as a 2d array
            coord (int, int): the reference coordinate/seat
            direction (int, int): the direction to check, as row & column deltas

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
            
            coord = (new_row, new_col)
        else:
            # have reached edge of bounds
            in_bounds = False
    return False


def count_occupied_neighbours(grid, coord, by_visibility=False):
    """Return the coordinates of all seats adjacent to a specified position

        NB: will  be less than 8 if the seat is at the edge of the grid

        Args:
            row (int): the row coord
            col (int): the col coord
            num_rows (int): the total number of rows
            num_cols (int): the total number of cols

        Returns:
            list((int, int)): list of coords of adjacent seats
    """
    num_rows = len(grid)
    num_cols = len(grid[0])

    if by_visibility:
        directions_occupied = [is_nearest_seat_in_direction_occupied(grid, coord, dirn) for dirn in DIRECTIONS]
    else:
        neighbour_coords = [apply_direction(coord, dirn) for dirn in DIRECTIONS]
        in_bounds = [(r, c) for(r, c) in neighbour_coords if 0 <= r < num_rows and 0 <= c < num_cols]
        directions_occupied = [grid[r][c] == OCCUPIED for (r, c) in in_bounds]
    return directions_occupied.count(True)


def calculate_next_state(current_state, occupied_neighbours, occupied_threshold):
    """Use current state and neighbour states to calculate new state according to rules

        Args:
            current_state (str): either '.', 'L' or '#'
            neighbour_states (list(str)): the states of surrounding seats

        Returns:
            str: the next state of the current position, either '.', 'L' or '#'
    """
    if current_state == EMPTY and occupied_neighbours == 0:
        return OCCUPIED
    elif current_state == OCCUPIED and occupied_neighbours >= occupied_threshold:
        return EMPTY
    else:
        return current_state


def iterate(grid, occupied_threshold, by_visibility):
    """Take the current grid state, apply iteration rules and return new grid state

        Args:
            grid (list(list(string)): the current grid state, as a 2D array of strings

        Returns:
            list(list(string)): the next grid state
            bool: whether the new grid is different to the incoming grid
    """    
    new_grid = []
    for row_index, row in enumerate(grid):
        new_row = []
        for column_index, current_state in enumerate(row):
            num_occupied_neighbours = count_occupied_neighbours(grid, (row_index, column_index), by_visibility=by_visibility)
            new_row.append(calculate_next_state(current_state, num_occupied_neighbours, occupied_threshold))
        new_grid.append(new_row)
    
    return (new_grid, new_grid == grid)


def count_occupied_seats_after_iterations(initial_grid, occupied_threshold, by_visibility):
    """Iterate grid by rules and count total occupied seats after stabilising

        Args:
            initial_grid (list(list(int))): the seat grid as a 2d array
            occupied_threshold (int): if at least this many seats adjacent to an
                occupied seat are also occupied, the seat will become empty
            by_visibility (bool): whether to use the immediate adjacent spaces (False)
                or to search for the nearest visible seat in that direction (True)

        Returns:
            int - the number of occupied seats either immediately adjacent or by line of sight
    """
    iterate_grid = True
    grid = initial_grid

    while iterate_grid:
        grid, grid_changed = iterate(grid, occupied_threshold=occupied_threshold, by_visibility=by_visibility)
        if grid_changed:
            iterate_grid = False

    return sum([row.count(OCCUPIED) for row in grid])


def part1(initial_grid):
    # iterate based only on immediate neighbours
    return count_occupied_seats_after_iterations(initial_grid, occupied_threshold=4, by_visibility=False)

def part2(initial_grid):
    # iterate based on nearest visible seats
    return count_occupied_seats_after_iterations(initial_grid, occupied_threshold=5, by_visibility=True)


if __name__ == "__main__":
    # run test against provided example
    example_input = load_input(path="example.txt")
    assert part1(example_input) == 37
    assert part2(example_input) == 26

    # run against real data
    values = load_input()
    print("Part 1: {}".format(part1(values)))
    print("Part 2: {}".format(part2(values)))
