import numpy as np
import cv2
import pyautogui
import random
import time

global hwnd
global iflag
global icoord
from PIL import Image
from functions import mini_map_image, random_breaks, Image_count, mini_map_bool

iflag = False


def determine_position_to_bank():
    if mini_map_bool('air_craft_bank.png', 0.85):
        print('player located @ step 1')
        print("to air alter")
        return 7
    if mini_map_bool('air_craft_mark_1.png', 0.85):
        print('player located @ step 2')
        print("to air alter")
        return 6
    if mini_map_bool('air_craft_mark_2.png', 0.85):
        print('player located @ step 3')
        print("to air alter")
        return 4
    if mini_map_bool('air_craft_mark_3.png', 0.85):
        print('player located @ step 4')
        print("to air alter")
        return 3
    if mini_map_bool('air_craft_mark_4.png', 0.85):
        print('player located @ step 5')
        print("to air alter")
        return 1

    if mini_map_bool('air_craft_mark_6.png', 0.85):
        print('player located @ step 6')
        print("to air alter")
        return 0
    else:
        print('player located @ air alter')
        print("to air alter")
        make_runes()
        return 0

def determine_position_to_airalter():
    if mini_map_bool('air_craft_bank.png', 0.85):
        print('player located @ step 1')
        print("to air alter")
        return 0
    if mini_map_bool('air_craft_mark_1.png', 0.85):
        print('player located @ step 2')
        print("to air alter")
        return 2
    if mini_map_bool('air_craft_mark_2.png', 0.85):
        print('player located @ step 3')
        print("to air alter")
        return 3
    if mini_map_bool('air_craft_mark_3.png', 0.85):
        print('player located @ step 4')
        print("to air alter")
        return 4
    if mini_map_bool('air_craft_mark_4.png', 0.85):
        print('player located @ step 5')
        print("to air alter")
        return 5
    if mini_map_bool('air_craft_mark_5.png', 0.85):
        print('player located @ step 6')
        print("to air alter")
        return 7
    if mini_map_bool('air_craft_mark_6.png', 0.85):
        print('player located @ step 6')
        print("to air alter")
        make_runes()
        return 8
    else:
        print('player located @ air alter')
        print("to air alter")
        make_runes()
        return 8


def invent_enabled():
    return Image_count('inventory_enabled.png', threshold=0.9)


def to_air_craft():
    step = 0
    invent = invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    runes = count_runes()
    if runes > 0:
        step = determine_position_to_airalter()
    else:
        b = 1  # random.randrange(1, 3)
        options = {1: to_bank}
        options[b]()
        find_area_custom(1, 'bank booth', 0, 5)
        c = random.uniform(6.5, 8.5)
        time.sleep(c)
        pick_item(1770 - 1280, 635)
        pick_item(1655 - 1280, 194)
        exit_bank()

    if step == 0:
        while mini_map_image('air_craft_bank.png', -5, -5, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_bank.png', 0, 0, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_bank.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 1 to air alter spot not found")
        print("step 1 to air alter")
        random_breaks(5, 8)
        step = 1

    if step == 1:
        while mini_map_image('air_craft_bank.png', 0, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_bank.png', 0, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_bank.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 2 to air alter spot not found")
        print("step 2 to air alter")
        random_breaks(8, 10)
        step = 2

    if step == 2:
        while mini_map_image('air_craft_mark_1.png', 10, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_1.png', 10, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_1.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 3 to air alter not found")
        print("step 3 to air alter")
        random_breaks(5, 8)
        step = 3

    if step == 3:
        while mini_map_image('air_craft_mark_2.png', 10, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_2.png', 10, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_2.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 4 to air alter not found")
        print("step 4 to air alter")
        random_breaks(5, 8)
        step = 4

    if step == 4:
        while mini_map_image('air_craft_mark_3.png', 0, 40, 0.6, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_3.png', 0, 40, 0.6, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_3.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 5 to air alter not found")
        print("step 5 to air alter")
        random_breaks(5, 8)
        step = 5

    if step == 5:
        while mini_map_image('air_craft_mark_4.png', 0, 15, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_4.png', 0, 15, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_4.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 6 to air alter not found")
        print("step 6 to air alter")
        random_breaks(5, 8)
        step = 6

    if step == 6:
        while mini_map_image('air_craft_mark_4.png', 0, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_4.png', 0, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_4.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 7 to air alter not found")
        print("step 7 to air alter")
        random_breaks(5, 8)
        step = 7

    if step == 7:
        while mini_map_image('air_craft_mark_5.png', -20, 20, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_5.png', -20, 20, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_5.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 8 to air alter not found")
        print("step 8 to air alter")
        random_breaks(12, 15)
        step = 8


def to_bank():
    step = 0
    invent = invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    runes = count_runes()
    if runes == 0:
        step = determine_position_to_bank()
    else:
        make_runes()

    if step == 0:
        while mini_map_image('air_craft_mark_6.png', 40, -10, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_6.png', 40, -10, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_6.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 1 to bank not found")
        print("step 1 to bank")
        random_breaks(10, 13)
        step = 1

    if step == 1:
        while mini_map_image('air_craft_mark_4.png', 0, -5, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_4.png', 0, -5, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_4.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 2 to bank not found")
        print("step 2 to bank")
        random_breaks(8, 10)
        step = 2
    if step == 2:
        while mini_map_image('air_craft_mark_4.png', 30, -15, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_4.png', 30, -15, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_4.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 3 to bank not found")
        print("step 3 to bank")
        random_breaks(5, 8)
        step = 3

    if step == 3:
        while mini_map_image('air_craft_mark_3.png', 5, -10, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_3.png', 5, -10, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_3.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 4 to bank not found")
        print("step 4 to bank")
        random_breaks(5, 8)
        step = 4

    if step == 4:
        while mini_map_image('air_craft_mark_2.png', 10, -10, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_2.png', 10, -10, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_2.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 5 to bank not found")
        print("step 5 to bank")
        random_breaks(5, 8)
        step = 5

    if step == 5:
        while mini_map_image('air_craft_mark_2.png', 5, -25, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_2.png', 5, -25, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_2.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 6 to bank not found")
        print("step 6 to bank")
        random_breaks(5, 8)
        step = 6

    if step == 6:
        while mini_map_image('air_craft_mark_1.png', 5, -15, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_1.png', 5, -15, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_1.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 7 to bank not found")
        print("step 7 to bank")
        random_breaks(5, 8)
        step = 7

    if step == 7:
        while mini_map_image('air_craft_bank.png', 5, 0, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_bank.png', 5, 0, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_bank.png', 0.85) == False:
                print("air alter not found")
                making_air_runes()
            print("step 8 to bank not found")
        print("step 8 to bank")
        random_breaks(8, 10)
        step = 8


def rune_Image():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("screen.png")
    png = 'screen.png'
    im = Image.open(png)  # uses PIL library to open image in memory

    # im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('runeshot.png')  # saves new cropped image


def find_area(rune, event):
    rune_Image()
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
            x = random.randrange(wi - 10, wi + 10)  # 950,960
            print('x: ', x)

            hi = round(y + (h / 2))
            y = random.randrange(hi - 10, hi + 10)  # 490,500
            print('y: ', y)
            pyautogui.moveTo(x, y)
            b = random.uniform(0.07, 0.11)
            pyautogui.click(duration=b, button='left')
            time.sleep(c)
    # show the images
    # cv2.imshow("Result", np.hstack([image, output]))
    # cv2.waitKey(0)


def find_area_custom(rune, event, l, t):
    rune_Image()
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
            x = random.randrange(wi - 10, wi + 10)  # 950,960
            print('x: ', x)

            hi = round(y + (h / 2))
            y = random.randrange(hi - l, hi + t)  # 490,500
            print('y: ', y)
            pyautogui.moveTo(x, y)
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
    c = random.uniform(1.5, 3)
    time.sleep(c)
    find_area(2, 'enter rune area')
    c = random.uniform(6.5, 8)
    time.sleep(c)
    find_area(1, 'enter rune area')
    c = random.uniform(4, 6)
    time.sleep(c)


def count_runes():
    return Image_count('rune_icon.png', threshold=0.8)


def making_air_runes():
    a = 1  # random.randrange(1, 3)
    options = {1: to_air_craft
               }
    options[a]()
    find_area_custom(2, 'air alter', 40, 40)
    c = random.uniform(6.5, 8.5)
    time.sleep(c)
    make_runes()
    b = 1  # random.randrange(1, 3)
    options = {1: to_bank
               }
    options[b]()
    find_area_custom(1, 'bank booth', 0, 5)
    c = random.uniform(6.5, 8.5)
    time.sleep(c)
    pick_item(1770 - 1280, 635)
    pick_item(1655 - 1280, 194)

    exit_bank()


j = 0
while j < 10:
    making_air_runes()
