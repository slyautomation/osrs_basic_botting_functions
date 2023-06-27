import core
import numpy as np
import cv2
import pyautogui
import random
import time
import keyboard
from win32gui import Polygon
from shapely.geometry import Polygon
import functions
import win32gui
global hwnd
global iflag
global icoord
from PIL import Image, ImageGrab

iflag = False
icoord = []
from functions import image_Rec_inventory

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
    
def skill_lvl_up():
    counter = 0
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"screen.png")
    img_rgb = cv2.imread('screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/' + 'Congrats_flag.png', 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    cv2.imwrite('res.png', img_rgb)
    return counter



def xp_check():
    return bool_alpha('thieving.png', 0.8, 560, 95, 610, 135)

def screen_I(left=0, top=0, right=0, bottom=0, name='screenshot.png'):
    if left != 0 or top != 0 or right != 0 or bottom != 0:
        myScreenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    else:
        myScreenshot = ImageGrab.grab()
    myScreenshot.save(name)

def bool_alpha(temp, threshold=0.89, left=0, top=0, right=0, bottom=0):
    screen_I(left, top, right, bottom, name='screenshot_bool.png')
    # read screenshot
    img = cv2.imread('screenshot_bool.png')
    # read image template
    template = cv2.imread('images/' + temp, cv2.IMREAD_UNCHANGED)
    # extract base image and alpha channel and make alpha 3 channels
    temp_a = template[:, :, 0:3]
    alpha = template[:, :, 3]
    alpha = cv2.merge([alpha, alpha, alpha])
    # set threshold
    threshold = threshold
    # do masked template matching and save correlation image
    corr_img = cv2.matchTemplate(img, temp_a, cv2.TM_CCORR_NORMED, mask=alpha)
    # search for max score
    max_val = 1
    # find max value of correlation image
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(corr_img)
    return max_val

def value_alpha(temp, threshold=0.89, left=0, top=0, right=0, bottom=0):
    screen_I(left, top, right, bottom, name='screenshot_bool.png')
    # read screenshot
    img = cv2.imread('screenshot_bool.png')
    # read image template
    template = cv2.imread('images/' + temp, cv2.IMREAD_UNCHANGED)
    # extract base image and alpha channel and make alpha 3 channels
    temp_a = template[:, :, 0:3]
    alpha = template[:, :, 3]
    alpha = cv2.merge([alpha, alpha, alpha])
    # set threshold
    threshold = threshold
    # do masked template matching and save correlation image
    corr_img = cv2.matchTemplate(img, temp_a, cv2.TM_CCORR_NORMED, mask=alpha)
    # search for max score
    max_val = 1
    # find max value of correlation image
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(corr_img)
    return min_val, max_val, min_loc, max_loc

def Image_count_alpha(temp, threshold=0.89, left=0, top=0, right=0, bottom=0):
    counter = 0
    screen_I(left, top, right, bottom, name='screenshot.png')
    # read screenshot
    img = cv2.imread('screenshot.png')
    # read pawn image template
    # template = cv2.imread('chess_template.png', cv2.IMREAD_UNCHANGED)
    template = cv2.imread('images/' + temp, cv2.IMREAD_UNCHANGED)
    hh, ww = template.shape[:2]
    # extract pawn base image and alpha channel and make alpha 3 channels
    temp_a = template[:, :, 0:3]
    alpha = template[:, :, 3]
    alpha = cv2.merge([alpha, alpha, alpha])
    # set threshold
    threshold = threshold
    # do masked template matching and save correlation image
    corr_img = cv2.matchTemplate(img, temp_a, cv2.TM_CCORR_NORMED, mask=alpha)
    # search for max score
    result = img.copy()
    max_val = 1
    while max_val > threshold:

        # find max value of correlation image
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(corr_img)
        #print(max_val, max_loc)

        if max_val > threshold:
            # draw match on copy of input
            counter += 1
            cv2.rectangle(result, max_loc, (max_loc[0] + ww, max_loc[1] + hh), (0, 0, 255), 2)
        else:
            break
    return counter

def thieve_object(item, left=0, top=0, right=860, bottom=775):
    screen_I(left, top, right, bottom)
    image = cv2.imread('screenshot.png')
    image = cv2.rectangle(image, pt1=(600, 0), pt2=(850, 200), color=(0, 0, 0), thickness=-1)
    image = cv2.rectangle(image, pt1=(0, 0), pt2=(150, 100), color=(0, 0, 0), thickness=-1)

    # define the list of boundaries
    # B, G, R

    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 Index
    pickup_high = ([250, 0, 167], [255, 5, 172])  # 3 Index
    attack_blue = ([200, 200, 0], [255, 255, 5])
    object_list = [red, green, amber, pickup_high, attack_blue]
    boundaries = [object_list[item]]

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
        # print(c)
        # print(np.squeeze(c))
        # print(Polygon(np.squeeze(c)))
        minx, miny, maxx, maxy = Polygon(np.squeeze(c)).bounds
        # print(minx, miny, maxx, maxy)
        x = random.randrange(minx + 1, max(maxx - 1, minx + 2))
        y = random.randrange(miny + 1, max(maxy - 1, miny + 2))
        # print('y: ', y)
        b = random.uniform(0.01, 0.02)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b)
        return (x, y)
    return False

def steal_man():
    pyautogui.PAUSE = 0
    global actions
    caps = False
    time_end = 0
    time_start = time.time()
    while True:
        caps = keyboard.is_pressed('capslock')
        if caps:
            print('thieving script stopped')
            exit()
        thieve_object(4)
        b = random.uniform(0.01, 0.09)
        time.sleep(b)
        thief = xp_check()
        if thief > 0.8:
            time_end = 0
            time_start = time.time()
        print('Thieving: %.2f' % thief + ' | seconds count: %.2f' % time_end)
        time_end = time.time() - time_start
        c = random.uniform(3, 5)
        if time_end > c:
            invent = functions.invent_enabled()
            if invent == 0:
                actions = 'opening inventory'
                pyautogui.press('esc')
            min_val, max_val, min_loc, max_loc = value_alpha('money_bag_2.png')
            if max_val == 1:
                x = max_loc[0] + random.randrange(1, 15)
                y = max_loc[1] + random.randrange(1, 15)
                b = random.uniform(0.01, 0.02)
                pyautogui.moveTo(x, y, duration=b)
                b = random.uniform(0.01, 0.05)
                pyautogui.click(duration=b)
                time_end = 0
                time_start = time.time()
                b = random.uniform(0.01, 0.15)
            time.sleep(b)

def steal_tea():
    global actions
    caps = False
    while True:
        caps = keyboard.is_pressed('capslock')
        if caps:
            print('thieving script stopped')
            exit()
        thieve_object(0,0,0,860,750)
        b = random.uniform(6, 8)
        time.sleep(b)
        d = random.uniform(0.10, 0.23)
        e = random.uniform(0.10, 0.25)
        pyautogui.keyDown('shift')
        time.sleep(d)
        image_Rec_inventory('tea_icon.png')
        time.sleep(e)
        pyautogui.keyUp('shift')

def steal_drop_fruit():
    global actions
    caps = False
    while True:
        caps = keyboard.is_pressed('capslock')
        if caps:
            print('thieving script stopped')
            exit()
        thieve_object(0,0,0,860,750)
        pyautogui.keyDown('shift')
        e = random.uniform(0.1, 1)
        time.sleep(e)
        image_Rec_inventory('apple_fruit.png')
        image_Rec_inventory('greenberry_fruit.png')
        image_Rec_inventory('strawberry_fruit.png')
        image_Rec_inventory('banana_fruit.png')
        image_Rec_inventory('exp_fruit.png')
        image_Rec_inventory('purple_fruit.png')
        image_Rec_inventory('lemon_fruit.png')
        image_Rec_inventory('pineapple_fruit.png')
        image_Rec_inventory('lime_fruit.png')
        image_Rec_inventory('papyaya_fruit.png')
        e = random.uniform(0.1, 1)
        time.sleep(e)
        pyautogui.keyUp('shift')
        pyautogui.press('shift')

if __name__ == "__main__":
    steal_man()
    #steal_tea()
    #steal_drop_fruit()

