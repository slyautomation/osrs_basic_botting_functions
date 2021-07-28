import numpy as np
import cv2
import pyautogui
import random
import time

global hwnd
global iflag
global icoord
from PIL import Image



iflag = False

def cropImage():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"C:\Users\i7 8700\PycharmProjects\osrs-botting\screen.png")
    png = 'screen.png'
    im = Image.open(png)  # uses PIL library to open image in memory
    left = 340
    top = 330
    right = 600
    bottom = 600

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('screenshot.png')  # saves new cropped image

def Image_Rec_clicker(image, event, iheight, iwidth, threshold, clicker):
    global icoord
    global iflag
    myScreenshot = pyautogui.screenshot()
    # print('getting screenshot')
    myScreenshot.save(r"C:\Users\i7 8700\PycharmProjects\osrs-botting\screen.png")
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
        b = random.uniform(0.2, 0.7)
        pyautogui.moveTo(icoord, duration=b)
        b = random.uniform(0.1, 0.3)
        pyautogui.click(icoord, duration=b, button=clicker)
    return iflag
def CraftNavToBank():
    c = random.uniform(10, 11)
    x = random.randrange(10, 15)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(60, 65)  # y = random.randrange(50, 60)
    print('y: ', y)
    Image_Rec_clicker('Earth_alter_mark1.png', 'To Alter spot', x, y, 0.7, 'left')
    time.sleep(c)
    print('1st step to bank')
    b = random.uniform(0.18, 0.622)
    x = random.randrange(700, 710)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(170, 175)  # y = random.randrange(50, 60)
    print('y: ', y)
    c = random.uniform(10.2, 10.77)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('2nd step')
    b = random.uniform(0.17, 0.544)
    x = random.randrange(730, 735)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(170, 175)  # y = random.randrange(50, 60)
    print('y: ', y)
    c = random.uniform(10.2, 10.77)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('3rd step')
    b = random.uniform(0.215, 0.453)
    x = random.randrange(700, 705)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(155, 160)  # y = random.randrange(50, 60)
    print('y: ', y)
    c = random.uniform(10.25, 10.72)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('4th step')
    b = random.uniform(0.215, 0.453)
    x = random.randrange(675, 680)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(120, 125)  # y = random.randrange(50, 60)
    print('y: ', y)
    c = random.uniform(10.25, 10.72)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('5th step')
    x = random.randrange(-2, 3)
    print('x: ', x)
    y = random.randrange(73, 78)
    print('y: ', y)
    Image_Rec_clicker('bank_mark3.png', 'entering bank', x, y, 0.8, 'left')
    print('final step to bank')
    c = random.uniform(9, 10)
    time.sleep(c)
def CraftNavToEarth():
    c = random.uniform(6.5, 6.9)
    x = random.randrange(2, 7)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(37, 42)  # 41
    print('y: ', y)
    Image_Rec_clicker('bank_mark3.png', 'To Bank Spot', x, y, 0.7, 'left')
    time.sleep(c)
    print('bank mark step')
    b = random.uniform(0.18, 0.622)
    x = random.randrange(805, 810)  #
    print('x: ', x)
    y = random.randrange(110, 115)  #
    print('y: ', y)
    c = random.uniform(11.4, 11.8)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('1st step')
    b = random.uniform(0.18, 0.622)
    x = random.randrange(800, 805)  #
    print('x: ', x)
    y = random.randrange(90, 95)  #
    print('y: ', y)
    c = random.uniform(11.4, 11.8)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('2nd step')
    b = random.uniform(0.17, 0.544)
    x = random.randrange(750, 755)  #
    print('x: ', x)
    y = random.randrange(41, 44)  #
    print('y: ', y)
    c = random.uniform(11.4, 11.8)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('3rd step')
    b = random.uniform(0.21, 0.455)
    x = random.randrange(750, 755)  #
    print('x: ', x)
    y = random.randrange(41, 44)  #
    print('y: ', y)
    c = random.uniform(11.4, 11.8)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('4th step')

    c = random.uniform(15, 15.5)
    x = random.randrange(100, 103)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(-25, -20)  # 41
    print('y: ', y)
    Image_Rec_clicker('earth_mark2.png', 'To earth rock', x, y, 0.7, 'left')
    time.sleep(c)
    print('final step next to mysterious stone')
    #spotalter()
def move_to_portal():
    c = random.uniform(8, 8.8)
    x = random.randrange(20, 23)  #
    print('x: ', x)
    y = random.randrange(8, 11)  #
    print('y: ', y)
    Image_Rec_clicker('earthalter_mark1.png', 'back to exit portal', x, y, 0.8, 'left')
    print('moving back to portal')
    time.sleep(c)
def earthalter():
    print('moving to earth alter')
    b = random.uniform(0.18, 0.622)
    x = random.randrange(738, 742)  #
    print('x: ', x)
    y = random.randrange(80, 85)  #
    print('y: ', y)
    c = random.uniform(9.2, 11.2)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.23)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)
def movetoalter():
    b = random.uniform(6, 8)
    print(int(b))
    x = random.randrange(30, 35)  #
    print('x: ', x)
    y = random.randrange(400, 405)  #
    print('y: ', y)
    pyautogui.moveTo(x, y, duration=b)

def find_object(item):
    cropImage()
    image = cv2.imread('screenshot.png')

    # define the list of boundaries
    # B, G, R
    bank_booth = ([0, 190, 190], [100, 255, 255])
    green = ([0, 180, 0], [80, 255, 80])

    bank_list = [bank_booth, green]
    boundaries = [bank_list[item]]
    # 1st tin
    # 2nd copper
    # 3rd empty
    # cowhide

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
        wmin = min(round(whalf / 2), 0)
        hmin = min(round(hhalf / 2), 0)

        # cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
        x = random.randrange(x + wmin + 340 + 2, x + whalf + 340 - 2)  # 950,960
        print('x: ', x)
        y = random.randrange(y + hmin + 330 + 1, y + hhalf + 330 - 5)  # 490,500
        print('y: ', y)
        b = random.uniform(0.05, 0.1)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b)
def Image_color():
    cropImage()
    #myScreenshot = pyautogui.screenshot()
    #myScreenshot.save(r"C:\Users\MMH\PycharmProjects\osrs-botting\screenshot.png")
    # import the necessary packages
    # construct the argument parse and parse the arguments
    #ap = argparse.ArgumentParser()
    #ap.add_argument("-i", "--image", help="path to the image")
    #args = vars(ap.parse_args())
    # load the image
    image = cv2.imread('screenshot.png')
    #image = cv2.imread(args["image"])
    # define the list of boundaries
    empty = ([75, 135, 150], [122, 155, 180])
    empty2 = ([50, 50, 50], [70, 70, 70])
    empty3 = ([15, 20,40], [25, 40, 70]) #B, G, R
    empty4 = ([130, 140, 145], [150, 160, 165])

    boundaries = [
        empty, empty2, empty3, empty4
    ]
    # 1st tin = ([103, 86, 65], [145, 133, 128])
    # 2nd copper = ([35, 70, 120], [65, 110, 170])
    # 3rd empty = ([50, 45, 45], [70, 70, 75])
    # cowhide = ([165, 165, 170], [180, 180, 190])

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
    b = random.uniform(0.15, 0.5)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.19)
    pyautogui.click(duration=b, button='left')
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


def earth_runes():
    j = 0
    while j < 10:
        find_object(0)
        pick_item(1770 - 1280, 635)
        pick_item(1655 - 1280, 194)
        exit_bank()
        CraftNavToEarth()
        find_object(0)
        find_object(1)
        move_to_portal()
        CraftNavToBank()


find_object(0)
pick_item(1770 - 1280, 635)
pick_item(1655 - 1280, 194)
exit_bank()
CraftNavToEarth()
find_object(0)
