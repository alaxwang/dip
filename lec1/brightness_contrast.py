#!/bin/python
import cv2
import numpy as np


img = cv2.imread('parrot.jpg')
gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dimg = np.float32(gimg);
dimg = dimg / 255;

scale = 1.2
scale_img = dimg * scale

gamma = 1.5
gamma_img = pow(dimg,gamma)


cv2.imshow("original image", gimg)
cv2.imshow("scale image", scale_img)
cv2.imshow("gamma image", gamma_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
