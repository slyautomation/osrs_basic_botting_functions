import numpy as np
import cv2
import pyautogui
import random
import time
from PIL import Image, ImageEnhance, ImageOps
import os

global hwnd
global iflag
global icoord
iflag = False
global newTime_break
newTime_break = False
global timer
global timer_break
global ibreak

import pytesseract

# change to where pytesseract is installed on your pc
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' 

# change to your user folder where osrs is installed

filename = "C:\\Users\\yourusername\\"

live_file = "jagex_cl_oldschool_LIVE.dat"

random_file = "random.dat"
try:
    os.remove(filename + live_file)
    os.remove(filename + random_file)
except OSError:
    pass

filename = "C:\\Users\\yourusername\\jagexcache\\oldschool\\LIVE\\"

for f in os.listdir(filename):
    try:
        if not f.startswith("main_file"):
            continue
        os.remove(os.path.join(filename, f))
    except OSError:
        pass

def deposit_all_Bank():
    banker = 50
    b = random.uniform(0.4, 0.77)
    x = random.randrange(480, 500)  # x = random.randrange(1040, 1050)
    y = random.randrange(623, 637)  # y = random.randrange(775, 805)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.23)
    pyautogui.click(duration=b, button='left')
    c = random.uniform(3.5, 4.5)
    time.sleep(c)

 def Miner_Image_quick():
    left = 150
    top = 150
    right = 600
    bottom = 750
    im = ImageGrab.grab(bbox=(left, top, right, bottom))
    im.save('miner_img.png', 'png')

def invent_crop():
    return screen_Image(620, 480, 820, 750, 'inventshot.png')

def resize_quick():
    left = 40
    top = 49
    right = 105
    bottom = 67

    im = ImageGrab.grab(bbox=(left, top, right, bottom))
    im.save('screen_resize.png', 'png')
 
def image_Rec_inventory(image, threshold, clicker, iheight=5, iwidth=5, ispace=10):
    global icoord
    global iflag
    invent_crop()
    img_rgb = cv2.imread('inventshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    pt = None
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    iflag = False
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        if pt is None:
            iflag = False
        else:
            iflag = True
            x = random.randrange(iwidth, iwidth + ispace)
            y = random.randrange(iheight, iheight + ispace)
            icoord = pt[0] + iheight + x
            icoord = (icoord, pt[1] + iwidth + y)
            b = random.uniform(0.1, 0.3)
            pyautogui.moveTo(icoord, duration=b)
            b = random.uniform(0.05, 0.15)
            pyautogui.click(icoord, duration=b, button=clicker)
    return iflag

def random_inventory():
    global newTime_break
    print('inventory tab')
    b = random.uniform(1.5, 15)
    pyautogui.press('f4')
    time.sleep(b)
    pyautogui.press('f4')
    b = random.uniform(1.5, 2)
    time.sleep(b)
    pyautogui.press('esc')
    newTime_break = True


def random_combat():
    global newTime_break
    print('combat tab')
    b = random.uniform(1.5, 15)
    pyautogui.press('f1')
    time.sleep(b)
    pyautogui.press('f1')
    b = random.uniform(1.5, 2)
    time.sleep(b)
    pyautogui.press('esc')
    newTime_break = True


def random_skills():
    global newTime_break
    print('skills tab')
    b = random.uniform(1.5, 15)
    pyautogui.press('f2')
    time.sleep(b)
    pyautogui.press('f2')
    b = random.uniform(1.5, 2)
    time.sleep(b)
    pyautogui.press('esc')
    newTime_break = True


def random_quests():
    global newTime_break
    print('quest tab')
    b = random.uniform(1.5, 15)
    pyautogui.press('f3')
    time.sleep(b)
    pyautogui.press('f3')
    b = random.uniform(1.5, 2)
    time.sleep(b)
    pyautogui.press('esc')
    newTime_break = True


def resizeImage():
    screen_Image(40, 49, 105, 67, 'screen_resize.png')
    png = 'screen_resize.png'
    im = Image.open(png)
    # saves new cropped image
    width, height = im.size
    new_size = (width * 4, height * 4)
    im1 = im.resize(new_size)
    im1.save('textshot.png')


def Image_to_Text(preprocess, image, parse_config='--psm 7'):
    # construct the argument parse and parse the arguments
    image = cv2.imread(image)
    image = cv2.bitwise_not(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # check to see if we should apply thresholding to preprocess the
    # image
    if preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # make a check to see if median blurring should be done to remove
    # noise
    if preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)

    if preprocess == 'adaptive':
        gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename), config=parse_config)
    os.remove(filename)
    print(text)
    return text


def screen_Image(left=0, top=0, right=0, bottom=0, name='screenshot.png'):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'screenshot.png')
    if left != 0 or top != 0 or right != 0 or bottom != 0:
        png = 'screenshot.png'
        im = Image.open(png)  # uses PIL library to open image in memory
        im = im.crop((left, top, right, bottom))  # defines crop points
        im.save(name)  # saves new cropped image
        # print('screeenshot saved')


def Image_color():
    screen_Image()
    image = cv2.imread('screenshot.png')
    # define the list of boundaries
    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 Index
    pickup_high = ([250, 0, 167], [255, 5, 172])  # 3 Index
    attack_blue = ([250, 250, 0], [255, 255, 5])

    boundaries = [
        red, green, amber, pickup_high, attack_blue
    ]

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        # show the images
        cv2.imshow("images", np.hstack([image, output]))
        cv2.waitKey(0)


def exit_bank():
    print('exit bank')
    c = random.uniform(0.3, 0.7)
    x = random.randrange(523, 540)
    print('x: ', x)
    y = random.randrange(40, 55)
    print('y: ', y)
    b = random.uniform(0.15, 0.6)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.19)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

def teleport_home():
    pyautogui.press('esc')
    random_breaks(0.1, 0.3)
    pyautogui.press('f6')
    random_breaks(0.1, 0.3)
    pick_item(1928-1280, 498)

def find_Object_precise(item, deep=20, left=0, top=0, right=0, bottom=0):
    screen_Image(left, top, right, bottom)
    image = cv2.imread('screenshot.png')

    # define the list of boundaries
    # B, G, R

    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 Index
    pickup_high = ([250, 0, 167], [255, 5, 172])  # 3 Index
    attack_blue = ([250, 250, 0], [255, 255, 5])
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
        x, y, w, h = cv2.boundingRect(c)

        whalf = max(round(w / 2), 1)
        hhalf = max(round(h / 2), 1)

        x = random.randrange(x + whalf - deep, x + max(whalf + deep, 1))
        print('x: ', x)
        y = random.randrange(y + hhalf - deep, y + max(hhalf + deep, 1))
        print('y: ', y)
        b = random.uniform(0.2, 0.4)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b)
        return True
    else:
        return False


def find_Object(item, left=0, top=0, right=0, bottom=0):
    screen_Image(left, top, right, bottom)
    image = cv2.imread('screenshot.png')

    # define the list of boundaries
    # B, G, R

    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 Index
    pickup_high = ([250, 0, 167], [255, 5, 172])  # 3 Index
    attack_blue = ([250, 250, 0], [255, 255, 5])
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
        x, y, w, h = cv2.boundingRect(c)

        x = random.randrange(x + 5, x + max(w - 5, 6))  # 950,960
        print('x: ', x)
        y = random.randrange(y + 5, y + max(h - 5, 6))  # 490,500
        print('y: ', y)
        b = random.uniform(0.2, 0.4)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b)


def spaces(a):
    if a == 1:
        d = random.uniform(0.05, 0.1)
        time.sleep(d)
        pyautogui.press('space')
    if a == 0:
        print("none")
    if a == 2:
        d = random.uniform(0.05, 0.1)
        time.sleep(d)
        pyautogui.press('space')
        d = random.uniform(0.05, 0.1)
        time.sleep(d)
        pyautogui.press('space')


def skill_lvl_up():
    counter = 0
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"screen.png")
    img_rgb = cv2.imread(r"screen.png")
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('Congrats_flag.png', 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    # cv2.imwrite('res.png', img_rgb)
    return counter


def pick_item_right(v, u, option=1):
    c = random.uniform(0.3, 0.7)
    d = random.uniform(0.05, 0.15)
    x = random.randrange(v - 10, v + 10)
    print('x: ', x)
    y = random.randrange(u - 5, u + 5)
    b = random.uniform(0.3, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='right')
    time.sleep(c)
    w = random.randrange(0, 10) + x
    print('x: ', x)
    one = random.randrange(40, 45) + y
    two = random.randrange(50, 55) + y
    three = random.randrange(60, 65) + y
    four = random.randrange(70, 75) + y
    five = random.randrange(80, 85) + y
    six = random.randrange(90,95) + y
    seven = random.randrange(100,105) + y
    eight = random.randrange(110,115) + y
    right_order = {1: one,
                   2: two,
                   3: three,
                   4: four,
                   5: five,
                   6: six,
                   7: seven,
                   8: eight
    }
    z = right_order[option]
    print('y: ', y)
    pyautogui.moveTo(w, z, duration=b)
    b = random.uniform(0.1, 0.19)
    pyautogui.click(duration=b)
    c = random.uniform(0.1, 0.4)
    time.sleep(c)


def pick_item(v, u):
    c = random.uniform(0.3, 0.7)
    d = random.uniform(0.05, 0.15)
    x = random.randrange(v - 10, v + 10)
    print('x: ', x)
    y = random.randrange(u - 5, u + 5)
    b = random.uniform(0.2, 0.6)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)


def deposit_secondItem():
    c = random.uniform(0.3, 0.7)
    x = random.randrange(690, 715)  # 950,960
    z = x
    print('x: ', x)
    y = random.randrange(495, 515)  # 490,500
    w = y
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

def mini_map_image(image, iwidth=0, iheight=0, threshold=0.7, clicker='left', xspace=0, yspace=0):
    screen_Image(1941 - 1280, 27, 2106 - 1280, 190, 'mini_map.png')
    global icoord
    global iflag
    img_rgb = cv2.imread('mini_map.png')
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
        x = random.randrange(iwidth, iwidth + 1 + xspace) + (1941 - 1280)
        y = random.randrange(iheight, iheight + 1 + yspace) + 27
        icoord = pt[0] + x
        icoord = (icoord, pt[1] + y)
        b = random.uniform(0.2, 0.7)
        pyautogui.moveTo(icoord, duration=b)
        b = random.uniform(0.1, 0.3)
        pyautogui.click(icoord, duration=b, button=clicker)
    return iflag

def mini_map_bool(image, threshold=0.7):
    screen_Image(1941 - 1280, 27, 2106 - 1280, 190, 'mini_map.png')
    global icoord
    global iflag
    img_rgb = cv2.imread('mini_map.png')
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
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    # print('result of pt')
    if pt is None:
        iflag = False
        # print(event, 'Not Found...')
    else:
        iflag = True
    return iflag

def xp_gain_check(image, threshold=0.5):
    screen_Image(1825 - 1280, 75, 1890 - 1280, 190, 'xp_gain.png')
    global iflag
    img_rgb = cv2.imread('xp_gain.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    pt = None
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    iflag = False
    for pt in zip(*loc[::-1]):
        iflag = True
    if pt is None:
        iflag = False
    return iflag

def Image_Rec_single(image, event, iheight, iwidth, threshold, clicker, ispace=20, cropx=0, cropy=0, playarea=True):
    global icoord
    global iflag
    if playarea:
        screen_Image(0, 0, 600, 750)
    else:
        screen_Image(620, 480, 820, 750)
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
        x = random.randrange(iwidth, iwidth + ispace) + cropx
        y = random.randrange(iheight, iheight + ispace) + cropy
        icoord = pt[0] + iheight + x
        icoord = (icoord, pt[1] + iwidth + y)
        b = random.uniform(0.2, 0.7)
        pyautogui.moveTo(icoord, duration=b)
        b = random.uniform(0.1, 0.3)
        pyautogui.click(icoord, duration=b, button=clicker)
    return iflag


def image_Rec_clicker(image, event, iheight, iwidth, threshold, clicker, ispace=20, cropx=0, cropy=0, playarea=True):
    global icoord
    global iflag
    if playarea:
        screen_Image(0, 0, 600, 750)
    else:
        screen_Image(620, 480, 820, 750)
    img_rgb = cv2.imread('screenshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    pt = None
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    iflag = False
    event = event
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        if pt is None:
            iflag = False
        else:
            iflag = True
            x = random.randrange(iwidth, iwidth + ispace) + cropx
            y = random.randrange(iheight, iheight + ispace) + cropy
            icoord = pt[0] + iheight + x
            icoord = (icoord, pt[1] + iwidth + y)
            b = random.uniform(0.1, 0.3)
            pyautogui.moveTo(icoord, duration=b)
            b = random.uniform(0.05, 0.15)
            pyautogui.click(icoord, duration=b, button=clicker)
    return iflag


def Image_count(object, threshold=0.8):
    counter = 0
    screen_Image(name='screenshot.png')
    img_rgb = cv2.imread('screenshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(object, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    return counter


def drop_item():
    pyautogui.keyUp('shift')
    c = random.uniform(0.1, 0.2)
    d = random.uniform(0.2, 0.23)

    time.sleep(c)
    pyautogui.keyDown('shift')
    time.sleep(d)


def release_drop_item():
    e = random.uniform(0.2, 0.3)
    f = random.uniform(0.1, 0.2)

    time.sleep(e)
    pyautogui.keyUp('shift')
    pyautogui.press('shift')
    time.sleep(f)


def random_breaks(minsec, maxsec):
    e = random.uniform(minsec, maxsec)
    time.sleep(e)


def findarea(object):
    screen_Image()
    image = cv2.imread('screenshot.png')
    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 Index
    pickup_high = ([250, 0, 167], [255, 5, 172])  # 3 Index
    attack_blue = ([250, 250, 0], [255, 255, 5])
    object_list = [red, green, amber, pickup_high, attack_blue]
    boundaries = [object_list[object]]
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
        cv2.drawContours(output, contours, -1, 255, 3)
        # find the biggest countour (c) by the area
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        # draw the biggest co  ntour (c) in green
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # show the images
    cv2.imshow("Result", np.hstack([image, output]))
    cv2.waitKey(0)


def health_text():
    screen_Image(left=1900 - 1280, top=89, right=1918 - 1280, bottom=101, name='health.png')
    png = 'health.png'
    im = Image.open(png)
    # saves new cropped image
    width, height = im.size
    new_size = (width * 4, height * 4)
    im1 = im.resize(new_size)
    # im1.save('health.png')
    im1 = im1.convert('LA')  # convert image to black and white
    im1.save('health.png')
    return int(Image_to_Text('thresh', 'health.png', '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'))


def remove_black():
    screen_Image(left=1909 - 1280, top=154, right=1930 - 1280, bottom=168, name='stamina.png')
    im = Image.open('stamina.png')
    im = im.convert('RGBA')
    data = np.array(im)
    # just use the rgb values for comparison
    rgb = data[:, :, :3]
    color = [0, 0, 0]  # Original value color = [246, 213, 139]
    black = [104, 90, 75, 255]
    white = [255, 255, 255, 255]
    mask = np.all(rgb == color, axis=-1)
    # change all pixels that match color to white
    data[mask] = black

    # change all pixels that don't match color to black
    ##data[np.logical_not(mask)] = black
    new_im = Image.fromarray(data)
    new_im.save('stamina.png')


def Stam_Text(image):
    # construct the argument parse and parse the arguments
    image = cv2.imread(image)
    # image = cv2.bitwise_not(image)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, image)
    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename), lang='eng',
                                       config='--psm 12 --oem 2 -c tessedit_char_whitelist=0123456789')
    # os.remove(filename)
    # print(text)
    return text


def get_red():
    remove_black()
    # define the list of boundaries
    # B, G, R
    image = cv2.imread('stamina.png')
    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    boundaries = [red]

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
    cv2.imwrite('stamina3.png', output)
    png = 'stamina3.png'
    im = Image.open(png)
    # saves new cropped image
    width, height = im.size
    new_size = (width * 10, height * 10)
    im1 = im.resize(new_size)
    im1.save('stamina3.png')


def replace_characters(temp):
    temp = temp.replace('q', '9')
    temp = temp.replace('?', '8')
    temp = temp.replace('h', '4')
    temp = temp.replace('S', '8')
    temp = temp.replace('/', '7')
    temp = temp.replace('l', '1')
    temp = temp.replace('L', '4')
    temp = temp.replace('k', '4')
    return temp


def resize_enahnce_invert_text(image):
    png = image
    im = Image.open(png)
    # saves new cropped image
    width, height = im.size
    new_size = (width * 10, height * 10)
    im1 = im.resize(new_size)

    enhancer = ImageEnhance.Sharpness(im1)
    factor = 2
    im1 = enhancer.enhance(factor)
    enhancer = ImageEnhance.Contrast(im1)
    factor = 2
    im1 = enhancer.enhance(factor)
    im1 = im1.convert('L')  # 1 just black # L or LA convert image to black and white #

    im1 = ImageOps.invert(im1)
    im1.save('stamina.png')


def stamina_text():
    stam_num = 100
    remove_black()

    resize_enahnce_invert_text('stamina.png')
    img = cv2.imread("stamina.png")
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.erode(thresh, kernel, iterations=1)
    cv2.imwrite('stamina.png', img)
    temp_num = Stam_Text('stamina.png')
    if len(temp_num) > 0:
        temp_num = replace_characters(temp_num)
    else:
        get_red()
        temp_num = replace_characters(Image_to_Text('blur', 'stamina3.png'))
    try:
        stam_num = int(temp_num)
    except ValueError:
        stan_num = 100
    return stam_num


"""
j = 0
while j == 0:
    print(stamina_text())
"""
# Image_color()
