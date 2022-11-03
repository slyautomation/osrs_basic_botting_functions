import numpy as np
import cv2
import pyautogui
import random
import time

import yaml

from core import getWindow

global hwnd
global iflag
global icoord
from PIL import Image
from functions import mini_map_image, random_breaks, Image_count, mini_map_bool
import functions

iflag = False

with open("pybot-config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

x_win, y_win, w_win, h_win = getWindow(data[0]['Config']['client_title'])

def determine_position_to_bank():
    print('determining position to bank')
    runes = count_runes()
    if runes > 1:
        return 8
    if mini_map_bool('air_craft_bank.png', 0.7):
        print('player located @ step 1')
        print("to bank")
        return 7
    if mini_map_bool('air_craft_mark_1.png', 0.7):
        print('player located @ step 2')
        print("to bank")
        return 6
    if mini_map_bool('air_craft_mark_2.png', 0.7):
        print('player located @ step 3')
        print("to bank")
        return 4
    if mini_map_bool('air_craft_mark_3.png', 0.7):
        print('player located @ step 4')
        print("to bank")
        return 3
    if mini_map_bool('air_craft_mark_4.png', 0.7):
        print('player located @ step 5_1')
        print("to bank")
        return 2
    if mini_map_bool('air_craft_mark_5.png', 0.7):
        print('player located @ step 5_2')
        print("to bank")
        return 1
    if mini_map_bool('air_craft_mark_6.png', 0.7):
        print('player located @ step 6_1')
        print("to bank")
        return 0
    if mini_map_bool('air_craft_mark_7.png', 0.7):
        print('player located @ step 6_2')
        make_runes()
        print("to bank")
        return 2
    if mini_map_bool('air_craft_mark_8.png', 0.7):
        print('player located @ step 6_3')
        mini_map_image('air_craft_mark_8.png', 45, -10, 0.7, 'left', 15, 10)
        print("to bank")
        random_breaks(8, 12)
        return 0
    if mini_map_bool('air_craft_mark_9.png', 0.7):
        print('player located @ step 6_4')
        mini_map_image('air_craft_mark_9.png', 45, -10, 0.7, 'left', 15, 10)
        print("to bank")
        random_breaks(8, 12)
        return 0
    print('player unable to be located')
    print("to air alter")
    return 1

def determine_position_to_airalter():
    print('determining position to air alter')
    runes = count_runes()
    if runes == 0 or runes == 1:
        return 8
    if mini_map_bool('air_craft_bank.png', 0.7):
        print('player located @ step 1')
        print("to air alter")
        return 0
    if mini_map_bool('air_craft_mark_1.png', 0.7):
        print('player located @ step 2')
        print("to air alter")
        return 2
    if mini_map_bool('air_craft_mark_2.png', 0.7):
        print('player located @ step 3')
        print("to air alter")
        return 3
    if mini_map_bool('air_craft_mark_3.png', 0.7):
        print('player located @ step 4')
        print("to air alter")
        return 4
    if mini_map_bool('air_craft_mark_4.png', 0.7):
        print('player located @ step 5')
        print("to air alter")
        return 5
    if mini_map_bool('air_craft_mark_9.png', 0.7):
        print('player located @ step 5')
        print("to air alter")
        return 5
    if mini_map_bool('air_craft_mark_5.png', 0.7):
        print('player located @ step 6_1')
        print("to air alter")
        return 7
    if mini_map_bool('air_craft_mark_6.png', 0.7):
        print('player located @ step 6_2')
        print("to air alter")
        make_runes()
        return 8
    if mini_map_bool('air_craft_mark_7.png', 0.7):
        print('player located @ air alter')
        print("to air alter")
        make_runes()
        return 8
    if mini_map_bool('air_craft_mark_9.png', 0.7):
        print('player located @ step 6_3')
        mini_map_image('air_craft_mark_9.png', 45, 10, 0.7, 'left', 15, 10)
        print("to air alter")
        random_breaks(8, 12)
        return 0

    print('player unable to be located')
    print("to air alter")
    return 0


def invent_enabled():
    return Image_count('inventory_enabled.png', threshold=0.9)


def to_air_craft():
    step = 0
    invent = invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    runes = count_runes()
    if runes > 1:
        step = determine_position_to_airalter()
    else:
        b = 1  # random.randrange(1, 3)
        options = {1: to_bank}
        options[b]()
        functions.find_Object(1, left=0, top=0, right=w_win, bottom=h_win)
        print('bank booth')
        c = random.uniform(6.5, 8.5)
        time.sleep(c)
        pick_item(1770 - 1280, 635)
        pick_item(1655 - 1280, 194)
        exit_bank()

    if step == 0:
        while mini_map_image('air_craft_bank.png', -5, -5, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_bank.png', 0, 0, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_bank.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 1 to air alter spot not found")
        print("step 1 to air alter")
        random_breaks(5, 8)
        step = 1

    if step == 1:
        while mini_map_image('air_craft_bank.png', 0, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_bank.png', 0, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_bank.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 2 to air alter spot not found")
        print("step 2 to air alter")
        random_breaks(8, 10)
        step = 2

    if step == 2:
        while mini_map_image('air_craft_mark_1.png', 10, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_1.png', 10, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_1.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 3 to air alter not found")
        print("step 3 to air alter")
        random_breaks(5, 8)
        step = 3

    if step == 3:
        while mini_map_image('air_craft_mark_2.png', 10, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_2.png', 10, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_2.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 4 to air alter not found")
        print("step 4 to air alter")
        random_breaks(5, 8)
        step = 4

    if step == 4:
        while mini_map_image('air_craft_mark_3.png', 0, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_3.png', 0, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_3.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 5 to air alter not found")
        print("step 5 to air alter")
        random_breaks(5, 8)
        step = 5

    if step == 5:
        while mini_map_image('air_craft_mark_4.png', 0, 15, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_4.png', 0, 15, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_4.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 6 to air alter not found")
        print("step 6 to air alter")
        random_breaks(5, 8)
        step = 6

    if step == 6:
        while mini_map_image('air_craft_mark_4.png', 0, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_4.png', 0, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_4.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 7 to air alter not found")
        print("step 7 to air alter")
        random_breaks(5, 8)
        step = 7

    if step == 7:
        while mini_map_image('air_craft_mark_5.png', -20, 20, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_5.png', -20, 20, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_5.png', 0.7) == False:
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
    if runes == 0 or runes == 1:
        step = determine_position_to_bank()
    else:
        make_runes()

    if step == 0:
        while mini_map_image('air_craft_mark_6.png', 40, -10, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_6.png', 40, -10, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_6.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 1 to bank not found")
        print("step 1 to bank")
        random_breaks(10, 13)
        step = 1

    if step == 1:
        while mini_map_image('air_craft_mark_5.png', 0, -25, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_5.png', 0, -25, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_5.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 2 to bank not found")
        print("step 2 to bank")
        random_breaks(8, 10)
        mini_map_image('air_craft_mark_5.png', 0, -55, 0.7, 'left', 15, 10)
        random_breaks(5, 8)
        step = 2
    if step == 2:
        while mini_map_image('air_craft_mark_4.png', 30, -15, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_4.png', 30, -15, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_4.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 3 to bank not found")
        print("step 3 to bank")
        random_breaks(8, 11)
        step = 3

    if step == 3:
        while mini_map_image('air_craft_mark_3.png', 5, -10, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_3.png', 5, -10, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_3.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 4 to bank not found")
        print("step 4 to bank")
        random_breaks(5, 8)
        step = 4

    if step == 4:
        while mini_map_image('air_craft_mark_2.png', 10, -10, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_2.png', 10, -10, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_2.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 5 to bank not found")
        print("step 5 to bank")
        random_breaks(5, 8)
        step = 5

    if step == 5:
        while mini_map_image('air_craft_mark_2.png', 5, -25, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_2.png', 5, -25, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_2.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 6 to bank not found")
        print("step 6 to bank")
        random_breaks(5, 8)
        step = 6

    if step == 6:
        while mini_map_image('air_craft_mark_1.png', 5, -15, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_1.png', 5, -15, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_1.png', 0.7) == False:
                print("air alter not found")
                making_air_runes()
            print("step 7 to bank not found")
        print("step 7 to bank")
        random_breaks(5, 8)
        step = 7

    if step == 7:
        while mini_map_image('air_craft_bank.png', 5, 0, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_bank.png', 5, 0, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_bank.png', 0.7) == False:
                print("air alter not found")
                functions.find_Object(2, left=0, top=0, right=w_win, bottom=h_win)
                random_breaks(8, 10)
                making_air_runes()
            print("step 8 to bank not found")
        print("step 8 to bank")
        random_breaks(8, 10)
        step = 8


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
    if mini_map_bool('air_craft_mark_7.png', 0.7) == False:
        functions.find_Object(2, left=0, top=0, right=w_win, bottom=h_win)
        c = random.uniform(1.5, 3)
        time.sleep(c)
    c = random.uniform(1.5, 3)
    time.sleep(c)
    functions.find_Object(2, left=0, top=0, right=w_win, bottom=h_win)
    print('making runes')
    c = random.uniform(6.5, 8)
    time.sleep(c)
    functions.find_Object(1, left=0, top=0, right=w_win, bottom=h_win)
    print('enter rune area')
    c = random.uniform(4, 6)
    time.sleep(c)


def count_runes():
    invent = functions.invent_enabled()
    if invent == 0:
        actions = 'opening inventory'
        pyautogui.press('esc')
    return Image_count('rune_icon.png', threshold=0.7)


def making_air_runes():
    invent = functions.invent_enabled()
    if invent == 0:
        actions = 'opening inventory'
        pyautogui.press('esc')
    a = 1  # random.randrange(1, 3)
    functions.Image_Rec_single('activity_adviser.png', 'close activity advisor', iheight=5, iwidth=120, threshold=0.9, ispace=10, playarea=True)
    options = {1: to_air_craft
               }
    options[a]()
    runes = count_runes()
    if runes > 1:
        print("player has runes to craft")
        functions.find_Object(2, left=0, top=0, right=w_win, bottom=h_win)
        print('air alter')
        c = random.uniform(6.5, 8.5)
        time.sleep(c)
        make_runes()
    b = 1  # random.randrange(1, 3)
    functions.Image_Rec_single('activity_adviser.png', 'close activity advisor', iheight=5, iwidth=120, threshold=0.9, ispace=10, playarea=True)
    options = {1: to_bank
               }
    options[b]()
    functions.find_Object(1, left=0, top=0, right=w_win, bottom=h_win)
    print('bank booth')
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
        making_air_runes()
