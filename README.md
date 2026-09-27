# Sorting Algorithm Visualizer

An interactive Python/Pygame demonstration of bubble, insertion, selection, merge, and quick sort. Watch comparisons and swaps while switching between ascending and descending order.

## Run locally

Requires Python 3 and a desktop display.

```bash
git clone https://github.com/FuaadBashi/Sorting-Algorithm-visulaizer.git
cd Sorting-Algorithm-visulaizer
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pygame
python main.py
```

On Windows, activate with `.venv\Scripts\activate`.

## Controls

| Key | Action |
| --- | --- |
| Space | Start sorting |
| R | Generate a new list |
| A / D | Ascending / descending |
| B / I / S / M / Q | Bubble / insertion / selection / merge / quick sort |

## Code to explore

[main.py](main.py) contains the sorting implementations, drawing, and keyboard event loop. Compare how each algorithm advances the visualization and handles the same input.

This is an educational visualization; animation duration is not an algorithm benchmark.
