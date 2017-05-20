#coding=utf-8  
import cv2  
import numpy as np  
  
image = cv2.imread("lena.bmp")  
 
lut = np.zeros(256, dtype = image.dtype )#创建空的查找表  
  
hist,bins = np.histogram(image.flatten(),256,[0,256])   
cdf = hist.cumsum() #计算累积直方图  
cdf_m = np.ma.masked_equal(cdf,0) #除去直方图中的0值  
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())#等同于前面介绍的lut[i] = int(255.0 *p[i])公式  
cdf = np.ma.filled(cdf_m,0).astype('uint8') #将掩模处理掉的元素补为0  
 
result = cv2.LUT(image, cdf)    
cv2.imshow("image", np.hstack([image, result]))
cv2.waitKey(0)  
cv2.destroyAllWindows()  