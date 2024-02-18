# 画像の赤と緑チャンネルを交換する
import numpy as np
import sys
import cv2

#load image
fname_in = sys.argv[1]
fname_out = sys.argv[2]

img = cv2.imread(fname_in)


height = img.shape[0]
width = img.shape[1]
for y in range(height) :
    for x in range(width) :
        green = img[y,x,1]
        red = img[y,x,2]
        img[y,x,2] = green
        img[y,x,1] = red

#save image
cv2.imwrite(fname_out, img )
