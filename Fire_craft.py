import numpy as np
import cv2
import pyautogui
import random
import time

global hwnd
global iflag
global icoord
from PIL import Image
from functions import mini_map_image, random_breaks, Image_count, mini_map_bool, screen_Image

iflag = False


def determine_position_to_bank():
    print('determining position to bank')
    if mini_map_bool('fire_craft_runealter.png', 0.85):
        print('player located @ fire alter')
        print("to bank")
        find_area(1, 'to exit portal')
        c = random.uniform(12, 14)
        time.sleep(c)
        return 0
    if mini_map_bool('fire_craft_mark_6.png', 0.85):
        print('player located @ step 1')
        print("to bank")
        return 0
    if mini_map_bool('fire_craft_mark_5.png', 0.85):
        print('player located @ step 2')
        print("to bank")
        return 1
    if mini_map_bool('fire_craft_mark_4.png', 0.85):
        print('player located @ step 3')
        print("to bank")
        return 2
    if mini_map_bool('fire_craft_mark_3.png', 0.85):
        print('player located @ step 4')
        print("to bank")
        return 4
    if mini_map_bool('fire_craft_mark_2.png', 0.85):
        print('player located @ step 5')
        print("to bank")
        return 5
    if mini_map_bool('fire_craft_bank.png', 0.85):
        print('player located @ step 7')
        print("to bank")
        return 6
    if mini_map_bool('fire_craft_mark_1.png', 0.85):
        print('player located @ step 6')
        print("to bank")
        return 6


def determine_position_to_firealter():
    print('determining position to fire alter')
    if mini_map_bool('fire_craft_runealter.png', 0.85):
        print('player located @ fire alter')
        print("to bank")
        return 7
    if mini_map_bool('fire_craft_mark_6.png', 0.85):
        print('player located @ step 7')
        print("to fire alter")
        find_area_custom(2, 'fire alter', 40, 40)
        c = random.uniform(6.5, 8.5)
        time.sleep(c)
        return 7
    if mini_map_bool('fire_craft_bank.png', 0.85):
        print('player located @ step 1')
        print("to fire alter")
        return 0
    if mini_map_bool('fire_craft_mark_1.png', 0.85):
        print('player located @ step 2')
        print("to fire alter")
        return 1
    if mini_map_bool('fire_craft_mark_2.png', 0.85):
        print('player located @ step 3')
        print("to fire alter")
        return 3
    if mini_map_bool('fire_craft_mark_3.png', 0.85):
        print('player located @ step 4')
        print("to fire alter")
        return 4
    if mini_map_bool('fire_craft_mark_4.png', 0.85):
        print('player located @ step 5')
        print("to fire alter")
        return 5
    if mini_map_bool('fire_craft_mark_5.png', 0.85):
        print('player located @ step 6')
        print("to fire alter")
        return 6


def to_fire_craft():
    step = 0
    invent = invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    runes = count_runes()
    if runes > 0:
        step = determine_position_to_firealter()
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
        while mini_map_image('fire_craft_bank.png', 10, 30, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_bank.png', 0, 0, 0.7, 'left', 15, 10)
            if mini_map_bool('fire_craft_bank.png', 0.85) == False:
                print("fire alter not found")
                making_fire_runes()
            print("step 1 to fire alter spot not found")
        print("step 1 to fire alter")
        random_breaks(5, 8)
        step = 1

    if step == 1:
        while mini_map_image('fire_craft_mark_1.png', -10, -5, 0.7, 'left', 15, 10) == False:
            mini_map_image('fire_craft_mark_1.png', -10, -5, 0.7, 'left', 15, 10)
            if mini_map_bool('fire_craft_mark_1.png', 0.85) == False:
                print("fire alter not found")
                making_fire_runes()
            print("step 2 to fire alter spot not found")
        print("step 2 to fire alter")
        random_breaks(8, 10)
        step = 2

    if step == 2:
        while mini_map_image('fire_craft_mark_1.png', -50, -5, 0.7, 'left', 15, 10) == False:
            mini_map_image('fire_craft_mark_1.png', -50, -5, 0.7, 'left', 15, 10)
            if mini_map_bool('fire_craft_mark_1.png', 0.85) == False:
                print("fire alter not found")
                making_fire_runes()
            print("step 3 to air alter not found")
        print("step 3 to air alter")
        random_breaks(5, 8)
        step = 3

    if step == 3:
        while mini_map_image('fire_craft_mark_2.png', -35, -5, 0.7, 'left', 15, 10) == False:
            mini_map_image('fire_craft_mark_2.png', -35, -5, 0.7, 'left', 15, 10)
            if mini_map_bool('fire_craft_mark_2.png', 0.85) == False:
                print("fire alter not found")
                making_fire_runes()
            print("step 4 to fire alter not found")
        print("step 4 to fire alter")
        random_breaks(5, 8)
        step = 4

    if step == 4:
        while mini_map_image('fire_craft_mark_3.png', -40, 0, 0.7, 'left', 15, 10) == False:
            mini_map_image('fire_craft_mark_3.png', -40, 0, 0.7, 'left', 15, 10)
            if mini_map_bool('fire_craft_mark_3.png', 0.85) == False:
                print("fire alter not found")
                making_fire_runes()
            print("step 5 to fire alter not found")
        print("step 5 to fire alter")
        random_breaks(5, 8)
        step = 5

    if step == 5:
        while mini_map_image('fire_craft_mark_4.png', -10, 55, 0.7, 'left', 15, 10) == False:
            mini_map_image('fire_craft_mark_4.png', -10, 55, 0.7, 'left', 15, 10)
            if mini_map_bool('fire_craft_mark_4.png', 0.85) == False:
                print("fire alter not found")
                making_fire_runes()
            print("step 6 to fire alter not found")
        print("step 6 to fire alter")
        random_breaks(5, 8)
        step = 6

    if step == 6:
        while mini_map_image('fire_craft_mark_5.png', -10, 15, 0.7, 'left', 5, 10) == False:
            mini_map_image('fire_craft_mark_5.png', -10, 15, 0.7, 'left', 5, 10)
            if mini_map_bool('fire_craft_mark_5.png', 0.85) == False:
                print("fire alter not found")
                making_fire_runes()
            print("step 7 to fire alter not found")
        print("step 7 to fire alter")
        random_breaks(35, 40)
        print('made it to fire alter...')
        step = 7


def invent_enabled():
    return Image_count('inventory_enabled.png', threshold=0.9)


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
        while mini_map_image('fire_craft_mark_6.png', 45, -5, 0.7, 'left', 5, 15) == False:
            mini_map_image('fire_craft_mark_6.png', 45, -5, 0.7, 'left', 5, 15)
            if mini_map_bool('fire_craft_mark_6.png', 0.85) == False:
                print("fire alter not found")
                make_runes()
            print("step 1 to bank not found")
        print("step 1 to bank")
        random_breaks(30, 35)
        step = 1

    if step == 1:
        while mini_map_image('fire_craft_mark_5.png', 40, -5, 0.7, 'left', 15, 10) == False:
            mini_map_image('fire_craft_mark_5.png', 40, -5, 0.7, 'left', 15, 10)
            if mini_map_bool('fire_craft_mark_5.png', 0.85) == False:
                print("fire alter not found")
                making_fire_runes()
            print("step 2 to bank not found")
        print("step 2 to bank")
        random_breaks(8, 10)
        step = 2
    if step == 2:
        while mini_map_image('fire_craft_mark_4.png', 30, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('fire_craft_mark_4.png', 30, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('fire_craft_mark_4.png', 0.85) == False:
                print("fire alter not found")
                making_fire_runes()
            print("step 3 to bank not found")
        print("step 3 to bank")
        random_breaks(5, 8)
        step = 3

    if step == 3:
        while mini_map_image('fire_craft_mark_4.png', 60, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('fire_craft_mark_4.png', 60, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('fire_craft_mark_4.png', 0.85) == False:
                print("fire alter not found")
                making_fire_runes()
            print("step 4 to bank not found")
        print("step 4 to bank")
        random_breaks(5, 8)
        step = 4

    if step == 4:
        while mini_map_image('fire_craft_mark_3.png', 30, -10, 0.7, 'left', 15, 10) == False:
            mini_map_image('fire_craft_mark_3.png', 30, -10, 0.7, 'left', 15, 10)
            if mini_map_bool('fire_craft_mark_3.png', 0.85) == False:
                print("fire alter not found")
                making_fire_runes()
            print("step 5 to bank not found")
        print("step 5 to bank")
        random_breaks(5, 8)
        step = 5

    if step == 5:
        while mini_map_image('fire_craft_mark_2.png', 50, -10, 0.7, 'left', 15, 10) == False:
            mini_map_image('fire_craft_mark_2.png', 50, -10, 0.7, 'left', 15, 10)
            if mini_map_bool('fire_craft_mark_2.png', 0.85) == False:
                print("fire alter not found")
                making_fire_runes()
            print("step 6 to bank not found")
        print("step 6 to bank")
        random_breaks(5, 8)
        step = 6

    if step == 6:
        while mini_map_image('fire_craft_mark_1.png', 35, -10, 0.7, 'left', 15, 10) == False:
            mini_map_image('fire_craft_mark_1.png', 35, -10, 0.7, 'left', 15, 10)
            if mini_map_bool('fire_craft_mark_1.png', 0.85) == False:
                print("fire alter not found")
                making_fire_runes()
            print("step 7 to bank not found")
        print("step 7 to bank")
        random_breaks(11, 13)
        step = 7


def rune_Image():
    screen_Image(0, 0, 860, 825, 'runeshot.png')


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
    c = random.uniform(12, 14)
    time.sleep(c)
    find_area(1, 'to exit portal')
    c = random.uniform(12, 14)
    time.sleep(c)


def count_runes():
    return Image_count('rune_icon.png', threshold=0.8)


def last_step_tofirealter():
    while mini_map_image('fire_craft_runealter.png', 0, 0, 0.7, 'left', 15, 10) == False:
        mini_map_image('fire_craft_runealter.png', 0, 0, 0.7, 'left', 15, 10)
        if mini_map_image('fire_craft_runealter.png', 0, 0, 0.7, 'left', 15, 10) == False:
            print("fire alter not found")
            make_runes()
            break


def making_fire_runes():
    a = 1  # random.randrange(1, 3)
    options = {1: to_fire_craft
               }
    options[a]()
    print("steps completed to fire alter")
    find_area_custom(2, 'fire alter', 40, 40)
    c = random.uniform(6.5, 8.5)
    time.sleep(c)
    last_step_tofirealter()
    print("going into fire alter...")
    random_breaks(10, 12)
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


if __name__ == "__main__":
    x = random.randrange(100, 250)
    y = random.randrange(400, 500)
    pyautogui.click(x, y, button='right')
    j = 0
    while j < 10:
        making_fire_runes()
