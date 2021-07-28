import numpy as np
import cv2
import pyautogui
import random
import time
import argparse

import multiprocessing
from multiprocessing import Process, Pipe

global hwnd
global iflag
global icoord
from PIL import Image
# from matplotlib import pyplot as plt
from Dialogue_Decrypter import determineText

iflag = False
def RcropImage():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"screen.png")
    png = 'screen.png'
    im = Image.open(png)  # uses PIL library to open image in memory
    left = 100
    top = 200
    right = 600
    bottom = 600

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('screenshot.png')  # saves new cropped image
def DcropImage():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"screen.png")
    png = 'screen.png'
    im = Image.open(png)  # uses PIL library to open image in memory
    left = 200
    top = 300
    right = 530
    bottom = 530

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('screenshot.png')  # saves new cropped image
def BcropImage():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"screen.png")
    png = 'screen.png'
    im = Image.open(png)  # uses PIL library to open image in memory
    left = 400
    top = 250
    right = 800
    bottom = 475
    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('screenshot.png')  # saves new cropped image
def cropImage():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"screen.png")
    png = 'screen.png'
    im = Image.open(png)  # uses PIL library to open image in memory
    left = 340
    top = 330
    right = 600
    bottom = 600

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('screenshot.png')  # saves new cropped image
def find_portal_area():
    cropImage()
    # import the necessary packages
    # construct the argument parse and parse the arguments
    #ap = argparse.ArgumentParser()
    #ap.add_argument("-i", "--image", help="path to the image")
    #args = vars(ap.parse_args())
    # load the image
    image = cv2.imread('screenshot.png')
    #image = cv2.imread(args["image"])
    # define the list of boundaries

    # B, G, R
    rock_rune = ([50, 50, 50], [70, 70, 70])
    portal = ([75, 135, 150], [122, 155, 180])
    banker = ([103, 86, 65], [145, 133, 128])
    boundaries = [portal]

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
        #if (cv2.__version__[0] > 3):
            #contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #else:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) != 0:
            # draw in blue the contours that were founded
            #cv2.drawContours(output, contours, -1, 255, 3)

            # find the biggest countour (c) by the area
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)

            # draw the biggest contour (c) in green
            #cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #coal = [8, 10]
            #copper = (2.3, 4.2)
            c = random.uniform(4,6)
            b = random.uniform(0.25, 0.65)
            x = random.randrange(x+340, x+345)  # 950,960
            y = random.randrange(y+330, y+335)  # 490,500
            pyautogui.moveTo(x, y, duration=b)
            b = random.uniform(0.1, 0.19)
            pyautogui.click(duration=b)
            print('entering back into portal')
            time.sleep(c)
    # show the images
    #cv2.imshow("Result", np.hstack([image, output]))

    #cv2.waitKey(0)
def findrune_rock():
    RcropImage()
    # import the necessary packages
    # construct the argument parse and parse the arguments
    #ap = argparse.ArgumentParser()
    #ap.add_argument("-i", "--image", help="path to the image")
    #args = vars(ap.parse_args())
    # load the image
    image = cv2.imread('screenshot.png')
    #image = cv2.imread(args["image"])
    # define the list of boundaries

    # B, G, R
    rock_rune = ([50, 50, 50], [70, 70, 70])
    portal = ([75, 135, 150], [122, 155, 180])
    banker = ([103, 86, 65], [145, 133, 128])
    boundaries = [rock_rune]

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
        #if (cv2.__version__[0] > 3):
            #contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #else:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) != 0:
            # draw in blue the contours that were founded
            #cv2.drawContours(output, contours, -1, 255, 3)

            # find the biggest countour (c) by the area
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)

            # draw the biggest contour (c) in green
            #cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #coal = [8, 10]
            #copper = (2.3, 4.2)
            c = random.uniform(2.3,2.6)
            b = random.uniform(0.25, 0.65)
            x = random.randrange(x+120, x+130)  # 950,960
            w = x
            y = random.randrange(y+205, y+210)  # 490,500
            z = y
            print('moving mouse to mysterious rock spot')
            pyautogui.moveTo(x, y, duration=b)
            b = random.uniform(0.1, 0.19)
            pyautogui.click(duration=b, button='right')

            time.sleep(c)

            c = random.uniform(6,7)
            b = random.uniform(0.25, 0.65)
            x = random.randrange(w, w+10)  # 950,960
            y = random.randrange(z+23, z+27)  # 490,500
            print('selecting first option')
            pyautogui.moveTo(x, y, duration=b)
            b = random.uniform(0.1, 0.19)
            pyautogui.click(duration=b, button='left')
            time.sleep(c)
    # show the images
    #cv2.imshow("Result", np.hstack([image, output]))

    #cv2.waitKey(0)
def Image_Rec_clicker(image, event, iheight, iwidth, threshold, clicker):
    global icoord
    global iflag
    myScreenshot = pyautogui.screenshot()
    # print('getting screenshot')
    myScreenshot.save(r"screen.png")
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
    c = random.uniform(1.5, 2)
    x = random.randrange(5, 20)  #
    print('x: ', x)
    y = random.randrange(5, 20)  #
    print('y: ', y)
    Image_Rec_clicker('water_tailsmen.png', 'use tailsmen', x, y, 0.7, 'left')
    print('using water tailsmen')
    time.sleep(c)
def deposit_secondItem():
    c = random.uniform(2, 2.5)
    x = random.randrange(690, 705)
    z = x
    print('x: ', x)
    y = random.randrange(500, 513)
    w = y
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='right')
    time.sleep(c)
    print('stand in second bank cubicle')
    c = random.uniform(2, 2.5)
    x = random.randrange(z, z + 15)
    print('x: ', x)
    y = random.randrange(w + 103, w + 107)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)
def textdecrypt():
    flag = determineText('enter')
    print(flag)
def movetoalter():
    b = random.uniform(6, 8)
    print(int(b))
    x = random.randrange(30, 35)  #
    print('x: ', x)
    y = random.randrange(400, 405)  #
    print('y: ', y)

    pyautogui.moveTo(x, y, duration=b)
def spotalter():
    if __name__ == '__main__':
        p1 = Process(target=movetoalter)
        p2 = Process(target=textdecrypt)
        p1.start()
        p2.start()
        while p2.is_alive():
            b = 1  # print(p2.is_alive())
        p1.terminate()
def depositBank():
    banker = 50
    b = random.uniform(0.4, 0.77)
    x = random.randrange(480, 505)  # x = random.randrange(1040, 1050)
    y = random.randrange(565, 585)  # y = random.randrange(775, 805)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.23)
    pyautogui.click(duration=b, button='left')
    c = random.uniform(3.5, 4.5)
    time.sleep(c)

def withdraw_mud_items():
    b = random.uniform(0.4, 0.77)
    x = random.randrange(125, 145)  # x = random.randrange(1040, 1050)
    y = random.randrange(150, 170)  # y = random.randrange(775, 805)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.23)
    pyautogui.click(duration=b, button='left')
    c = random.uniform(2, 2.5)
    time.sleep(c)

    c = random.uniform(2, 2.5)
    x = random.randrange(365, 385)
    z = x
    print('x: ', x)
    y = random.randrange(115, 135)
    w = y
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='right')
    time.sleep(c)
    print('withrawing mud items')
    c = random.uniform(2, 2.5)
    x = random.randrange(z, z + 15)
    print('x: ', x)
    y = random.randrange(w + 103, w + 107)
    print('y: ', y)
    b = random.uniform(0.2, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)
def find_banker_good(item):
    if item == 0:
        DcropImage()
        d = 200
        e = 300
        g = 2
        i = 2.5
    else:
        BcropImage()
        d = 400
        e = 250
        g = 5
        i = 8

    # import the necessary packages
    # construct the argument parse and parse the arguments
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--image", help="path to the image")
    # args = vars(ap.parse_args())
    # load the image
    image = cv2.imread('screenshot.png')
    # image = cv2.imread(args["image"])
    # define the list of boundaries
    # B, G, R
    depositbox= ([60, 78, 86], [75, 90, 100])
    banker = ([130, 140, 145], [150, 160, 165])
    furnace = ([25, 25, 30], [38, 38, 50])
    bank_booth = ([0, 35, 55], [10, 50, 70])
    bank_human = ([45, 25, 32], [57, 35, 48])
    bank_list = [depositbox, banker, furnace, bank_booth]
    boundaries = [bank_list[item]]
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
        x = random.randrange(x + 304 + wmin, x + 304 + whalf)  # 950,960
        print('x: ', x)
        y = random.randrange(y + 304 + hmin, y + 304 + hhalf)  # 490,500
        print('y: ', y)
        b = random.uniform(0.05, 0.1)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b)


def moneymaker_mud_runes():
    j = 0
    while j < 10:
        withdraw_mud_items()
        CraftNavToEarth()
        findrune_rock()
        earthalter()
        findrune_rock()
        move_to_portal()
        find_portal_area()
        CraftNavToBank()
        find_banker_good(3)
        deposit_secondItem()

#textdecrypt()
#Image_color()
#find_portal_area()
#CraftNavToBank()
#find_banker_good(3)
#deposit_secondItem()
moneymaker_mud_runes()
