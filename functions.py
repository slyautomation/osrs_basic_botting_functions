import numpy as np
import cv2
import pyautogui
import random
import time
from PIL import Image
import os


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def Image_to_Text(preprocess, image):
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
    text = pytesseract.image_to_string(Image.open(filename), config='--psm 7')
    os.remove(filename)
    print(text)
    return text

def screen_Image(left=0, top=0, right=0, bottom=0,name='screenshot.png'):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"C:\Users\i7 8700\PycharmProjects\osrs_basic_botting_functions\screenshot.png")
    if left != 0 and top != 0 and right != 0 and bottom != 0:
        png = 'screenshot.png'
        im = Image.open(png)  # uses PIL library to open image in memory
        im = im.crop((left, top, right, bottom))  # defines crop points
        im.save(name)  # saves new cropped image


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

def find_Object(item):
    screen_Image()
    image = cv2.imread('screenshot.png')

    # define the list of boundaries
    # B, G, R

    red = ([0, 0, 180], [80, 80, 255]) # 0 Index
    green = ([0, 180, 0], [80, 255, 80]) # 1 Index
    amber = ([0, 200, 200], [60, 255, 255]) # 2 Index
    pickup_high = ([250, 0, 167], [255, 5, 172]) # 3 Index
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
        y = random.randrange(y + 5, y + max(h - 5, 6)) # 490,500
        print('y: ', y)
        b = random.uniform(0.2, 0.4)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b)

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

def Image_Rec_single(image, event, iheight, iwidth, threshold, clicker, ispace=20, cropx=0, cropy=0):
    global icoord
    global iflag

    screen_Image(name='screen_clicker.png')
    img_rgb = cv2.imread(r"screen_clicker.png")
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

def image_Rec_clicker(image, event, iheight, iwidth, threshold, clicker, ispace=20, cropx=0, cropy=0):
    global icoord
    global iflag
    screen_Image(name='screenshot.png')
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
            b = random.uniform(0.2, 0.7)
            pyautogui.moveTo(icoord, duration=b)
            b = random.uniform(0.1, 0.3)
            pyautogui.click(icoord, duration=b, button=clicker)
    return iflag

def Image_count(object):
    counter = 0
    screen_Image(name='screenshot.png')
    img_rgb = cv2.imread('screenshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(object,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
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

def random_breaks(minsec,maxsec):
    e = random.uniform(minsec,maxsec)
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


#findarea(1)