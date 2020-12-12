import numpy as np

from script import rotate_vector

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

