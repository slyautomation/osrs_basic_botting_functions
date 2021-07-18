import pyautogui
import random
import time

import pytesseract
from functions import Image_count
from functions import skill_lvl_up
from functions import spaces
from functions import pick_item
from functions import random_combat
from functions import random_quests
from functions import random_skills
from functions import random_inventory
from functions import random_breaks
from functions import find_Object_precise
from functions import exit_bank
from functions import Image_Rec_single
from functions import deposit_secondItem

import core

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


def pick_gold_bars():
    pick_item(1751 - 1280, 123)  # pick in bank
    random_breaks(0.5, 1.5)


def pick_sapphires():
    pick_item(1751 - 1280, 123)  # pick in bank
    random_breaks(0.5, 1.5)
    pick_item(1703 - 1280, 159)  # pick in bank
    random_breaks(0.5, 1.5)


def pick_silver_bars():
    pick_item(1751 - 1280, 198)  # 375 # pick in bank
    random_breaks(0.5, 1.5)


def bank_spot_edgville():
    find_Object_precise(1, 5, 0, 0, 860, 775)  # green


def craft_spot_edgville():
    find_Object_precise(0, 5, 0, 0, 860, 775)  # red


def craft_gold_ring():
    pick_item(1389 - 1280, 277)  # 375
    random_breaks(0.5, 1.5)


def craft_sapphire_ring():
    pick_item(1439 - 1280, 277)  # 375
    random_breaks(0.5, 1.5)


def craft_bar_items(num, type, craft_item, run_time_minutes=360):
    # run_time_minutes 6hrs by default
    t_end = time.time() + 60 * run_time_minutes
    while time.time() < t_end:
        if type == 2:
            j = round((num) / 13) + 1
        else:
            j = round((num) / 27) + 1

        pick_options = {0: pick_gold_bars,
                        1: pick_silver_bars,
                        2: pick_sapphires
                        }
        craft_options = {'gold_ring': craft_gold_ring,
                         'sapphire_ring': craft_sapphire_ring,
                         }
        barlist = ['gold_bar.png', 'silver_bar.png', 'gold_bar.png']
        while j > 0:
            bank_spot_edgville()
            random_breaks(9.5, 11)
            deposit_secondItem()
            random_breaks(0.3, 0.5)
            pick_options[type]()
            exit_bank()
            random_breaks(0.05, 0.2)
            inv = Image_count(barlist[type])  # 0 or 1
            craft_spot_edgville()
            random_breaks(9.5, 11)
            craft_options[craft_item]()
            while inv > 0:
                if skill_lvl_up() != 0:
                    print('level up')
                    random_breaks(0.2, 3)
                    pyautogui.press('space')
                    random_breaks(0.1, 3)
                    pyautogui.press('space')
                    a = random.randrange(0, 2)
                    # print(a)
                    spaces(a)
                    craft_spot_edgville()
                    random_breaks(1, 2)
                    craft_options[craft_item]()
                inv = Image_count(barlist[type])
                print(inv)
            j -= 1
            random_breaks(0.4, 0.8)


# run_time_minutes 6hrs by default

if __name__ == "__main__":
    craft_bar_items(2200, 2, 'sapphire_ring', run_time_minutes=360)
