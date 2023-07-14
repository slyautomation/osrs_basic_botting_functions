import datetime
import win32gui
from threading import Thread
import core
import yaml
from functions import Image_count, invent_enabled
from functions import image_Rec_clicker
from functions import screen_Image
from functions import release_drop_item
from functions import drop_item
from functions import Image_to_Text
from functions import invent_crop
from functions import resizeImage
from PIL import ImageGrab

from functions import random_combat
from functions import random_quests
from functions import random_skills
from functions import random_inventory
from functions import random_breaks

import numpy as np
import cv2
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
import slyautomation_title


class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR


def gfindWindow(data):  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, data)
    # hwnd = win32gui.GetForegroundWindow()860
    # print('findWindow:', hwnd)
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

def Fisher_Image_quick():
    left = 150
    top = 150
    right = 600
    bottom = 750

    im = ImageGrab.grab(bbox=(left, top, right, bottom))
    im.save('images/screenshot.png', 'png')

def Fisher_Image():
    screen_Image(150, 150, 600, 750, 'images/screenshot.png')

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
    # print("dropping ore done")
    actions = "all fish dropped"

def findarea_single(fish, cropx, cropy):
    Fisher_Image_quick()
    image = cv2.imread(r"images/screenshot.png")

    # B, G, R
    # --------------------- ADD OBJECTS -------------------
    lobster = ([60, 30, 10], [120, 70, 40])
    red = ([0, 0, 180], [80, 80, 255])
    green = ([0, 180, 0], [80, 255, 80])
    amber = ([0, 160, 160], [80, 255, 255])
    # --------------------- ADD OBJECTS -------------------
    fish_list = [lobster, red, green, amber]
    boundaries = [fish_list[fish]]
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
        # print('x: ', x)
        y = random.randrange(y + 5, y + max(h - 5, 6)) + cropy  # 490,500
        # print('y: ', y)
        b = random.uniform(0.1, 0.3)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(7, 10)
        pyautogui.click(duration=b)
        return (x, y)

def count_geo():
    return Image_count('geo_icon.png')

def inv_count(name):
    return Image_count(name + '_fish.png')

def timer_countdown():
    global Run_Duration_hours
    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    # print(t_end)
    final = round((60 * 60 * Run_Duration_hours) / 1)
    # print(final)
    for i in range(final):
        # the exact output you're looking for:
        print(bcolors.OK + f'\r[%-10s] %d%%' % ('=' * round((i / final) * 10), round((i / final) * 100)),
              f'time left: {(t_end - time.time()) / 60 :.2f} mins | coords: {spot} | status: {fished_text} | fish: {fish_count} | gems: {gem_count} | clues: {clue_count} | {actions}',
              end='')
        time.sleep(1)


def count_items():
    global Run_Duration_hours
    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    while time.time() < t_end:
        global ore, powerlist, fish_count, fished_text, clue_count
        fish_count = int(inv_count(powerlist[ore]))
        clue_count = int(count_geo())
        time.sleep(0.1)


def print_progress(time_left, spot, fished_text, powerlist, fish, actions):
    print(bcolors.OK +
          f'\rtime left: {time_left} | coords: {spot} | status: {fished_text} | fish: {int(inv_count(powerlist[fish]))} | clues: {int(count_geo())} | {actions}',
          end='')


def powerfisher_text(fish, num, Take_Human_Break=False, Run_Duration_hours=5):
    global spot, fished_text, time_left, powerlist, actions, powerlist, t_end, fish_count, clue_count
    powerlist = ['lobster', 'red', 'green', 'amber']
    print("Will break in: %.2f" % (ibreak / 60) + " minutes |", "Fish Selected:", powerlist[fish])
    t1 = Thread(target=timer_countdown)
    t1.start()
    spot = (0, 0)
    actions = 'None'
    fished_text = 'Not Fishing'

    t_end = time.time() + (60 * 60 * Run_Duration_hours)
    while time.time() < t_end:
        invent = invent_enabled()
        if invent == 0:
            actions = 'opening inventory'
            pyautogui.press('esc')
        time_left = str(datetime.timedelta(seconds=round(t_end - time.time(), 0)))
        actions = 'None'
        randomizer(timer_break, ibreak)
        r = random.uniform(0.1, 5)
        fish_count = int(inv_count(powerlist[fish]))
        clue_count = int(count_geo())
        inventory = fish_count + clue_count
        if inventory > 26:
            actions = 'dropping fish starting...'
            actions = drop_fish()
            random_breaks(0.2, 0.7)
        fished_text = Image_to_Text('thresh', 'textshot.png')
        if fished_text.strip().lower() != 'fishing' and fished_text.strip().lower() != 'fishing':
            fished_text = 'Not Fishing'
            spot = findarea_single(num, 150, 150)
            if Take_Human_Break:
                c = random.triangular(0.05, 6, 0.5)
                time.sleep(c)
        else:
            fished_text = 'Fishing'


spot = (0, 0)
actions = 'None'
fished_text = 'Not Fishing'
time_left = 0

# -------------------------------

powerlist = ['lobster', 'red', 'green', 'amber']

fish_count = 0
gem_count = 0
clue_count = 0
# -------------------------------

if __name__ == "__main__":
    x = random.randrange(100, 250)
    y = random.randrange(400, 500)
    pyautogui.click(x, y, button='right')
    ibreak = random.randrange(300, 2000)
    timer_break = timer()

    # ----- ORE -------
    lobster = 0

    # ----- OBJECT MARKER COLOR ------
    red = 1
    green = 2
    amber = 3

    # --------- CHANGE TO RUN FOR AMOUNT OF HOURS ----------------
    Run_Duration_hours = 3

    # | fish to drop | marker color | take break | how long to run for in hours
    powerfisher_text(lobster, red, Take_Human_Break=True, Run_Duration_hours=Run_Duration_hours)

    # os.system('shutdown -s -f')