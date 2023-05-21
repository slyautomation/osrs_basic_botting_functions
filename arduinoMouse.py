# In seconds. Any duration less than this is rounded to 0.0 to instantly move
# the mouse.
import collections
import ctypes
import platform
import random
import sys
import time
import ctypes.wintypes

import serial

Point = collections.namedtuple("Point", "x y")
Size = collections.namedtuple("Size", "width height")
# FIXES SLOW TIME.SLEEP IN WINDOWS OS
timeBeginPeriod = ctypes.windll.winmm.timeBeginPeriod #new
timeBeginPeriod(1) #new

MINIMUM_DURATION = 0.1
# If sleep_amount is less than MINIMUM_DURATION, time.sleep() will be a no-op and the mouse cursor moves there instantly.
MINIMUM_SLEEP = 0.05

# The number of seconds to pause after EVERY public function call. Useful for debugging:
PAUSE = 0.1  # Tenth-second pause by default.


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))

def linear(n):
    """
    Returns ``n``, where ``n`` is the float argument between ``0.0`` and ``1.0``. This function is for the default
    linear tween for mouse moving functions.

    This function was copied from PyTweening module, so that it can be called even if PyTweening is not installed.
    """

    if not 0.0 <= n <= 1.0:
        raise print("Argument must be between 0.0 and 1.0.")
    return n

def _position():
    """Returns the current xy coordinates of the mouse cursor as a two-integer
    tuple by calling the GetCursorPos() win32 function.

    Returns:
      (x, y) tuple of the current xy coordinates of the mouse cursor.
    """

    cursor = ctypes.wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
    return (cursor.x, cursor.y)

def _size():
    """Returns the width and height of the screen as a two-integer tuple.

    Returns:
      (width, height) tuple of the screen size, in pixels.
    """
    return (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))

def position(x=None, y=None):
    """
    Returns the current xy coordinates of the mouse cursor as a two-integer tuple.

    Args:
      x (int, None, optional) - If not None, this argument overrides the x in
        the return value.
      y (int, None, optional) - If not None, this argument overrides the y in
        the return value.

    Returns:
      (x, y) tuple of the current xy coordinates of the mouse cursor.

    NOTE: The position() function doesn't check for failsafe.
    """
    posx, posy = _position()
    posx = int(posx)
    posy = int(posy)
    if x is not None:  # If set, the x parameter overrides the return value.
        posx = int(x)
    if y is not None:  # If set, the y parameter overrides the return value.
        posy = int(y)
    return Point(posx, posy)

def size():
    """Returns the width and height of the screen as a two-integer tuple.

    Returns:
      (width, height) tuple of the screen size, in pixels.
    """
    return Size(*_size())

def getPointOnLine(x1, y1, x2, y2, n):
    """
    Returns an (x, y) tuple of the point that has progressed a proportion ``n`` along the line defined by the two
    ``x1``, ``y1`` and ``x2``, ``y2`` coordinates.

    This function was copied from pytweening module, so that it can be called even if PyTweening is not installed.
    """
    x = ((x2 - x1) * n) + x1
    y = ((y2 - y1) * n) + y1
    return (x, y)


def last_adjust(x, y, Debug=False):
    posx, posy = _position()
    if Debug:
        print(x,y)
    if posx > x:
        mov_x = x - posx
    else:
        mov_x = posx - x

    if posy > y:
        mov_y = y - posy
    else:
        mov_y = posy - y
    if Debug:
        print(posx - x, posy - y)
    write_read(str(int(mov_x)) + ";" + str(int(mov_y)))
def _moveTo(x, y, Debug=False):
    """Send the mouse move event to Windows by calling SetCursorPos() win32
    function.

    Args:
      button (str): The mouse button, either 'left', 'middle', or 'right'
      x (int): The x position of the mouse event.
      y (int): The y position of the mouse event.

    Returns:
      None
    """
    mov_x = 0
    mov_y = 0
    posx, posy = _position()
    if Debug:
        print(posx, posy)
    if posx > x:
        mov_x = x - posx
    else:
        mov_x = posx - x

    if posy > y:
        mov_y = y - posy
    else:
        mov_y = posy - y

    if Debug:
        print(posx - x, posy - y)
    write_read(str(int(mov_x)) + ";" + str(int(mov_y)))

def _mouseMoveDrag(moveOrDrag, x, y, xOffset, yOffset, duration, tween=linear, Debug=False):


    xOffset = int(xOffset) if xOffset is not None else 0
    yOffset = int(yOffset) if yOffset is not None else 0

    if x is None and y is None and xOffset == 0 and yOffset == 0:
        return  # Special case for no mouse movement at all.

    startx, starty = position()

    x = int(x) if x is not None else startx
    y = int(y) if y is not None else starty

    # x, y, xOffset, yOffset are now int.
    x += xOffset
    y += yOffset

    width, height = size()


    # If the duration is small enough, just move the cursor there instantly.
    steps = [(x, y)]

    if duration > MINIMUM_DURATION:
        # Non-instant moving/dragging involves tweening:
        num_steps = max(width, height)
        if Debug:
            print('num_steps:', num_steps)
        sleep_amount = duration / num_steps
        if sleep_amount < MINIMUM_SLEEP:
            num_steps = int(duration / MINIMUM_SLEEP)
            num_steps = num_steps * 4
            sleep_amount = duration / num_steps
        if Debug:
            print('num_steps:', num_steps)
        steps = [getPointOnLine(startx, starty, x, y, tween(n / num_steps)) for n in range(num_steps)]
        # Making sure the last position is the actual destination.
        steps.append((x, y))

    for tweenX, tweenY in steps:
        if len(steps) > 1:
            # A single step does not require tweening.
            time.sleep(sleep_amount)

        tweenX = int(round(tweenX))
        tweenY = int(round(tweenY))

        if moveOrDrag == "move":
            _moveTo(tweenX, tweenY)
        else:
            raise NotImplementedError("Unknown value of moveOrDrag: {0}".format(moveOrDrag))
    if Debug:
        print("last:", tweenX, tweenY)


def arduino_mouse(x=100, y=100, duration=0.3,button=None,  port='COM5', baudrate=115200, Debug=False):
    global arduino
    #arduino = serial.Serial(port=port, baudrate=baudrate, timeout=.1)
    _mouseMoveDrag('move', x, y, xOffset=0, yOffset=0, duration=duration, tween=linear)
    time.sleep(0.01)
    if Debug:
        print(position())
    if position() != (x, y):
        last_adjust(x, y)
        time.sleep(0.01)
        if Debug:
            print(position())
    if position() != (x, y):
        last_adjust(x, y)
        time.sleep(0.01)
        if Debug:
            print(position())
    c = random.uniform(0.001, 0.01)
    time.sleep(c)

    # l is read by arduino to mean click left and r is to right click
    if button != None:
        if button == 'left':
            write_read(str('l'))
        if button == 'right':
            write_read(str('r'))

port='COM5'
baudrate=115200
arduino = serial.Serial(port=port, baudrate=baudrate, timeout=.1)
if __name__ == "__main__":
    time.sleep(3.5)
    arduino_mouse(x=100, y=150, duration=0.3, button='right', Debug=False, port='COM5', baudrate=115200)
