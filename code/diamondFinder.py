import cv2 as cv
import imutils
from capture import WindowCapture
from diamondFindecConst import *


class DiamondFinder():
    def __init__(self, name='Minecraft 1.18.2 - Singleplayer'):
        self.wincap = WindowCapture(name)

    def capture(self):
        self.image = self.wincap.get_screenshot()
        self.dim = (self.image.shape[1], self.image.shape[0])

    def is_diamond(self):
        self.x_diamond = -1
        self.y_diamond = -1
        screenshot = self.image
        hsv = cv.cvtColor(cv.UMat(screenshot), cv.COLOR_BGR2HSV)
        mask_diamond = cv.inRange(
            hsv, lower_range_diamond, upper_range_diamond)

        mask = cv.imread('code/image/mask_diamond.png', 0)
        dim = (screenshot.shape[1], screenshot.shape[0])
        mask_hotbar = cv.resize(mask, dim)
        res = cv.bitwise_and(mask_diamond, mask_hotbar)

        kernel = np.ones((7, 7), np.uint8)
        res = cv.dilate(res, kernel, iterations=10)
        res = cv.erode(res, kernel, iterations=10)

        contours = cv.findContours(
            res, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        contours = imutils.grab_contours(contours)

        try:
            for c in contours:
                # compute the center of the contour
                M = cv.moments(c)
                self.x_diamond = int(M["m10"] / M["m00"])
                self.y_diamond = int(M["m01"] / M["m00"])
        except:
            pass

        if self.x_diamond != -1 and self.y_diamond != -1:
            return True
        return False

    def is_lava(self):
        self.x_lava = -1
        self.y_lava = -1
        screenshot = self.image
        hsv = cv.cvtColor(cv.UMat(screenshot), cv.COLOR_BGR2HSV)
        mask_lava = cv.inRange(hsv, lower_range_lava, upper_range_lava)

        kernel = np.ones((7, 7), np.uint8)

        mask_lava = cv.erode(mask_lava, kernel, iterations=7)

        contours = cv.findContours(
            mask_lava, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)

        try:
            for c in contours:
                # compute the center of the contour
                M = cv.moments(c)
                self.x_lava = int(M["m10"] / M["m00"])
                self.y_lava = int(M["m01"] / M["m00"])
        except:
            pass

        if self.x_lava != -1 and self.y_lava != -1:
            return True
        return False

    def get_dimension(self):
        return self.dim

    def get_position_diamond(self):
        return ((int)(-self.dim[0]/2 + self.x_diamond), (int)(-self.dim[1]/2 + self.y_diamond))

    def get_position_lava(self):
        return (self.x_lava, self.y_lava)
