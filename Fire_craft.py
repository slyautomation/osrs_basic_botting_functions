import os
import win32gui
import numpy as np
import cv2
import pyautogui
import random
import time

import yaml

import core
global hwnd
global iflag
global icoord
from PIL import Image
from functions import mini_map_image, random_breaks, Image_count, mini_map_bool, screen_Image
import functions
iflag = False

with open("pybot-config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

x_win, y_win, w_win, h_win = core.getWindow(data[0]['Config']['client_title'])

def findWindow(data):  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, data)
    # hwnd = win32gui.GetForegroundWindow()860
    #print('findWindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)
    # win32gui.ShowWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)
    
def determine_position_to_bank():
    print('determining position to bank')
    if mini_map_bool('fire_craft_runealter.png', 0.85):
        print('player located @ fire alter')
        print("to bank")
        functions.find_Object(1, left=0, top=0, right=w_win, bottom=h_win)
        print("exit portal")
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
    if mini_map_bool('fire_craft_mark_6.png', 0.85):
        print('player located @ step 7')
        print("to fire alter")
        functions.find_Object(2, left=0, top=0, right=w_win, bottom=h_win)
        c = random.uniform(6.5, 8.5)
        time.sleep(c)
        return 7
    if mini_map_bool('fire_craft_runealter.png', 0.85):
        print('player located @ fire alter')
        last_step_tofirealter()
        print("to bank")
        return 7



def to_fire_craft():
    global bank_runes_position_x, bank_runes_position_x
    step = 0
    invent = invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    runes = count_runes()
    time.sleep(0.5)
    if runes > 0:
        step = determine_position_to_firealter()
    else:
        b = 1  # random.randrange(1, 3)
        options = {1: to_bank}
        options[b]()
        functions.find_Object(1, left=0, top=0, right=w_win, bottom=h_win)
        c = random.uniform(8, 10)
        time.sleep(c)
        get_runes(bank_runes_position_x, bank_runes_position_y)

    if step == 0:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step0 = mini_map_image('fire_craft_bank.png', -10, 45, 0.7, 'left', 15, 10)
        while step0 == False:
            while time_end < x:
                time.sleep(3)
                step0 = mini_map_image('fire_craft_bank.png', -10, 45, 0.7, 'left', 15, 10)
                print("step 1 to fire alter spot not found")
                time_end = time.time() - time_start
                if step0 == True:
                    break
            if step0 == False:
                making_fire_runes()
        print("step 1 to fire alter")
        random_breaks(7, 9)
        step = 1

    if step == 1:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step1 = mini_map_image('fire_craft_mark_1.png', -10, 10, 0.7, 'left', 15, 10)
        while step1 == False:
            while time_end < x:
                time.sleep(3)
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
        step2 = mini_map_image('fire_craft_mark_1.png', -35, 10, 0.7, 'left', 15, 10)
        while step2 == False:
            while time_end < x:
                time.sleep(3)
                step2 = mini_map_image('fire_craft_mark_1.png', -35, 10, 0.7, 'left', 15, 10)
                print("step 3 to air alter not found")
                time_end = time.time() - time_start
                if step2 == True:
                    break
            if step2 == False:
                making_fire_runes()
        print("step 3 to air alter")
        random_breaks(9, 12)
        step = 3

    if step == 3:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step3 = mini_map_image('fire_craft_mark_3.png', 10, 25, 0.7, 'left', 15, 10)
        while step3 == False:
            while time_end < x:
                time.sleep(3)
                print(time_end)
                step3 = mini_map_image('fire_craft_mark_3.png', 10, 25, 0.7, 'left', 15, 10)
                print("step 4 to fire alter not found")
                time_end = time.time() - time_start
                if step3 == True:
                    break
            if step3 == False:
                making_fire_runes()
        print("step 4 to fire alter")
        random_breaks(9, 12)
        step = 4

    if step == 4:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step4 = mini_map_image('fire_craft_mark_3.png', -30, 10, 0.7, 'left', 15, 10)
        while step4 == False:
            while time_end < x:
                time.sleep(3)
                print(time_end)
                step4 = mini_map_image('fire_craft_mark_3.png', -30, 10, 0.7, 'left', 15, 10)
                print("step 5 to fire alter not found")
                time_end = time.time() - time_start
                if step4 == True:
                    break
            if step4 == False:
                making_fire_runes()
        print("step 5 to fire alter")
        random_breaks(9, 12)
        step = 5

    if step == 5:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step5 = mini_map_image('fire_craft_mark_4.png', -10, 45, 0.7, 'left', 15, 10)
        while step5 == False:
            while time_end < x:
                time.sleep(3)
                print(time_end)
                step5 = mini_map_image('fire_craft_mark_4.png', -10, 45, 0.7, 'left', 15, 10)
                print("step 6 to fire alter not found")
                time_end = time.time() - time_start
                if step5 == True:
                    break
            if step5 == False:
                making_fire_runes()
        print("step 6 to fire alter")
        random_breaks(9, 12)
        step = 6

    if step == 6:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step6 = mini_map_image('fire_craft_mark_5.png', -10, 15, 0.7, 'left', 5, 10)
        while step6 == False:
            while time_end < x:
                time.sleep(3)
                print(time_end)
                step6 = mini_map_image('fire_craft_mark_5.png', -10, 15, 0.7, 'left', 5, 10)
                print("step 7 to fire alter not found")
                time_end = time.time() - time_start
                if step6 == True:
                    break
            if step6 == False:
                making_fire_runes()
        print("step 7 to fire alter")
        random_breaks(40, 45)
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
    time.sleep(0.5)
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
                time.sleep(3)
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
                time.sleep(3)
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
                time.sleep(3)
                step2 = mini_map_image('fire_craft_mark_4.png', 30, 40, 0.7, 'left', 15, 10)
                print("step 3 to bank not found")
                time_end = time.time() - time_start
                if step2 == True:
                    break
            if step2 == False:
                making_fire_runes()
        print("step 3 to bank")
        random_breaks(7, 9)
        step = 3

    if step == 3:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step3 = mini_map_image('fire_craft_mark_4.png', 60, 40, 0.7, 'left', 15, 10)
        while step3 == False:
            while time_end < x:
                time.sleep(3)
                step3 = mini_map_image('fire_craft_mark_4.png', 60, 40, 0.7, 'left', 15, 10)
                print("step 4 to bank not found")
                time_end = time.time() - time_start
                if step3 == True:
                    break
            if step3 == False:
                making_fire_runes()
        print("step 4 to bank")
        random_breaks(7, 9)
        step = 4

    if step == 4:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step4 = mini_map_image('fire_craft_mark_3.png', 40, 15, 0.7, 'left', 15, 10)
        while step4 == False:
            while time_end < x:
                time.sleep(3)
                step4 = mini_map_image('fire_craft_mark_3.png', 40, 15, 0.7, 'left', 15, 10)
                print("step 5 to bank not found")
                time_end = time.time() - time_start
                if step4 == True:
                    break
            if step4 == False:
                making_fire_runes()
        print("step 5 to bank")
        random_breaks(7, 9)
        step = 5

    if step == 5:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step5 = mini_map_image('fire_craft_mark_2.png', 0, 20, 0.7, 'left', 15, 10)
        while step5 == False:
            while time_end < x:
                time.sleep(3)
                step5 = mini_map_image('fire_craft_mark_2.png', 0, 20, 0.7, 'left', 15, 10)
                print("step 6 to bank not found")
                time_end = time.time() - time_start
                if step5 == True:

                    break
            if step5 == False:
                making_fire_runes()
        print("step 6 to bank")
        random_breaks(9, 11)
        step = 6
    if step == 6:
        time_start = time.time()
        time_end = time.time() - time_start
        x = random.uniform(7, 10)
        step6 = mini_map_image('fire_craft_mark_1.png', 35, 5, 0.7, 'left', 15, 10)
        while step6 == False:
            while time_end < x:
                time.sleep(3)
                step6 = mini_map_image('fire_craft_mark_1.png', 35, 5, 0.7, 'left', 15, 10)
                print("step 7 to bank not found")
                time_end = time.time() - time_start
                if step5 == True:

                    break
            if step6 == False:
                making_fire_runes()
        print("step 7 to bank")
        random_breaks(9, 11)

def rune_Image():
    screen_Image(0, 0, 860, 825, 'runeshot.png')


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
    functions.find_Object(2, left=0, top=0, right=w_win, bottom=h_win)
    print('enter rune area')
    c = random.uniform(3, 5)
    time.sleep(c)
    functions.find_Object(1, left=0, top=0, right=w_win, bottom=h_win)
    print('exit portal')
    c = random.uniform(12, 14)
    time.sleep(c)


def count_runes():
    return Image_count('rune_icon.png', threshold=0.8)

def get_runes(bank_x, bank_y):
    bank = Image_count('bank_deposit.png', 0.7)
    print("bank deposit open:", bank)
    if bank > 0:
        functions.deposit_all_Bank()
        pick_item(bank_x, bank_y)
        functions.exit_bank()
    else:
        print("bank inventory not found")
        making_fire_runes()

def last_step_tofirealter():
    global bank_runes_position_x, bank_runes_position_y
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
            making_fire_runes(bank_runes_position_x, bank_runes_position_y)
            break
    random_breaks(9, 12)


def making_fire_runes(bank_x, bank_y):
    print("start of fire runecrafting script")
    a = 1  # random.randrange(1, 3)
    options = {1: to_fire_craft
               }
    options[a]()
    print("steps completed to fire alter")
    functions.find_Object(2, left=0, top=0, right=w_win, bottom=h_win)
    c = random.uniform(6.5, 8.5)
    time.sleep(c)
    last_step_tofirealter()
    print("going into fire alter...")
    make_runes()
    b = 1  # random.randrange(1, 3)
    options = {1: to_bank
               }
    options[b]()
    functions.find_Object(1, left=0, top=0, right=w_win, bottom=h_win)
    c = random.uniform(8, 10)
    time.sleep(c)
    get_runes(bank_x, bank_y)


bank_runes_position_x = 375
bank_runes_position_y = 123
Run_Duration_Hours = 4

# object mark/ highlight bank chest in duel arena green
# object mark/ highlight entrance to fire alter yellow
# object mark/ highlight inside the fire alter yellow and the exit portal green

if __name__ == "__main__":
    findWindow("RuneLite")
    x = random.randrange(100, 250)
    y = random.randrange(400, 500)
    pyautogui.click(x, y, button='right')
    t_end = time.time() + (60 * 60 * Run_Duration_Hours)
    while time.time() < t_end:
        making_fire_runes(bank_runes_position_x, bank_runes_position_y)
    #os.system('shutdown -s -f')
    
