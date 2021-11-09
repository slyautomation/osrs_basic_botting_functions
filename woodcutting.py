import numpy as np
import cv2
import pyautogui
import random
import time
import os
import functions
import pytesseract
from PIL import Image
from functions import Image_count, image_Rec_clicker, screen_Image, 
    release_drop_item, drop_item, Image_to_Text, random_breaks, 
    invent_crop,Image_Rec_single,resizeImage,skill_lvl_up,spaces,mini_map_image,
    random_combat,random_quests, random_skills,random_inventory,random_breaks, find_Object,xp_gain_check

global hwnd,iflag,icoord, newTime_break,timer,timer_break,ibreak
iflag = False
newTime_break = False


def random_break(start, c):
    global newTime_break
    startTime = time.time()
    # 1200 = 20 minutes
    a = random.randrange(0, 4)
    if startTime - start > c:
        options[a]()
        newTime_break = True


def randomizer(timer_breaks, ibreaks):
    global newTime_break
    global timer_break
    global ibreak
    random_break(timer_breaks, ibreaks)
    if newTime_break == True:
        timer_break = timer()
        ibreak = random.randrange(600, 2000)
        newTime_break = False

    # b = random.uniform(4, 5)


def timer():
    startTime = time.time()
    return startTime


def random_pause():
    b = random.uniform(20, 250)
    print('pausing for ' + str(b) + ' seconds')
    time.sleep(b)
    newTime_break = True


iflag = False

options = {0: random_inventory,
           1: random_combat,
           2: random_skills,
           3: random_quests,
           4: random_pause}


def drop_wood(type):
    print("dropping wood starting...")
    invent_crop()
    drop_item()
    image_Rec_clicker(type + '_icon.png', 'dropping item', 5, 5, 0.9, 'left', 10, 620, 480, False)
    release_drop_item()
    print("dropping wood done")


def firespot(spot):
    firespots = ['firespot_varrock_wood', 'firespot_draynor_willow', 'firespot_draynor_oak'
        , 'firespot_farador_oak', 'firespot_draynor_wood', 'firespot_lumbridge_wood']
    x_dy = random.randrange(-40,-30)
    y_dy = random.randrange(15,25)
    xy_firespots = [[45, 57], [50, 40], [80, 40], [x_dy, y_dy], [25, 20], [0, -5]]

    x = xy_firespots[firespots.index(spot)][0]
    y = xy_firespots[firespots.index(spot)][1]

    print(mini_map_image(spot + '.png', x, y, 0.7, 'left', 5, 0))
    # print(mini_map_image(spot + '.png',  45, 57, 0.7, 'left', 5, 0)) # varrock wood
    # print(mini_map_image(spot + '.png', 50, 40, 0.7, 'left', 5, 0)) # draynor willow
    # print(mini_map_image(spot + '.png', 80, 40, 0.7, 'left', 5, 0)) # draynor oak
    # print(mini_map_image(spot + '.png', 25, 20, 0.7, 'left', 5, 0))  # farador oak
    # print(mini_map_image(spot + '.png', 25, 20, 0.7, 'left', 5, 0))  # draynor wood


def bank_spot():
    find_Object_precise(1, 5, 0, 0, 860, 775)
def pick_random_tree_spot(num):
    find_Object(num)  # 2 = amber

def invent_enabled():
    return Image_count('inventory_enabled.png', threshold=0.9)


def deposit_bank_items():
    bank = Image_count('bank_deposit.png', 0.75)
    if bank > 0:
        deposit_secondItem()
        random_breaks(0.3, 0.5)
        exit_bank()
        mini_map_image('draynor_bank_spot.png', 35, 40, 0.7, 'left', 15, 10)
        return bank
    else:
        print("bank inventory not found")
        bank_spot()
        random_breaks(5, 10)
        return bank

def powercutter(type, firemaking=False, bank_items=False, spot='', num=2, Take_Human_Break=True, Run_Duration_hours=6):
    j = 0
    if firemaking:
        inv = 26
    else:
        inv = 27
    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    while time.time() < t_end:
        randomizer(timer_break, ibreak)
        resizeImage()
        fished = Image_to_Text('thresh', 'textshot.png')
        # print(fished)
        if fished.lower() != 'woodcutting' and fished.lower() != 'joodcuttine' and fished.lower() != 'foodcuttir' and fished.lower() != 'foodcuttin' and fished.lower() != 'joodcuttinc':
            random_breaks(0.2, 3)
            pick_random_tree_spot(num)
            random_breaks(5, 7)
        if skill_lvl_up() != 0:
            print('level up')
            random_breaks(0.2, 3)
            pyautogui.press('space')
            random_breaks(0.1, 3)
            pyautogui.press('space')
            a = random.randrange(0, 2)
            # print(a)
            spaces(a)
        # invent_crop()
        invent = invent_enabled()
        print(invent)
        if invent == 0:
            pyautogui.press('esc')
        invent_count = Image_count(type + '_icon.png')
        print("wood: ", invent_count)
        if invent_count > inv:
            if firemaking:
                firespot(spot)
                random_breaks(5, 8)
                d = random.randrange(15, 20)
                while invent_count > d:
                    invent_count = Image_count(type + '_icon.png')
                    print("wood: ", invent_count)
                    random_breaks(0.1, 0.3)
                    Image_Rec_single('tinderbox.png', 'burning wood', 5, 5, 0.9, 'left', 8, 620, 480, False)
                    random_breaks(0.1, 0.3)
                    Image_Rec_single(type + '_icon.png', 'burning wood', 5, 5, 0.9, 'left', 8, 620, 480, False)
                    fire = False
                    time_start = time.time()
                    while not fire:
                        fire = xp_gain_check('firemaking_xp.png')
                        if not fire:
                            fire = xp_gain_check('firemaking_xp2.png')
                        print(fire)
                        time_end = time.time() - time_start
                        print("seconds count: %02d", time_end)
                        if time_end > 30:
                            invent_count = 0
                            fire = True
                            break
            if bank_items:
                invent = invent_enabled()
                print(invent)
                if invent == 0:
                    pyautogui.press('esc')
                bank_spot()
                bank = deposit_bank_items()
                random_breaks(9.5, 11)
                while bank == 0:
                    bank = deposit_bank_items()
            else:
                random_breaks(0.2, 0.7)
                drop_wood(type)
            if Take_Human_Break:
                c = random.triangular(0.1, 50, 5)
                time.sleep(c)




if __name__ == "__main__":
    time.sleep(2)
    resizeImage()
    x = random.randrange(100, 250)
    y = random.randrange(400, 500)
    pyautogui.click(x, y, button='right')
    ibreak = random.randrange(300, 2000)
    print('will br   eak in   ' + str(ibreak / 60) + ' minutes')
    timer_break = timer()
    firespots = ['firespot_varrock_wood', 'firespot_draynor_willow', 'firespot_draynor_oak'
        , 'firespot_farador_oak', 'firespot_draynor_wood']
    powercutter('oak', firemaking=False, bank_items=True, spot='', num=2, Take_Human_Break=True, Run_Duration_hours=5)
