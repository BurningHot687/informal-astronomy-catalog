# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "astropy>=8.0",
#   "pdr>=1.4"
# ]
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

Gemini 3.5 Flash was used for a portion of the code. Treat it accordingly. After all, I am learning too, and this is the only way I got for a while.
"""

import sys
from pathlib import Path

import pdr
from astropy.io import fits


def process_file(file_path: Path) -> None:
    """Accepts a single file and converts into a `.fits` file"""
    print(f"Reading `{file_path.name}`")

    try:
        dataset = pdr.read(str(file_path))
        print(f"Keys: {list(dataset.keys())}")

        # Apparently IMAGE key is actually image, who would've guessed?
        image_data = dataset["IMAGE"]
        fits_header = fits.Header()
        pds_metadata = dataset.metadata

        for key, value in pds_metadata.items():
            # I have no clue what I'm doing, forgive me later
            if not isinstance(value, (str, int, float)):
                value = str(value)

            fits_header[key] = value

        hdu = fits.PrimaryHDU(image_data, header=fits_header)

        output_path: Path = file_path.with_suffix(".fits")
        hdu.writeto(output_path, overwrite=True)
        print(f"Saved `{output_path.name}`")
    except Exception as e:
        print(f"[ERROR : pdr] {e}")
        sys.exit(1)


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "[ERROR: in] Path not provided\n\nUsage:\n    `uv run tools/img_lbl_to_fits.py <path>"
        )
        sys.exit(1)

    raw_input: str = sys.argv[1]
    target_path: Path = Path(raw_input).expanduser().resolve()

    if not target_path.exists():
        print(f"[ERROR: path] Path `{target_path}` does not exist")
        sys.exit(1)

    if target_path.is_file():
        process_file(target_path)
    elif target_path.is_dir():
        all_labels: list[Path] = list(
            set(target_path.glob("*.lbl")) | set(target_path.glob("*.LBL"))
        )

        # What? This is possible, cool.
        # I am used to someting more akin to
        # if len(all_labels) == 0
        if not all_labels:
            print(f"[warn] No files found in `{target_path}`")
            sys.exit(0)

        print(f"Found {len(all_labels)} labels. Starting batch conversion...")

        success_count = 0
        for label in all_labels:
            try:
                print(f"-> Starting conversion of {label}")
                process_file(label)
                success_count += 1
            except SystemExit:
                print(f"[ERROR] Skipped {label}")
                continue

        print(
            f"Batch conversion completed. {success_count}/{len(all_labels)} successful"
        )


if __name__ == "__main__":
    main()
