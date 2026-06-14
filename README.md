# metadata-eraser

Remove metadata from image files.

## Setup

```bash
python3 -m pip install -r requirements.txt
```

## Usage

```bash
python3 metadata_eraser.py photo.jpg screenshot.png --output-dir cleaned
```

Each cleaned file is written with a `_clean` suffix in the selected output directory.
