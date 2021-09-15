# Autodetection-For-Listen
流程如下：
- [输入一张图片转为img，根据像素点切分左右耳的正方形区域](./预处理)
- [手动标记符号位置类别信息，输入Faster-RCNN模型训练](./训练)
- 将两个图片分别输入模型的predict.py得到result.txt以及图像
- [读取result.txt的结果，输入get_value.py获得频率和分贝值](./get_value.py)
