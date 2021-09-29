#!/usr/bin/env/python
#-*- coding:utf8 -*-
# Power by Liuzhen 2021-09-29 15:10:59

import os
import fitz
from convert import pdf_image
from cut import cut_image
from predict import predict

    
def convert(pdfPath, imgPath):
    pdf_image(pdfPath, imgPath,1,1,0) # pdf转jpg
    cut_image(imgPath+".jpg")
 

def main():
    convert("../20210301谢胤.pdf","../rua")
    predict("../left_rua.jpg")

if __name__ == '__main__':
    main()
