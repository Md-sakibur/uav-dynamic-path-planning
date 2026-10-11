
import numpy as np

from src.astar import astar, get_neighbors, heuristic


def test_heuristic():
    assert heuristic((0, 0), (3, 4)) == 7


def test_neighbors_stay_inside_grid():
    neighbors = get_neighbors((0, 0), rows=3, cols=3)

    assert set(neighbors) == {(1, 0), (0, 1)}


def test_astar_finds_valid_path():
    grid = np.array([
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
    ])

    path = astar(grid, start=(0, 0), goal=(3, 3))

    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (3, 3)

    # Every path cell must be free.
    for row, col in path:
        assert grid[row, col] == 0

    # Each move must be to an adjacent cell.
    for current, nxt in zip(path, path[1:]):
        distance = (
            abs(current[0] - nxt[0])
            + abs(current[1] - nxt[1])
        )
        assert distance == 1


def test_astar_returns_none_when_blocked():
    grid = np.array([
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ])

    path = astar(grid, start=(0, 0), goal=(0, 2))

    assert path is None
