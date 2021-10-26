import numpy as np
import cv2
import pyautogui
import random
import time
import os
from PIL import Image
import pytesseract
import functions
from functions import screen_Image
from functions import image_Rec_clicker
from functions import random_combat
from functions import random_quests
from functions import random_skills
from functions import random_inventory
# from core import findWindow_runelite
from functions import Image_Rec_single

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


def mini_map_image():
    screen_Image(1963 - 1280, 57, 2068 - 1280, 155, 'mini_map.png')


def Find_on_Map(image, event, threshold):
    global icoord
    global iflag
    img_rgb = cv2.imread(r'world.png')
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
    if pt is None:
        iflag = False
    else:
        iflag = True
        cv2.imwrite(r'res.png', img_rgb)

    return iflag


def Find_on_Region(image, event, threshold):
    global icoord
    global iflag
    img_rgb = cv2.imread(r'west_varrock_mines.png')
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
    if pt is None:
        iflag = False
    else:
        iflag = True
        cv2.imwrite(r'res_region.png', img_rgb)
        im = Image.open(r'res_region.png')
        im.show(title="result")
    print('left:', pt[0], 'right:', pt[0] + w, 'top:', pt[1], 'bottom:', pt[1] + h)
    print('center x:', ((pt[0] + w) + pt[0])/2, 'center y:', ((pt[1] + h) + pt[1])/2)
    return iflag


mini_map_image()
# print(Find_on_Map('mini_map.png', 'find on map', 0.6))
print(Find_on_Region('mini_map.png', 'find on map', 0.6))
