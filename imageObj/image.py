import pyautogui
from imageObj import findFile
class imageObj:

    def __init__(self, imageName, trustLevel, windowSize, *args, gray=False):
        # here i am defining each piece that makes up the image location argument
        self.trustLevel = trustLevel
        self.imageName = imageName
        self.windowSize = windowSize
        self.gray = gray
        self.X = 0
        self.Y = 0
        self.screenShot = False

    def findImage(self):
        # This method constructs the locateOnScreen method 
        # storing the return value as screenshot
        if not self.screenShot:
            print('no loc for obj', self.imageName, 'using win region')
            self.screenShot = self._create_Argument(self.imageName, self.trustLevel, self.gray, self.windowSize)

        else:
            print('using objLoc', self.imageName)
            objRegion = [self.screenShot.left + 10,
                         self.screenShot.top + 10,
                         self.screenShot.width + 5,
                         self.screenShot.height + 5]
            gray = True
            self.screenShot = self._create_Argument(self.imageName, self.trustLevel, gray, objRegion)
        return self.screenShot

    def searchFObj(self, objMode, ratio=1.05, newImg=''):
        # a method to lower the trust level without doing object.trustLevel = num
        # instead call object.lowerTrustLevel() ratio can be changed,
        # but becomes useless above 1.05
        if objMode == 'lowerTru':
            self.trustLevel = round(self.trustLevel / ratio, 2)
        # change what img is used for obj detect
        elif objMode == 'newImg':
            self.imageName = findFile.getFile(newImg)
            pass

    @staticmethod
    def _create_Argument(first, second, third, forth):
        # finally this function constructs the locateOnScreen function,
        # without storing its value till the findImage method is called
        return pyautogui.locateOnScreen(first, confidence=second, grayscale=third, region=(forth[0],
                                                                                           forth[1],
                                                                                           forth[2],
                                                                                           forth[3]))
