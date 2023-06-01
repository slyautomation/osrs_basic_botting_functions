import os
import win32gui
import cv2
import numpy as np
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

pyautogui.FAILSAFE = False
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

def findWindow(data):  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, data)
    # hwnd = win32gui.GetForegroundWindow()860
    #print('findWindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)
    # win32gui.ShowWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)
    
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

def Image_Rec_single_random(image, threshold=0.7, clicker='left'):
    functions.screen_Image(620, 480, 820, 750, 'closest.png')
    img_rgb = cv2.imread('images/closest.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/' + image, 0)
    w, h = template.shape[::-1]
    pt = None
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    close_list = []
    close_points = []
    pos = pyautogui.position()
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        close_list.append(abs(abs(pos[0] - pt[0]) + abs(pos[1] - pt[1])))
        close_points.append(pt)
    if pt is None:
        print('not found')
        return False
    pick_random_item = random.randrange(0, len(close_points))
    coords = close_points[pick_random_item]
    print(coords)
    x = random.randrange(5, 20) + 620
    y = random.randrange(5, 20) + 480
    icoord = coords[0] + x
    icoord = (icoord, coords[1] + y)
    b = random.uniform(0.1, 0.7)
    pyautogui.moveTo(icoord, duration=b)
    b = random.uniform(0.01, 0.3)
    pyautogui.click(icoord, duration=b, button=clicker)
    return close_points
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

def item_inv(item):
    counter = 0
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"screen.png")
    img_rgb = cv2.imread('screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/' + str(item), 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    #cv2.imwrite('res.png', img_rgb)
    return counter
def make_item(volume, name, name2, x_i, y_i, x_i2, y_i2, number, i=55):
    j = round(volume/ 14)
    while j > 0:
        error_c = 0
        while functions.bank_ready(False) == False:
            if error_c > 3:
                exit()
            find_Object(1)
            c = random.uniform(1, 3)
            time.sleep(c)
            error_c += 1
        c = random.uniform(0.1, 0.6)
        functions.deposit_all_Bank()
        time.sleep(c)
        pick_item(x_i, y_i)
        pick_item(x_i2, y_i2)
        exit_bank()
        invent = functions.invent_enabled()
        print(invent)
        if invent == 0:
            pyautogui.press('esc')
        time_start = time.time()
        time_end = 0
        x = random.uniform(i, i+5)
        while item_inv(name) > 0 and time_end < x:
            invent = functions.invent_enabled()
            print(invent)
            if invent == 0:
                pyautogui.press('esc')
            e = random.uniform(0.1, 0.4)
            time.sleep(e)
            Image_Rec_single_random(name2, 0.7, 'left')
            e = random.uniform(0.1, 0.9)
            time.sleep(e)
            Image_Rec_single_random(name, 0.7, 'left')
            e = random.uniform(0.1, 1.1)
            time.sleep(e)
            pyautogui.press(number)
            while skill_lvl_up() == 0 and time_end < x:
                time_end = time.time() - time_start
                print('seconds count: %.2f' % time_end)
                print('items left: ', item_inv(name))
                while functions.make_enabled('make_how.png') == 1:
                    pyautogui.press(number)
                    e = random.uniform(0.1, 0.9)
                    time.sleep(e)
                if item_inv(name) == 0:
                    break
                if skill_lvl_up() == 1:
                    Image_Rec_single_random(name2, 0.7, 'left')
                    e = random.uniform(0.1, 0.9)
                    time.sleep(e)
                    Image_Rec_single_random(name, 0.7, 'left')
                    e = random.uniform(0.1, 0.4)
                    time.sleep(e)
                    pyautogui.press(number)

        time.sleep(c)
        j -= 1
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
    print("\rto cookspot")
    while mini_map_image('alkarid_fishspot_step_1.png', 10, -20,  0.7, 'left', 15, 10 ) == False:
        mini_map_image('alkarid_fishspot_step_1.png', 10, -20,  0.7, 'left', 15, 10)
        print("\rstep 1 to cooking spot  not found")
    random_breaks(5, 8)
    print("\rto cookspot - step 1")
    while mini_map_image('alkarid_fishspot_step_1.png',10, -50,   0.7, 'left',10, 15 ) == False:
        mini_map_image('alkarid_fishspot_step_1.png', 10, -50,  0.7, 'left',10, 15)
        print("\rstep 2 to cooking spot  not found")
    random_breaks(5, 8)
    print("\rto cookspot - step 2")
    while mini_map_image('alkarid_fishspot_step_2.png', 15, 10,  0.7, 'left', 10, 0) == False:
        mini_map_image('alkarid_fishspot_step_2.png', 15, 10,  0.7, 'left', 10, 0)
        print("\rstep 3 to cooking spot  not found")
    random_breaks(5, 8)
    print("\rto cookspot - step 3")
    while mini_map_image('alkarid_fishspot_step_2.png',10, -30, 0.7, 'left',15, 10 ) == False:
        mini_map_image('alkarid_fishspot_step_2.png',10,-30, 0.7, 'left', 15, 10)
        print("\rstep 4 to cooking spot  not found")
    random_breaks(5, 8)
    find_Object(1, left=0, top=0, right=1890-1280, bottom=800)  # green
    random_breaks(5, 8)
    print("\rto cookspot - step 4")

def to_alkarid_fishspot():
    print("to fishspot")
    while mini_map_image('alkarid_fishspot_step_2.png',15, 10, 0.7, 'left', 10, 0) == False:
        mini_map_image('alkarid_fishspot_step_2.png', 15, 10, 0.7, 'left', 10, 0)
        print("\rstep 1 to fishing spot not found")

    random_breaks(5, 8)
    print("\rto fishspot- step 1")
    while mini_map_image('alkarid_fishspot_step_2.png', 15, 10, 0.7, 'left', 10, 40) == False:
        mini_map_image('alkarid_fishspot_step_2.png', 15, 10, 0.7, 'left', 10, 40)
        print("\rstep 2 to fishing spot not found")

    random_breaks(5, 8)
    print("\rto fishspot - step 2")
    while mini_map_image('alkarid_fishspot_step_3.png', 15, 10,  0.7, 'left', 10, 30) == False:
        mini_map_image('alkarid_fishspot_step_3.png', 15, 10,  0.7, 'left', 10, 30)
        print("\rstep 3 to fishing spot not found")

    random_breaks(5, 8)
    print("\rto fishspot - step 3")
    while mini_map_image('alkarid_fishspot_step_1.png', 15, 10,  0.7, 'left',30, 5) == False:
        mini_map_image('alkarid_fishspot_step_1.png',  15, 10,  0.7, 'left', 30, 5)
        print("\rstep 4 to fishing spot  not found")

    random_breaks(10, 12)
    print("\rto fishspot - step 4")
    pick_random_fishing_spot('prawn_fish')
    random_breaks(3, 5)
    print("\rto fishspot - step 5")
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

def combine_items(item, Pause=False):
    functions.Image_Rec_single_closest("images/vial_water.png") # water
    c = random.uniform(0.1,0.9)
    time.sleep(c)
    Image_Rec_single_random("images/" + item + "_icon.png") # item
    c = random.uniform(0.1, 1)
    time.sleep(c)
    pyautogui.press('space')
    c = random.uniform(1, 2)
    time.sleep(c)
    while functions.make_enabled("make_herb.png") == 1:
        pyautogui.press('space')
        e = random.uniform(0.1, 0.9)
        time.sleep(e)
    if Pause:
        c = random.uniform(0, 10)
        time.sleep(c)
def make_raw_pies(volume=1000):
    make_item(volume, 'pie_shell.png', 'raw_bear.png', 184, 340, 280, 340, 'space', i=30)
    make_item(volume, 'bear_pie.png', 'raw_chompy.png', 375, 340, 320, 340, 'space', i=30)
    make_item(volume, 'chompy_pie.png', 'raw_rabbit.png', 230, 340, 470, 340, 'space', i=30)
def cooking_guild(volume=100, item='shark.png', x=375, y=305):
    j = round(volume / 28)
    while j > 0:
        invent = functions.invent_enabled()
        #print(invent)
        if invent == 0:
            pyautogui.press('esc')
        time.sleep(0.1)
        if functions.invent_count(item, 0.99) == 0:
            find_Object(1, left=0, top=0, right=1890 - 1280, bottom=800)  # green
            time_start = time.time()
            while functions.make_enabled('bank_deposit.png') == 0:
                time_end = time.time() - time_start
                time.sleep(0.1)
                if time_end > 15:
                    break
            if time_end < 15:
                c = random.uniform(0.1,1.5)
                time.sleep(c)
                functions.deposit_all_Bank()
                pick_item(x, y)
                functions.exit_bank()

        find_Object(0, left=0, top=0, right=1890 - 1280, bottom=800)  # green
        time_start_2 = time.time()
        while functions.make_enabled('make_how.png') == 0:
            time_end_2 = time.time() - time_start_2
            time.sleep(0.1)
            if time_end_2 > 15:
                break
        if time_end_2 < 15:
            c = random.uniform(0.1,1)
            time.sleep(c)
            pyautogui.press('space')
            while functions.invent_count(item, 0.99) > 0:
                inv = functions.invent_count(item, 0.99)
                print('\r' + item + " : " + str(inv), end='')
                time.sleep(0.1)
            c = random.uniform(0.1, 3)
            time.sleep(c)
            j -= 1
            print('\n' + str(j) + ' ' + item + ' runs left to cook')

def count_cook_rod():
    salmon_1 = functions.invent_count('salmon_fish.png', 0.99)
    trout_1 = functions.invent_count('trout_fish.png', 0.99)
    salmon_2 = functions.invent_count('salmon_cooked.png', 0.99)
    trout_2 = functions.invent_count('trout_cooked.png', 0.99)
    if salmon_1 is None:
        salmon_1 = 0
    if salmon_2 is None:
        salomn_2 = 0
    if trout_1 is None:
        trout_1 = 0
    if trout_2 is None:
        trout_2 = 0
    all_prawns = (int(salmon_1) + int(trout_1)) - (int(salmon_2) + int(trout_2))
    return all_prawns
def cook_all_fish_fire(Take_Human_Break=False):
    Image_Rec_single('salmon_fish.png','cook fish', 5, 5, 0.99, 'left', 8, False)
    random_breaks(0.1, 1)
    find_Object(1, left=0, top=0, right=1890-1280, bottom=800)  # green
    random_breaks(5, 8)
    pyautogui.press('space')
    random_breaks(0.1, 1)
    if functions.make_enabled('make_how.png') == 1:
        pyautogui.press('space')
    all_prawns = count_cook_rod()
    while all_prawns > 0:
        all_prawns = count_cook_rod()
        cooking_time = False
        time_start = time.time()
        while not cooking_time:
            all_prawns = count_cook_rod()
            if functions.make_enabled('make_how.png') == 1:
                pyautogui.press('space')
                cooking_time = True
            if skill_lvl_up() != 0:
                random_breaks(0.1, 0.25)
                find_Object(1, left=0, top=0, right=1890 - 1280, bottom=800)  # green
                random_breaks(0.6, 1.2)
                pyautogui.press('space')
                cooking_time = True
            if all_prawns <= 0:
                print('all fish cooked')
                cooking_time = True
                break
            print('cooking still: ', all_prawns)
            cooking_time = xp_gain_check('cooking_xp.png', 0.9)
            if not cooking_time:
                cooking_time = xp_gain_check('cooking_xp2.png', 0.9)
            print(cooking_time)
            time_end = time.time() - time_start
            print('seconds count: %.2f' % time_end)
            x = random.uniform(7, 10)
            if time_end > x:
                Image_Rec_single('salmon_fish.png','cook fish', 5, 5, 0.99, 'left', 8, False)
                random_breaks(0.1, 0.5)
                find_Object(1, left=0, top=0, right=1890 - 1280, bottom=800)  # green
                random_breaks(0.1, 0.5)
                if functions.make_enabled('make_how.png') == 1:
                    pyautogui.press('space')
                cooking_time = True
                break
        if Take_Human_Break:
            c = random.uniform(0.1, 50)
            time.sleep(c)


def cook_all_critters(Take_Human_Break=False):
    invent = functions.invent_enabled()
    #print(invent)
    if invent == 0:
        pyautogui.press('esc')
    random_breaks(0.1, 0.25)
    #find_Object(1)  # green
    random_breaks(0.6, 1.2)
    pyautogui.press('space')
    all_prawns = count_cook()
    while all_prawns > 0:
        all_prawns = count_cook()
        #print('cooking still: ', all_prawns)
        cooking_time = False
        time_start = time.time()
        while not cooking_time:
            all_prawns = count_cook()
            if skill_lvl_up() != 0:
                random_breaks(0.1, 0.25)
                find_Object(1, left=0, top=0, right=1890 - 1280, bottom=800)  # green
                random_breaks(0.6, 1.2)
                pyautogui.press('space')
                cooking_time = True
            if all_prawns <= 0:
                cooking_time = True
                break
            print('cooking still: ', all_prawns)
            cooking_time = xp_gain_check('cooking_xp.png', 0.8)
            if not cooking_time:
                cooking_time = xp_gain_check('cooking_xp2.png', 0.8)
            time_end = time.time() - time_start
            print('seconds count: %.2f' % time_end)
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

def count_cook():
    prawn_1 = functions.invent_count('prawn_fish.png')
    prawn_2 = functions.invent_count('prawn_cooked.png', 0.99)
    prawn_4 = functions.invent_count('anch_cooked.png', 0.99)
    prawn_3 = functions.invent_count('prawn_burnt.png', 0.99)
    if prawn_1 is None:
        prawn_1 = 0
    if prawn_2 is None:
        prawn_2 = 0
    if prawn_3 is None:
        prawn_3 = 0
    if prawn_4 is None:
        prawn_4 = 0
    all_prawns = int(prawn_1) - (int(prawn_2) + int(prawn_3) + int(prawn_4))
    return all_prawns

def barb_village_powercook_and_fish(Run_Duration_hours=6, invent_full=27):
    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    while time.time() < t_end:
        invent = functions.invent_enabled()
        #print(invent)
        if invent == 0:
            pyautogui.press('esc')
        invent = functions.invent_count('salmon_fish.png') + functions.invent_count(r'sea_puzzle.png')
        while invent < invent_full:
            invent = functions.invent_enabled()
            #print(invent)
            if invent == 0:
                pyautogui.press('esc')
            resizeImage()
            fishing_text = Image_to_Text('thresh', 'textshot.png')
            if fishing_text.strip().lower() != 'fishing' and fishing_text.strip().lower() != 'fishinq' and fishing_text.strip().lower() != 'ishing' and fishing_text.strip().lower() != 'pishing':
                random_breaks(0.2, 3)
                pick_random_fishing_spot('salmon_fish')
                random_breaks(5, 10)
            if skill_lvl_up() != 0:
                print("\rfish & clues: ", invent, 'leveled up!', end='')
                random_breaks(0.2, 3)
                pyautogui.press('space')
                random_breaks(0.1, 3)
                pyautogui.press('space')
                a = random.randrange(0, 2)
                # print(a)
                spaces(a)
            invent_crop()
            invent = functions.invent_count('salmon_fish.png') + functions.invent_count('sea_puzzle.png')
            print("\rfish & clues: ", invent, end='')
        cook_all_fish_fire()
        drop_fish()
def alkarid_powercook_and_fish(Take_Human_Break=False, Run_Duration_hours=6):
    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    while time.time() < t_end:
        invent = functions.invent_enabled()
        #print(invent)
        if invent == 0:
            pyautogui.press('esc')
        if functions.invent_count('prawn_fish.png') + functions.invent_count(r'sea_puzzle.png') > 27:
            to_alkarid_cookspot()
            cook_all_critters(Take_Human_Break)
            drop_prawns()
        else:
            to_alkarid_fishspot()
        invent = functions.invent_count('prawn_fish.png') + functions.invent_count(r'sea_puzzle.png')
        while invent < 27:
            invent = functions.invent_enabled()
            #print(invent)
            if invent == 0:
                pyautogui.press('esc')
            resizeImage()
            fishing_text = Image_to_Text('thresh', 'textshot.png')
            if fishing_text.strip().lower() != 'fishing' and fishing_text.strip().lower() != 'fishinq' and fishing_text.strip().lower() != 'ishing' and fishing_text.strip().lower() != 'pishing':
                random_breaks(0.2, 3)
                pick_random_fishing_spot('prawn_fish')
                random_breaks(5, 10)
            if skill_lvl_up() != 0:
                print("\rfish & clues: ", invent, 'leveled up!', end='')
                random_breaks(0.2, 3)
                pyautogui.press('space')
                random_breaks(0.1, 3)
                pyautogui.press('space')
                a = random.randrange(0, 2)
                # print(a)
                spaces(a)
            invent_crop()
            invent = functions.invent_count('prawn_fish.png') + functions.invent_count('sea_puzzle.png')
            print("\rfish & clues: ", invent, end='')
        to_alkarid_cookspot()
        cook_all_critters(Take_Human_Break)
        drop_prawns()


# while True:
#     print("\rfish & clues: ", count_cook(), end='')
if __name__ == "__main__":
    findWindow("RuneLite")
    x = random.randrange(100, 250)
    y = random.randrange(400, 500)
    pyautogui.click(x, y, button='right')
    #barb_village_powercook_and_fish(Run_Duration_hours=6, invent_full=26)
    #alkarid_powercook_and_fish(Take_Human_Break=False, Run_Duration_hours=5.4)
    #make_banking_food(13000, 'wine') # makes 1000 food at the bank
    #make_item(1852, 'grape.png', 'waterjug.png', 135, 125, 185, 125, 'space', i=30)
    cooking_guild(volume=9000, item='shark.png', x=470, y=305)
    print('making pies')
    #make_raw_pies(volume=1000)
    #make_item(773, 'pie_shell.png', 'raw_bear.png', 184, 340, 280, 340, 'space', i=30)
    #make_item(783, 'bear_pie.png', 'raw_chompy.png', 375, 340, 325, 340, 'space', i=30)
    #make_item(1012, 'chompy_pie.png', 'raw_rabbit.png', 230, 340, 470, 340, 'space', i=30)
    #os.system('shutdown -s -f')
