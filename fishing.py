from threading import Thread
import win32gui
import numpy as np
import cv2
import pyautogui
import random
import time
import os
import functions
import pytesseract
from PIL import Image
from functions import Image_count
from functions import image_Rec_clicker
from functions import screen_Image
from functions import release_drop_item
from functions import drop_item
from functions import Image_to_Text
from functions import random_breaks
from functions import invent_crop
from functions import Image_Rec_single
from functions import resizeImage
from functions import skill_lvl_up
from functions import spaces
from functions import random_combat
from functions import random_quests
from functions import random_skills
from functions import random_inventory
from functions import random_breaks

# from core import findWindow_runelite

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


def random_pause():
    b = random.uniform(20, 250)
    print('pausing for ' + str(b) + ' seconds')
    time.sleep(b)
    newTime_break = True


iflag = False

options = {0: random_inventory,
           1: random_combat,
           2: random_skills,
           3: random_quests,
           4: random_pause}


def drop_fish():
    global actions
    actions = "dropping fish"
    invent_crop()
    drop_item()
    image_Rec_clicker(r'prawn_fish.png', 'dropping item', 5, 5, 0.9, 'left', 10, False, False)
    image_Rec_clicker(r'trout_fish.png', 'dropping item', 5, 5, 0.9, 'left', 10, False, False)
    image_Rec_clicker(r'salmon_fish.png', 'dropping item', 5, 5, 0.9, 'left', 10, False, False)
    image_Rec_clicker(r'lobster_fish.png', 'dropping item', 5, 5, 0.9, 'left', 10, False, False)
    release_drop_item()
    actions = "all fish dropped"


def find_fish(showCoords=False, left=0, top=0, right=800, bottom=800, boundaries=[([110, 100, 0], [195, 180, 60])]):
    functions.screen_Image(left, top, right, bottom)
    image = cv2.imread('images/screenshot.png')
    image = cv2.rectangle(image, pt1=(600, 0), pt2=(850, 200), color=(0, 0, 0), thickness=-1)
    image = cv2.rectangle(image, pt1=(0, 0), pt2=(150, 100), color=(0, 0, 0), thickness=-1)
    #cv2.imwrite('images/screenshot3.png', image)
    # define the list of boundaries
    # B, G, R

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
        #print(len(contours))
        # find the biggest countour (c) by the area
        c = max(contours, key=cv2.contourArea)
        #print(contours)
        x, y, w, h = cv2.boundingRect(c)
        #image = cv2.rectangle(image, pt1=(x, y), pt2=(x+w, y+h), color=(0, 0, 255), thickness=2)
        if showCoords:
            print(x, y, w, h)
        x = random.randrange(x + 5, x + max(w - 5, 6)) + left  # 950,960
        #print('x: ', x)
        y = random.randrange(y + 5, y + max(h - 5, 6)) + top  # 490,500
        #print('y: ', y)
        b = random.uniform(0.2, 0.4)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b)
        # show the images
        #cv2.imshow("Result", np.hstack([image, output]))
        #cv2.waitKey(0)
        return (x, y)
    else:
        return False
def pick_random_fishing_spot(showCoords=False):
    fish = find_fish()
    return fish

def timer_countdown():
    global Run_Duration_hours
    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    #print(t_end)
    final = round((60 * 60 * Run_Duration_hours) / 1)
    #print(final)
    for i in range(final):
        # the exact output you're looking for:
        print(bcolors.OK + f'\r[%-10s] %d%%' % ('='*round((i/final)*10), round((i/final)*100)), f'time left: {(t_end - time.time())/60 :.2f} mins | coords: {coords} | status: {fishing_text} | fish: {fish_count} | clues: {clue_count} | {actions}', end='')
        time.sleep(1)

def powerfisher(fish_type, Run_Duration_hours=6):
    global ibreak, coords, fishing_text, time_left, powerlist, actions, t_end, fish_count, clue_count, invent_count
    t_end = time.time() + (60 * 60 * Run_Duration_hours)

    print('Will break in: %.2f' % (ibreak / 60) + ' minutes |', "Fish Type Selected:", fish_type)
    t1 = Thread(target=timer_countdown)
    t1.start()

    while time.time() < t_end:
        randomizer(timer_break, ibreak)
        resizeImage()
        fishing_text = Image_to_Text('thresh', 'textshot.png')
        # print(fished)
        if fishing_text.strip().lower() != 'fishing' and fishing_text.strip().lower() != 'fishinq' and fishing_text.strip().lower() != 'ishing' and fishing_text.strip().lower() != 'pishing':
            random_breaks(0.2, 3)
            pick_random_fishing_spot(fish_type)
            random_breaks(5, 10)
        if skill_lvl_up() != 0:
            actions = 'level up'
            random_breaks(0.2, 3)
            pyautogui.press('space')
            random_breaks(0.1, 3)
            pyautogui.press('space')
            a = random.randrange(0, 2)
            # print(a)
            spaces(a)
        actions = 'none'
        invent_crop()
        fish_count = functions.invent_count(fish_type + '.png')
        if fish_type == 'prawn_fish':
            fish_count = functions.invent_count(fish_type + '.png', 0.95) + functions.invent_count('anch_fish.png', 0.95)
        clue_count = Image_count(r'sea_puzzle.png')
        invent = fish_count + clue_count
        if fish_type == 'prawn_fish' or fish_type == 'lobster_fish':
            z = 27
        else:
            z = 26
        if invent > z - 2:
            invent = functions.invent_enabled()
            if invent == 0:
                actions = 'opening inventory'
                pyautogui.press('esc')
            random_breaks(0.2, 0.7)
            drop_fish()
            random_breaks(0.2, 0.7)
            pick_random_fishing_spot(fish_type)


coords = (0, 0)
actions = 'None'
fishing_text = 'Not Fishing'
time_left = 0

#-------------------------------

invent_count = 0
fish_type = 'prawn_fish'
fish_count = 0
clue_count = 0
#-------------------------------
findWindow("RuneLite")

if __name__ == "__main__":
    time.sleep(2)
    resizeImage()
    x = random.randrange(100, 250)
    y = random.randrange(400, 500)
    pyautogui.click(x, y, button='right')
    ibreak = random.randrange(300, 2000)
    timer_break = timer()
    # --------- CHANGE TO RUN FOR AMOUNT OF HOURS ----------------
    Run_Duration_hours = 5.1
    powerfisher(fish_type, Run_Duration_hours=Run_Duration_hours)
