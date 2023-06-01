import math
import win32gui
import numpy as np
import cv2
import pyautogui
import random
import time

import requests
import simplejson
import yaml

import core
from core import findWindow

global hwnd
global iflag
global icoord
from PIL import Image
from functions import mini_map_image, random_breaks, Image_count, mini_map_bool
import functions

iflag = False

with open("pybot-config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)



x_win, y_win, w_win, h_win = core.getWindow('RuneLite')

client_top_border = 30
client_side_border = 50
tiles_pixels = 4
offset_minimap_x = 377.0
offset_minimap_y = 195.0
offset_minimap_x_resize = 72
offset_minimap_y_resize = 81
offset_run_button_x = 150
offset_run_button_y = 130
offset_logout_x = 10
offset_logout_y = 10
degreesPerYaw: float = 360 / 2048

def findWindow(data):  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, data)
    # hwnd = win32gui.GetForegroundWindow()860
    #print('findWindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)
    # win32gui.ShowWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)

def find_center_minimap_resizable(window_features: list) -> list:
    '''Returns the center of the window, excluding the borders.'''
    x, y, w, h = window_features
    map_center_x = x + (w -offset_minimap_x_resize)
    map_center_y = y + offset_minimap_y_resize
    return [map_center_x, map_center_y]

def compute_tiles(live_x: int, live_y: int, new_x: int, n_y: int) -> list:
    global degreesPerYaw, tiles_pixels
    '''Returns the range to click from the minimap center in amount of tiles.'''
    # Get live camera data.
    camera_data = plugin('camera')
    print("camera data:", camera_data)
    while camera_data is None:
        camera_data = plugin('camera')
    if camera_data != None:
        # Get camera angle.
        yaw = camera_data['yaw']
        # Account for anticlockwise OSRS minimap.
        degrees = 360 - degreesPerYaw * yaw
        # Turn degrees into pi-radians.
        theta = math.radians(degrees)
        # Turn position difference into pixels difference.
        x_reg = (new_x - live_x) * tiles_pixels
        y_reg = (live_y - n_y) * tiles_pixels
        # Formulas to compute norm of a vector in a rotated coordinate system.
        tiles_x = x_reg * math.cos(theta) + y_reg * math.sin(theta)
        tiles_y = -x_reg * math.sin(theta) + y_reg * math.cos(theta)
        return [round(tiles_x, 1), round(tiles_y, 1)]
    return [live_x, live_y]
def change_position(center_mini: list, live_pos: list, new_pos: list):
    '''Clicks the minimap to change position'''
    tiles = compute_tiles(live_pos[0], live_pos[1], new_pos[0], new_pos[1])
    print("x:", center_mini[0] + tiles[0], "y:", center_mini[1] + tiles[1])
    print("y1:", center_mini[1], "y2:", tiles[1])
    pyautogui.click(center_mini[0] + tiles[0], center_mini[1] + tiles[1])

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
        make_runes_at_alter()
        print("to bank")
        return 2
    if mini_map_bool('air_craft_mark_8.png', 0.7):
        print('player located @ step 6_3')
        mini_map_image('air_craft_mark_8.png', 45, -10, 0.7, 'left', 15, 10)
        print("to bank")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(8, 12)
        return 0
    if mini_map_bool('air_craft_mark_9.png', 0.7):
        print('player located @ step 6_4')
        mini_map_image('air_craft_mark_9.png', 45, -10, 0.7, 'left', 15, 10)
        print("to bank")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(8, 12)
        return 0
    print('player unable to be located')
    print("to air alter")
    return 1

def determine_position_to_airalter():
    print('determining position to air alter')
    runes = count_runes()
    print(runes)
    if Plugin_Enabled:
        live_pos = plugin('worldPoint')
        print(live_pos['y'])
        if live_pos['y'] > 4800:
            window = x_win, y_win, w_win, h_win
            center_minimap = find_center_minimap_resizable(window)
            pyautogui.moveTo(center_minimap)
            x_new = random.randrange(2840,2845)
            y_new = random.randrange(4827, 4833)
            cur_pos = live_pos['x'], live_pos['y']
            new_pos = x_new, y_new
            change_position(center_minimap, cur_pos, new_pos)
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
            if runes > 1:
                make_runes_at_alter()
            else:
                functions.find_Object(1, left=0, top=0, right=w_win, bottom=h_win)
                time.sleep(2)
                while plugin() != 808:
                    time.sleep(0.1)
                c = random.uniform(0.1, 1)
                time.sleep(c)

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
        make_runes_at_alter()
        return 8
    if mini_map_bool('air_craft_mark_7.png', 0.7):
        print('player located @ air alter')
        print("to air alter")
        make_runes_at_alter()
        return 8
    if mini_map_bool('air_craft_mark_9.png', 0.7):
        print('player located @ step 6_3')
        mini_map_image('air_craft_mark_9.png', 45, 10, 0.7, 'left', 15, 10)
        print("to air alter")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(8, 12)
        return 0

    print('player unable to be located')
    print("to air alter")
    return 0



def to_air_craft():
    global bank_runes_position_x, bank_runes_position_y
    step = 0
    invent = functions.invent_enabled()
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
        x = random.randrange(800, 900)
        y = random.randrange(800, 900)
        pyautogui.moveTo(x, y, duration=0.1)
        print('bank booth')
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            c = random.uniform(6.5, 8.5)
            time.sleep(c)
        withdraw_bank_runes(bank_runes_position_x, bank_runes_position_y)

    if step == 0:
        while mini_map_image('air_craft_bank.png', -5, -5, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_bank.png', 0, 0, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_bank.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 1 to air alter spot not found")
        print("step 1 to air alter")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(5, 8)
        step = 1

    if step == 1:
        while mini_map_image('air_craft_bank.png', 0, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_bank.png', 0, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_bank.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 2 to air alter spot not found")
        print("step 2 to air alter")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(8, 10)
        step = 2

    if step == 2:
        while mini_map_image('air_craft_mark_1.png', 10, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_1.png', 10, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_1.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 3 to air alter not found")
        print("step 3 to air alter")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(5, 8)
        step = 3

    if step == 3:
        while mini_map_image('air_craft_mark_2.png', 10, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_2.png', 10, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_2.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 4 to air alter not found")
        print("step 4 to air alter")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(5, 8)
        step = 4

    if step == 4:
        while mini_map_image('air_craft_mark_3.png', 0, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_3.png', 0, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_3.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 5 to air alter not found")
        print("step 5 to air alter")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(5, 8)
        step = 5

    if step == 5:
        while mini_map_image('air_craft_mark_4.png', 0, 15, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_4.png', 0, 15, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_4.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 6 to air alter not found")
        print("step 6 to air alter")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(5, 8)
        step = 6

    if step == 6:
        while mini_map_image('air_craft_mark_4.png', 0, 40, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_4.png', 0, 40, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_4.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 7 to air alter not found")
        print("step 7 to air alter")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(5, 8)
        step = 7

    if step == 7:
        while mini_map_image('air_craft_mark_5.png', -20, 20, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_5.png', -20, 20, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_5.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 8 to air alter not found")
        print("step 8 to air alter")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(12, 15)
        step = 8


def to_bank():
    global bank_runes_position_x, bank_runes_position_y
    step = 0
    invent = functions.invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    runes = count_runes()
    if runes == 0 or runes == 1:
        step = determine_position_to_bank()
    else:
        make_runes_at_alter()
    if step == 0:
        while mini_map_image('air_craft_mark_6.png', 40, -10, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_6.png', 40, -10, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_6.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 1 to bank not found")
        print("step 1 to bank")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(10, 13)
        step = 1

    if step == 1:
        while mini_map_image('air_craft_mark_5.png', 0, -25, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_5.png', 0, -25, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_5.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 2 to bank not found")
        print("step 2 to bank")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(8, 10)
        mini_map_image('air_craft_mark_5.png', 0, -55, 0.7, 'left', 15, 10)
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(5, 8)
        step = 2

    if step == 2:
        time_start = time.time()
        time_end = 0
        c = random.uniform(12.5, 14.5)
        step2 = mini_map_image('air_craft_mark_4.png', 30, -15, 0.7, 'left', 15, 10)
        while step2 == False and time_end < c:
            time_end = time.time() - time_start
            time.sleep(0.3)
            step2 = mini_map_image('air_craft_mark_4.png', 30, -15, 0.7, 'left', 15, 10)
            print(step2)
        if step2 == False:
            print("air alter not found")
            runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 3 to bank not found")
        else:
            print("step 3 to bank")
            if Plugin_Enabled:
                time.sleep(2)
                while plugin() != 808:
                    time.sleep(0.1)
                c = random.uniform(0.1, 1)
                time.sleep(c)
            else:
                random_breaks(8, 11)
            step = 3

    if step == 3:
        while mini_map_image('air_craft_mark_3.png', 5, -10, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_3.png', 5, -10, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_3.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 4 to bank not found")
        print("step 4 to bank")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(5, 8)
        step = 4

    if step == 4:
        while mini_map_image('air_craft_mark_2.png', 10, -10, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_2.png', 10, -10, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_2.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 5 to bank not found")
        print("step 5 to bank")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(5, 8)
        step = 5

    if step == 5:
        while mini_map_image('air_craft_mark_2.png', 5, -25, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_2.png', 5, -25, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_2.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 6 to bank not found")
        print("step 6 to bank")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(5, 8)
        step = 6

    if step == 6:
        while mini_map_image('air_craft_mark_1.png', 5, -15, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_mark_1.png', 5, -15, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_mark_1.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 7 to bank not found")
        print("step 7 to bank")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(5, 8)
        step = 7

    if step == 7:
        while mini_map_image('air_craft_bank.png', 5, 0, 0.7, 'left', 15, 10) == False:
            mini_map_image('air_craft_bank.png', 5, 0, 0.7, 'left', 15, 10)
            if mini_map_bool('air_craft_bank.png', 0.7) == False:
                print("air alter not found")
                runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
            print("step 8 to bank not found")
        print("step 8 to bank")
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            random_breaks(8, 10)
        step = 8


def make_runes_at_alter():
    if mini_map_bool('air_craft_mark_7.png', 0.7) == False:
        functions.find_Object(2, left=0, top=0, right=w_win, bottom=h_win)
        c = random.uniform(1.5, 3)
        time.sleep(c)
    if Plugin_Enabled:
        time.sleep(2)
        while plugin() != 808:
            time.sleep(0.1)
        c = random.uniform(0.1, 1)
        time.sleep(c)
    else:
        c = random.uniform(1.5, 3)
        time.sleep(c)
    functions.find_Object(2, left=0, top=0, right=w_win, bottom=h_win)
    print('making runes')
    if Plugin_Enabled:
        time.sleep(2)
        while plugin() != 808:
            time.sleep(0.1)
        c = random.uniform(0.1, 1)
        time.sleep(c)
    else:
        c = random.uniform(6.5, 8)
        time.sleep(c)
    functions.find_Object(1, left=0, top=0, right=w_win, bottom=h_win)
    print('enter rune area')
    if Plugin_Enabled:
        time.sleep(2)
        while plugin() != 808:
            time.sleep(0.1)
        c = random.uniform(0.1, 1)
        time.sleep(c)
    else:
        c = random.uniform(4, 6)
        time.sleep(c)


def count_runes():
    invent = functions.invent_enabled()
    if invent == 0:
        actions = 'opening inventory'
        pyautogui.press('esc')
    return functions.invent_count('rune_icon.png', threshold=0.7)


def withdraw_bank_runes(rune_x,rune_y):
    x = random.randrange(800, 900)
    y = random.randrange(800, 900)
    pyautogui.moveTo(x,y)
    error_c = 0
    bank = functions.bank_ready(False)
    while bank == False:
        if error_c > 3:
            exit()
        if Plugin_Enabled:
            if plugin() == 808:
                functions.find_Object(1, left=0, top=0, right=w_win, bottom=h_win) # mark / highlight object marker for the bank booth - GREEN
        else:
            functions.find_Object(1, left=0, top=0, right=w_win,
                                 bottom=h_win)  # mark / highlight object marker for the bank booth - GREEN
        x = random.randrange(800, 900)
        y = random.randrange(800, 900)
        pyautogui.moveTo(x, y, duration=0.1)
        c = random.uniform(3, 6)
        time.sleep(c)
        bank = functions.bank_ready(False)
        error_c += 1
    print('bank booth')
    functions.deposit_all_Bank()
    functions.pick_item(rune_x, rune_y)
    functions.exit_bank(Debug=False)


def runecrafting_air_runes(bankrune_x=185,bankrune_y=305):
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
        functions.find_Object(2, left=0, top=0, right=w_win, bottom=h_win) # mark / highlight object marker for the entrance to air alter - YELLOW
        print('air alter')
        if Plugin_Enabled:
            time.sleep(2)
            while plugin() != 808:
                time.sleep(0.1)
            c = random.uniform(0.1, 1)
            time.sleep(c)
        else:
            c = random.uniform(6.5, 8.5)
            time.sleep(c)
        make_runes_at_alter()
    b = 1  # random.randrange(1, 3)
    options = {1: to_bank
               }
    options[b]()
    x = random.randrange(800, 900)
    y = random.randrange(800, 900)
    pyautogui.moveTo(x, y, duration=0.1)
    withdraw_bank_runes(bankrune_x, bankrune_y) # mark / highlight object marker for the bank booth at falador - GREEN

def plugin(category='animation pose'):
    c = s.get("http://localhost:8081/events", stream=True)
    data = simplejson.loads(c.text)
    data[category]
    #print(data[category])
    return data[category]

bank_runes_position_x = 375
bank_runes_position_y = 123
Run_Duration_Hours = 4
# object mark / highlught bank booth in falador green
# mark / highlight object marker for the entrance to air alter yellow
# mark / highlight object marker inside the air alter yellow and exit portal green

Plugin_Enabled = True
if Plugin_Enabled:
    s = requests.session()
    print(plugin())
if __name__ == "__main__":
    x = random.randrange(100, 250)
    y = random.randrange(400, 500)
    pyautogui.click(x, y, button='right')
    t_end = time.time() + (60 * 60 * Run_Duration_Hours)
    while time.time() < t_end:
        runecrafting_air_runes(bank_runes_position_x, bank_runes_position_y)
