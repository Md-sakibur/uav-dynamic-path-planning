from src.metrics import calculate_metrics


def test_calculate_metrics():
    metrics = calculate_metrics(
        success=True,
        initial_path_length=10,
        path_length=12,
        planning_times_ms=[1.0, 3.0],
        replanning_count=2,
        collision_count=0,
        dynamic_obstacle_moves=4,
    )

    assert metrics["success"] is True
    assert metrics["initial_path_length"] == 10
    assert metrics["path_length"] == 12
    assert metrics["planning_calls"] == 2
    assert metrics["total_planning_time_ms"] == 4.0
    assert metrics["average_planning_time_ms"] == 2.0
    assert metrics["replanning_count"] == 2
    assert metrics["collision_count"] == 0
    assert metrics["dynamic_obstacle_moves"] == 4