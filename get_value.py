import numpy as np
  
data = np.loadtxt('./result.txt')
data = data.T # 第一行x坐标 第二行y坐标 第三行类别
  
Range =np.array([13, 51.5, 102.5, 154, 206, 244.5, 270, 296, 322]) * 200 / 370 # 切一半
  
Range2Freq = {1:125, 2:250, 3:500, 4:1000, 5:2000, 6:3000, 7:4000,8:6000,9:8000} # 范围与频率的对照
  
index = Range.searchsorted(data[0])
data[0] = np.array([Range2Freq[key] for key in index]) # 通过范围确定所属的频率
data[1] = data[1] * 150 / 200 - 20  # 通过scaling获取db值                                                                                                                                                               
print(data.T)
