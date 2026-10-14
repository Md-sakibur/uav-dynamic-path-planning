
from src.environment import create_grid
from src.astar import astar
from src.visualization import plot_grid


def run_replanning_demo(seed=42):
    """Simulate a new obstacle blocking the UAV's path."""

    grid = create_grid(seed=seed)
    start = (0, 0)
    goal = (grid.shape[0] - 1, grid.shape[1] - 1)

    # Find the original route.
    original_path = astar(grid, start, goal)

    if original_path is None:
        raise RuntimeError("No initial path exists.")

    print("Initial path found: True")
    print("Initial moves:", len(original_path) - 1)

    # Add an obstacle to the original path.
    # Choose a location where an alternative route exists.
    replanned_path = None
    blocked_cell = None

    for cell in original_path[1:-1]:
        updated_grid = grid.copy()
        updated_grid[cell] = 1

        candidate_path = astar(updated_grid, start, goal)

        if candidate_path is not None:
            grid = updated_grid
            blocked_cell = cell
            replanned_path = candidate_path
            break

    if replanned_path is None:
        raise RuntimeError("Could not find a suitable replanning scenario.")

    print("Obstacle added at:", blocked_cell)
    print("Replanning successful: True")
    print("New route moves:", len(replanned_path) - 1)

    # Display and save the new route.
    plot_grid(
        grid,
        replanned_path,
        save_path="results/replanned_path.png",
    )


if __name__ == "__main__":
    run_replanning_demo()
