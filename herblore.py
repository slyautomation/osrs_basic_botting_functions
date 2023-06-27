import os
import subprocess
import win32gui
import numpy as np
import cv2
import pyautogui
import random
import time
import core
global hwnd
global iflag
global icoord
import functions
import yaml
from functions import find_Object, deposit_all_Bank, deposit_secondItem, \
    exit_bank, image_Rec_clicker, Image_Rec_single
iflag = False
icoord = []
pyautogui.FAILSAFE = False

def gfindWindow(data):  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, data)
    # hwnd = win32gui.GetForegroundWindow()860
    #print('findWindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)
    # win32gui.ShowWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)


with open("pybot-config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

try:
    gfindWindow(data[0]['Config']['client_title'])
except BaseException:
    print("Unable to find window:", data[0]['Config']['client_title'], "| Please see list of window names below:")
    core.printWindows()
    pass

try:
    x_win, y_win, w_win, h_win = core.getWindow(data[0]['Config']['client_title'])
except BaseException:
    print("Unable to find window:", data[0]['Config']['client_title'], "| Please see list of window names below:")
    core.printWindows()
    pass
    
def Image_Rec_single_closest(image, threshold=0.7, clicker='left'):
    functions.screen_Image(620, 480, 820, 750, 'closest.png')
    img_rgb = cv2.imread('images/closest.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
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


def vial_inv(vial):
    counter = 0
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"screen.png")
    img_rgb = cv2.imread('screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/' + str(vial) + '_icon.png', 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    #cv2.imwrite('res.png', img_rgb)
    return counter
# cv2.waitKey(0)

def skill_lvl_up():
    counter = 0
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"screen.png")
    img_rgb = cv2.imread('screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/Congrats_flag.png', 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    cv2.imwrite('res.png', img_rgb)
    return counter
def cleaning_weeds(weed):
    x = random.randrange(5, 40)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(5, 40)  # y = random.randrange(50, 60)
    print('y: ', y)
    image_Rec_clicker(str(weed) + '_grime.png','cleaning weed', threshold=0.8, fast=True, playarea=False)

def combine_items(item, Pause=False):
    Image_Rec_single_closest("images/vial_water.png") # water
    c = random.uniform(0.1,0.9)
    time.sleep(c)
    Image_Rec_single_closest("images/" + item + "_icon.png") # item
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

def single_pick_potion_item(v,u):
    c = random.uniform(0.1, 0.7)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(v-10, v+10)
    print('x: ', x)
    y = random.randrange(u-5, u+5)
    b = random.uniform(0.1, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)

def pick_potion_item(v,u):
    c = random.uniform(0.1, 0.7)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(v-10, v+10)
    print('x: ', x)
    y = random.randrange(u-5, u+5)
    b = random.uniform(0.1, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='right')
    time.sleep(c)
    w = random.randrange(0, 10) + x
    print('x: ', x)
    z = random.randrange(65, 70) + y #52, 62
    print('y: ', y)
    pyautogui.moveTo(w, z, duration=b)
    b = random.uniform(0.1, 0.19)
    pyautogui.click(duration=b)
    c = random.uniform(0.1, 0.5)
    time.sleep(c)

# def grind_horns(item):
#     c = random.uniform(0.1, 0.8)
#     find_Object(1)
#     time.sleep(c)
#     c = random.uniform(0.1, 0.6)
#     deposit_secondItem()
#     time.sleep(c)
#     pick_potion_item(470, 485)
#     c = random.uniform(0.1, 0.25)
#     exit_bank()
#     time.sleep(c)
#     combine_items()
#     while vial_inv(item) > 0:  # harra #guam #toad
#         while skill_lvl_up() == 0:
#             print('skills are: ', skill_lvl_up())
#             print('items left: ', vial_inv(item))  # guam #harra
#             print('keep making money!!!')
#             if vial_inv(item) == 0:  # guam #harra
#                 break
#         if vial_inv(item) == 0:  # guam #harra
#             break
#         if skill_lvl_up() == 1:
#             break
#     time.sleep(c)
def cast_superglass(v,u):
    c = random.uniform(0.1, 0.3)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(v-5, v+5)
    #print('x: ', x)
    y = random.randrange(u-5, u+5)
    b = random.uniform(0.1, 0.4)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)
def pick_seaweed(v,u):
    c = random.uniform(0.01, 0.2)
    d = random.uniform(0.01, 0.05)
    x = random.randrange(v-8, v+8)
    #print('x: ', x)
    y = random.randrange(u-5, u+5)
    b = random.uniform(0.1, 0.3)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)
    c = random.uniform(0.01, 0.2)
    d = random.uniform(0.01, 0.05)
    x = random.randrange(v - 9, v + 9)
    #print('x: ', x)
    y = random.randrange(u - 5, u + 5)
    b = random.uniform(0.02, 0.2)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)
    c = random.uniform(0.05, 0.2)
    d = random.uniform(0.01, 0.05)
    x = random.randrange(v - 9, v + 9)
    #print('x: ', x)
    y = random.randrange(u - 5, u + 5)
    b = random.uniform(0.05, 0.2)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)
def pick_bucket_sand(v,u):
    c = random.uniform(0.1, 0.4)
    d = random.uniform(0.05, 0.2)
    x = random.randrange(v-10, v+10)
    #print('x: ', x)
    y = random.randrange(u-5, u+5)
    b = random.uniform(0.1, 0.4)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='right')
    time.sleep(c)
    w = random.randrange(0, 10) + x
    #print('x: ', x)
    z = random.randrange(70, 75) + y #52, 62
    #print('y: ', y)
    pyautogui.moveTo(w, z, duration=b)
    b = random.uniform(0.05, 0.2)
    pyautogui.click(duration=b)
    c = random.uniform(0.1, 0.2)
    time.sleep(c)


def pick_all_item(v,u):
    c = random.uniform(0.1, 0.8)
    d = random.uniform(0.05, 0.15)
    x = random.randrange(v-10, v+10)
    print('x: ', x)
    y = random.randrange(u-5, u+5)
    b = random.uniform(0.1, 0.85)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)

def pick_grimy_item(v,u):
    c = random.uniform(0.1, 0.8)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(v-10, v+10)
    print('x: ', x)
    y = random.randrange(u-5, u+5)
    b = random.uniform(0.1, 0.85)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='right')
    time.sleep(c)
    w = random.randrange(0, 10) + x
    print('x: ', x)
    z = random.randrange(100, 105) + y #100, 105 #110,115
    print('y: ', y)
    pyautogui.moveTo(w, z, duration=b)
    b = random.uniform(0.1, 0.19)
    pyautogui.click(duration=b)
    c = random.uniform(1.7, 2.6)
    time.sleep(c)

def takepotion():
    Image_Rec_single('prayer4_potion.png', 'taking potion', 0.95, 'left')
    j = 0
    while j < 10:
        print('ass potion')
        d = random.uniform(63, 64)
        time.sleep(d)
        potion = Image_Rec_single('prayer4_potion.png', 'taking potion', 0.95, 'left')
        if potion is False:
            potion = Image_Rec_single('prayer2_potion.png', 'taking potion', 0.95, 'left')
            if potion is False:
                potion = Image_Rec_single('prayer1_potion.png', 'taking potion', 0.95, 'left')
def superglass_money():
    a = random.uniform(0.1, 0.35)
    find_Object(1)
    deposit_secondItem()
    pick_bucket_sand(472,269)
    pick_seaweed(423, 269)
    time.sleep(a)
    a = random.uniform(0.1, 0.3)
    exit_bank()
    time.sleep(a)
    cast_superglass(642,607)
    a = random.uniform(3, 4)
    time.sleep(a)
    print("ready")

def clean_weeds(x,y,name):
    c = random.uniform(0.1, 0.8)
    error_c = 0
    while functions.bank_ready(False) == False:
        if error_c > 3:
            exit()
        find_Object(1)
        c = random.uniform(1, 3)
        time.sleep(c)
        error_c += 1
    c = random.uniform(0.1, 0.6)
    deposit_all_Bank()
    time.sleep(c)
    pick_all_item(x, y) #harra 227, 265 #guam 185, 265 #ranarr 185 485 #irit 425, 485 kwuarm 185, 520 avan 275, 520, cada 280,520 lant 425,520
    c = random.uniform(0.1, 0.25)
    exit_bank()
    time.sleep(c)
    c = random.uniform(0.1, 1)
    invent = functions.invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    cleaning_weeds(name) #guam #harra #ranarr #irit #kwuarm #avan #cada #lant
    time.sleep(c)



def make_potion(item, vialx, vialy, herbx, herby):
    c = random.uniform(0.1, 0.6)
    error_c = 0
    while functions.bank_ready(False) == False:
        if error_c > 3:
            exit()
        find_Object(1)
        c = random.uniform(1, 3)
        time.sleep(c)
        error_c += 1
    deposit_all_Bank()
    time.sleep(c)
    single_pick_potion_item(vialx, vialy) # water
    c = random.uniform(0.1, 0.25)
    single_pick_potion_item(herbx, herby) # herb item
    c = random.uniform(0.1, 0.25)
    exit_bank()
    time.sleep(c)
    combine_items(item)
    time_start = time.time()
    time_end = 0
    i = 9
    x = random.uniform(i, i+5)
    while vial_inv(item) > 0 and time_end < x: #harra #guam #toad
        while skill_lvl_up() == 0:
            time_end = time.time() - time_start
            print('skills are: ', skill_lvl_up())
            print('items left: ', vial_inv(item)) #guam #harra
            print('keep making money!!!')
            if vial_inv(item) == 0: #guam #harra
                break
        if vial_inv(item) == 0: #guam #harra
            break
        if skill_lvl_up() == 1:
            break
    time.sleep(c)

def superglassmaking(i):
    j = round(i)
    while j > 0:
        superglass_money()
        j -= 1
        print('superglass left: ', j)

def weedcleaning(i, x, y, name):
    j = round(i/28) + 1
    while j > 0:
        clean_weeds(x, y, name)
        #clean_weeds(280,161,'irit') #guam #harra #ranarr #irit #kwuarm #avan #cada #lant #cad #mar
        # harra 280, 410 #guam 280, 378 #toad 470, 450 #ranarr 230, 485 irit 330, 485 kwuarm 235, 520 avan 130, 520 cada 375,520 lant 470, 485
        j -= 1


def potionmaking(i):
    j = round(i/14)
    while j > 0:
            # used to make unfinished potions, 'item' is the herb name
            # vailx and vialy is the bank inventory of the vials of water
            # herbx and herby is the bank inventory for the herb
            make_potion('guam', 232, 307, 183, 341) # item, vialx, vialy, herbx, herby
            j -= 1

if __name__ == "__main__":
    #superglassmaking(50)
    # weedcleaning is used to clean herbs, the function values order is:
    # number of grimy herbs to clean.
    # the x and y of the grimy herb in the bank inventory.
    # name of the 'herb'. #guam #harra #ranarr #irit #kwuarm #avan #cada #lant #cad #marre #tar
    weedcleaning(100, 185, 305, 'guam')
    
    # potionmaking is used to make unfinished potions refer to the potionmaking function to make changes.
    # The variable it takes is the number of unfinished potions to make.
    potionmaking(100)
    #os.system('shutdown -s -f')
