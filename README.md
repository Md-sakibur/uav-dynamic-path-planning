

\# UAV Dynamic Path Planning and Obstacle Replanning



A Python-based grid simulation for studying UAV path planning, obstacle avoidance, and route replanning in changing environments.



This project extends a static path-planning prototype with a controlled dynamic-obstacle simulation, automated tests, performance metrics, and reproducible multi-seed experiments.



> \*\*Project scope:\*\* This is a software simulation prototype. It does not yet implement real-drone control, sensor-based obstacle tracking, motion prediction under uncertainty, or physical flight validation.



\## Objectives



\- Generate reproducible 2D environments containing static obstacles.

\- Find routes using the A\* search algorithm.

\- Simulate an obstacle changing position along an original route.

\- Replan from the UAV's current grid position as the simulated environment changes.

\- Measure route length, planning time, replanning frequency, success, and simulated collisions.

\- Evaluate the simulator over multiple random seeds.



\## Features



\- \*\*Grid environment:\*\* Configurable dimensions and obstacle probability.

\- \*\*A\* path planning:\*\* Four-directional movement with Manhattan-distance heuristic.

\- \*\*Obstacle-triggered replanning:\*\* Recalculate a route when the simulated obstacle changes position.

\- \*\*Visualization:\*\* Display obstacles, UAV route, start, goal, and moving-obstacle position.

\- \*\*Performance metrics:\*\* Record path lengths, planning calls, execution time, replanning count, and collision count.

\- \*\*Batch experiments:\*\* Run multiple seeded scenarios and export results to CSV.

\- \*\*Automated tests:\*\* Verify basic pathfinding, blocked environments, metrics, and one dynamic-simulation scenario.



\## Technologies



\- Python

\- NumPy

\- Matplotlib

\- pytest

\- Git and GitHub



\## Project Structure



```text

uav-dynamic-path-planning/

├── src/

│   ├── \_\_init\_\_.py

│   ├── environment.py

│   ├── astar.py

│   ├── simulation.py

│   ├── metrics.py

│   └── visualization.py

├── tests/

│   ├── test\_astar.py

│   ├── test\_metrics.py

│   └── test\_simulation.py

├── experiments/

│   └── run\_experiments.py

├── results/

│   ├── environment.png

│   ├── astar\_path.png

│   ├── dynamic\_replanning.png

│   ├── experiment\_results.csv

│   ├── experiment\_success.png

│   ├── experiment\_path\_length.png

│   └── experiment\_planning\_time.png

├── docs/

├── main.py

├── requirements.txt

├── README.md

└── .gitignore

```



\## Installation



Python 3.13 was used during development. From the project directory, create and activate a virtual environment.



Windows Command Prompt:



```cmd

py -m venv .venv

.venv\\Scripts\\activate.bat

python -m pip install -r requirements.txt

```



\## Run the Simulation



Run the default dynamic-obstacle demonstration:



```cmd

python main.py

```



Alternatively:



```cmd

python -m src.simulation

```



The simulation generates a grid, calculates an initial route, updates the moving obstacle, and repeatedly replans using A\*. It displays and saves the final visualization to `results/dynamic\_replanning.png`.



\## Run the Experiments



Execute:



```cmd

python -m experiments.run\_experiments

```



The batch runner evaluates 20 random seeds, from 42 through 61, and generates:



\- `results/experiment\_results.csv`

\- `results/experiment\_success.png`

\- `results/experiment\_path\_length.png`

\- `results/experiment\_planning\_time.png`



Scenarios without an initial path are retained as unsuccessful attempts in the experiment results.



\## Run the Tests



Execute:



```cmd

python -m pytest -v

```



The current automated test suite contains six tests covering the A\* heuristic, neighbor boundaries, path validity, unreachable goals, metric calculations, and one dynamic-simulation scenario.



\## Preliminary Experiment Results



In one reported batch of 20 seeds (42–61):



| Result | Observation |

|---|---:|

| Scenarios attempted | 20 |

| Successful journeys | 15 |

| Scenarios with no initial path | 5 |

| Overall success rate | 75% |

| Detected collisions in completed runs | 0 |



These are preliminary results from the current simulator, not a general performance guarantee.



The five unsuccessful scenarios did not have an initial route through their static grid maps. This is distinct from a failure caused by a moving obstacle.



The simulator uses known grid occupancy and selects obstacle updates that preserve the possibility of reaching the goal. Consequently, the reported zero collision count does not establish collision avoidance under arbitrary obstacle motion, imperfect sensing, or real-world flight conditions.



Planning times are machine-dependent and should be interpreted as measurements of this implementation, not as a real-time flight-performance guarantee.



\## Current Limitations



\- The environment is two-dimensional and grid-based.

\- Only four-directional movements are supported.

\- A\* uses known obstacle occupancy rather than sensor-derived observations.

\- The moving obstacle follows a simplified, deterministic update rule.

\- The obstacle update logic avoids choices that make the goal unreachable.

\- There is no explicit obstacle-tracking or motion-prediction model.

\- The simulator does not model UAV dynamics, flight constraints, or sensor noise.

\- No physical drone experiments have been performed.



\## Future Work



Potential research extensions include:



1\. Compare A\* with other path-planning baselines under identical scenarios.

2\. Introduce obstacle-motion uncertainty and imperfect observations.

3\. Add explicit obstacle tracking and short-term motion prediction.

4\. Investigate safer and more responsive replanning strategies.

5\. Study smoother trajectories and realistic UAV motion constraints.

6\. Expand the benchmark and report statistical summaries across more scenarios.



\## Research Context



This prototype provides a baseline for further investigation of dynamic UAV navigation. It is intended to support the exploration of tracking-aware path planning and guidance in uncertain environments. Tracking, prediction, and uncertainty-aware planning remain future research tasks rather than implemented features.



\## Author



Md-sakibur



