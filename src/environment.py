import numpy as np


def create_grid(rows=20, cols=20, obstacle_probability=0.2, seed=42):
    """
    Create a 2D grid for UAV path planning.

    0 = free cell
    1 = obstacle
    """

    rng = np.random.default_rng(seed)

    grid = (rng.random((rows, cols)) < obstacle_probability).astype(int)

    grid[0, 0] = 0
    grid[rows - 1, cols - 1] = 0

    return grid