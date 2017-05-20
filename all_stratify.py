#coding=utf-8  

import cv2
import numpy as np
fn = "lena.bmp"

def stratify(lv, p):
    lv -= 1
    interval = 255/lv
    left = p/interval
    right = left+1
    if right*interval-p > p-left*interval:
        return left*interval
    else:
        return right*interval

if __name__ == '__main__':
    print 'loading %s ...' % fn
    print 'processing...'
    img = cv2.imread(fn)
    w = img.shape[1]
    h = img.shape[0]
    img64 = np.zeros(img.shape)
    img8 = np.zeros(img.shape)
    img2 = np.zeros(img.shape)

    for xi in xrange(0,w):
        for xj in xrange(0,h):
            for k in range(3):
                img[xj,xi,k] = stratify(2, int(img[xj,xi,k]))   

    lut = np.zeros(256, dtype = img.dtype )#创建空的查找表  
  
    hist,bins = np.histogram(img.flatten(),256,[0,256])   
    cdf = hist.cumsum() #计算累积直方图  
    cdf_m = np.ma.masked_equal(cdf,0) #除去直方图中的0值  
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())#等同于前面介绍的lut[i] = int(255.0 *p[i])公式  
    cdf = np.ma.filled(cdf_m,0).astype('uint8') #将掩模处理掉的元素补为0  
     
    result = cv2.LUT(img, cdf)            

    cv2.imshow('img', result)
    cv2.waitKey()
    cv2.destroyAllWindows()
