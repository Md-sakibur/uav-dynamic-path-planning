
import matplotlib.pyplot as plt


def plot_grid(grid, path=None, save_path="results/environment.png"):
    """Display the grid and optionally draw an A* path."""

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.imshow(grid, cmap="Greys", vmin=0, vmax=1)

    # Draw the route before the start and goal markers.
    if path:
        path_rows = [point[0] for point in path]
        path_cols = [point[1] for point in path]

        ax.plot(
            path_cols,
            path_rows,
            color="dodgerblue",
            linewidth=2.5,
            marker="o",
            markersize=3,
            label="A* Path",
        )

    ax.scatter(
        0, 0,
        color="green",
        s=120,
        edgecolors="black",
        label="Start",
        zorder=3,
    )

    goal_x = grid.shape[1] - 1
    goal_y = grid.shape[0] - 1

    ax.scatter(
        goal_x, goal_y,
        color="red",
        s=120,
        edgecolors="black",
        label="Goal",
        zorder=3,
    )

    ax.set_title("UAV A* Path Planning")
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")
    ax.set_xticks(range(grid.shape[1]))
    ax.set_yticks(range(grid.shape[0]))
    ax.grid(True, linewidth=0.4, alpha=0.5)
    ax.legend()

    plt.tight_layout()
    fig.savefig(save_path, dpi=200, bbox_inches="tight")
    plt.show()
