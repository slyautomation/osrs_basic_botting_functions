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
    myScreenshot.save(r"C:\Users\MMH\PycharmProjects\osrs-botting\screen.png")
    png = 'screen.png'
    im = Image.open(png)  # uses PIL library to open image in memory
    left = 100
    top = 200
    right = 600
    bottom = 600

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('screenshot.png')  # saves new cropped image

def cropImage():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"C:\Users\MMH\PycharmProjects\osrs-botting\screen.png")
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
    myScreenshot.save(r"C:\Users\MMH\PycharmProjects\osrs-botting\screen.png")
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

    b = random.uniform(0.18, 0.622)
    x = random.randrange(797, 802)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(80, 85)  # y = random.randrange(50, 60)
    print('y: ', y)
    c = random.uniform(22, 24)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('1st step to bank')

    b = random.uniform(0.18, 0.622)
    x = random.randrange(797, 805)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(82, 88)  # y = random.randrange(50, 60)
    print('y: ', y)
    c = random.uniform(10.7, 11.1)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('2nd step to bank')

    b = random.uniform(0.18, 0.622)
    x = random.randrange(797, 805)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(120, 125)  # y = random.randrange(50, 60)
    print('y: ', y)
    c = random.uniform(10.2, 10.77)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('3rd step to bank')

    b = random.uniform(0.18, 0.622)
    x = random.randrange(797, 805)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(120, 125)  # y = random.randrange(50, 60)
    print('y: ', y)
    c = random.uniform(10.2, 10.77)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('3rd step to bank')

    b = random.uniform(0.18, 0.622)
    x = random.randrange(797, 805)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(115, 120)  # y = random.randrange(50, 60)
    print('y: ', y)
    c = random.uniform(10.2, 10.77)
    pyautogui.click(x, y, 1, duration=b, button='left')
    time.sleep(c)
    print('3rd step to bank')


def CraftNavToFire():

    c = random.uniform(10, 11)
    x = random.randrange(1, 5)  # x = random.randrange(1795, 1800)
    print('x: ', x)
    y = random.randrange(1, 5)  # y = random.randrange(50, 60)
    print('y: ', y)
    Image_Rec_clicker('fire_alter_mark1.png', 'To Alter spot', x, y, 0.8, 'left')
    time.sleep(c)
    print('1st step to fire alter')


    b = random.uniform(0.18, 0.622)
    x = random.randrange(-50, -45)  #
    print('x: ', x)
    y = random.randrange(-25, -20)  #
    print('y: ', y)
    c = random.uniform(11.4, 11.8)
    Image_Rec_clicker('fire_alter_mark2.png', 'To Alter spot', x, y, 0.8, 'left')
    time.sleep(c)
    print('2nd step')

    b = random.uniform(0.18, 0.622)
    x = random.randrange(-20, -15)  #
    print('x: ', x)
    y = random.randrange(40, 45)  #
    print('y: ', y)
    c = random.uniform(11.4, 11.8)
    Image_Rec_clicker('fire_alter_mark3.png', 'To Alter spot', x, y, 0.8, 'left')
    time.sleep(c)
    print('3rd step')


def firealter():
    print('rune crafting at alter')
    b = random.uniform(0.18, 0.622)
    x = random.randrange(775, 780)  #
    print('x: ', x)
    y = random.randrange(155, 160)  #
    print('y: ', y)
    c = random.uniform(9.2, 11.2)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.1, 0.23)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)
def find_banker():
    cropImage()
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
    banker_window = ([103, 86, 65], [145, 133, 128])
    banker = ([130, 140, 145], [150, 160, 165])
    furnace = ([25, 25, 30], [38, 38, 50])
    boundaries = [
        banker
    ]
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
        # show the images
        ret, thresh = cv2.threshold(mask, 40, 255, 0)
        #cv2.imshow("images", np.hstack([image, output]))
        #cv2.waitKey(0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) != 0:
            # draw in blue the contours that were founded
            # cv2.drawContours(output, contours, -1, 255, 3)

            # find the biggest countour (c) by the area
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)

            # draw the biggest contour (c) in green
            # cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)

            c = random.uniform(3.5, 4.7)
            b = random.uniform(0.25, 0.65)
            x = random.randrange(x + 345, x + 350)  # 950,960
            y = random.randrange(y + 355, y + 360)  # 490,500
            pyautogui.moveTo(x, y, duration=b)
            b = random.uniform(0.1, 0.19)
            pyautogui.click(duration=b)
            time.sleep(c)

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

CraftNavToBank()
#CraftNavToFire()
#firealter()