from time import perf_counter

from src.environment import create_grid
from src.astar import astar
from src.visualization import plot_grid
from src.metrics import calculate_metrics, print_metrics


def run_dynamic_demo(seed=42, max_steps=200, show_plot=True):
    """Simulate a moving obstacle and repeated path replanning."""

    static_grid = create_grid(seed=seed)
    rows, cols = static_grid.shape

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    planning_times_ms = []

    def timed_astar(grid, current, target):
        started = perf_counter()
        result = astar(grid, current, target)
        elapsed_ms = (perf_counter() - started) * 1000

        planning_times_ms.append(elapsed_ms)
        return result

    # Find the initial path.
    initial_path = timed_astar(static_grid, start, goal)

    if initial_path is None:
        raise RuntimeError("No initial path exists.")

    initial_path_length = len(initial_path) - 1

    # Find a path cell we can block without making
    # the destination unreachable.
    dynamic_obstacle = None
    obstacle_index = None

    for index in range(3, len(initial_path) - 1):
        candidate = initial_path[index]

        test_grid = static_grid.copy()
        test_grid[candidate] = 1

        if astar(test_grid, start, goal) is not None:
            dynamic_obstacle = candidate
            obstacle_index = index
            break

    if dynamic_obstacle is None:
        raise RuntimeError(
            "Could not create a safe obstacle scenario."
        )

    obstacle_start = dynamic_obstacle
    current = start
    visited = [start]

    executed_moves = 0
    replanning_count = 0
    collision_count = 0
    dynamic_obstacle_moves = 0
    success = False

    for _ in range(max_steps):
        # Construct the current map with the latest
        # moving-obstacle position.
        active_grid = static_grid.copy()
        active_grid[dynamic_obstacle] = 1

        # Plan a route from the UAV's current position.
        path = timed_astar(active_grid, current, goal)
        replanning_count += 1

        if path is None:
            break

        if current == goal:
            success = True
            break

        if len(path) < 2:
            break

        # Move one cell along the calculated route.
        next_position = path[1]

        # Safety check before movement.
        if active_grid[next_position] != 0:
            collision_count += 1
            break

        current = next_position
        visited.append(current)
        executed_moves += 1

        if current == goal:
            success = True
            break

        # Advance the obstacle along the original path.
        # Only choose a position that preserves a possible
        # route from the UAV's current position to the goal.
        new_obstacle = None
        new_index = None

        for index in range(
            obstacle_index + 1,
            len(initial_path) - 1,
        ):
            candidate = initial_path[index]

            # Do not place the obstacle on the UAV's
            # already visited cells or on the goal.
            if candidate in visited or candidate == goal:
                continue

            test_grid = static_grid.copy()
            test_grid[candidate] = 1

            if astar(test_grid, current, goal) is not None:
                new_obstacle = candidate
                new_index = index
                break

        if new_obstacle is not None:
            dynamic_obstacle = new_obstacle
            obstacle_index = new_index
            dynamic_obstacle_moves += 1

    # Prepare the final grid and remaining planned path.
    final_grid = static_grid.copy()
    final_grid[dynamic_obstacle] = 1

    remaining_path = astar(final_grid, current, goal)
    display_path = list(visited)

    if remaining_path is not None and remaining_path[0] == current:
        display_path.extend(remaining_path[1:])

    plot_grid(
        final_grid,
        display_path,
        save_path="results/dynamic_replanning.png",
        dynamic_obstacle=dynamic_obstacle,
        show=show_plot,
    )

    metrics = calculate_metrics(
        success=success,
        initial_path_length=initial_path_length,
        path_length=executed_moves,
        planning_times_ms=planning_times_ms,
        replanning_count=replanning_count,
        collision_count=collision_count,
        dynamic_obstacle_moves=dynamic_obstacle_moves,
    )

    print("Initial path found: True")
    print("Moving obstacle started at:", obstacle_start)
    print("Final moving obstacle position:", dynamic_obstacle)
    print_metrics(metrics)

    return metrics


if __name__ == "__main__":
    run_dynamic_demo()