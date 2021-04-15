import numpy as np
import cv2
import pyautogui
import random
import time
import os

import pytesseract
from PIL import Image
from functions import Image_count
from functions import image_Rec_clicker
from functions import screen_Image
from functions import release_drop_item
from functions import drop_item
from functions import Image_to_Text
from functions import random_breaks
from functions import invent_crop
from functions import Image_Rec_single
from functions import resizeImage
from functions import skill_lvl_up
from functions import spaces

from functions import random_combat
from functions import random_quests
from functions import random_skills
from functions import random_inventory
from functions import random_breaks
#from core import findWindow_runelite

global hwnd
global iflag
global icoord
iflag = False
global newTime_break
newTime_break = False
global timer
global timer_break
global ibreak





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

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
iflag = False

options = {0: random_inventory,
           1: random_combat,
           2: random_skills,
           3: random_quests,
           4: random_pause}

def drop_fish():
    print("dropping fish starting...")
    invent_crop()
    drop_item()
    image_Rec_clicker(r'prawn_fish.png', 'dropping item', 5, 5, 0.9, 'left', 10, 620, 480, False)
    image_Rec_clicker(r'trout_fish.png', 'dropping item', 5, 5, 0.9, 'left', 10, 620, 480, False)
    image_Rec_clicker(r'salmon_fish.png', 'dropping item', 5, 5, 0.9, 'left', 10,  620, 480, False)
    image_Rec_clicker(r'lobster_fish.png', 'dropping item', 5, 5, 0.9, 'left', 10, 620, 480, False)
    release_drop_item()
    print("dropping fish done")

def pick_random_fishing_spot(type):
    Image_Rec_single(type + '.png', 'picking fishing spot', 5, 5,  0.7, 'left', 10)

def powerfisher(type):
    j = 0
    while j < 10:
        randomizer(timer_break, ibreak)
        resizeImage()
        fished = Image_to_Text('thresh', 'textshot.png')
        #print(fished)
        if fished.lower() != 'fishing' and fished.lower() != 'plt]' and fished.lower() != 'ele]':
            random_breaks(0.2, 3)
            pick_random_fishing_spot(type)
            random_breaks(5, 10)
        if skill_lvl_up() != 0:
            print('level up')
            random_breaks(0.2, 3)
            pyautogui.press('space')
            random_breaks(0.1, 3)
            pyautogui.press('space')
            a = random.randrange(0, 2)
            #print(a)
            spaces(a)
        #invent_crop()
        invent = Image_count(type + '.png') + Image_count(r'sea_puzzle.png')
        print("fish & clues: ", invent)
        if type == 'prawn_fish' or type == 'lobster_fish':
            z = 26
        else:
            z = 25
        if invent > z - 2:
            random_breaks(0.2, 0.7)
            drop_fish()
            random_breaks(0.2, 0.7)
            pick_random_fishing_spot(type)

time.sleep(2)
resizeImage()
x = random.randrange(100, 250)
y = random.randrange(400, 500)
pyautogui.click(x, y, button='right')
ibreak = random.randrange(300, 2000)
print('will break in   ' + str(ibreak / 60) + ' minutes')
timer_break = timer()
powerfisher('lobster_fish')
