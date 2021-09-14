import cv2 as cv                                                                                                                                                                                                        
import numpy as np
import os

#img = cv.imread('./2.png') # 读取图像 准备筛选颜色

#cutted = img[120:350,50:520]
#cv.imwrite('./cutted_2.png',cutted)

ret = True

def seperate_color(frame):  # 分离颜色 后来没用上
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # 转换hsv格式
    lower_hsv = np.array([0,43,46])
    high_hsv = np.array([10,255,255])
    mask = cv.inRange(hsv, lowerb = lower_hsv, upperb = high_hsv)
    return mask

Images = os.listdir('/lustre/home/acct-hpc/hpcwlz/Listen/Img/img/converted')
# print('../Left/'+Images[2])

for image in Images:
    if(image[-3:]!='png'):  # 只转换图片文件
        continue
    path = '../'+image
    img = cv.imread(path)
    cutted = img[120:350,50:520]
    right = cutted[18:218,16:216]
    left = cutted[18:218,253:453]
    cv.resize(right,[512,512])
    cv.resize(left,[512,512])
    cv.imwrite('../Left/'+image,left)
    cv.imwrite('../Right/'+image,right)
