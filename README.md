# ARK Survival Ascended Colors

![ASA Colors](https://cdn.discordapp.com/attachments/1071315724208984144/1182279248145297418/asa-color-table.png)

This Python script creates a Tkinter application to display a table with colored cells based on provided data. Each cell represents a color with a specific name, family, and hex code. The table is organized by families, and the colors are sorted based on a color wheel.

## Features

- Each family has its own column in the table.
- Text color in each cell is automatically adjusted for readability.

## Usage

1. Run the Python script using the following command:

    ```bash
    python colors.py
    ```

2. The Tkinter window will open, displaying the color table.


## Requirements

- Python 3.x
- Tkinter library
```bash
    pip install tk
```
- Pillow (PIL) library
```bash
    pip install pillow
```

## Future
- The table is ordered based on a color wheel
  - Something along the lines of the more red the color is the more left it is in the table
- The table is sorted from coldest to warmest color.
  - Darker colors up top transitions down to lighter colors
- The table can be saved as a PNG image.
