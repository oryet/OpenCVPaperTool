import cv2
import numpy as np
from PublicLib.public import *


# 高斯平滑处理
def GaussThreshold(img):
    img = cv2.GaussianBlur(img, (5, 5), 0)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)
    kernel = np.ones((2, 2), np.uint8)
    th3 = cv2.morphologyEx(th3, cv2.MORPH_CLOSE, kernel)
    return th3


def fitline(img):
    rows, cols = img.shape[:2]
    [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
    lefty = int((-x * vy / vx) + y)
    righty = int(((cols - x) * vy / vx) + y)
    img = cv2.line(img, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)
    return img


def imgprocc(filename):
    img = cv2.imread(filename, 0)
    if img is not None:
        img = GaussThreshold(img)

        # img = fitline(img)

        imgsave(filename, img)


def imgsave(filename, img):
    fname = os.path.basename(filename)
    fdir = os.path.dirname(filename)
    if len(fdir) > 0:
        savepath = fdir + '\\dodir\\'
        mkdir(savepath)
    else:
        savepath = ''
    cv2.imwrite(savepath + fname, img)


if __name__ == '__main__':
    imgprocc('test.jpg')