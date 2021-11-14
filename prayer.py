import random
import time

import cv2
import numpy as np
import pyautogui
import win32gui

#import functions

offset_minimap_x_resize = 72
offset_minimap_y_resize = 81
client_top_border = 30
client_side_border = 50
def get_window(windowname):
    '''Returns the position of the window and the size of the window excluding the borders.'''
    # Get window handle.
    hwnd = win32gui.FindWindow(None, windowname)
    # Set window to foreground.
    win32gui.SetForegroundWindow(hwnd)
    # Get the window size.
    rect = win32gui.GetWindowRect(hwnd)
    # Adjust size for borders
    x = rect[0]
    y = rect[1] + client_top_border
    w = rect[2] - x - client_side_border
    h = rect[3] - y - client_top_border
    return [x, y, w, h]



def find_center_minimap(window_features):
    '''Returns the center of the window, excluding the borders.'''
    x, y, w, h = window_features
    map_center_x = x + (w - offset_minimap_x_resize)
    map_center_y = y + offset_minimap_y_resize
    return [map_center_x, map_center_y]

def get_center_window(window_features):
    '''Returns the center of the window, excluding the borders.'''
    center_x = round(window_features[0] + window_features[2] / 2)
    center_y = round(window_features[1] + window_features[3] / 2)
    return [center_x, center_y]

def get_screenshot():
    """Returns a screenshot with BGR colors"""
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    return image

def find_object_contour(color):
    """Returns the contour of color marked objects on screen."""
    # define the list of boundaries
    # highlight purple = 0 / cyan = 1
    boundaries = [[[200, 0, 100], [255, 30, 190]], [[254, 0, 0], [255, 1, 0]]]
    lower = boundaries[color][0]
    upper = boundaries[color][1]
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    # find the colors within the specified boundaries and apply the mask
    image = get_screenshot()
    mask = cv2.inRange(image, lower, upper)
    _ = cv2.bitwise_and(image, image, mask=mask)
    _, thresh = cv2.threshold(mask, 40, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours

def find_closest_object(color):
    window = get_window('OpenOSRS')
    center_screen = get_center_window(window)
    """Returns the coordinates of the center of the closest object."""
    contours = find_object_contour(color)
    if contours == ():
        return []
    distance = []
    # Compute distance
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        distance.append(np.sqrt((x - center_screen[0]) ** 2 + (y - center_screen[1]) ** 2))
    # Find the closest object
    min_value = min(distance)
    index_min = distance.index(min_value)
    x, y, w, h = cv2.boundingRect(contours[index_min])
    x_center = round(x + w / 2)
    y_center = round(y + h / 2)
    return [x_center, y_center]

def image_Rec_clicker(image, event, iheight, iwidth, threshold, clicker, ispace=5):
    global icoord
    global iflag
    pyautogui.screenshot('screenshot.png')
    img_rgb = cv2.imread('screenshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    pt = None
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    iflag = False
    event = event
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        if pt is None:
            iflag = False
        else:
            iflag = True
            x = random.randrange(iwidth, iwidth + ispace)
            y = random.randrange(iheight, iheight + ispace)
            icoord = pt[0] + iheight + x
            icoord = (icoord, pt[1] + iwidth + y)
            b = random.uniform(0.1, 0.3)
            pyautogui.moveTo(icoord, duration=b)
            b = random.uniform(0.05, 0.15)
            pyautogui.click(icoord, duration=b, button=clicker)
            c = random.uniform(0.6, 1)
            time.sleep(c)
    return iflag

def click_closest_object(color=0):
    """Clicks the marked object that is closest to the player."""
    x,y = find_closest_object(color)
    if x !=0 and y !=0:
        pyautogui.moveTo(x, y, 0.1)
        pyautogui.click()
        return True
    return False


x = 0
while x < 10:
    if click_closest_object(color=0):
        print('got item')  # pick up highlighted loot
        c = random.uniform(5, 8)
        time.sleep(c)
    if image_Rec_clicker('bones_icon.png', 'bury bones', 5, 5, 0.7, 'left', 10):
        c = random.uniform(0.6, 1)
        time.sleep(c)
    c = random.uniform(0.1, 1)
    time.sleep(c)