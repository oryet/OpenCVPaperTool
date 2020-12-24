"""
Created on 2020-12-23 17:02:12
@author: jerry
"""
import cv2, numpy as np, os
unexcpetlist = [
 '.jpg', '.png']

def excpetfile(file_name):
    for e in unexcpetlist:
        if e == file_name[-len(e):]:
            return 1

    return 0


def mkdir(path):
    path = path.strip()
    path = path.rstrip('\\')
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path, 511)
        print(path + '目录创建成功')
        return True
    return False


def dirloop(p):
    for path, dir_list, file_list in p:
        for file_name in file_list:
            if excpetfile(file_name) == 1:
                tp = os.path.join(path, file_name)
                imgprocc(tp)


def imgprocc(filename):
    img = cv2.imread(filename, 0)
    if img is not None:
        img = cv2.GaussianBlur(img, (5, 5), 0)
        th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)
        kernel = np.ones((2, 2), np.uint8)
        th3 = cv2.morphologyEx(th3, cv2.MORPH_CLOSE, kernel)
        fname = os.path.basename(filename)
        fdir = os.path.dirname(filename)
        savepath = fdir + '\\dodir\\'
        mkdir(savepath)
        cv2.imwrite(savepath + fname, th3)


if __name__ == '__main__':
    dirpath = input('请输入需要处理的文件目录:\n')
    if os.path.exists(dirpath):
        p = os.walk(dirpath)
        dirloop(p)
    else:
        print('输入目录错误\n')
# okay decompiling PaperToolMain.cpython-37.pyc
