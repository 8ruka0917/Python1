# 画像の赤と緑チャンネルを交換する
import numpy as np
import sys
import cv2

#load image
img_size  = int(sys.argv[1])
fname_out = sys.argv[2]

#真っ黒な画像を作成
img = np.zeros((img_size, img_size), dtype = np.uint8)

height = img.shape[0]
width = img.shape[1]
a = 1
b = 1
count = 0
plus = 0
            
for y in range(height) :
    number = int(a)  #numberがインデックス
    for x in range(width) :
        count = 0 #公約数のカウント
        for i in range(1,number+1) :
            if number % i == 0:
                count = count + 1
        if count == 2:
            img[y,x] = 255
        plus = plus + 1 #隣のインデックスに足す値
        number = number + plus #隣のインデックスに足してインデックスの数を増やす 
    plus = b #列に足す数の初期値(=2)
    b = b + 1  #列番号を増やす
    a = a + b  #前の列の最初のインデックス＋列番号
    
#save image
cv2.imwrite(fname_out, img )
