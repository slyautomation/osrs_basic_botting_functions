import numpy as np
import cv2
import pyautogui
import random
import time
import argparse
import os

global hwnd
global iflag
global icoord
import pytesseract
from PIL import Image
from functions import Image_to_Text
from functions import resizeImage
from functions import random_combat
from functions import random_quests
from functions import random_skills
from functions import random_inventory
from functions import image_Rec_clicker

# from core import findWindow_runelite


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
iflag = False

global newTime_break

newTime_break = False

global timer
global timer_break
global ibreak


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


def McropImage():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"screen.png")
    png = r"screen.png"
    im = Image.open(png)  # uses PIL library to open image in memory
    left = 150
    top = 150
    right = 600
    bottom = 750

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save(r"screenshot2.png")  # saves new cropped image


def findarea_attack(object, deep=20):
    McropImage()
    image = cv2.imread(r"screenshot2.png")

    # B, G, R
    # --------------------- ADD OBJECTS -------------------
    red = ([0, 0, 180], [80, 80, 255])
    green = ([0, 180, 0], [80, 255, 80])
    pickup_high = ([200, 0, 100], [255, 30, 190])
    attack_blue = ([250, 250, 0], [255, 255, 5])
    amber = ([0, 160, 160], [80, 255, 255])
    # --------------------- ADD OBJECTS -------------------
    ore_list = [red, green, pickup_high, attack_blue, amber]
    boundaries = [ore_list[object]]
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
        # if (cv2.__version__[0] > 3):
        # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # else:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        # draw in blue the contours that were founded
        # cv2.drawContours(output, contours, -1, 255, 3)
        # find the biggest countour (c) by the area
        c = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(c)
        # draw the biggest contour (c) in green
        whalf = max(round(w / 2), 1)
        hhalf = max(round(h / 2), 1)

        # cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
        x = random.randrange(x + 150 + whalf - deep, x + 150 + max(whalf + deep, 1))  # 950,960
        print('attack x: ', x)
        y = random.randrange(y + 150 + hhalf - deep, y + 150 + max(hhalf + deep, 1))  # 490,500
        print('attack y: ', y)
        b = random.uniform(0.05, 0.1)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b)
        return True
    return False
    # show the images
    # cv2.imshow("Result", np.hstack([image, output]))


def powerattack_text(monster='chicken', burybones=True, Take_Human_Break=False):
    j = 0
    group = monster_list.index(monster)
    while j < 10:
        randomizer(timer_break, ibreak)
        r = random.uniform(0.1, 5)
        resizeImage()
        mined = Image_to_Text('thresh', 'textshot.png')
        print(monster_array[group])
        attack = 0
        for monsters in monster_array[group]:
            # print(monsters)
            if mined.lower() != monsters:
                attack += 1
        if attack == len(monster_array[group]):
            d = random.uniform(0.05, 0.1)
            time.sleep(d)
            if burybones and image_Rec_clicker('bones_icon.png', 'bury bones', 5, 5, 0.7, 'left', 5, 620, 480, False):
                c = random.uniform(0.6, 1)
                time.sleep(c)
            if findarea_attack(2, 5):  # pick up highlighted loot
                c = random.uniform(3, 5)
                time.sleep(c)
            if findarea_attack(3):  # attack npc/monster
                c = random.uniform(3, 5)
                time.sleep(c)
                if Take_Human_Break:
                    c = random.uniform(0.1, 50)
                    time.sleep(c)


if __name__ == "__main__":
    # ----- UPDATE WITH ALL VARIATIONS OF MONSTER'S IMAGE TO TEXT RESULT IN LINE WITH MONSTER_LIST -----
    monster_array = [
        ['chicken'], ['guard', 'gua rd'], ['cow', 'cou'], ['monk'], ['imp'], ['skeleton']
    ]
    # --------------------------------------------------------------------------------------------------
    monster_list = ['chicken', 'guard', 'cow', 'monk', 'imp', 'skeleton']

    resizeImage()
    x = random.randrange(100, 250)
    y = random.randrange(400, 500)
    pyautogui.click(x, y, button='right')
    ibreak = random.randrange(300, 2000)
    print('will break in   ' + str(ibreak / 60) + ' minutes')
    timer_break = timer()
    powerattack_text('cow', Take_Human_Break=True)
