import matplotlib.pyplot as plt


def plot_grid(grid):
    """
    Display and save the UAV grid environment.

    0 = free cell
    1 = obstacle
    """

    fig, ax = plt.subplots(figsize=(8, 8))

    # Display free cells and obstacles.
    ax.imshow(grid, cmap="Greys", vmin=0, vmax=1)

    # Mark the starting position.
    ax.scatter(
        0, 0,
        color="green",
        s=120,
        label="Start",
        edgecolors="black"
    )

    # Mark the goal position.
    goal_x = grid.shape[1] - 1
    goal_y = grid.shape[0] - 1

    ax.scatter(
        goal_x, goal_y,
        color="red",
        s=120,
        label="Goal",
        edgecolors="black"
    )

    ax.set_title("UAV Path Planning Environment")
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")
    ax.set_xticks(range(grid.shape[1]))
    ax.set_yticks(range(grid.shape[0]))
    ax.grid(True, linewidth=0.4, alpha=0.5)
    ax.legend()

    plt.tight_layout()

    # Save the image before displaying it.
    fig.savefig(
        "results/environment.png",
        dpi=200,
        bbox_inches="tight"
    )

    plt.show()