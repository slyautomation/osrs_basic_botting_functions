
import core
import cv2
import numpy as np

global hwnd
global iflag
global icoord

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


options = {0: random_inventory,
           1: random_combat,
           2: random_skills,
           3: random_quests,
           4: random_pause}


def Miner_Image():
    screen_Image(150, 150, 600, 750, 'miner_img.png')

def rim_minetobank():
    c = random.uniform(14, 15)
    x = 45
    y = 5
    while Image_Rec_single('rim_mine_spot1.png', 'rim mining spot', x, y, 0.7, 'left') != True:
        print('finding 1st step to bank')
    time.sleep(c)
    print('1st step to bank')

    c = random.uniform(9, 10)
    x = 10
    y = 1
    while Image_Rec_single('port_sarim_jewl.png', 'To Port Sarmin Jewlery', x, y, 0.7, 'left') != True:
        print('finding 2nd step to bank')
    time.sleep(c)
    print('2nd step to bank')

    c = random.uniform(9, 10)
    x = 52
    y = -25
    while Image_Rec_single('port_sarim_jewl.png', 'To Port Sarmin Jewlery', x, y, 0.7, 'left') != True:
        print("finding 3rd step to bank")

    time.sleep(c)
    print('3rd step to bank')

    c = random.uniform(11, 12)
    x = 75
    y = 25
    while Image_Rec_single('port_sarim_spot_water.png', 'To Port Sarmin Watery', x, y, 0.7, 'left') != True:
        print("finding 4th step to bank")
    time.sleep(c)
    print('4th step to bank')

    b = random.uniform(0.175, 0.677)
    x = random.randrange(750, 755)
    print('x: ', x)
    y = random.randrange(175, 180)
    print('y: ', y)
    c = random.uniform(10, 12)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('5th step to bank')
    b = random.uniform(0.175, 0.677)
    x = random.randrange(750, 755)  # 1755,1765
    print('x: ', x)
    y = random.randrange(140, 145)  # 175,185
    print('y: ', y)
    c = random.uniform(9, 10)
    pyautogui.click(x, y, 1, duration=b, button='left')
    print('last step to bank')
    time.sleep(c)
    c = random.uniform(2.1, 3)
    find_banker()
    time.sleep(c)
    depositbox()

def rim_minetoclay():

    b = random.uniform(0.175, 0.677)
    x = random.randrange(705, 710)  # 1755,1765
    print('x: ', x)
    y = random.randrange(55, 60)  # 175,185
    print('y: ', y)
    c = random.uniform(13, 14)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('first step to mine clay')

    c = random.uniform(11, 12)
    x = 0
    y = 40
    while Image_Rec_single('port_sarim_spot_water.png', 'To Port Sarmin Watery', x, y, 0.7, 'left') != True:
        print('finding 2nd clay mine step')
    time.sleep(c)
    print('2nd step to mine clay')

    c = random.uniform(9, 10)
    x = -15
    y = -10
    while Image_Rec_single('port_sarim_jewl.png', 'To Port Sarmin Jewlery', x, y, 0.7, 'left') != True:
        print('finding 3rd clay mine step')
    time.sleep(c)
    print('3rd step to mine clay')

    c = random.uniform(9, 10)
    x = -50
    y = 30
    while Image_Rec_single('port_sarim_jewl.png', 'To Port Sarmin Jewlery', x, y, 0.7, 'left') != True:
        print('finding 4th clay mine step')
    time.sleep(c)
    print('4th step to mine clay')

    c = random.uniform(14, 15)
    x = -8
    y = 33
    while Image_Rec_single('rim_mine_spot1.png', 'rim mining spot', x, y, 0.7, 'left') != True:
        print('finding 5th clay mine step')
    time.sleep(c)
    print('5th step to mine clay')

def find_banker():
    find_Object_precise(0, 5, 0, 0, 610, 775)  # red

def depositbox():
    c = random.uniform(3.5, 4.5)
    b = random.uniform(0.25, 0.65)
    x = random.randrange(370, 390)  # 950,960
    print('x: ', x)
    y = random.randrange(440, 460)  # 490,500
    print('y: ', y)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.19)
    pyautogui.click(duration=b)
    print('depositing clay')

def Image_Rec_single(image, event, iwidth, iheight, threshold, clicker, ispace=5):
    global icoord
    global iflag
    screen_Image(0, 0, 860, 820)
    img_rgb = cv2.imread('screenshot.png')
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
        x = random.randrange(iwidth, iwidth + ispace)
        y = random.randrange(iheight, iheight + ispace)
        icoord = pt[0] + x
        icoord = (icoord, pt[1] + y)
        b = random.uniform(0.2, 0.7)
        pyautogui.moveTo(icoord, duration=b)
        b = random.uniform(0.1, 0.3)
        pyautogui.click(icoord, duration=b, button=clicker)
    return iflag

def Miner_Image():
    screen_Image(150, 150, 600, 750, 'miner_img.png')
def findarea_single(ore, cropx, cropy):
    Miner_Image()
    image = cv2.imread(r"miner_img.png")

    # B, G, R
#--------------------- ADD OBJECTS -------------------
    tin = ([103, 86, 65], [145, 133, 128])
    copper = ([35, 70, 120], [65, 110, 170])
    coal = ([20, 30, 30], [30, 50, 50])
    iron = ([15, 20, 40], [25, 40, 70])
    iron2 = ([17, 20, 42], [25, 38, 70])
    clay = ([50, 105, 145], [60, 125, 165])
    red = ([0, 0, 180], [80, 80, 255])
    green = ([0, 180, 0], [80, 255, 80])
    amber = ([0, 160, 160], [80, 255, 255])
    # --------------------- ADD OBJECTS -------------------
    ore_list = [tin, copper, coal, iron, iron2, clay, red, green, amber]
    boundaries = [ore_list[ore]]
    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        ret, thresh = cv2.threshold(mask, 40, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        # find the biggest countour (c) by the area
        c = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(c)
        x = random.randrange(x + 5, x + max(w - 5, 6)) + cropx  # 950,960
        print('x: ', x)
        y = random.randrange(y + 5, y + max(h - 5, 6)) + cropy # 490,500
        print('y: ', y)
        b = random.uniform(0.1, 0.2)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.02, 0.07)
        pyautogui.click(duration=b)
def count_gems():
    return Image_count('gem_icon.png')
def count_geo():
    return Image_count('geo_icon.png')
def count_gems2():
    return Image_count('gem_icon2.png')
def inv_count(name):
    return Image_count(name + '_ore.png')

def moneymaker_clay():
    j = 0
    while j < 10:
        randomizer(timer_break, ibreak)
        r = random.uniform(0.1, 1)
        inventory = int(inv_count('clay')) + int(count_gems()) + int(count_gems2()) + int(count_geo())
        print('ore: ', int(inventory), "| gems: ", int(count_gems() + count_gems2()), "| clues: ", int(count_geo()))
        if inventory > 27:
            random_breaks(0.2, 0.7)
            rim_minetobank()
            rim_minetoclay()

        resizeImage()
        mined_text = Image_to_Text('thresh', 'textshot.png')
        if mined_text.lower() != 'mining':
            random_breaks(0.05, 0.1)
            print('not mining')
            find_Object_precise(2,20,0,0,650,650)


#rim_minetoclay()
#rim_minetobank()
#"""
resizeImage()
x = random.randrange(100, 250)
y = random.randrange(400, 500)
pyautogui.click(x, y, button='right')
ibreak = random.randrange(300, 2000)
print('will break in   ' + str(ibreak / 60) + ' minutes')
timer_break = timer()
moneymaker_clay()
#"""