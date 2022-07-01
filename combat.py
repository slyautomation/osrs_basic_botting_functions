import numpy as np
import cv2
import pyautogui
import random
import time
import argparse
import os
global hwnd
global iflag
global icoord
import datetime
import pytesseract
from PIL import Image, ImageGrab
from functions import Image_to_Text, findarea_attack_quick
from functions import resizeImage
from functions import random_combat
from functions import random_quests
from functions import random_skills
from functions import random_inventory
from functions import image_Rec_clicker
import functions
import core

iflag = False

global newTime_break

newTime_break = False

global timer
global timer_break
global ibreak


def timer():
    startTime = time.time()
    return startTime


def random_pause():
    b = random.uniform(20, 250)
    print('pausing for ' + str(b) + ' seconds')
    time.sleep(b)
    newTime_break = True


options = {0: random_inventory,
           1: random_combat,
           2: random_skills,
           3: random_quests,
           4: random_pause}


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



def powerattack_text(monster='chicken', burybones=True, Pickup_loot=False, Take_Human_Break=False, Run_Duration_hours=6):
    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    # using the datetime.fromtimestamp() function
    date_time = datetime.datetime.fromtimestamp(t_end)
    print(date_time)
    group = monster_list.index(monster)
    while time.time() < t_end:
        randomizer(timer_break, ibreak)
        r = random.uniform(0.1, 5)
        resizeImage()
        mined = Image_to_Text('thresh', 'textshot.png')
        print(mined)
        print(monster_array[group])
        attack = 0
        for monsters in monster_array[group]:
            # print(monsters)
            if mined.lower() != monsters:
                attack += 1
        if attack == len(monster_array[group]):
            d = random.uniform(0.05, 0.1)
            time.sleep(d)
            if burybones and image_Rec_clicker('bones_icon.png', 'bury bones', 5, 5, 0.7, 'left', 5, False):
                c = random.uniform(0.6, 1)
                time.sleep(c)
            if Pickup_loot:
                if findarea_attack_quick(2, 5):  # pick up highlighted loot
                    c = random.uniform(3, 5)
                    time.sleep(c)
            if findarea_attack_quick(3):  # attack npc/monster
                c = random.uniform(3, 5)
                time.sleep(c)
                if Take_Human_Break:
                    c = random.triangular(0.1, 50, 3)
                    time.sleep(c)


if __name__ == "__main__":
    # do whatever you do
    # ----- UPDATE WITH ALL VARIATIONS OF MONSTER'S IMAGE TO TEXT RESULT IN LINE WITH MONSTER_LIST -----
    monster_array = [
        ['chicken'], ['guard', 'gua rd'], ['cow', 'cou'], ['monk'], ['imp'], ['skeleton'], ['dwarf', 'dwarf‘']
    ]
    # --------------------------------------------------------------------------------------------------
    monster_list = ['chicken', 'guard', 'cow', 'monk', 'imp', 'skeleton', 'dwarf']

    resizeImage()
    x = random.randrange(100, 250)
    y = random.randrange(400, 500)
    pyautogui.click(x, y, button='right')
    ibreak = random.randrange(300, 2000)
    print('will break in   ' + str(ibreak / 60) + ' minutes')
    timer_break = timer()
    powerattack_text('cow', Take_Human_Break=False, Run_Duration_hours=4)
    #os.system('shutdown -s -f')
