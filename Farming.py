import os
import subprocess

import numpy as np
import cv2
import pyautogui
import random
import time

global hwnd
global iflag
global icoord
import functions
from functions import find_Object, deposit_all_Bank, deposit_secondItem, \
    exit_bank, image_Rec_clicker, Image_Rec_single
iflag = False
icoord = []




def vial_inv(vial):
    counter = 0
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"screen.png")
    img_rgb = cv2.imread('screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(str(vial) + '_icon.png', 0)
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
    template = cv2.imread('Congrats_flag.png', 0)
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

def combine_items():
    c = random.uniform(0.3,0.9)
    b = random.uniform(0.21, 0.44)
    x = random.randrange(692, 712)  # 950,960
    y = random.randrange(497, 512)  # 490,500
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.05, 0.09)
    pyautogui.click(duration=b)
    time.sleep(c)

    c = random.uniform(0.8, 1)
    b = random.uniform(0.062, 0.12)
    x = random.randrange(777, 792)  # 950,960
    y = random.randrange(612, 628)  # 570, 590 # 490,500
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.05, 0.09)
    pyautogui.click(duration=b)
    time.sleep(c)
    pyautogui.press('space')
    #c = random.uniform(6, 14.5)
    #time.sleep(c)

def single_pick_potion_item(v,u):
    c = random.uniform(0.3, 0.7)
    d = random.uniform(0.05, 0.15)
    x = random.randrange(v-10, v+10)
    print('x: ', x)
    y = random.randrange(u-5, u+5)
    b = random.uniform(0.3, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)

def pick_potion_item(v,u):
    c = random.uniform(0.3, 0.7)
    d = random.uniform(0.05, 0.15)
    x = random.randrange(v-10, v+10)
    print('x: ', x)
    y = random.randrange(u-5, u+5)
    b = random.uniform(0.3, 0.7)
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
    c = random.uniform(0.25, 0.5)
    time.sleep(c)

def grind_horns(item):
    c = random.uniform(0.3, 0.8)
    find_Object(1)
    time.sleep(c)
    c = random.uniform(0.2, 0.6)
    deposit_secondItem()
    time.sleep(c)
    pick_potion_item(470, 485)
    c = random.uniform(0.1, 0.25)
    exit_bank()
    time.sleep(c)
    combine_items()
    while vial_inv(item) > 0:  # harra #guam #toad
        while skill_lvl_up() == 0:
            print('skills are: ', skill_lvl_up())
            print('items left: ', vial_inv(item))  # guam #harra
            print('keep making money!!!')
            if vial_inv(item) == 0:  # guam #harra
                break
        if vial_inv(item) == 0:  # guam #harra
            break
        if skill_lvl_up() == 1:
            break
    time.sleep(c)
def cast_superglass(v,u):
    c = random.uniform(0.1, 0.3)
    d = random.uniform(0.05, 0.15)
    x = random.randrange(v-5, v+5)
    #print('x: ', x)
    y = random.randrange(u-5, u+5)
    b = random.uniform(0.1, 0.4)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)
def pick_seaweed(v,u):
    c = random.uniform(0.05, 0.2)
    d = random.uniform(0.01, 0.05)
    x = random.randrange(v-8, v+8)
    #print('x: ', x)
    y = random.randrange(u-5, u+5)
    b = random.uniform(0.1, 0.3)
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
    c = random.uniform(0.3, 0.8)
    d = random.uniform(0.05, 0.15)
    x = random.randrange(v-10, v+10)
    print('x: ', x)
    y = random.randrange(u-5, u+5)
    b = random.uniform(0.5, 0.85)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)

def pick_grimy_item(v,u):
    c = random.uniform(0.3, 0.8)
    d = random.uniform(0.05, 0.15)
    x = random.randrange(v-10, v+10)
    print('x: ', x)
    y = random.randrange(u-5, u+5)
    b = random.uniform(0.5, 0.85)
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
    a = random.uniform(0.2, 0.35)
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



def make_poition(item):
    c = random.uniform(0.3, 0.6)
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
    single_pick_potion_item(185, 124) # water
    c = random.uniform(0.1, 0.25)
    single_pick_potion_item(230, 124)
    c = random.uniform(0.1, 0.25)
    exit_bank()
    time.sleep(c)
    combine_items()
    while vial_inv(item) > 0: #harra #guam #toad
        while skill_lvl_up() == 0:
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
            make_poition('guam')
            #make_poition('irit', 426,444)
            #make_poition('irit', 328, 160)
            j -= 1

if __name__ == "__main__":
    #superglassmaking(50)
    potionmaking(6402)
    #weedcleaning(2986, 137, 124, 'harra')
    #os.system('shutdown -s -f')
