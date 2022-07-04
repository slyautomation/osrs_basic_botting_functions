from threading import Thread

from PIL import ImageGrab

import core
import cv2
import numpy as np

global hwnd
global iflag
global icoord
import functions
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


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

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
    global actions
    b = random.uniform(20, 250)
    actions = 'pausing for ' + str(b) + ' seconds'
    time.sleep(b)
    newTime_break = True


options = {0: random_inventory,
           1: random_combat,
           2: random_skills,
           3: random_quests,
           4: random_pause}




def rim_minetobank():
    global actions
    c = random.uniform(14, 15)
    x = 45
    y = 5
    while Image_Rec_single('rim_mine_spot1.png', 'rim mining spot', x, y, 0.7, 'left') != True:
        actions = 'finding 1st step to bank'
    time.sleep(c)
    actions = '1st step to bank'

    c = random.uniform(9, 10)
    x = 10
    y = 1
    while Image_Rec_single('port_sarim_jewl.png', 'To Port Sarmin Jewlery', x, y, 0.7, 'left') != True:
        actions = 'finding 2nd step to bank'
    time.sleep(c)
    actions = '2nd step to bank'

    c = random.uniform(9, 10)
    x = 52
    y = -25
    while Image_Rec_single('port_sarim_jewl.png', 'To Port Sarmin Jewlery', x, y, 0.7, 'left') != True:
        actions = "finding 3rd step to bank"

    time.sleep(c)
    actions = '3rd step to bank'

    c = random.uniform(11, 12)
    x = 75
    y = 25
    while Image_Rec_single('port_sarim_spot_water.png', 'To Port Sarmin Watery', x, y, 0.7, 'left') != True:
        actions = "finding 4th step to bank"
    time.sleep(c)
    actions = '4th step to bank'

    b = random.uniform(0.175, 0.677)
    x = random.randrange(750, 755)
    #print('x: ', x)
    y = random.randrange(175, 180)
    #print('y: ', y)
    c = random.uniform(10, 12)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    actions = '5th step to bank'
    b = random.uniform(0.175, 0.677)
    x = random.randrange(750, 755)  # 1755,1765
    #print('x: ', x)
    y = random.randrange(140, 145)  # 175,185
    #print('y: ', y)
    c = random.uniform(9, 10)
    pyautogui.click(x, y, 1, duration=b, button='left')
    actions = 'last step to bank'
    time.sleep(c)
    c = random.uniform(2.1, 3)
    find_banker()
    actions = 'finding deposit box'
    time.sleep(c)
    depositbox()
    actions = 'finished deposit end of function'
    c = random.uniform(1, 5)
    time.sleep(c)
def rim_minetoclay():
    global actions
    actions = 'start of function'
    b = random.uniform(0.175, 0.677)
    x = random.randrange(710, 725)
    #print('x: ', x)
    y = random.randrange(50, 60)
    #print('y: ', y)
    c = random.uniform(10, 12)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    actions = '1st step to mining clay'
    c = random.uniform(11, 12)
    x = -5
    y = -10
    while Image_Rec_single('clay_deposit_spot2.png', 'To Port Sarmin Watery', x, y, 0.9, 'left') != True:
        Image_Rec_single('clay_deposit_spot1.png', 'To Port Sarmin Watery', x, y, 0.9, 'left')
        Image_Rec_single('clay_deposit_spot3.png', 'To Port Sarmin Watery', x, y, 0.9, 'left')
        actions = 'finding 2nd clay mine step'
    time.sleep(c)
    actions = '2nd step to mine clay'

    c = random.uniform(11, 12)
    x = 0
    y = 40
    while Image_Rec_single('port_sarim_spot_water.png', 'To Port Sarmin Watery', x, y, 0.7, 'left') != True:
        actions = 'finding 2nd clay mine step'
    time.sleep(c)
    actions = '2nd step to mine clay'

    c = random.uniform(9, 10)
    x = -15
    y = -10
    while Image_Rec_single('port_sarim_jewl.png', 'To Port Sarmin Jewlery', x, y, 0.7, 'left') != True:
        actions = 'finding 3rd clay mine step'
    time.sleep(c)
    actions = '3rd step to mine clay'

    c = random.uniform(9, 10)
    x = -50
    y = 30
    while Image_Rec_single('port_sarim_jewl.png', 'To Port Sarmin Jewlery', x, y, 0.7, 'left') != True:
        actions = 'finding 4th clay mine step'
    time.sleep(c)
    actions = '4th step to mine clay'

    c = random.uniform(14, 15)
    x = -8
    y = 33
    while Image_Rec_single('rim_mine_spot1.png', 'rim mining spot', x, y, 0.7, 'left') != True:
        actions = 'finding 5th clay mine step'
    time.sleep(c)
    actions = '5th step to mine clay'

def find_banker():
    find_Object_precise(0, 5, 0, 0, 610, 775)  # red

def depositbox():
    global actions
    c = random.uniform(3.5, 4.5)
    b = random.uniform(0.25, 0.65)
    x = random.randrange(370, 390)  # 950,960
    #print('x: ', x)
    y = random.randrange(440, 460)  # 490,500
    #print('y: ', y)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.19)
    pyautogui.click(duration=b)
    actions = 'depositing clay'

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

def Miner_Image_quick():
    left = 150
    top = 150
    right = 600
    bottom = 750

    im = ImageGrab.grab(bbox=(left, top, right, bottom))
    im.save('miner_img.png', 'png')


def findarea_single(ore, cropx=150, cropy=150):
    Miner_Image_quick()
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
        #print('x: ', x)
        y = random.randrange(y + 5, y + max(h - 5, 6)) + cropy # 490,500
        #print('y: ', y)
        b = random.uniform(0.1, 0.2)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.02, 0.07)
        pyautogui.click(duration=b)
        return (x, y)
    return(0,0)
def count_gems():
    return Image_count('gem_icon.png')
def count_geo():
    return Image_count('geo_icon.png')
def count_gems2():
    return Image_count('gem_icon2.png')
def inv_count(name):
    return Image_count(name + '_ore.png')

def timer_countdown():
    global Run_Duration_hours
    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    #print(t_end)
    final = round((60 * 60 * Run_Duration_hours) / 1)
    #print(final)
    for i in range(final):
        # the exact output you're looking for:
        print(bcolors.OK + f'\r[%-10s] %d%%' % ('='*round((i/final)*10), round((i/final)*100)), f'time left: {(t_end - time.time())/60 :.2f} mins | coords: {spot} | status: {mined_text} | ore: {ore_count} | gems: {gem_count} | clues: {clue_count} | {actions}', end='')
        time.sleep(1)

def moneymaker_clay(Take_Human_Break=False, Run_Duration_hours=4, color=6):
    global spot, mined_text, time_left, powerlist, actions, powerlist, t_end, gem_count, ore_count, clue_count
    print("Will break in: %.2f" % (ibreak / 60) + " minutes |", "Mine Ore Selected: Clay")
    t1 = Thread(target=timer_countdown)
    t1.start()

    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    while time.time() < t_end:
        randomizer(timer_break, ibreak)
        r = random.uniform(0.1, 1)
        gem_count = int(count_gems() + count_gems2())
        ore_count = int(inv_count('clay'))
        clue_count = int(count_geo())
        inventory = gem_count + ore_count + clue_count
        if inventory > 27:
            random_breaks(0.2, 0.7)
            actions = 'Going to Bank'
            rim_minetobank()
            actions = 'Going to Mining Spot'
            rim_minetoclay()

        resizeImage()
        mined_text = Image_to_Text('thresh', 'textshot.png')
        if mined_text.lower() != 'mining' and mined_text.lower() != 'mininq':
            actions = 'Not mining'
            spot = findarea_single(color)
            if Take_Human_Break:
                c = random.triangular(0.05, 30, 0.5)
                time.sleep(c)


x = random.randrange(100, 250)
y = random.randrange(400, 500)
pyautogui.click(x, y, button='right')
ibreak = random.randrange(300, 2000)
print('will break in   ' + str(ibreak / 60) + ' minutes')
timer_break = timer()
spot = (0, 0)
actions = 'None'
mined_text = 'Not Mining'
# ----- OBJECT MARKER COLOR ------
red = 6
green = 7
amber = 8

# --------- CHANGE TO RUN FOR AMOUNT OF HOURS ----------------
Run_Duration_hours = 4

moneymaker_clay(True, Run_Duration_hours, red)

