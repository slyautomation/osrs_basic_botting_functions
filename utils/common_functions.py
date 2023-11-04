import cv2
import numpy as np
import pyautogui
from PIL import Image, ImageGrab
from shapely import Polygon
import random

image_ranges = {
    #       left, up, right, bottom
    'default': (0, 0, 0, 0),
    'left-half': (0, 0, 1282, 1370),
    # this assumes the screen is on the 2nd half of the window
    'canifis-start-jump': (558, 0, 1000, 1200),
    'canifis-first-jump': (800, 400, 1250, 900),
    'canifis-second-jump': (200, 200, 1840, 900),
    'canifis-third-jump': (0, 0, 768, 1200),
    'canifis-fourth-jump': (0, 0, 950, 1200),
    'canifis-fifth-jump': (200, 0, 1250, 1250),
    'canifis-sixth-jump': (255, 255, 1840, 1100),
    'canifis-final-jump': (0, 0, 768, 1100),
}

def screen_Image(screenSize, name='screenshot.png'):
    if screenSize not in image_ranges:
        raise ValueError(f"{screenSize} is not within the range")
    myScreenshot = ImageGrab.grab() if screenSize == 'default' else ImageGrab.grab(bbox=image_ranges[screenSize])
    myScreenshot.save('images/' + name)


# Define your color ranges in a dictionary
color_ranges = {
    'red': ([0, 0, 180], [80, 80, 255]),
    'green': ([0, 180, 0], [80, 255, 80]),
    'amber': ([0, 200, 200], [60, 255, 255]),
    'pickup_high': ([250, 0, 167], [255, 5, 172]),
    'attack_blue': ([200, 200, 0], [255, 255, 5]),
    'agility':  ([0, 183, 245], [0, 183, 245]),
}


def find_object_precise_new(color_name, screenSize='default'):
    # Check if the color_name is one of the predefined colors
    if color_name not in color_ranges:
        raise ValueError(f"{color_name} is not a valid color name")

    # If the color_name is valid, get the color ranges
    color = color_ranges[color_name]

    screen_Image(screenSize)
    imageDirectory = 'images/screenshot.png'
    image = cv2.imread(imageDirectory)
    image = cv2.rectangle(image, pt1=(600, 0), pt2=(850, 200), color=(0, 0, 0), thickness=-1)
    image = cv2.rectangle(image, pt1=(0, 0), pt2=(150, 100), color=(0, 0, 0), thickness=-1)
    boundaries = [color]

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        ret, thresh = cv2.threshold(mask, 40, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        # find the biggest countour (c) by the area
        c = max(contours, key=cv2.contourArea)
        # print(c)
        # print(np.squeeze(c))
        # print(Polygon(np.squeeze(c)))

        minx, miny, maxx, maxy = Polygon(np.squeeze(c)).bounds
        # print(minx, miny, maxx, maxy)

        x_delta_from_screenshot = image_ranges[screenSize][0]
        y_delta_from_screenshot = image_ranges[screenSize][1]

        x = random.randrange(minx + 1, max(minx + 2, maxx - 1)) + x_delta_from_screenshot
        y = random.randrange(miny + 1, max(miny + 2, maxy - 1)) + y_delta_from_screenshot
        b = random.uniform(0.1, 0.4)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b)
        return (x, y)
    return False
