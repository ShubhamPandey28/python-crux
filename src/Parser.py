import cv2 
import numpy as np

class Parser(object):

    def __init__(self):
        self.img = None
        self.imgcpy = None
        self.cu = None
        self.cp = None
        self.ru = 0
        self.rp = 0

    def fit(self,imagePath):

        self.img = cv2.imread(imagePath,cv2.IMGREAD_GRAYSCALE)
        self.imgcpy = self.img.copy()
    
    def getpenumbra(self):

        ret, thresh = cv2.threshold(self.img, 200, 255, cv2.THRESH_BINARY_INV)
        ero = cv2.erode(thresh, np.ones((5,5)))
        dil = cv2.dilate(ero, np.ones((5,5)))
        img, contours, hierarchy = cv2.findContours(dil, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        for cnt in contours:
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radius = int(radius)
            self.cp = center
        self.rp = radius
        
    def getumbra(self):

        ret, thresh = cv2.threshold(self.img, 70, 255, cv2.THRESH_BINARY_INV)
        ero = cv2.erode(thresh, np.ones((5,5)))
        dil = cv2.dilate(ero, np.ones((5,5)))
        img, contours, hierarchy = cv2.findContours(dil, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        for cnt in contours:
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radius = int(radius)
            self.cu = center
        self.ru = radius    

def imshow(img):
    cv2.imshow("image",img)
    cv2.waitKey(0)
        