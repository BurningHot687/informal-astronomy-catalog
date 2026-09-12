# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""
# Combine `.img` and `.lbl` into `.fits`

Enter a file location and it will combine the two into a `.fits`. You may enter either the `.img` or the `.lbl`, provided they have the same file name and are in the same directory.

You may also enter a directory location and it will automatically loop over all files and combine them.

## Pre-requisites
You need to use `uv` to run this file. You can find installation info [here](https://docs.astral.sh/uv/getting-started/installation/).

## Usage

```bash
uv run tools/img_lbl_to_fits.py <path>
```

## Info

- Author: BurningHot687
- License: MIT
- Version: 0.1.0
"""


def main():
    print("Hello world")


if __name__ == "__main__":
    main()
