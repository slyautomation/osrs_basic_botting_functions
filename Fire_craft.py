import numpy as np
import cv2
import pyautogui
import random
import time
import core
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
    #return temp

def determine_position_to_firealter():
    print('determining position to fire alter')
    if mini_map_bool('fire_craft_runealter.png', 0.85):
        print('player located @ fire alter')
        last_step_tofirealter()
        print("to bank")
        return 7
    if mini_map_bool('fire_craft_mark_5.png', 0.85):
        print('player located @ step 6')
        print("to fire alter")
        return 6
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

    #return temp


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
        get_runes()

    if step == 0:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step0 = mini_map_image('fire_craft_bank.png', 10, 30, 0.7, 'left', 15, 10)
        while step0 == False:
            while time_end < x:
                step0 = mini_map_image('fire_craft_bank.png', 10, 30, 0.7, 'left', 15, 10)
                print("step 1 to fire alter spot not found")
                time_end = time.time() - time_start
                if step0 == True:
                    break
            if step0 == False:
                making_fire_runes()
        print("step 1 to fire alter")
        random_breaks(6.5, 9.5)
        step = 1

    if step == 1:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step1 = mini_map_image('fire_craft_mark_1.png', -10, 10, 0.7, 'left', 15, 10)
        while step1 == False:
            while time_end < x:
                step1 = mini_map_image('fire_craft_mark_1.png', -10, 10, 0.7, 'left', 15, 10)
                print("step 2 to fire alter spot not found")
                time_end = time.time() - time_start
                if step1 == True:
                    break
            if step1 == False:
                making_fire_runes()
        print("step 2 to fire alter")
        random_breaks(8, 10)
        step = 2

    if step == 2:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step2 = mini_map_image('fire_craft_mark_1.png', -50, 10, 0.7, 'left', 15, 10)
        while step2 == False:
            while time_end < x:
                step2 = mini_map_image('fire_craft_mark_1.png', -50, 10, 0.7, 'left', 15, 10)
                print("step 3 to air alter not found")
                time_end = time.time() - time_start
                if step2 == True:
                    break
            if step2 == False:
                making_fire_runes()
        print("step 3 to air alter")
        random_breaks(6.5, 9.5)
        step = 3

    if step == 3:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step3 = mini_map_image('fire_craft_mark_2.png', -50, 20, 0.7, 'left', 15, 10)
        while step3 == False:
            while time_end < x:
                print(time_end)
                step3 = mini_map_image('fire_craft_mark_2.png', -50, 20, 0.7, 'left', 15, 10)
                print("step 4 to fire alter not found")
                time_end = time.time() - time_start
                if step3 == True:
                    break
            if step3 == False:
                making_fire_runes()
        print("step 4 to fire alter")
        random_breaks(6.5, 9.5)
        step = 4

    if step == 4:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step4 = mini_map_image('fire_craft_mark_3.png', -30, 10, 0.7, 'left', 15, 10)
        while step4 == False:
            while time_end < x:
                print(time_end)
                step4 = mini_map_image('fire_craft_mark_3.png', -30, 10, 0.7, 'left', 15, 10)
                print("step 5 to fire alter not found")
                time_end = time.time() - time_start
                if step4 == True:
                    break
            if step4 == False:
                making_fire_runes()
        print("step 5 to fire alter")
        random_breaks(6.5, 9.5)
        step = 5

    if step == 5:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step5 = mini_map_image('fire_craft_mark_4.png', -10, 55, 0.7, 'left', 15, 10)
        while step5 == False:
            while time_end < x:
                print(time_end)
                step5 = mini_map_image('fire_craft_mark_4.png', -10, 55, 0.7, 'left', 15, 10)
                print("step 6 to fire alter not found")
                time_end = time.time() - time_start
                if step5 == True:
                    break
            if step5 == False:
                making_fire_runes()
        print("step 6 to fire alter")
        random_breaks(6.5, 9.5)
        step = 6

    if step == 6:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step6 = mini_map_image('fire_craft_mark_5.png', -10, 15, 0.7, 'left', 5, 10)
        while step6 == False:
            while time_end < x:
                print(time_end)
                step6 = mini_map_image('fire_craft_mark_5.png', -10, 15, 0.7, 'left', 5, 10)
                print("step 7 to fire alter not found")
                time_end = time.time() - time_start
                if step6 == True:
                    break
            if step6 == False:
                making_fire_runes()
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
        to_fire_craft()

    if step == 0:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step0 = mini_map_image('fire_craft_mark_6.png', 43, -5, 0.7, 'left', 5, 15)
        while step0 == False:
            while time_end < x:
                step0 = mini_map_image('fire_craft_mark_6.png', 43, -5, 0.7, 'left', 5, 15)
                print("step 1 to bank not found")
                time_end = time.time() - time_start
                if step0 == True:
                    break
            if step0 == False:
                making_fire_runes()
        print("step 1 to bank")
        random_breaks(30, 35)
        step = 1

    if step == 1:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step1 = mini_map_image('fire_craft_mark_5.png', 40, -5, 0.7, 'left', 15, 10)
        while step1 == False:
            while time_end < x:
                step1 = mini_map_image('fire_craft_mark_5.png', 40, -5, 0.7, 'left', 15, 10)
                print("step 2 to bank not found")
                time_end = time.time() - time_start
                if step1 == True:
                    break
            if step1 == False:
                making_fire_runes()
        print("step 2 to bank")
        random_breaks(8, 10)
        step = 2
    if step == 2:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step2 = mini_map_image('fire_craft_mark_4.png', 30, 40, 0.7, 'left', 15, 10)
        while step2 == False:
            while time_end < x:
                step2 = mini_map_image('fire_craft_mark_4.png', 30, 40, 0.7, 'left', 15, 10)
                print("step 3 to bank not found")
                time_end = time.time() - time_start
                if step2 == True:
                    break
            if step2 == False:
                making_fire_runes()
        print("step 3 to bank")
        random_breaks(6.5, 9.5)
        step = 3

    if step == 3:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step3 = mini_map_image('fire_craft_mark_4.png', 60, 40, 0.7, 'left', 15, 10)
        while step3 == False:
            while time_end < x:
                step3 = mini_map_image('fire_craft_mark_4.png', 60, 40, 0.7, 'left', 15, 10)
                print("step 4 to bank not found")
                time_end = time.time() - time_start
                if step3 == True:
                    break
            if step3 == False:
                making_fire_runes()
        print("step 4 to bank")
        random_breaks(6.5, 9.5)
        step = 4

    if step == 4:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step4 = mini_map_image('fire_craft_mark_3.png', 40, 15, 0.7, 'left', 15, 10)
        while step4 == False:
            while time_end < x:
                step4 = mini_map_image('fire_craft_mark_3.png', 40, 15, 0.7, 'left', 15, 10)
                print("step 5 to bank not found")
                time_end = time.time() - time_start
                if step4 == True:
                    break
            if step4 == False:
                making_fire_runes()
        print("step 5 to bank")
        random_breaks(6.5, 9.5)
        step = 5

    if step == 5:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step5 = mini_map_image('fire_craft_mark_2.png', 15, 20, 0.7, 'left', 15, 10)
        while step5 == False:
            while time_end < x:
                step5 = mini_map_image('fire_craft_mark_2.png', 15, 20, 0.7, 'left', 15, 10)
                print("step 6 to bank not found")
                time_end = time.time() - time_start
                if step5 == True:
                    break
            if step5 == False:
                making_fire_runes()
        print("step 6 to bank")
        random_breaks(7, 9)
        step = 6


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
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) != 0:
            print(event)
            # find the biggest countour (c) by the area
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            print('x:', x, ' | y: ', x + w)
            # draw the biggest contour (c) in green
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)

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

def find_area_custom(rune, event, l=10, t=10,i=10, k=10):
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
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) != 0:
            print(event)
            # find the biggest countour (c) by the area
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            # draw the biggest contour (c) in green
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)

            c = random.uniform(0.12, 0.25)
            b = random.uniform(0.1, 0.3)
            wi = round(x + (w / 2))
            x = random.randrange(wi - i, wi + k)  # 950,960
            print('x: ', x)

            hi = round(y + (h / 2))
            y = random.randrange(hi - l, hi + t)  # 490,500
            print('y: ', y)
            pyautogui.moveTo(x, y)
            b = random.uniform(0.07, 0.11)
            pyautogui.click(duration=b, button='left')
            time.sleep(c)


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
    find_area_custom(2, 'using fire alter', 20, 20, 20, 20)
    c = random.uniform(3, 5)
    time.sleep(c)
    find_area(1, 'to exit portal')
    c = random.uniform(12, 14)
    time.sleep(c)


def count_runes():
    return Image_count('rune_icon.png', threshold=0.8)

def get_runes():
    bank = Image_count('bank_deposit.png', 0.75)
    print("bank deposit open:", bank)
    if bank > 0:
        pick_item(1770 - 1280, 635)
        pick_item(1655 - 1280, 194)
        exit_bank()
    else:
        print("bank inventory not found")
        making_fire_runes()

def last_step_tofirealter():
    time_start = time.time()
    time_end = time.time() - time_start
    x = random.uniform(7, 10)
    print("going to last step inside fire alter")
    laststep = mini_map_image('fire_craft_runealter.png', 0, 0, 0.7, 'left', 15, 10)
    while laststep == False:
        while time_end < x:
            laststep = mini_map_image('fire_craft_runealter.png', 0, 0, 0.7, 'left', 15, 10)
            time_end = time.time() - time_start
            if laststep == True:
                break
        if laststep == False:
            making_fire_runes()
            break
    random_breaks(9, 12)


def making_fire_runes():
    print("start of fire runecrafting script")
    a = 1  # random.randrange(1, 3)
    options = {1: to_fire_craft
               }
    options[a]()
    print("steps completed to fire alter")
    find_area_custom(2, 'entering fire alter', 40, 40, 20, 20)
    c = random.uniform(6.5, 8.5)
    time.sleep(c)
    last_step_tofirealter()
    print("going into fire alter...")
    make_runes()
    b = 1  # random.randrange(1, 3)
    options = {1: to_bank
               }
    options[b]()
    find_area_custom(1, 'bank booth', 0, 5)
    c = random.uniform(6.5, 8.5)
    time.sleep(c)
    get_runes()

if __name__ == "__main__":
    x = random.randrange(100, 250)
    y = random.randrange(400, 500)
    pyautogui.click(x, y, button='right')
    j = 0
    while j < 10:
        making_fire_runes()
