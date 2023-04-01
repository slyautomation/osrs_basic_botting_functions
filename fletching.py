import os

import numpy as np
import cv2
import pyautogui
import random
import time

global hwnd
global iflag
global icoord

iflag = False
icoord = []

import functions
from functions import bank_ready, exit_bank, find_Object, pick_item, deposit_secondItem
def wood_inv(wood):
    counter = 0
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"screen.png")
    img_rgb = cv2.imread('screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(str(wood), 0)
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

def Image_Single_clicker(image, event, threshold, clicker):
    global icoord
    global iflag

    myScreenshot = pyautogui.screenshot()
    #print('getting screenshot')
    myScreenshot.save(r"screen.png")
    img_rgb = cv2.imread('screen.png')
    #print('screenshot taken')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    pt = None
    #print('getting match requirements')
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    #print('determine loc and threshold')
    #if len(loc[0]) == 0:
        #exit()
    iflag = False
    event = event
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    #print('result of pt')
    if pt is None:
        iflag = False
        return None
        #print(event, 'Not Found...')
    else:
        iflag = True
        x = random.randrange(5, 20)
        y = random.randrange(5, 20)
        #cv2.imwrite('res.png', img_rgb)
        #print(event, 'Found...')
        icoord = pt[0] + x
        icoord = (icoord, pt[1] + y)
        b = random.uniform(0.01, 0.2)
        pyautogui.moveTo(icoord, duration=b)
        b = random.uniform(0.01, 0.13)
        pyautogui.click(icoord, duration=b, button=clicker)
    return icoord
def Image_Rec_clicker(image, event, threshold, clicker):
    global icoord
    global iflag

    myScreenshot = pyautogui.screenshot()
    #print('getting screenshot')
    myScreenshot.save(r"screen.png")
    img_rgb = cv2.imread('screen.png')
    #print('screenshot taken')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    pt = None
    #print('getting match requirements')
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    #print('determine loc and threshold')
    #if len(loc[0]) == 0:
        #exit()
    iflag = False
    event = event
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    #print('result of pt')
        if pt is None:
            iflag = False
        #print(event, 'Not Found...')
        else:
            iflag = True
            x = random.randrange(5, 30)
            y = random.randrange(5, 30)
            #cv2.imwrite('res.png', img_rgb)
            #print(event, 'Found...')
            icoord = pt[0] + x
            icoord = (icoord, pt[1] + y)
            b = random.uniform(0.1, 0.17)
            pyautogui.moveTo(icoord,duration=b)
            b = random.uniform(0.01, 0.2)
            pyautogui.click(icoord, duration=b, button=clicker)
    return iflag
def Image_Rec_clicker2(image, event, iheight, iwidth, threshold, clicker):
    global icoord
    global iflag
    myScreenshot = pyautogui.screenshot()
    # print('getting screenshot')
    myScreenshot.save(r"screen.png")
    img_rgb = cv2.imread('screen.png')
    # print('screenshot taken')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    pt = None
    # print('getting match requirements')
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    # print('determine loc and threshold')
    # if len(loc[0]) == 0:
    # exit()
    iflag = False
    event = event
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    # print('result of pt')
    if pt is None:
        iflag = False
        # print(event, 'Not Found...')
    else:
        iflag = True
        # cv2.imwrite('res.png', img_rgb)
        # print(event, 'Found...')
        icoord = pt[0] + iheight
        icoord = (icoord, pt[1] + iwidth)
        b = random.uniform(0.1, 0.7)
        pyautogui.moveTo(icoord, duration=b)
        b = random.uniform(0.01, 0.3)
        pyautogui.click(icoord, duration=b, button=clicker)
    return iflag


def pick_string_bow_bank():
    c = random.uniform(0.1, 0.9)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(170, 195)
    print('x: ', x)
    y = random.randrange(150, 170)
    b = random.uniform(0.1, 1.2)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='right')
    time.sleep(c)
    w = random.randrange(0, 10) + x
    print('x: ', x)
    z = random.randrange(55, 60) + y
    print('y: ', y)
    pyautogui.moveTo(w, z, duration=b)
    b = random.uniform(0.01, 0.19)
    pyautogui.click(duration=b)
    c = random.uniform(0.1, 2.6)
    time.sleep(c)

    c = random.uniform(0.1, 0.9)
    d = random.uniform(0.05, 0.15)
    x = random.randrange(460, 490)
    print('x: ', x)
    y = random.randrange(120, 130)
    b = random.uniform(0.1, 1.2)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='right')
    time.sleep(c)
    w = random.randrange(0, 10) + x
    print('x: ', x)
    z = random.randrange(55, 60) + y
    print('y: ', y)
    pyautogui.moveTo(w, z, duration=b)
    b = random.uniform(0.01, 0.19)
    pyautogui.click(duration=b)
    c = random.uniform(0.1, 2.6)
    time.sleep(c)

def pick_flecting_wood_bank():
    c = random.uniform(0.1, 0.9)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(125, 145)
    print('x: ', x)
    y = random.randrange(120, 130)
    b = random.uniform(0.1, 1.2)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='right')
    time.sleep(c)
    w = random.randrange(0, 10) + x
    print('x: ', x)
    z = random.randrange(68, 72) + y
    print('y: ', y)
    pyautogui.moveTo(w, z, duration=b)
    b = random.uniform(0.01, 0.19)
    pyautogui.click(duration=b)
    c = random.uniform(0.1, 2.6)
    time.sleep(c)

def pick_roots_bank():
    c = random.uniform(0.1, 0.9)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(125, 145)
    print('x: ', x)
    y = random.randrange(120, 130)
    b = random.uniform(0.1, 1.2)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='right')
    time.sleep(c)
    w = random.randrange(0, 10) + x
    print('x: ', x)
    z = random.randrange(68, 72) + y
    print('y: ', y)
    pyautogui.moveTo(w, z, duration=b)
    b = random.uniform(0.1, 0.19)
    pyautogui.click(duration=b)
    c = random.uniform(0.1, 2.6)
    time.sleep(c)

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
        #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    #cv2.imwrite('res.png', img_rgb)
    return counter

def make_crossbow_lumb_climbstairs_down():
    c = random.uniform(6,8)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(730, 750)
    print('x: ', x)
    y = random.randrange(170, 180)
    print('y: ', y)
    b = random.uniform(0.1, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)
    c = random.uniform(0.1, 2)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(360, 390)
    print('x: ', x)
    y = random.randrange(425, 445)
    print('y: ', y)
    b = random.uniform(0.1, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)
def make_crossbow_lumb_climbstairs_up():
    c = random.uniform(8, 10)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(200, 240)
    print('x: ', x)
    y = random.randrange(620, 650)
    print('y: ', y)
    b = random.uniform(0.1, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)
    pyautogui.press('1')

def make_crossbow_crafting_lumb():
    c = random.uniform(8, 10)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(490, 540)
    print('x: ', x)
    y = random.randrange(70, 115)
    print('y: ', y)
    b = random.uniform(0.1, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)
    pyautogui.press('1')

def make_crossbow_string_bank_lumb():
    c = random.uniform(8, 10)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(490, 540)
    print('x: ', x)
    y = random.randrange(70, 115)
    print('y: ', y)
    b = random.uniform(0.1, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)
    pyautogui.press('1')

def fletch_darts():
    c = random.uniform(0.01, 0.1)
    b = random.uniform(0.01, 0.05)
    x = random.randrange(645, 665)  # 950,960
    y = random.randrange(495, 515)  # 490,500
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.01, 0.06)
    pyautogui.click(duration=b)
    time.sleep(c)

    c = random.uniform(0.01, 0.10)
    b = random.uniform(0.01, 0.05)
    x = random.randrange(685, 705)  # 950,960
    y = random.randrange(495, 515)  # 490,500
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.01, 0.05)
    pyautogui.click(duration=b)
    time.sleep(c)

def fletch_bolts():
    c = random.uniform(0.01, 0.13)
    b = random.uniform(0.01, 0.091)
    x = random.randrange(645, 665)  # 950,960
    y = random.randrange(495, 515)  # 490,500
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.01, 0.06)
    pyautogui.click(duration=b)
    time.sleep(c)

    c = random.uniform(0.1, 1.2)
    b = random.uniform(0.01, 0.12)
    x = random.randrange(695, 715)  # 950,960
    y = random.randrange(495, 515)  # 490,500
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.01, 0.09)
    pyautogui.click(duration=b)
    time.sleep(c)
    pyautogui.press('space')
    c = random.uniform(12.5, 14.5)
    time.sleep(c)

def string_bow(bow):
    c = random.uniform(0.1, 1.5)
    b = random.uniform(0.1, 0.44)
    x = random.randrange(690, 715)  # 950,960
    y = random.randrange(495, 515)  # 490,500
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.01, 0.09)
    pyautogui.click(duration=b)
    time.sleep(c)

    c = random.uniform(0.1, 1.5)
    b = random.uniform(0.01, 0.12)
    x = random.randrange(775, 795)  # 950,960
    y = random.randrange(570, 590)  # 490,500
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.01, 0.09)
    pyautogui.click(duration=b)
    time.sleep(c)
    pyautogui.press(bow)
    #c = random.uniform(6, 14.5)
    #time.sleep(c)


def string_bows(name, x, y, x2, y2):
    c = random.uniform(0.1, 6)
    e = random.uniform(0.1, 0.9)
    error_c = 0
    while bank_ready(False) == False:
        if error_c > 3:
            exit()
        find_Object(1)
        c = random.uniform(1, 3)
        time.sleep(c)
        functions.deposit_all_Bank()
        error_c += 1
    pick_item(x, y)
    pick_item(x2, y2)
    exit_bank()
    invent = functions.invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    time_start = time.time()
    time_end = 0
    x = random.uniform(40, 45)
    while wood_inv('images/stringbow_icon.png') > 0 or time_end < x:
        Image_Rec_single_closest('images/stringbow_icon.png', 0.7, 'left')
        e = random.uniform(0.1, 0.9)
        time.sleep(e)
        Image_Rec_single_closest(name, 0.95, 'left')
        e = random.uniform(0.1, 0.9)
        time.sleep(e)
        pyautogui.press('space')
        while skill_lvl_up() == 0:
            time_end = time.time() - time_start
            e = random.uniform(0.1, 0.4)
            time.sleep(e)
            while functions.make_enabled('make_string.png') == 1:
                pyautogui.press('space')
                e = random.uniform(0.1, 0.9)
                time.sleep(e)
            print('skills are: ', skill_lvl_up())
            print('wood left: ', wood_inv('images/stringbow_icon.png'))
            print('keep making money!!!')
            if wood_inv('images/stringbow_icon.png') == 0:
                break
        if wood_inv('images/stringbow_icon.png') == 0:
            break
            if skill_lvl_up() == 1:
                Image_Rec_single_closest('images/stringbow_icon.png', 0.7, 'left')
                e = random.uniform(0.1, 0.9)
                time.sleep(e)
                Image_Rec_single_closest(name, 0.7, 'left')
                e = random.uniform(0.1, 0.9)
                time.sleep(e)
                pyautogui.press('space')
    time.sleep(c)

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
    #cv2.imwrite('res.png', img_rgb)
    pick_random_item = random.randrange(0, len(close_points))
    #print(close_points)
    #print("list: ", str(len(close_points)))
    #min_value = min(close_list)
    #min_index = close_list.index(min_value)
    #coords = close_points[min_index]
    coords = close_points[pick_random_item]
    print(coords)
    #print('min_value:', min_value, '| min_index:', min_index)
    x = random.randrange(5, 20) + 620
    y = random.randrange(5, 20) + 480
    icoord = coords[0] + x
    icoord = (icoord, coords[1] + y)
    b = random.uniform(0.1, 0.7)
    pyautogui.moveTo(icoord, duration=b)
    b = random.uniform(0.01, 0.3)
    pyautogui.click(icoord, duration=b, button=clicker)
    return close_points

def fletch_bows(name, x_i, y_i, number, i=55):
    error_c = 0
    while bank_ready() == False:
        if error_c > 3:
            exit()
        find_Object(1)
        c = random.uniform(1, 3)
        time.sleep(c)
        error_c += 1
    pick_item(x_i, y_i)
    exit_bank()
    invent = functions.invent_enabled()
    print(invent)
    if invent == 0:
        pyautogui.press('esc')
    time_start = time.time()
    time_end = 0
    x = random.uniform(i, i+5)
    while wood_inv(name) > 0 and time_end < x:
        invent = functions.invent_enabled()
        print(invent)
        if invent == 0:
            pyautogui.press('esc')
        e = random.uniform(0.1, 0.4)
        time.sleep(e)
        if Image_Single_clicker('images/knife.png', 'fletching bows', 0.7, 'left') is None:
            Image_Single_clicker('images/chisel.png', 'fletching bows', 0.7, 'left')
        e = random.uniform(0.1, 0.9)
        time.sleep(e)
        Image_Rec_single_closest(name, 0.7, 'left')
        e = random.uniform(0.1, 1.1)
        time.sleep(e)
        pyautogui.press(number)
        while skill_lvl_up() == 0 and time_end < x:
            time_end = time.time() - time_start
            print('time delay:', time_end)
            print('wood left: ', wood_inv(name))
            while functions.make_enabled() == 1:
                pyautogui.press(number)
                e = random.uniform(0.1, 0.9)
                time.sleep(e)
            if wood_inv(name) == 0:
                break
            if skill_lvl_up() == 1:
                if Image_Single_clicker('images/knife.png', 'fletching bows', 0.7, 'left') is None:
                    Image_Single_clicker('images/chisel.png', 'fletching bows', 0.7, 'left')
                e = random.uniform(0.1, 0.9)
                time.sleep(e)
                Image_Rec_single_closest(name, 0.7, 'left')
                e = random.uniform(0.1, 0.4)
                time.sleep(e)
                pyautogui.press(number)

    time.sleep(c)


j = round(6800/14)
while j > 0:
    # string_bows used to string bows variables for function is:
    # file path for the bows image, #images/magic_longbow.png #images/oak_longbow.png #images/maple_longbow.png
    # the x and y for the bow item in the bank inventory
    # the x and y for the bow string in the bank inventory
    string_bows('images/magic_longbow.png', 327, 336, 378, 269)
    
    # fletch_bows is used to fletch wood into shafts or bows. can also be used to cut gems into bolt tips.
    # fletch bows variables are: # file path for the gem or the wood type: #ruby_icon  #sapphire_icon #diamond_icon #wood_icon #oak_icon #maple_icon
    # the x and y for the item in the bank inventory
    # the number or space to press to make the type of bow, shafts or bolt tips.
    # use 80 for making bolt tips else use 55 due to the timing of fletching items
    
    #fletch_bows('images/ruby_icon.png', 330, 126, 'space', 80)
    print('actions left:', j)
    
    # fletch_bolts is used for adding feathers to shafts, bolt tips to bolts or arrow tips to shafts.
    #fletch_bolts()
    
    # fletch_darts are used to make unfinished dart tips with feathers or unfinished bolts with feathers
    #fletch_darts()
    j -= 1
#os.system('shutdown -s -f')
# use in idle pyautogui.displayMousePosition()
#import pyautogui


