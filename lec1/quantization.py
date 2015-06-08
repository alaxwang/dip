#!/bin/python
import cv2

img = cv2.imread('face.jpg')
gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Image")
for i in range(1,9):
  num_of_level = pow(2,i)
  level_gap = 256 / num_of_level
  new_img = (gimg / level_gap) * level_gap 
  cv2.imshow("Image", new_img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

