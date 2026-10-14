def calculate_metrics(
    *,
    success,
    initial_path_length,
    path_length,
    planning_times_ms,
    replanning_count,
    collision_count,
    dynamic_obstacle_moves,
):
    """Calculate performance metrics for one simulation."""

    planning_calls = len(planning_times_ms)
    total_time = sum(planning_times_ms)

    average_time = (
        total_time / planning_calls
        if planning_calls
        else 0.0
    )

    return {
        "success": bool(success),
        "initial_path_length": initial_path_length,
        "path_length": path_length,
        "planning_calls": planning_calls,
        "total_planning_time_ms": round(total_time, 3),
        "average_planning_time_ms": round(average_time, 3),
        "replanning_count": replanning_count,
        "collision_count": collision_count,
        "dynamic_obstacle_moves": dynamic_obstacle_moves,
    }


def print_metrics(metrics):
    """Print simulation metrics in a readable format."""

    print("\n--- UAV Simulation Performance ---")
    print("Successful journey:", metrics["success"])
    print("Initial path length:", metrics["initial_path_length"], "moves")
    print("Executed path length:", metrics["path_length"], "moves")
    print("Planning calls:", metrics["planning_calls"])
    print("Replanning count:", metrics["replanning_count"])
    print(
        "Total planning time:",
        metrics["total_planning_time_ms"],
        "ms",
    )
    print(
        "Average planning time:",
        metrics["average_planning_time_ms"],
        "ms",
    )
    print("Collision count:", metrics["collision_count"])
    print("Moving obstacle steps:", metrics["dynamic_obstacle_moves"])