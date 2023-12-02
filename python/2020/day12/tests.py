import numpy as np

from script import rotate_vector

DIRECTION_VECTORS = {
    "N": np.array([[0], [1]]),
    "E": np.array([[1], [0]]),
    "S": np.array([[0], [-1]]),
    "W": np.array([[-1], [0]])
}

def test_left_rotation():
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["N"], 90), DIRECTION_VECTORS["W"])
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["E"], 90), DIRECTION_VECTORS["N"])
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["W"], 90), DIRECTION_VECTORS["S"])
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["S"], 90), DIRECTION_VECTORS["E"])

    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["E"], 180), DIRECTION_VECTORS["W"])
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["W"], 180), DIRECTION_VECTORS["E"])
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["S"], 180), DIRECTION_VECTORS["N"])
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["N"], 180), DIRECTION_VECTORS["S"])

def test_right_rotation():
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["N"], -90), DIRECTION_VECTORS["E"])
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["E"], -90), DIRECTION_VECTORS["S"])
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["W"], -90), DIRECTION_VECTORS["N"])
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["S"], -90), DIRECTION_VECTORS["W"])

    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["E"], -180), DIRECTION_VECTORS["W"])
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["W"], -180), DIRECTION_VECTORS["E"])
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["S"], -180), DIRECTION_VECTORS["N"])
    assert np.array_equal(rotate_vector(DIRECTION_VECTORS["N"], -180), DIRECTION_VECTORS["S"])

