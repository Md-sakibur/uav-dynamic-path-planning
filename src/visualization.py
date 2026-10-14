
import matplotlib.pyplot as plt


def plot_grid(
    grid,
    path=None,
    save_path="results/environment.png",
    dynamic_obstacle=None,
):
    """Display and save the grid, path, and moving obstacle."""

    fig, ax = plt.subplots(figsize=(8, 8))

    # Display free cells and static obstacles.
    ax.imshow(grid, cmap="Greys", vmin=0, vmax=1)

    # Draw the UAV's planned or executed path.
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
            label="UAV Path",
            zorder=2,
        )

    # Highlight the dynamic obstacle with an orange X.
    if dynamic_obstacle is not None:
        row, col = dynamic_obstacle

        ax.scatter(
            col,
            row,
            marker="X",
            color="orange",
            s=180,
            edgecolors="black",
            label="Moving obstacle",
            zorder=4,
        )

    # Mark the UAV's starting position.
    ax.scatter(
        0,
        0,
        color="green",
        s=120,
        edgecolors="black",
        label="Start",
        zorder=3,
    )

    # Mark the destination.
    goal_x = grid.shape[1] - 1
    goal_y = grid.shape[0] - 1

    ax.scatter(
        goal_x,
        goal_y,
        color="red",
        s=120,
        edgecolors="black",
        label="Goal",
        zorder=3,
    )

    ax.set_title("UAV Dynamic Path Planning")
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")

    ax.set_xticks(range(grid.shape[1]))
    ax.set_yticks(range(grid.shape[0]))

    ax.grid(True, linewidth=0.4, alpha=0.5)
    ax.legend()
    plt.tight_layout()

    # Save the visualization before displaying it.
    fig.savefig(save_path, dpi=200, bbox_inches="tight")
    plt.show()
    plt.close(fig)
