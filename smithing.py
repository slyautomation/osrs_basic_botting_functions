
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

def pick_iron_bars():
    pick_item(1655 - 1280, 162)
    random_breaks(0.5, 1.5)

def pick_bronze_bars():
    pick_item(1655 - 1280, 123) #375
    random_breaks(0.5, 1.5)

def pick_steel_bars():
    pick_item(1703 - 1280, 162)
    random_breaks(0.5, 1.5)

def pick_mithril_bars():
    pick_item(1703 - 1280, 123)
    random_breaks(0.5, 1.5)

def bank_spot_varrock():
    find_Object_precise(2, 8) #amber


def smith_spot_varrock():
    find_Object_precise(0, 5, 0, 0, 610, 775) #red

def cast_superheat():
    pick_item(2029 - 1280, 573)

def smith_object(type):
    Image_Rec_single(type, 'smith weapon/armour', 10, 10, 0.8, 'left', 20, 0, 0, True)

def smith_items(num, bar, vol, smith_item):
    j = round((num*vol) / 27) + 1
    pick_options = {0: pick_bronze_bars,
               1: pick_iron_bars,
                    2: pick_steel_bars,
                3: pick_mithril_bars
                    }
    barlist = ['bronze_bar.png', 'iron_bar.png', 'steel_bar.png', 'mithril_bar.png']
    while j > 0:
        bank_spot_varrock()
        random_breaks(7.5, 9)
        deposit_secondItem()
        random_breaks(0.3, 0.5)
        pick_options[bar]()
        exit_bank()
        random_breaks(0.05, 0.2)
        inv = Image_count(barlist[bar])
        smith_spot_varrock()
        random_breaks(7.5, 9)
        smith_object(smith_item + '.png')
        while inv > vol:
            if skill_lvl_up() != 0:
                print('level up')
                random_breaks(0.2, 3)
                pyautogui.press('space')
                random_breaks(0.1, 3)
                pyautogui.press('space')
                a = random.randrange(0, 2)
                # print(a)
                spaces(a)
                smith_spot_varrock()
                random_breaks(1, 2)
                smith_object(smith_item + '.png')
            inv = Image_count(barlist[bar])
        j -= 1
        random_breaks(0.4, 0.8)

def smith_to_40():
    # ------ SMITH TO 40 ------- # 222 bronze # 485 iron # 600 steel
    smith_items(32, 0, 1, 'bronze_axe')
    smith_items(95, 0, 2, 'bronze_scimitar')
    smith_items(69, 1, 1, 'iron_axe')
    smith_items(208, 1, 2, 'iron_scimitar')
    smith_items(202, 2, 1, 'steel_axe')
    smith_items(198, 2, 2, 'steel_scimitar')

smith_items(1082, 2, 3, 'steel_chainbody')

steel_smithables = ['steel_axe', 'steel_scimitar', 'steel_nails', 'steel_chainbody']