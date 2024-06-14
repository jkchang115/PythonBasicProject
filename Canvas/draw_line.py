"""
File: 
Name:Jack Chang
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 30
# global variable
window = GWindow()
count = 0  # to count the click
current_x = 0 # x axis of current click
current_y = 0 # y axis of current click


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_CircleLine)


def draw_CircleLine(mouse):
    # draw circle(odd click) and line (event click)
    global count
    global current_x
    global current_y
    count += 1
    if count % 2 == 1:  # draw circle
        circle = GOval(SIZE, SIZE)
        circle.filled = False
        circle.color = 'black'
        window.add(circle, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        # record current place(x,y)
        current_x = mouse.x
        current_y = mouse.y
    else:  # remove old circle and draw new line
        old_obj = window.get_object_at(current_x,current_y)  # get old circle object from current place (x,y)
        window.remove(old_obj) # remove it
        line = GLine(current_x,current_y,mouse.x,mouse.y)
        window.add(line)


if __name__ == "__main__":
    main()
