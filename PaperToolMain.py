# -*- coding: utf-8 -*-
"""
Created on 2020-12-23 17:02:12
@author: jerry
"""
import cv2
import numpy as np
import os

unexcpetlist = ['.jpg', '.png']


def excpetfile(file_name):
    for e in unexcpetlist:
        if e == file_name[-len(e):]:  # 筛选.log
            return 1
    return 0

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录,创建目录操作函数
        '''
        os.mkdir(path)与os.makedirs(path)的区别是,当父目录不存在的时候os.mkdir(path)不会创建，os.makedirs(path)则会创建父目录
        '''
        #此处路径最好使用utf-8解码，否则在磁盘中可能会出现乱码的情况
        os.makedirs(path, 0o777)
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path+' 目录已存在')
        return False

def dirloop(p):
    for path, dir_list, file_list in p:
        for file_name in file_list:
            # 特殊文件不用处理
            if (excpetfile(file_name) == 1):
                tp = os.path.join(path, file_name)
                imgprocc(tp)

def imgprocc(filename):
    img = cv2.imread(filename, 0)
    # print(img.shape)

    # 中值滤波
    # img = cv2.medianBlur(img,5)

    # 0 是指根据窗口大小（ 5,5 ）来计算高斯函数标准差
    img = cv2.GaussianBlur(img, (5, 5), 0)

    # ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    # 11 为 Block size, 2 为 C 值
    # th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,2)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)

    # 开运算
    kernel = np.ones((2, 2), np.uint8)
    # th3 = cv2.morphologyEx(th3, cv2.MORPH_OPEN, kernel)
    th3 = cv2.morphologyEx(th3, cv2.MORPH_CLOSE, kernel)
    fname = os.path.basename(filename)
    fdir = os.path.dirname(filename)
    savepath = fdir + '\\dodir\\'
    mkdir(savepath)
    cv2.imwrite(savepath + fname, th3)



if __name__ == '__main__':
    # dirpath = r'F:/Source/Python/OpenCVPaperTool/Pic/'
    dirpath = input("请输入需要处理的文件目录:\n")
    if os.path.exists(dirpath):
        p = os.walk(dirpath)
        dirloop(p)
    else:
        print("输入的目录不存在！\n")
