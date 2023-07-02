"""
File: bouncing_ball.py
Name:Andy
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
click = False  # Check if circle not rebound


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global click
    window = GWindow(800, 500, title='bouncing_ball.py')
    circle = GOval(SIZE, SIZE)
    circle.filled = True
    window.add(circle, x=START_X, y=START_Y)
    onmouseclicked(function)
    number = 0
    while True:
        pause(DELAY)
        if number >= 3:  # bouncing ball limit
            break
        if click:
            number += 1
            vy = 0   # vertical speed
            while True:
                circle.move(VX,  vy)
                if circle.x+circle.width >= window.width:  # circle bump into right window
                    window.add(circle, x=START_X, y=START_Y)  # circle move initial position
                    click = False
                    break
                else:
                    vy += GRAVITY
                    if circle.y + circle.height >= window.height and vy > 0:  # circle  bump into bottom window
                        vy *= -REDUCE
                pause(DELAY)


def function(mouse):
    global click
    click = True


if __name__ == "__main__":
    main()
