from threading import Thread

import keyboard
from PIL import ImageGrab

import core
import cv2
import numpy as np

global hwnd
global iflag
global icoord
import functions
from functions import Image_count
from functions import screen_Image
from functions import Image_to_Text
from functions import resizeImage
from functions import find_Object_precise

from functions import random_combat
from functions import random_quests
from functions import random_skills
from functions import random_inventory
from functions import random_breaks

import time
import random
import pyautogui

global hwnd
global iflag
global icoord
iflag = False
global newTime_break
newTime_break = False
global timer
global timer_break
global ibreak


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

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
    global actions
    b = random.uniform(20, 250)
    actions = 'pausing for ' + str(b) + ' seconds'
    time.sleep(b)
    newTime_break = True


options = {0: random_inventory,
           1: random_combat,
           2: random_skills,
           3: random_quests,
           4: random_pause}


def determine_position_to_bank():
    global ore_count, gem_count, clue_count, actions
    if ore_count + gem_count + clue_count < 27:
        return 4
    if functions.mini_map_bool('port_sarim_spot_water.png', 0.85):
        actions = 'player located @ step 2'
        return 2
    if functions.mini_map_bool('port_sarim_jewl.png', 0.85):
        actions = 'player located @ step 1'
        return 1
    if functions.mini_map_bool('rim_mine_spot1.png', 0.85):
        actions = 'player located @ step 0'
        return 0
    else:
        return 0

def determine_position_to_clay():
    global ore_count, gem_count, clue_count, actions
    gem_count = int(count_gems() + count_gems2())
    ore_count = int(inv_count('clay'))
    clue_count = int(count_geo())
    if ore_count + gem_count + clue_count > 27:
        return 6
    if functions.mini_map_bool('clay_deposit_spot1.png', 0.85):
        actions = 'player located @ step 1 Spot 5 _1'
        return 0
    if functions.mini_map_bool('clay_deposit_spot4.png', 0.85):
        actions = 'player located @ step 1 Spot 5 _4'
        return 0
    if functions.mini_map_bool('clay_deposit_spot5.png', 0.85):
        actions = 'player located @ step 1 Spot 5 _5'
        return 1
    if functions.mini_map_bool('clay_deposit_spot3.png', 0.85):
        actions = 'player located @ step 1 Spot 5 _3'
        return 1
    if functions.mini_map_bool('clay_deposit_spot2.png', 0.85):
        actions = 'player located @ step 1 Spot 5 _2'
        return 1
    if functions.mini_map_bool('port_sarim_spot_water.png', 0.85):
        actions = 'player located @ step 2'
        return 2
    if functions.mini_map_bool('port_sarim_jewl.png', 0.85):
        actions = 'player located @ step 3'
        return 3
    if functions.mini_map_bool('rim_mine_spot1.png', 0.85):
        actions = 'player located @ step 4'
        return 5
    if functions.mini_map_bool('bank_deposit.png', 0.85):
        actions = 'player located @ step 0'
        return 0
    else:
        return 0

def rim_minetobank():
    global actions
    step = 0
    step = determine_position_to_bank()
    c = random.uniform(14, 15)
    x = 60
    y = 25
    if step == 0:
        while functions.mini_map_image('rim_mine_spot1.png', x, y, 0.8, 'left') != True:
            actions = 'finding 1st step to bank'
        time.sleep(c)
        actions = '1st step to bank'
        step = 1

    c = random.uniform(9, 10)
    x = 10
    y = 1
    if step == 1:
        while functions.mini_map_image('port_sarim_jewl.png', x, y, 0.8, 'left') != True:
            actions = 'finding 2nd step to bank'
        time.sleep(c)
        actions = '2nd step to bank'


    c = random.uniform(9, 10)
    x = 50
    y = -25
    if step == 1:
        while functions.mini_map_image('port_sarim_jewl.png', x, y, 0.8, 'left') != True:
            actions = 'finding 3rd step to bank'
        time.sleep(c)
        actions = '3rd step to bank'
        step = 2

    c = random.uniform(11, 12)
    x = 75
    y = 25
    if step == 2:
        while functions.mini_map_image('port_sarim_spot_water.png', x, y, 0.8, 'left') != True:
            actions = "finding 4th step to bank"
        time.sleep(c)
        actions = '4th step to bank'
        step = 3

    if step == 3:
        b = random.uniform(0.175, 0.677)
        x = random.randrange(750, 755)
        #print('x: ', x)
        y = random.randrange(175, 180)
        #print('y: ', y)
        c = random.uniform(10, 12)
        pyautogui.click(x, y, 1, duration=b, button='left')
        time.sleep(c)
        actions = '5th step to bank'
        b = random.uniform(0.175, 0.677)
        x = random.randrange(750, 755)  # 1755,1765
        #print('x: ', x)
        y = random.randrange(140, 145)  # 175,185
        #print('y: ', y)
        c = random.uniform(9, 10)
        pyautogui.click(x, y, 1, duration=b, button='left')
        actions = 'last step to bank'
        time.sleep(c)
        c = random.uniform(2.1, 3)
        find_banker()
        actions = 'finding deposit box'
        time.sleep(c)
        while not depositbox():
            c = random.uniform(2.1, 3)
            find_banker()
            actions = 'finding deposit box'
            time.sleep(c)
        actions = 'finished deposit end of function'
        c = random.uniform(1, 5)
        time.sleep(c)
        step = 4

def nums(first_number, last_number, step=1):
    return range(first_number, last_number+1, step)

def rim_minetoclay():
    global actions
    actions = 'start of function'
    step = 0
    step = determine_position_to_clay()
    if step == 0:
        b = random.uniform(0.175, 0.677)
        x = random.randrange(710, 725)
        #print('x: ', x)
        y = random.randrange(60, 70)
        #print('y: ', y)
        c = random.uniform(10, 12)
        pyautogui.click(x, y, 1, duration=b, button='left')
        time.sleep(c)
        actions = '0 step to mining clay'
        step = 1
    c = random.uniform(11, 12)
    x = -5
    y = 0
    if step == 1:
        spot = functions.mini_map_image('clay_deposit_spot5.png', x, 5, 0.85, 'left')
        while spot != True:
            actions = 'finding 1st clay mine step'
            for i in nums(1, 5):
                if i == 5 or i == 3 or i == 1:
                    y = 5
                spot = functions.mini_map_image('clay_deposit_spot' + str(i) + '.png', x, y, 0.85, 'left')
                if spot:
                    actions = '1st clay mine step found _' + str(i)
                    break


        time.sleep(c)
        actions = '1st step to mine clay'
        step = 2
    c = random.uniform(11, 12)
    x = 0
    y = 40
    if step == 2:
        while functions.mini_map_image('port_sarim_spot_water.png', x, y, 0.85, 'left') != True:
            actions = 'finding 2nd clay mine step'
        time.sleep(c)
        actions = '2nd step to mine clay'
        step = 3

    c = random.uniform(9, 10)
    x = -15
    y = -10
    if step == 3:
        while functions.mini_map_image('port_sarim_jewl.png', x, y, 0.85, 'left') != True:
            actions = 'finding 3rd clay mine step'
        time.sleep(c)
        actions = '3rd step to mine clay'
        step = 4

    c = random.uniform(9, 10)
    x = -50
    y = 30
    if step == 4:
        while functions.mini_map_image('port_sarim_jewl.png', x, y, 0.85, 'left') != True:
            actions = 'finding 4th clay mine step'
        time.sleep(c)
        actions = '4th step to mine clay'
        step = 5

    c = random.uniform(14, 15)
    x = -8
    y = 33
    if step == 5:
        while functions.mini_map_image('rim_mine_spot1.png', x, y, 0.9, 'left') != True:
            actions = 'finding 5th clay mine step'
        time.sleep(c)
        actions = '5th step to mine clay'
        step = 6

def find_banker():
    find_Object_precise(0, 0, 0, 700, 800)  # red

def depositbox():
    global actions
    if functions.Image_count('bank_deposit.png', 0.8, 0, 0, 700, 800) > 0:
        b = random.uniform(0.1, 0.65)
        x = random.randrange(370, 390)  # 950,960
        y = random.randrange(440, 460)  # 490,500
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.1)
        pyautogui.click(duration=b)
        actions = 'successful deposit...'
        c = random.uniform(0.1, 1)
        time.sleep(c)
        gem_count = int(count_gems() + count_gems2())
        ore_count = int(inv_count('clay'))
        clue_count = int(count_geo())
        total_invent = gem_count + ore_count + clue_count
        if total_invent > 0:
            return False
        return True
    actions = 'deposit box not found...'
    return False

def count_gems():
    return Image_count('gem_icon.png')
def count_geo():
    return Image_count('geo_icon.png')
def count_gems2():
    return Image_count('gem_icon2.png')
def inv_count(name):
    return Image_count(name + '_ore.png')

def timer_countdown():
    global Run_Duration_hours, stop_script
    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    #print(t_end)
    final = round((60 * 60 * Run_Duration_hours) / 1)
    #print(final)
    for i in range(final):
        caps = keyboard.is_pressed('capslock')
        if caps or stop_script:
            stop_script = True
            print('\n manually stopped script!!!')
            exit()
        # the exact output you're looking for:
        print(bcolors.OK + f'\r[%-10s] %d%%' % ('='*round((i/final)*10), round((i/final)*100)), f'time left: {(t_end - time.time())/60 :.2f} mins | coords: {spot} | status: {mined_text} | ore: {ore_count} | gems: {gem_count} | clues: {clue_count} | {actions}', end='')
        time.sleep(1)

def moneymaker_clay(Take_Human_Break=False, Run_Duration_hours=4, color=6):
    global stop_script, spot, mined_text, time_left, powerlist, actions, powerlist, t_end, gem_count, ore_count, clue_count
    print("Will break in: %.2f" % (ibreak / 60) + " minutes |", "Mine Ore Selected: Clay")
    t1 = Thread(target=timer_countdown)
    t1.start()
    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    invent = functions.invent_enabled()
    if invent == 0:
        actions = 'opening inventory'
        pyautogui.press('esc')
    gem_count = int(count_gems() + count_gems2())
    ore_count = int(inv_count('clay'))
    clue_count = int(count_geo())
    if ore_count + gem_count + clue_count > 27:
        rim_minetobank()
        rim_minetoclay()
    step = determine_position_to_clay()
    if step != 5:
        rim_minetoclay()
    while time.time() < t_end:
        caps = keyboard.is_pressed('capslock')
        if caps or stop_script:
            stop_script = True
            print('\n manually stopped script!!!')
            exit()
        invent = functions.invent_enabled()
        if invent == 0:
            actions = 'opening inventory'
            pyautogui.press('esc')
        randomizer(timer_break, ibreak)
        r = random.uniform(0.1, 1)
        gem_count = int(count_gems() + count_gems2())
        ore_count = int(inv_count('clay'))
        clue_count = int(count_geo())
        inventory = gem_count + ore_count + clue_count
        if inventory > 27:
            random_breaks(0.1, 0.7)
            actions = 'Going to Bank'
            rim_minetobank()
            actions = 'Going to Mining Spot'
            rim_minetoclay()
        mined_text = Image_to_Text('thresh', 'textshot.png')
        if mined_text.strip().lower() != 'mining' and mined_text.strip().lower() != 'mininq':
            #actions = 'Not mining'
            spot = functions.find_Object(color, 0, 0, 700, 800)
            if Take_Human_Break:
                c = random.triangular(0.05, 30, 0.5)
                time.sleep(c)
            else:
                c = random.triangular(0.05, 0.1, 0.08)
                time.sleep(c)


x = random.randrange(100, 250)
y = random.randrange(400, 500)
pyautogui.click(x, y, button='right')
ibreak = random.randrange(300, 2000)
timer_break = timer()
spot = (0, 0)
actions = 'None'
mined_text = 'Not Mining'
ore_count = 0
gem_count = 0
clue_count = 0
stop_script = False
# ----- OBJECT MARKER COLOR FOR CLAY ------
red = 0
green = 1
amber = 2

# --------- CHANGE TO RUN FOR AMOUNT OF HOURS ----------------
Run_Duration_hours = 4
# TO STOP SCRIPT WHILE MINING HOLD CAPSLOCK KEY
moneymaker_clay(Take_Human_Break=False, Run_Duration_hours=Run_Duration_hours, color=green)

