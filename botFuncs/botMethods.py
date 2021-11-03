import pyautogui
from random import randint

class botObj:
    # TODO: write a method to retrive the screenshot var from a given image object
    def __init__(self,imageObjDict) -> None:
        # construct the bot object by passing it a dict of image objects,
        # who's keys are strings of that objects name,
        self.images = imageObjDict

    def returnImgObj(self, image):
        return self.images[image].findImage()

    def changeImgFile(self, image):
        return self.images[image].searchFObj('newImg', newImg=image+'1')
        
    def clickImage(self,screenShot):
        #TODO: screenshot will be unpacked from the image dictionary.
        # get all pyauto cords from screenshot if it was found
        if screenShot:
            # get raw center x,y cords for detection
            Location = pyautogui.center(screenShot)
            self.X, self.Y = Location  
            pyautogui.moveTo(self.X, self.Y, 0.1)
            pyautogui.doubleClick()

            return self.X, self.Y
        else:
            print('nothing found to click')

    def rightClickimage(self,screenShot):
        if screenShot:
            Location = pyautogui.center(screenShot)
            self.X, self.Y = Location
            pyautogui.moveTo(self.X, self.Y, 0.1)
            pyautogui.rightClick()

            return self.X, self.Y

    @staticmethod
    def _random_coordinate(x_lower, y_lower, x_range, y_range):
        #  Moves cursor to random location still above the object to be clicked
        x = randint(x_lower, x_lower + x_range)
        y = randint(y_lower, y_lower + y_range)
            # array of the click vars
            # randClick = [screenShot.left, screenShot.top, screenShot.width,
            #              screenShot.height]
            # click on rand location in that area
            # cords = self._random_coordinate(randClick[0], randClick[1], round(randClick[2]*0.7), round(randClick[3]*0.7))
            # self.X, self.Y = cords
        return x, y
