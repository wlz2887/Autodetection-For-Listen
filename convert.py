# 将路径下所有pdf转换为img

import os                                                                                                                                                                                                               
import fitz
 
def pdf_image(pdfPath, imgPath, zoom_x, zoom_y, rotation_angle, num):
    pdf = fitz.open(pdfPath)
    print(pdf.pageCount)
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
        pm = page.getPixmap(matrix = trans, alpha = False)
        pm.writePNG(imgPath + str(num)+".png")
    pdf.close()
 
pdfPath = "/lustre/home/acct-hpc/hpcwlz/Listen/Img/img/"
PDF = os.listdir(pdfPath)
cnt = 0

 
for pdf in PDF:
    if(pdf[-1]!="f"):
        continue
    pdf_image(pdfPath+pdf, "/lustre/home/acct-hpc/hpcwlz/Listen/Img/img/converted/",1,1,0,cnt)
    cnt+=1
