import csv
from pathlib import Path

import matplotlib

# Batch experiments should save charts without opening
# a separate window for every run.
matplotlib.use("Agg")

import matplotlib.pyplot as plt

from src.simulation import run_dynamic_demo


RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

FIELDNAMES = [
    "seed",
    "success",
    "initial_path_length",
    "path_length",
    "planning_calls",
    "total_planning_time_ms",
    "average_planning_time_ms",
    "replanning_count",
    "collision_count",
    "dynamic_obstacle_moves",
    "error",
]


def main():
    rows = []

    # Run 20 reproducible scenarios.
    for seed in range(42, 62):
        print(f"\nRunning experiment with seed {seed}...")

        try:
            metrics = run_dynamic_demo(
                seed=seed,
                show_plot=False,
            )

            row = {
                "seed": seed,
                **metrics,
                "error": "",
            }

        except RuntimeError as exc:
            # Retain scenarios that the current simulator
            # cannot complete.
            row = {name: "" for name in FIELDNAMES}
            row.update({
                "seed": seed,
                "success": False,
                "error": str(exc),
            })

        rows.append(row)

        print("Success:", row["success"])

        if row["error"]:
            print("Reason:", row["error"])

    # Save every scenario, including failed scenarios.
    csv_path = RESULTS_DIR / "experiment_results.csv"

    with csv_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=FIELDNAMES,
        )
        writer.writeheader()
        writer.writerows(rows)

    successful = [row for row in rows if row["success"]]
    success_rate = 100 * len(successful) / len(rows)

    print("\n--- Experiment Summary ---")
    print("Total scenarios:", len(rows))
    print("Successful scenarios:", len(successful))
    print(f"Success rate: {success_rate:.1f}%")
    print("CSV saved to:", csv_path)

    # Chart 1: success or failure by random seed.
    plt.figure(figsize=(10, 5))
    plt.bar(
        [row["seed"] for row in rows],
        [int(bool(row["success"])) for row in rows],
    )
    plt.xlabel("Random seed")
    plt.ylabel("Success (1 = yes, 0 = no)")
    plt.title("UAV Simulation Success by Seed")
    plt.ylim(0, 1.1)
    plt.tight_layout()
    plt.savefig(
        RESULTS_DIR / "experiment_success.png",
        dpi=200,
    )
    plt.close()

    # Chart 2: executed path length for successful runs.
    if successful:
        plt.figure(figsize=(10, 5))
        plt.bar(
            [row["seed"] for row in successful],
            [row["path_length"] for row in successful],
        )
        plt.xlabel("Random seed")
        plt.ylabel("Executed moves")
        plt.title("Executed Path Length by Seed")
        plt.tight_layout()
        plt.savefig(
            RESULTS_DIR / "experiment_path_length.png",
            dpi=200,
        )
        plt.close()

        # Chart 3: measured A* planning time.
        plt.figure(figsize=(10, 5))
        plt.bar(
            [row["seed"] for row in successful],
            [row["total_planning_time_ms"] for row in successful],
        )
        plt.xlabel("Random seed")
        plt.ylabel("Planning time (ms)")
        plt.title("Measured Planning Time by Seed")
        plt.tight_layout()
        plt.savefig(
            RESULTS_DIR / "experiment_planning_time.png",
            dpi=200,
        )
        plt.close()

    print("Experiment charts saved in:", RESULTS_DIR)


if __name__ == "__main__":
    main()