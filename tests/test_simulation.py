from src.simulation import run_dynamic_demo


def test_dynamic_simulation_completes_without_collision():
    metrics = run_dynamic_demo(
        seed=42,
        show_plot=False,
    )

    assert metrics["success"] is True
    assert metrics["collision_count"] == 0
    assert metrics["replanning_count"] > 0
    assert metrics["dynamic_obstacle_moves"] > 0
    assert metrics["path_length"] >= metrics["initial_path_length"]