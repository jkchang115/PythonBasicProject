"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # ensure space after final year
    xlocat = GRAPH_MARGIN_SIZE + year_index * ((width - GRAPH_MARGIN_SIZE * 2) // len(YEARS))
    return xlocat


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # Draw the horizontal lines at the top and bottom
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # Draw vertical lines and year labels
    for i, year in enumerate(YEARS):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=str(year), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of names, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid
    y_dis = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 # Calculate y-coordinate spacing

    for i, name in enumerate(lookup_names):
        color = COLORS[i % len(COLORS)]

        for j in range(len(YEARS)):
            year = YEARS[j]
            # Get rank for the current year, default to 1001 if not found
            rank = int(name_data[name].get(str(year), 1001))
            # Calculate x and y coordinates for the current year
            x1 = get_x_coordinate(CANVAS_WIDTH, j)
            y1 = GRAPH_MARGIN_SIZE + rank * y_dis if rank <= 1000 else CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            # IF Next year exist, Draw the line
            if j < len(YEARS) - 1:
                next_year = YEARS[j + 1]
                next_rank = int(name_data[name].get(str(next_year), 1001))

                x2 = get_x_coordinate(CANVAS_WIDTH, j + 1)
                y2 = GRAPH_MARGIN_SIZE + next_rank * y_dis if next_rank <= 1000 else CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

                canvas.create_line(x1, y1, x2, y2, fill=color, width=LINE_WIDTH)
            # Draw the name and rank at the current year's position
            name_str = f"{name} {rank if rank <= 1000 else '*'}"
            canvas.create_text(x1 + TEXT_DX, y1, text=name_str, fill=color, anchor=tkinter.SW)

# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
