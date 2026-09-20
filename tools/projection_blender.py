# /// script
# dependencies = [
#   "pyproj",
#   "matplotlib",
#   "numpy",
# ]
# ///

"""
# Blend between two map projections and calculate simple distortion factor

Simply edit the code in the marked location '=== EDIT START ===' and '=== EDIT STOP ===' to then run and see a result. It's very dumb, and it very much works

## Pre-requisites
You need to use `uv` to run this file. You can find installation info [here](https://docs.astral.sh/uv/getting-started/installation/).

## Usage

```bash
uv run tools/projection_blender.py
```

## Info

- Author: BurningHot687
- License: MIT
- Version: 0.1.0

Gemini 3.5 Flash was used for a portion of the code. Treat it accordingly. After all, I am learning too, and this is the only way I got for a while.
"""

from pyproj import Transformer

projections_list: dict[str, str] = {"mercator": "EPSG:3857", "mollweide": "ESRI:54009"}


def main():
    # === EDIT START ===

    # `t` is the blend between projection A and projection B
    # Interval [0.0, 1.0]
    t: float = 0.0

    # Choose which projection either a or b should be
    # Use `projections_list` to find the names
    projection_a: str = "mercator"
    projection_b: str = "mercator"

    # === EDIT STOP ===

    print(
        f"=> New Blended Projection : Blend Factor {t} : Projections {projection_a} & {projection_b}"
    )


if __name__ == "__main__":
    main()
