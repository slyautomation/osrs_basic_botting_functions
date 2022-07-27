import pyautogui
import random
import time
import functions
from fishing import pick_random_fishing_spot

from functions import random_combat, skill_lvl_up, Image_to_Text, spaces, resizeImage, find_Object_precise
from functions import random_quests
from functions import random_skills
from functions import random_inventory
from functions import random_breaks
from functions import Image_Rec_single

global hwnd
global iflag
global icoord
import core
from functions import pick_item, mini_map_image, random_breaks, find_Object, Image_count, xp_gain_check, drop_item, \
    release_drop_item, image_Rec_clicker, invent_crop
from functions import pick_item_right
from functions import exit_bank


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


def timer():
    startTime = time.time()
    return startTime


iflag = False


def bank_booth():
    c = random.uniform(0.6, 0.8)
    b = random.uniform(0.12, 0.28)
    x = random.randrange(340, 440)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(380, 500)  # y = random.randrange(50, 60)
    print('y: ', y)
    d = random.uniform(0.05, 0.19)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click()
    time.sleep(c)


def deposit_secondItem():
    c = random.uniform(0.4, 0.8)
    x = random.randrange(695, 715)  # 950,960
    z = x
    print('x: ', x)
    y = random.randrange(500, 515)  # 490,500
    w = y
    print('y: ', y)
    b = random.uniform(0.2, 0.6)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='right')
    time.sleep(c)
    print('stand in second bank cubicle')
    c = random.uniform(0.6, 0.9)
    x = random.randrange(z, z + 15)
    print('x: ', x)
    y = random.randrange(w + 100, w + 105)  # 110, 115
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)


def wine():
    a = random.uniform(0.1, 0.35)
    bank_booth()
    pick_item(490, 635)  # deposit all
    pick_item(135, 125)  # jug
    pick_item(185, 125)  # grapes
    time.sleep(a)
    a = random.uniform(0.05, 0.2)
    exit_bank()
    time.sleep(a)
    pick_item(660, 515)
    pick_item(745, 625)
    a = random.uniform(1, 2)
    time.sleep(a)
    pyautogui.press('space')
    a = random.uniform(17.5, 19)
    time.sleep(a)
    print("ready")

def apple_pie():
    a = random.uniform(0.1, 0.35)
    bank_booth()
    pick_item(490, 635)  # deposit all
    pick_item(135, 125)  # apple
    pick_item(185, 125)  # pie shell
    time.sleep(a)
    a = random.uniform(0.05, 0.2)
    exit_bank()
    time.sleep(a)
    pick_item(660, 515)
    pick_item(745, 625)
    a = random.uniform(1, 2)
    time.sleep(a)
    pyautogui.press('space')
    a = random.uniform(17.5, 19)
    time.sleep(a)
    print("ready")

def pastry():
    a = random.triangular(0.1, 0.5, 5)
    bank = False
    while bank == False:
        find_Object_precise(1, 5, 0, 0, 860, 775)
        b = random.triangular(0.1, 10, 0.5)
        time.sleep(b)
        bank = functions.bank_ready(False)
        print("bank deposit open:", bank)
    pick_item(490, 635)  # deposit all
    print('deposited')
    pick_item(135, 125)  # flour
    pick_item(185, 125)  # water
    print('items taken')
    time.sleep(a)
    exit_bank()
    invent = functions.invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    a = random.triangular(0.1, 0.5, 5)
    time.sleep(a)

    pick_item(660, 515)
    pick_item(745, 625)
    a = random.uniform(1, 2)
    time.sleep(a)
    pyautogui.press('2')
    inv = Image_count('flour.png')
    a = random.uniform(17.5, 19)
    time.sleep(a)
    print("ready")

def pizza():
    a = random.triangular(0.1, 0.5, 5)
    bank = False
    while bank == False:
        find_Object_precise(0, 5, 0, 0, 620, 775)
        b = random.triangular(3, 10, 3.5)
        time.sleep(b)
        bank = functions.bank_ready(False)
        print("bank deposit open:", bank)
    pick_item(490, 635)  # deposit all
    print('deposited')
    pick_item(185, 125)  # flour
    pick_item(230, 125)  # water
    print('items taken')
    time.sleep(a)
    exit_bank()
    invent = functions.invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    a = random.triangular(0.1, 0.5, 5)
    time.sleep(a)
    pick_item(660, 515)
    pick_item(745, 625)
    a = random.triangular(1, 2, 5)
    time.sleep(a)
    pyautogui.press('3')
    inv = Image_count('flour.png')
    while inv > 2:
        time.sleep(0.6)
        inv = Image_count('flour.png', 0.97)
        print(inv)
    time.sleep(a)
    print("ready")

def pieshell():
    a = random.uniform(0.1, 0.35)
    bank_booth()
    pick_item(490, 635)  # deposit all
    pick_item(420, 125)  # pie shell
    pick_item(375, 125)  # dough
    time.sleep(a)
    a = random.uniform(0.05, 0.2)
    exit_bank()
    time.sleep(a)
    pick_item(660, 515)
    pick_item(745, 625)
    a = random.uniform(1, 2)
    time.sleep(a)
    pyautogui.press('space')
    a = random.uniform(10, 15)
    time.sleep(a)
    print("ready")

def make_banking_food(volume, bank_food):
    while round(volume / 10) > 0:
        bank_options = {'wine': wine,
                        'pizza': pizza,
                        'a_pie': apple_pie,
                        'pastry': pastry,
                        'pie_shell': pieshell}
        bank_options[bank_food]()
        volume -= 1
        print(bank_food + ' left: ', round(volume / 10))

def to_alkarid_cookspot():
    print("to cookspot")
    while mini_map_image('alkarid_fishspot_step_1.png', 10, -20,  0.7, 'left', 15, 10 ) == False:
        mini_map_image('alkarid_fishspot_step_1.png', 10, -20,  0.7, 'left', 15, 10)
        print("step 1 to cooking spot  not found")
    random_breaks(5, 8)

    while mini_map_image('alkarid_fishspot_step_1.png',10, -50,   0.7, 'left',10, 15 ) == False:
        mini_map_image('alkarid_fishspot_step_1.png', 10, -50,  0.7, 'left',10, 15)
        print("step 1 to cooking spot  not found")
    random_breaks(5, 8)

    while mini_map_image('alkarid_fishspot_step_2.png', 15, 10,  0.7, 'left', 10, 0) == False:
        mini_map_image('alkarid_fishspot_step_2.png', 15, 10,  0.7, 'left', 10, 0)
        print("step 2 to cooking spot  not found")
    random_breaks(5, 8)

    while mini_map_image('alkarid_fishspot_step_2.png',10, -30, 0.7, 'left',15, 10 ) == False:
        mini_map_image('alkarid_fishspot_step_2.png',10,-30, 0.7, 'left', 15, 10)
        print("step 2 to cooking spot  not found")
    random_breaks(5, 8)
    find_Object(1, left=0, top=0, right=1890-1280, bottom=800)  # green
    random_breaks(5, 8)


def to_alkarid_fishspot():
    print("to fishspot")
    while mini_map_image('alkarid_fishspot_step_2.png',15, 10, 0.7, 'left', 10, 0) == False:
        mini_map_image('alkarid_fishspot_step_2.png', 15, 10, 0.7, 'left', 10, 0)
        print("step 1 to fishing spot not found")

    random_breaks(5, 8)

    while mini_map_image('alkarid_fishspot_step_2.png', 15, 10, 0.7, 'left', 10, 40) == False:
        mini_map_image('alkarid_fishspot_step_2.png', 15, 10, 0.7, 'left', 10, 40)
        print("step 1 to fishing spot not found")

    random_breaks(5, 8)

    while mini_map_image('alkarid_fishspot_step_3.png', 15, 10,  0.7, 'left', 10, 30) == False:
        mini_map_image('alkarid_fishspot_step_3.png', 15, 10,  0.7, 'left', 10, 30)
        print("step 1 to fishing spot not found")

    random_breaks(5, 8)

    while mini_map_image('alkarid_fishspot_step_1.png', 15, 10,  0.7, 'left',30, 5) == False:
        mini_map_image('alkarid_fishspot_step_1.png',  15, 10,  0.7, 'left', 30, 5)
        print("step 2 to fishing spot  not found")

    random_breaks(10, 12)
    pick_random_fishing_spot('prawn_fish')
    random_breaks(3, 5)

def drop_prawns():
    invent_crop()
    drop_item()
    image_Rec_clicker(r'prawn_fish.png', 'dropping item', 5, 5, 0.6, 'left', 10, False)
    release_drop_item()

def drop_fish():
    invent_crop()
    drop_item()
    image_Rec_clicker(r'salmon_fish.png', 'dropping item', 5, 5, 0.7, 'left', 10, False)
    release_drop_item()

def cook_all_fish_fire(Take_Human_Break=False):
    Image_Rec_single('salmon_fish.png','cook fish', 5, 5, 0.99, 'left', 8, False)
    random_breaks(0.1, 0.25)
    find_Object_precise(1, deep=5)  # green
    random_breaks(1, 1.5)
    pyautogui.press('space')
    salmon_1 = Image_count('salmon_fish.png', 0.99)
    trout_1 = Image_count('trout_fish.png', 0.99)
    salmon_2 = Image_count('salmon_cooked.png', 0.99)
    trout_2 = Image_count('trout_cooked.png', 0.99)
    if salmon_1 is None:
        salmon_1 = 0
    if salmon_2 is None:
        salomn_2 = 0
    if trout_1 is None:
        trout_1 = 0
    if trout_2 is None:
        trout_2 = 0
    all_prawns = (int(salmon_1) + int(trout_1)) - (int(salmon_2) + int(trout_2))
    while all_prawns > 0:
        salmon_1 = Image_count('salmon_fish.png', 0.99)
        trout_1 = Image_count('trout_fish.png', 0.99)
        salmon_2 = Image_count('salmon_cooked.png', 0.99)
        trout_2 = Image_count('trout_cooked.png', 0.99)
        if salmon_1 is None:
            salmon_1 = 0
        if salmon_2 is None:
            salomn_2 = 0
        if trout_1 is None:
            trout_1 = 0
        if trout_2 is None:
            trout_2 = 0
        all_prawns = (int(salmon_1) + int(trout_1)) - (int(salmon_2) + int(trout_2))
        print('cooking still: ', all_prawns)
        cooking_time = False
        time_start = time.time()
        while not cooking_time:
            cooking_time = xp_gain_check('cooking_xp.png')
            if not cooking_time:
                cooking_time = xp_gain_check('cooking_xp2.png')
            print(cooking_time)
            time_end = time.time() - time_start
            print("seconds count: %02d", time_end)
            x = random.uniform(7, 10)
            if time_end > x:
                Image_Rec_single('salmon_fish.png','cook fish', 5, 5, 0.99, 'left', 8, False)
                random_breaks(0.1, 0.25)
                find_Object_precise(1, deep=5)  # green
                random_breaks(1, 1.5)
                pyautogui.press('space')
                cooking_time = True
                break
        if Take_Human_Break:
            c = random.uniform(0.1, 50)
            time.sleep(c)


def cook_all_critters(Take_Human_Break=False):
    invent = functions.invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    random_breaks(0.1, 0.25)
    #find_Object(1)  # green
    random_breaks(0.6, 1.2)
    pyautogui.press('space')
    prawn_1 = Image_count('prawn_fish.png')
    prawn_2 = Image_count('prawn_cooked.png', 0.99)
    prawn_4 = Image_count('anch_cooked.png', 0.99)
    prawn_3 = Image_count('prawn_burnt.png', 0.99)
    if prawn_1 is None:
        prawn_1 = 0
    if prawn_2 is None:
        prawn_2 = 0
    if prawn_3 is None:
        prawn_3 = 0
    if prawn_4 is None:
        prawn_4 = 0
    all_prawns = int(prawn_1) - (int(prawn_2) + int(prawn_3) + int(prawn_4))
    while all_prawns > 0:
        prawn_1 = Image_count('prawn_fish.png')
        prawn_2 = Image_count('prawn_cooked.png', 0.99)
        prawn_4 = Image_count('anch_cooked.png', 0.99)
        prawn_3 = Image_count('prawn_burnt.png', 0.99)
        if prawn_1 is None:
            prawn_1 = 0
        if prawn_2 is None:
            prawn_2 = 0
        if prawn_3 is None:
            prawn_3 = 0
        if prawn_4 is None:
            prawn_4 = 0
        all_prawns = int(prawn_1) - (int(prawn_2) + int(prawn_3) + int(prawn_4))
        print('cooking still: ', all_prawns)
        cooking_time = False
        time_start = time.time()
        while not cooking_time:
            cooking_time = xp_gain_check('cooking_xp.png')
            if not cooking_time:
                cooking_time = xp_gain_check('cooking_xp2.png')
            print(cooking_time)
            time_end = time.time() - time_start
            print("seconds count: %02d", time_end)
            x = random.uniform(7, 10)
            if time_end > x:
                random_breaks(0.1, 0.25)
                find_Object(1,left=0, top=0, right=1890-1280, bottom=800)  # green
                random_breaks(0.6, 1.2)
                pyautogui.press('space')
                cooking_time = True
                break
        if Take_Human_Break:
            c = random.triangular(0.1, 5, 0.5)
            time.sleep(c)


def alkarid_powercook_and_fish(Take_Human_Break=False, Run_Duration_hours=6):
    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    while time.time() < t_end:
        invent = functions.invent_enabled()
        print(invent)
        if invent == 0:
            pyautogui.press('esc')
        if Image_count('prawn_fish.png') + Image_count(r'sea_puzzle.png') > 27:
            to_alkarid_cookspot()
        else:
            to_alkarid_fishspot()
        invent = Image_count('prawn_fish.png') + Image_count(r'sea_puzzle.png')
        while invent < 27:
            invent = functions.invent_enabled()
            print(invent)
            if invent == 0:
                pyautogui.press('esc')
            resizeImage()
            fished = Image_to_Text('thresh', 'textshot.png')
            print(fished)
            if fished.strip().lower() != 'fishing' and fished.lower() != 'plt]' and fished.lower() != 'ele]' and fished.lower() != 'fishinq':
                random_breaks(0.2, 3)
                pick_random_fishing_spot('prawn_fish')
                random_breaks(5, 10)
            if skill_lvl_up() != 0:
                print('level up')
                random_breaks(0.2, 3)
                pyautogui.press('space')
                random_breaks(0.1, 3)
                pyautogui.press('space')
                a = random.randrange(0, 2)
                # print(a)
                spaces(a)
            invent_crop()
            invent = Image_count('prawn_fish.png') + Image_count(r'sea_puzzle.png')
            print("fish & clues: ", invent)
        to_alkarid_cookspot()
        cook_all_critters(Take_Human_Break)
        drop_prawns()


if __name__ == "__main__":
    x = random.randrange(100, 250)
    y = random.randrange(400, 500)
    pyautogui.click(x, y, button='right')
    alkarid_powercook_and_fish(Take_Human_Break=True, Run_Duration_hours=3)
    #make_banking_food(1000, 'pizza') # makes 1000 food at the bank
