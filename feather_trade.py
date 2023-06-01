import random
import time
import win32gui
import pyautogui

import functions
from functions import find_Object_right, pick_item_right, image_Rec_inventory, pick_item

def findWindow(data):  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, data)
    # hwnd = win32gui.GetForegroundWindow()860
    #print('findWindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)
    # win32gui.ShowWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)
    
def gerrants_shop_active():
    shop = functions.Image_count('gerrant_shop.png', 0.75)
    if shop > 0:
        return True
    else:
        return False
    return False

def tynan_shop_active():
    shop = functions.Image_count('tynan_shop.png', 0.75)
    if shop > 0:
        return True
    else:
        return False
    return False
def trade_gerrant():
    shop = False
    while shop == False:
        while functions.find_Object_right_quick(4) == False:
            d = random.uniform(0.1, 0.3)
            time.sleep(d)
        d = random.uniform(3, 5)
        time.sleep(d)
        shop = gerrants_shop_active()

def trade_tynan():
    shop = False
    while shop == False:
        while functions.find_Object_right_quick(4) == False:
            d = random.uniform(0.1, 0.3)
            time.sleep(d)
        d = random.uniform(3, 5)
        time.sleep(d)
        shop = tynan_shop_active()
def get_feathers():
    pick_item_right(1420-1280, 300, 4)
    d = random.uniform(0.1,0.5)
    time.sleep(d)
    pick_item(1815 - 1280, 215)
    invent = functions.invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    image_Rec_inventory('feather_pack.png', 0.8, 'left')
    d = random.uniform(1, 4)
    time.sleep(d)


def get_bait():
    pick_item_right(1700 - 1280, 255, 4)
    d = random.uniform(0.1, 0.5)
    time.sleep(d)
    pick_item(1815 - 1280, 215)
    invent = functions.invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    image_Rec_inventory('bait_pack.png', 0.8, 'left')


def get_sandworms():
    print('worms, ', functions.Image_count('tynan_shop.png'))
    if functions.Image_count('tynan_shop.png') > 0:
        pick_item_right(1466 - 1280, 300, 2)
        d = random.uniform(0.1, 0.5)
        time.sleep(d)
        pick_item(1815 - 1280, 215)
        invent = functions.invent_enabled()
        print(invent)
        if invent == 0:
            pyautogui.press('esc')
        image_Rec_inventory('bait_pack.png', 0.8, 'left')
        d = random.uniform(8, 10)
        time.sleep(d)


Run_Duration_hours = 0.5
t_end = time.time() + (60 * 60 * Run_Duration_hours)
while time.time() < t_end:
    trade_tynan()
    get_sandworms()
