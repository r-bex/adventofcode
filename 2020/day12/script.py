import sys
sys.path.append("..")
from utils.utils import load_input

import numpy as np
from scipy.spatial.distance import cityblock

direction_vectors = {
    "N": np.array([0, 1]),
    "E": np.array([1, 0]),
    "S": np.array([0, -1]),
    "W": np.array([-1, 0])
}


def parse_instruction(line):
    line = line.replace("\n", "")
    action = line[0]
    amount = int(line[1:])
    return (action, amount)


def rotate_vector(vector, angle_deg):
    # assumes rotating about origin 0,0
    angle_rads = np.radians(angle_deg)
    rotation_matrix = np.array([
        [np.cos(angle_rads), -np.sin(angle_rads)],
        [np.sin(angle_rads), np.cos(angle_rads)]
    ])
    rotated_vector = np.dot(rotation_matrix, np.transpose(vector))
    return np.int64(np.rint(np.transpose(rotated_vector)))


def part1(instructions, initial_position=(0, 0), initial_bearing=(1,0)):
    position = np.array(initial_position)
    bearing = np.array(initial_bearing)

    for (direction, magnitude) in instructions:
        if direction in ["L", "R"]:
            angle_multiplier = 1 if direction == "L" else -1
            bearing = rotate_vector(bearing, angle_multiplier * magnitude)
        else:
            direction_vector = bearing if direction == "F" else direction_vectors[direction]
            position += magnitude * direction_vector
            
    return cityblock(initial_position, position)

def move_towards_waypoint(ship_position, waypoint_position, magnitude):
    waypoint_offset = waypoint_position - ship_position
    ship_position += magnitude * waypoint_offset
    waypoint_position = ship_position + waypoint_offset
    return (ship_position, waypoint_position)

def rotate_waypoint_about_ship(ship_position, waypoint_position, rotation_direction, rotation_angle):
    waypoint_offset = waypoint_position - ship_position
    angle_multiplier = -1 if rotation_direction == "R" else 1
    new_waypoint_offset = rotate_vector(waypoint_offset, angle_multiplier*rotation_angle)
    new_waypoint_position = ship_position + new_waypoint_offset
    return new_waypoint_position

def part2(instructions, initial_waypoint_position=(10, 1), initial_ship_position=(0, 0)):
    ship_position = np.array(initial_ship_position)
    waypoint_position = np.array(initial_waypoint_position)

    for (direction, magnitude) in instructions:
        if direction in ["L", "R"]:
            # rotate waypoint about ship
            waypoint_position = rotate_waypoint_about_ship(
                ship_position,
                waypoint_position,
                direction,
                magnitude
            )
        elif direction in ["N", "E", "W", "S"]:
            # move waypoint
            waypoint_position += magnitude * direction_vectors[direction]
        elif direction == "F":
            # move in direction of waypoint (waypoint moves with it)
            (ship_position, waypoint_position) = move_towards_waypoint(
                ship_position,
                waypoint_position,
                magnitude
            )

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