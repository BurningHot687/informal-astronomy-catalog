# /// script
# dependencies = [
#   "pyproj",
#   "matplotlib",
#   "numpy",
# ]
# ///

"""
# Blend between two map projections and calculate simple distortion factor

Simply edit the code in the marked location '=== EDIT START ===' and '=== EDIT STOP ===' to then run and see a result. It's very dumb, and it very much works.

This was created for 2 reasons:
1. To make experimenting with hybrid projections much easier and more varied
2. To attempt to find a better map projection than Winkel Tripel without having to flip a disc over. This is based on the Princeton study, which should hopefully be contacted at some point to investigate the matter more scientifically. You may find the study [here](https://arxiv.org/abs/2102.08176v1)

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

import sys

from pyproj import Transformer

projections_list: dict[str, str] = {
    "mercator": "EPSG:3857",
    "mollweide": "ESRI:54009",
    "equirectangular": "EPSG:4326",
}


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

    code_a: str | None = projections_list.get(projection_a)
    code_b: str | None = projections_list.get(projection_b)

    if not code_a or not code_b:
        print(
            "[ERROR : in] Could not find one of the projections. Please check for spelling errors and reference `projections_list`."
        )
        sys.exit(1)

    if t > 1.0 or t < 0.0:
        print(f"[ERROR : in] `t` is at {t}, which is outside of the range [0.0, 1.0].")
        sys.exit(1)

    print(
        f"=> New Blended Projection : Blend Factor {t} : Projections {projection_a} & {projection_b}"
    )

    formula_a = Transformer.from_crs("EPSG:4326", code_a, always_xy=True)
    formula_b = Transformer.from_crs("EPSG:4326", code_b, always_xy=True)

    # A test point to be removed later: Sydney, Australia?
    lat, long = -33.86, 151.21
    x_a, y_a = formula_a.transform(long, lat)
    x_b, y_b = formula_b.transform(long, lat)

    x_blend = (1.0 - t) * x_a + t * x_b
    y_blend = (1.0 - t) * y_a + t * y_b

    print(f"=> Test point: Lat {lat} Long {long} : X {x_blend:.3f} Y {y_blend:.3f}")


if __name__ == "__main__":
    main()
