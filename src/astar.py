
import heapq


def heuristic(position, goal):
    """Estimate distance using Manhattan distance."""
    return (
        abs(position[0] - goal[0])
        + abs(position[1] - goal[1])
    )


def get_neighbors(position, rows, cols):
    """Return valid up, down, left and right neighbors."""
    row, col = position

    candidates = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1),
    ]

    return [
        (r, c)
        for r, c in candidates
        if 0 <= r < rows and 0 <= c < cols
    ]


def astar(grid, start=(0, 0), goal=None):
    """
    Find a shortest path through a grid using A*.

    0 = free cell
    1 = obstacle

    Returns a list of (row, column) coordinates,
    or None if no path exists.
    """
    rows, cols = grid.shape

    if goal is None:
        goal = (rows - 1, cols - 1)

    for row, col in (start, goal):
        if not (0 <= row < rows and 0 <= col < cols):
            raise ValueError("Start or goal is outside the grid.")

    if grid[start] == 1 or grid[goal] == 1:
        return None

    open_heap = [(heuristic(start, goal), 0, start)]
    came_from = {}
    g_score = {start: 0}
    closed_set = set()

    while open_heap:
        _, current_cost, current = heapq.heappop(open_heap)

        if current_cost != g_score.get(current):
            continue

        if current == goal:
            path = [goal]

            while path[-1] != start:
                path.append(came_from[path[-1]])

            path.reverse()
            return path

        closed_set.add(current)

        for neighbor in get_neighbors(current, rows, cols):
            if grid[neighbor] == 1 or neighbor in closed_set:
                continue

            new_cost = current_cost + 1

            if new_cost < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = new_cost

                priority = new_cost + heuristic(neighbor, goal)

                heapq.heappush(
                    open_heap,
                    (priority, new_cost, neighbor)
                )

    return None
