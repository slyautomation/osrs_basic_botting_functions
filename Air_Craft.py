import numpy as np
import cv2
import pyautogui
import random
import time
import argparse

global hwnd
global iflag
global icoord
from PIL import Image
# from matplotlib import pyplot as plt

iflag = False


def find_area_test(rune, event):
    rune_Image()
    # myScreenshot = pyautogui.screenshot()
    # myScreenshot.save(r"C:\Users\MMH\PycharmProjects\osrs-botting\screenshot.png")
    # import the necessary packages
    # construct the argument parse and parse the arguments
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--image", help="path to the image")
    # args = vars(ap.parse_args())
    # load the image
    image = cv2.imread('runeshot.png')
    # image = cv2.imread(args["image"])
    # define the list of boundaries
    # B, G, R
    red = ([0, 0, 180], [80, 80, 255])
    green = ([0, 180, 0], [80, 255, 80])
    amber = ([0, 160, 160], [80, 255, 255])

    ore_list = [red, green, amber]
    boundaries = [ore_list[rune]]

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
        # if (cv2.__version__[0] > 3):
        # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # else:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) != 0:
            print(event)
            # draw in blue the contours that were founded
            # cv2.drawContours(output, contours, -1, 255, 3)

            # find the biggest countour (c) by the area
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)

            # draw the biggest contour (c) in green
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # coal = [8, 10]
            # copper = (2.3, 4.2)
    # show the images
    cv2.imshow("Result", np.hstack([image, output]))
    cv2.waitKey(0)



def to_air_craft():
    c = random.uniform(14, 15)
    x = random.randrange(2000, 2010) - 1280
    print('x: ', x)
    y = random.randrange(170, 180)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(12, 13)
    x = random.randrange(2015, 2025) - 1280
    print('x: ', x)
    y = random.randrange(170, 180)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(13.5, 15)
    x = random.randrange(2000, 2010) - 1280
    print('x: ', x)
    y = random.randrange(170, 180)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(15, 17)
    x = random.randrange(1975, 1985) - 1280
    print('x: ', x)
    y = random.randrange(150, 160)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)
def to_air_craft_2():
    c = random.uniform(6.5, 7.5)
    x = random.randrange(2002, 2008) - 1280
    print('x: ', x)
    y = random.randrange(110, 120)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(9.5, 10.5)
    x = random.randrange(2015, 2025) - 1280
    print('x: ', x)
    y = random.randrange(170, 180)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(9, 10)
    x = random.randrange(2015, 2025) - 1280
    print('x: ', x)
    y = random.randrange(160, 170)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11)
    x = random.randrange(2015, 2025) - 1280
    print('x: ', x)
    y = random.randrange(160, 170)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(14, 15)
    x = random.randrange(1965, 1975) - 1280
    print('x: ', x)
    y = random.randrange(135, 155)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(15, 16)
    x = random.randrange(1990, 2010) - 1280
    print('x: ', x)
    y = random.randrange(155, 165)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

def to_air_craft_3():
    c = random.uniform(7, 8)
    x = random.randrange(2002, 2008) - 1280
    print('x: ', x)
    y = random.randrange(110, 120)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11)
    x = random.randrange(2015, 2025) - 1280
    print('x: ', x)
    y = random.randrange(170, 180)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11)
    x = random.randrange(2015, 2025) - 1280
    print('x: ', x)
    y = random.randrange(160, 170)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11)
    x = random.randrange(2015, 2025) - 1280
    print('x: ', x)
    y = random.randrange(160, 170)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11)
    x = random.randrange(2015, 2025) - 1280
    print('x: ', x)
    y = random.randrange(160, 170)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(15, 17)
    x = random.randrange(1960, 1970) - 1280
    print('x: ', x)
    y = random.randrange(130, 140)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

def to_bank():
    c = random.uniform(12.5, 13.5)
    x = random.randrange(2060, 2070) - 1280
    print('x: ', x)
    y = random.randrange(60, 70)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(12.5, 13.5)
    x = random.randrange(2060, 2070) - 1280
    print('x: ', x)
    y = random.randrange(60, 70)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(12, 13)
    x = random.randrange(2025, 2035) - 1280
    print('x: ', x)
    y = random.randrange(40, 50)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(12, 13)
    x = random.randrange(2030, 2040) - 1280
    print('x: ', x)
    y = random.randrange(40, 50)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(20, 21)
    x = random.randrange(2035, 2045) - 1280
    print('x: ', x)
    y = random.randrange(55, 66)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)

    pyautogui.click(duration=b, button='left')
    time.sleep(c)

def to_bank_2():
    c = random.uniform(10, 11.5)
    x = random.randrange(2060, 2070) - 1280
    print('bank 2 | 1 x: ', x)
    y = random.randrange(75, 90)
    print('bank 2 | 1 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11.5)
    x = random.randrange(2060, 2070) - 1280
    print('bank 2 | 2 x: ', x)
    y = random.randrange(75, 90)
    print('bank 2 | 2 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11.5)
    x = random.randrange(2025, 2035) - 1280
    print('bank 2 | 3 x: ', x)
    y = random.randrange(75, 90)
    print('bank 2 | 3 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11.5)
    x = random.randrange(2000, 2015) - 1280
    print('bank 2 | 4 x: ', x)
    y = random.randrange(75, 90)
    print('bank 2 | 4 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11.5)
    x = random.randrange(2025, 2035) - 1280
    print('bank 2 | 5 x: ', x)
    y = random.randrange(75, 90)
    print('bank 2 | 5 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11.5)
    x = random.randrange(2020, 2030) - 1280
    print('bank 2 | 6 x: ', x)
    y = random.randrange(75, 90)
    print('bank 2 | 6 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11.5)
    x = random.randrange(2025, 2035) - 1280
    print('bank 2 | 7 x: ', x)
    y = random.randrange(75, 90)
    print('bank 2 | 7 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11.5)
    x = random.randrange(2010, 2025) - 1280
    print('bank 2 | 8 x: ', x)
    y = random.randrange(75, 90)
    print('bank 2 | 8 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11.5)
    x = random.randrange(2010, 2025) - 1280
    print('bank 2 | 9 x: ', x)
    y = random.randrange(75, 85)
    print('bank 2 | 9 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11.5)
    x = random.randrange(2025, 2035) - 1280
    print('bank 2 | 10 x: ', x)
    y = random.randrange(75, 90)
    print('bank 2 | 10 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)
def to_bank_3():
    c = random.uniform(10, 11.5)
    x = random.randrange(2010, 2040) - 1280
    print('bank 3 | 1 x: ', x)
    y = random.randrange(50, 70)
    print('bank 3 | 1 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11.5)
    x = random.randrange(2060, 2080) - 1280
    print('bank 3 | 2 x: ', x)
    y = random.randrange(90, 115)
    print('bank 3 | 2 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11.5)
    x = random.randrange(2020, 2040) - 1280
    print('bank 3 | 3 x: ', x)
    y = random.randrange(50, 65)
    print('bank 3 | 3 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11.5)
    x = random.randrange(2025, 2035) - 1280
    print('bank 3 | 4 x: ', x)
    y = random.randrange(65, 80)
    print('bank 3 | 4 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(10, 11.5)
    x = random.randrange(1985, 2010) - 1280
    print('bank 3 | 5 x: ', x)
    y = random.randrange(65, 80)
    print('bank 3 | 5 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)

    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(12, 13)
    x = random.randrange(1995, 2010) - 1280
    print('bank 3 | 6 x: ', x)
    y = random.randrange(65, 80)
    print('bank 3 | 6 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(12, 13)
    x = random.randrange(1995, 2010) - 1280
    print('bank 3 | 7 x: ', x)
    y = random.randrange(65, 80)
    print('bank 3 | 7 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(12, 13)
    x = random.randrange(1995, 2010) - 1280
    print('bank 3 | 8 x: ', x)
    y = random.randrange(65, 80)
    print('bank 3 | 8 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(12, 13)
    x = random.randrange(2025, 2030) - 1280
    print('bank 3 | 9 x: ', x)
    y = random.randrange(65, 80)
    print('bank 3 | 9 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

    c = random.uniform(12, 13)
    x = random.randrange(2025, 2035) - 1280
    print('bank 3 | 10 x: ', x)
    y = random.randrange(65, 80)
    print('bank 3 | 10 y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)
def rune_Image():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("screen.png")
    png = 'screen.png'
    im = Image.open(png)  # uses PIL library to open image in memory

    #im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('runeshot.png')  # saves new cropped image

def find_area(rune, event):
    rune_Image()
    # myScreenshot = pyautogui.screenshot()
    # myScreenshot.save(r"C:\Users\MMH\PycharmProjects\osrs-botting\screenshot.png")
    # import the necessary packages
    # construct the argument parse and parse the arguments
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--image", help="path to the image")
    # args = vars(ap.parse_args())
    # load the image
    image = cv2.imread('runeshot.png')
    # image = cv2.imread(args["image"])
    # define the list of boundaries
    # B, G, R
    red = ([0, 0, 180], [80, 80, 255])
    green = ([0, 180, 0], [80, 255, 80])
    amber = ([0, 200, 200], [60, 255, 255])

    ore_list = [red, green, amber]
    boundaries = [ore_list[rune]]

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
        # if (cv2.__version__[0] > 3):
        # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # else:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) != 0:
            print(event)
            # draw in blue the contours that were founded
            # cv2.drawContours(output, contours, -1, 255, 3)

            # find the biggest countour (c) by the area
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            print('x:', x, ' | y: ', x + w)
            # draw the biggest contour (c) in green
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # coal = [8, 10]
            # copper = (2.3, 4.2)

            c = random.uniform(0.12, 0.2)
            b = random.uniform(0.1, 0.35)
            wi = round(x + (w / 2))
            x = random.randrange(wi - 10, wi + 10) # 950,960
            print('x: ', x)

            hi = round(y + (h / 2))
            y = random.randrange(hi - 10, hi + 10)# 490,500
            print('y: ', y)
            pyautogui.moveTo(x, y, duration=b)
            b = random.uniform(0.07, 0.11)
            pyautogui.click(duration=b, button='left')
            time.sleep(c)
    # show the images
    # cv2.imshow("Result", np.hstack([image, output]))
    # cv2.waitKey(0)

def find_area_custom(rune, event, l, t):
    rune_Image()
    # myScreenshot = pyautogui.screenshot()
    # myScreenshot.save(r"C:\Users\MMH\PycharmProjects\osrs-botting\screenshot.png")
    # import the necessary packages
    # construct the argument parse and parse the arguments
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--image", help="path to the image")
    # args = vars(ap.parse_args())
    # load the image
    image = cv2.imread('runeshot.png')
    # image = cv2.imread(args["image"])
    # define the list of boundaries
    # B, G, R
    red = ([0, 0, 180], [80, 80, 255])
    green = ([0, 180, 0], [80, 255, 80])
    amber = ([0, 200, 200], [60, 255, 255])

    ore_list = [red, green, amber]
    boundaries = [ore_list[rune]]

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
        # if (cv2.__version__[0] > 3):
        # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # else:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) != 0:
            print(event)
            # draw in blue the contours that were founded
            # cv2.drawContours(output, contours, -1, 255, 3)

            # find the biggest countour (c) by the area
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            # draw the biggest contour (c) in green
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # coal = [8, 10]
            # copper = (2.3, 4.2)

            c = random.uniform(0.12, 0.25)
            b = random.uniform(0.1, 0.3)
            wi = round(x + (w / 2))
            x = random.randrange(wi - 10, wi + 10) # 950,960
            print('x: ', x)

            hi = round(y + (h / 2))
            y = random.randrange(hi - l, hi + t)# 490,500
            print('y: ', y)
            pyautogui.moveTo(x, y, duration=b)
            b = random.uniform(0.07, 0.11)
            pyautogui.click(duration=b, button='left')
            time.sleep(c)
    # show the images
    # cv2.imshow("Result", np.hstack([image, output]))
    # cv2.waitKey(0)

def exit_bank():
    print('exit bank')
    c = random.uniform(0.3, 0.7)
    x = random.randrange(523, 540)
    print('x: ', x)
    y = random.randrange(40, 55)
    print('y: ', y)
    b = random.uniform(0.15, 0.5)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.19)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

def pick_item(v, u):
    c = random.uniform(0.3, 0.7)
    d = random.uniform(0.05, 0.15)
    x = random.randrange(v - 10, v + 10)
    print('x: ', x)
    y = random.randrange(u - 5, u + 5)
    b = random.uniform(0.2, 0.6)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)

def make_runes():
    c = random.uniform(1.5, 2)
    time.sleep(c)
    find_area(2, 'enter rune area')
    c = random.uniform(6.5, 7.5)
    time.sleep(c)
    find_area(1, 'enter rune area')
    c = random.uniform(4, 5)
    time.sleep(c)

def making_air_runes():
    a = random.randrange(1, 3)
    options = {1 : to_air_craft,
               2 : to_air_craft_2,
               3 : to_air_craft_3
               }
    options[a]()
    find_area_custom(2, 'air alter', 40, 40)
    c = random.uniform(6.5, 7.5)
    time.sleep(c)
    make_runes()
    b = random.randrange(1, 3)
    options = {1: to_bank,
               2: to_bank_2,
               3: to_bank_3
               }
    options[b]()
    find_area_custom(1, 'bank booth', 0, 5)
    c = random.uniform(6.5, 7.5)
    time.sleep(c)
    pick_item(1770-1280, 635)
    pick_item(1655-1280, 194)

    exit_bank()

#find_area_test(2, 'enter rune area')

#to_air_craft_3()
#"""



j = 0
while j < 10:
    making_air_runes()
#"""

