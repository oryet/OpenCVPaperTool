"""
Created on 2020-12-23 17:02:12
@author: jerry
"""
from OpenCVPaperTool.ImgProc import *

unexcpetlist = [
 '.jpg', '.png']

def excpetfile(file_name):
    for e in unexcpetlist:
        if e == file_name[-len(e):]:
            return 1
    return 0


def dirloop(p):
    for path, dir_list, file_list in p:
        for file_name in file_list:
            if excpetfile(file_name) == 1:
                tp = os.path.join(path, file_name)
                imgprocc(tp)


if __name__ == '__main__':
    dirpath = input('请输入需要处理的文件目录:\n')
    if os.path.exists(dirpath):
        p = os.walk(dirpath)
        dirloop(p)
    else:
        print('输入目录错误\n')
