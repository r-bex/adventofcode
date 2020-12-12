import numpy as np

from script import rotate_vector, rotate_waypoint_about_ship, move_towards_waypoint

direction_vectors = {
    "N": np.array([0, 1]),
    "E": np.array([1, 0]),
    "S": np.array([0, -1]),
    "W": np.array([-1, 0])
}

def test_left_rotation():
    assert np.array_equal(rotate_vector(direction_vectors["N"], 90), direction_vectors["W"])
    assert np.array_equal(rotate_vector(direction_vectors["E"], 90), direction_vectors["N"])
    assert np.array_equal(rotate_vector(direction_vectors["W"], 90), direction_vectors["S"])
    assert np.array_equal(rotate_vector(direction_vectors["S"], 90), direction_vectors["E"])

    assert np.array_equal(rotate_vector(direction_vectors["E"], 180), direction_vectors["W"])
    assert np.array_equal(rotate_vector(direction_vectors["W"], 180), direction_vectors["E"])
    assert np.array_equal(rotate_vector(direction_vectors["S"], 180), direction_vectors["N"])
    assert np.array_equal(rotate_vector(direction_vectors["N"], 180), direction_vectors["S"])

def test_right_rotation():
    assert np.array_equal(rotate_vector(direction_vectors["N"], -90), direction_vectors["E"])
    assert np.array_equal(rotate_vector(direction_vectors["E"], -90), direction_vectors["S"])
    assert np.array_equal(rotate_vector(direction_vectors["W"], -90), direction_vectors["N"])
    assert np.array_equal(rotate_vector(direction_vectors["S"], -90), direction_vectors["W"])

    assert np.array_equal(rotate_vector(direction_vectors["E"], -180), direction_vectors["W"])
    assert np.array_equal(rotate_vector(direction_vectors["W"], -180), direction_vectors["E"])
    assert np.array_equal(rotate_vector(direction_vectors["S"], -180), direction_vectors["N"])
    assert np.array_equal(rotate_vector(direction_vectors["N"], -180), direction_vectors["S"])

def test_waypoint_rotation():
    ship_position = np.array([0, 0])
    waypoint_position = np.array([10, 4])
    new_waypoint_position = rotate_waypoint_about_ship(ship_position, waypoint_position, "R", 90)
    assert np.array_equal(new_waypoint_position, np.array([4, -10]))

def test_movement_towards_waypoint():
    ship_position = np.array([100, 10])
    waypoint_position = np.array([110, 14])
    (new_ship, new_waypoint) = move_towards_waypoint(ship_position, waypoint_position, 7)
    assert np.array_equal(new_ship, np.array([170, 38]))
    assert np.array_equal(new_waypoint, np.array([180, 42]))

    ship_position = new_ship
    waypoint_position = np.array([174, 28])
    (new_ship, new_waypoint) = move_towards_waypoint(ship_position, waypoint_position, 11)
    assert np.array_equal(new_ship, np.array([214, -72]))
    assert np.array_equal(new_waypoint, np.array([218, -82]))
