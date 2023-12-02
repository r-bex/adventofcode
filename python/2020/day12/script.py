import numpy as np
from scipy.spatial.distance import cityblock

from utils.utils import load_input


DIRECTION_VECTORS = {
    "N": np.array([[0], [1]]),
    "E": np.array([[1], [0]]),
    "S": np.array([[0], [-1]]),
    "W": np.array([[-1], [0]])
}


def parse_instruction(line):
    # parse file line into instruction plus value
    line = line.replace("\n", "")
    action = line[0]
    amount = int(line[1:])
    return (action, amount)


def rotate_vector(vector, angle_deg, clockwise):
    """Rotate the provided vector around (0,0) by the provided angle

        Args:
            vector (np.array): vector as numpy array with shape (2,1) i.e. column vector
            angle_deg (int): the angle to rotate by in degrees
            clockwise (bool): if True rotate clockwise, if False anti-clockwise

        Returns:
            vector (np.array): the rotated vector as a numpy column vector
    """
    if clockwise:
        angle_deg = -1 * angle_deg
    angle_rads = np.radians(angle_deg)

    rotation_matrix = np.array([
        [np.cos(angle_rads), -np.sin(angle_rads)],
        [np.sin(angle_rads), np.cos(angle_rads)]
    ])
    rotated_vector = rotation_matrix.dot(vector)
    return np.int64(np.rint(rotated_vector))


def part1(instructions, initial_ship_position=np.array([[0], [0]]), initial_ship_bearing=np.array([[1], [0]])):
    # rotations apply to ship and bearing is tracked
    position = np.array(initial_ship_position)
    bearing = np.array(initial_ship_bearing)

    for (direction, magnitude) in instructions:
        if direction in ["L", "R"]:
            clockwise = direction == "R"
            bearing = rotate_vector(bearing, magnitude, clockwise)
        else:
            direction_vector = bearing if direction == "F" else DIRECTION_VECTORS[direction]
            position += magnitude * direction_vector
            
    return cityblock(initial_ship_position, position)


def part2(instructions, initial_ship_position=np.array([[0], [0]]), initial_waypoint_offset=np.array([[10], [1]])):
    # rotations apply to waypoint and ship -> waypoint offset is tracked
    ship_position = np.array(initial_ship_position)
    waypoint_offset = np.array(initial_waypoint_offset)

    for (direction, magnitude) in instructions:
        if direction in ["L", "R"]:
            clockwise = direction == "R"
            waypoint_offset = rotate_vector(waypoint_offset, magnitude, clockwise)
        elif direction in ["N", "E", "W", "S"]:
            waypoint_offset += magnitude * DIRECTION_VECTORS[direction]
        elif direction == "F":
            ship_position += magnitude * waypoint_offset

    return cityblock(initial_ship_position, ship_position)


if __name__ == "__main__":
    # run test against provided example
    example_input = load_input(path="example.txt", parsing_func=parse_instruction)
    assert part1(example_input) == 25
    assert part2(example_input) == 286

    # run against real data
    instructions = load_input(parsing_func=parse_instruction)
    print("Part 1: {}".format(part1(instructions)))
    print("part 2: {}".format(part2(instructions)))
