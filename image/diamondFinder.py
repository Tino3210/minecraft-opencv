import cv2 as cv
import imutils
from time import time
from capture import WindowCapture
from diamondFindecConst import *

class DiamondFinder():
    def __init__(self, ):
        self.x = -1
        self.y = -1
        self.wincap = WindowCapture('Minecraft 1.18.2 - Singleplayer')
        
    def isDiamond(self):
        screenshot = self.wincap.get_screenshot()
        hsv = cv.cvtColor(cv.UMat(screenshot), cv.COLOR_BGR2HSV)
        mask_diamond = cv.inRange(hsv, lower_range_diamond, upper_range_diamond)
        mask_lava = cv.inRange(hsv, lower_range_lava, upper_range_lava)
        
        mask = cv.imread('mask_diamond.png',0)
        dim = (screenshot.shape[1],screenshot.shape[0])
        mask_hotbar = cv.resize(mask,dim)
        res = cv.bitwise_and(mask_diamond,mask_hotbar)
        
        kernel = np.ones((7,7), np.uint8)
        
        res = cv.dilate(res, kernel, iterations=10)
        res = cv.erode(res, kernel, iterations=10)
        
        contours= cv.findContours(res, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        
        
        contours = imutils.grab_contours(contours)

        try:
            for c in contours:
                # compute the center of the contour
                M = cv.moments(c)
                self.x = int(M["m10"] / M["m00"])
                self.y = int(M["m01"] / M["m00"])
        except:
            pass
        
        if self.x != -1 and self.y != -1:
            return True
        return False
    
    def getPosition(self):
        return (self.x, self.y)