"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
# constants for the setting
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
# window width and height
WIDTH = 800
HEIGHT = 500

count = 0  # numbers of bouncing
door = 0  # use 'door 'to control mouse click

window = GWindow(800, 500, title='bouncing_ball.py')
# setting the ball
ball = GOval(SIZE, SIZE)
ball.filled = True
ball.fill_color = 'black'
window.add(ball, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    set_ball()
    onmouseclicked(bouncing)


def bouncing(mouse):
    '''
    This function is to make the ball bounce three times.
    '''

    global door,count,ball
    dx = VX
    dy = GRAVITY
    if door == 0 and count < 3: # open the door when number of bouncing is less than three
        door = 1
        window.clear()
        ball = set_ball()
    while door > 0: # when door is open do the following loop
        ball.move(dx, dy)
        dy += GRAVITY
        if ball.y >= HEIGHT-SIZE:
            dy = -(dy*REDUCE)
        if ball.x >= WIDTH and ball.y <= HEIGHT:  # exceed the boundary then we close the door and set up the ball again
            set_ball()
            door = 0
            count += 1
        pause(DELAY)


def set_ball(): # to set the ball
    ball = GOval(SIZE,SIZE)
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    return ball


if __name__ == "__main__":
    main()
