# Day 18 - The Hirst Painting Project

## Project Overview

This project is a **Python turtle graphics program** inspired by Damien Hirst’s famous dot paintings.  
It uses the `turtle` module and the `colorgram` library to extract colors from an image and then paint a grid of colorful dots.

The program features:

- Extracting RGB colors from an image using the `colorgram` library
- Storing extracted colors in a list for random selection
- Drawing an **8x8 grid of colored dots** using the `turtle` graphics library
- Dynamic placement of dots with consistent spacing
- A `turtle` screen that remains open until the user clicks to close

---

## How to Use

1. Make sure you have Python installed.
2. Install the required colorgram library
3. Place an inspiration image (e.g., `painting_inspo.jpg`) in the same directory as the script.
4. Run the `main.py` file.
5. The program will:
   - Extract up to 64 colors from the image.
   - Generate an **8x8 dot painting** with randomly selected colors.
6. Click anywhere on the turtle window to exit.

---

## Skills Learned

During this project, I applied and strengthened the following Python skills:

- **Libraries & Modules**: Using `turtle` for graphics and `colorgram` for color extraction
- **Lists & Comprehensions**: Building a list of RGB color tuples
- **Loops**: Nested `for` loops for structured row-by-row drawing
- **Functions from Turtle**: Using `penup()`, `goto()`, `dot()`, and movement controls
- **Randomization**: Randomly selecting colors for each dot
- **Screen Setup**: Configuring the turtle graphics screen with custom dimensions

---

## Files Included

- `main.py` — the Hirst Painting Project program
- `painting_inspo.jpg` — an inspiration image used to extract colors

---

## Author

Sanika Surose
