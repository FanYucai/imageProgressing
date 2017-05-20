import cv2
import numpy as np
fn = "lena.bmp"
if __name__ == '__main__':
    print 'loading %s ...' % fn
    print 'processing...'
    img = cv2.imread(fn)
    w = img.shape[1]
    h = img.shape[0]
    ii = 0
    cv2.namedWindow('img')
    cv2.imshow('img',img)

    # for xi in xrange(0,w):
    #     for xj in xrange(0,h):
    #         for k in range(3):
    #             if int(img[xj,xi,k]+100) > 255:
    #                 img[xj,xi,k] = 255
    #             else:
    #                 img[xj,xi,k] = int(img[xj,xi,k]+100)            

    for xi in xrange(0,w):
        for xj in xrange(0,h):
            if int(img[xj,xi,2]+100) > 255:
                img[xj,xi,2] = 255
            else:
                img[xj,xi,2] = int(img[xj,xi,2]+100)            


        #show the process
        if xi%10==0 :print '.',
    cv2.namedWindow('img2')
    cv2.imshow('img2',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
