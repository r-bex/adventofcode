import numpy as np

from utils.utils import load_input

def shift_matrix(m, dir):
    new_row = np.zeros((1, m.shape[1]), dtype=np.int64)
    new_column = np.zeros((m.shape[0], 1), dtype=np.int64)
    if dir == "down":
        new_matrix = np.concatenate((new_row, m[:-1, :]), axis=0)
    elif dir == "up":
        new_matrix = np.concatenate((m[1:, :], new_row), axis=0)
    elif dir == "left":
        new_matrix = np.concatenate((m[:, 1:], new_column), axis=1)
    elif dir == "right":
        new_matrix = np.concatenate((new_column, m[:, :-1]), axis=1)
    return new_matrix


def find_lowest_points(matrix):
    adjacents = np.dstack((
        matrix,
        shift_matrix(matrix, "up"),
        shift_matrix(matrix, "left"),
        shift_matrix(matrix, "down"),
        shift_matrix(matrix, "right"),
    ))
    print(adjacents.shape)
    is_lowest = lambda arr: arr[0] == np.sort(arr)[0]
    mask = is_lowest(adjacents[:,:,:])
    print(mask)

    # apply mask to get places where first item is less than all subsequents


def part1(matrix):
    find_lowest_points(matrix)
    return -1

def part2(matrix):
    return -1

def load_matrix(path="data.txt"):
    parse_line = lambda l: np.array([int(c) for c in l])
    arrs = load_input(path, parsing_func=parse_line)
    return np.array(arrs)

if __name__ == "__main__":
    # load example and real input data
    example_input = load_matrix(path="example.txt")
    real_input = load_matrix()

    # part 1
    assert part1(example_input) == 15
    print("Part 1: {}".format(part1(real_input)))

    # part2
    # assert part2(example_input) == ???
    # print("Part 2: {}".format(part2(real_input)))