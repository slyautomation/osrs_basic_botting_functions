import re
from threading import Thread
import win32gui
import numpy as np
import cv2
import pyautogui
import random
import time
import argparse
import os
import yaml
import requests
import simplejson

global hwnd
global iflag
global icoord
import datetime
import pytesseract
from PIL import Image, ImageGrab
from functions import Image_to_Text, findarea_attack_quick
from functions import resizeImage
from functions import random_combat
from functions import random_quests
from functions import random_skills
from functions import random_inventory
from functions import image_Rec_clicker
import functions
import core

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

def timer_countdown():
    global Run_Duration_hours
    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    #print(t_end)
    final = round((60 * 60 * Run_Duration_hours) / 1)
    #print(final)
    for i in range(final):
        # the exact output you're looking for:
        print(bcolors.OK + f'\r[%-10s] %d%%' % ('='*round((i/final)*10), round((i/final)*100)), f'time left: {(t_end - time.time())/60 :.2f} mins | coords: {coords} | combat text: {combat_text} | {actions}', end='')
        time.sleep(1)


def powerattack_text(monster='chicken', burybones=True, Pickup_loot=False, Take_Human_Break=False, Run_Duration_hours=6):
    global ibreak, coords, combat_text, time_left, powerlist, actions, powerlist, t_end
    print('Will break in: %.2f' % (ibreak / 60) + ' minutes |', "Mob Selected:", monster)
    t1 = Thread(target=timer_countdown)
    t1.start()
    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    # using the datetime.fromtimestamp() function
    #date_time = datetime.datetime.fromtimestamp(t_end)
    #print(date_time)
    group = monster_list.index(monster)
    while time.time() < t_end:
        randomizer(timer_break, ibreak)
        r = random.uniform(0.1, 5)
        resizeImage()
        combat_text = Image_to_Text('thresh', 'textshot.png')
        combat_text = re.sub('[^A-Za-z0-9]+', ' ', combat_text)
        #print(combat_text)
        attack = 0
        for monsters in monster_array[group]:
            #print(monsters)
            if combat_text.strip().lower().find(monsters) == -1:
                attack += 1
        if Plugin_Enabled:
            if attack == monster:
                attack = 1
        if attack == len(monster_array[group]):
            d = random.uniform(0.05, 0.1)
            time.sleep(d)
            if burybones and image_Rec_clicker('bones_icon.png', 'bury bones', 5, 5, 0.7, 'left', 5, False):
                c = random.uniform(0.6, 1)
                time.sleep(c)
            if Pickup_loot:
                coords = findarea_attack_quick(2, 5)
                if coords[0] != 0:  # pick up highlighted loot
                    c = random.uniform(3, 5)
                    time.sleep(c)
            coords = findarea_attack_quick(3)
            if coords[0] != 0:   # attack npc/monster
                c = random.uniform(3, 5)
                time.sleep(c)
                if Take_Human_Break:
                    c = random.triangular(0.1, 50, 3)
                    time.sleep(c)

coords = (0, 0)
actions = 'None'
combat_text = 'Not in Combsat'
time_left = 0


def plugin(category='npc name'):
    c = s.get("http://localhost:8081/events", stream=True)
    data = simplejson.loads(c.text)
    data[category]
    #print(data[category])
    return data[category]

    
# ------ SET TO TRUE IF USING HTTPSERVER PLUGIN --------

Plugin_Enabled = True
if Plugin_Enabled:
    s = requests.session()

if __name__ == "__main__":
    # ----- UPDATE WITH ALL VARIATIONS OF MONSTER'S IMAGE TO TEXT RESULT IN LINE WITH MONSTER_LIST -----
    monster_array = [
        ['chicken'], ['guard', 'gua rd'], ['cow', 'cou'], ['monk'], ['imp'], ['skeleton'], ['dwarf'], ['giant frog', 'giant', 'frog']
    ]
    x = random.randrange(100, 250)
    y = random.randrange(400, 500)
    pyautogui.click(x, y, button='right')
    ibreak = random.randrange(300, 2000)
    timer_break = timer()

    # --------- CHANGE TO RUN FOR AMOUNT OF HOURS ----------------
    Run_Duration_hours = 4.3
    # --------------------------------------------------------------------------------------------------
    monster_list = ['chicken', 'guard', 'cow', 'monk', 'imp', 'skeleton', 'dwarf', 'giant frog']

    powerattack_text('chicken', Take_Human_Break=True, Run_Duration_hours=Run_Duration_hours)
    #os.system('shutdown -s -f')
