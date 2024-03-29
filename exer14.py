# ハーフトーン処理（ディザ法）
import numpy as np
import cv2
import sys

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像をロードしてグレースケール化
img = cv2.imread( fname_in )
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#出力画像を準備
H = img.shape[0]
W = img.shape[1]
img_out = np.zeros((H,W), np.uint8)



#ハーフトーン画像を作成計算
#ディザパターンは次のような２次元配列で表現できます
mask = np.array([[15,7,13,1], [4,11,5,9], [12,3,14,6], [0,8,2,10]])

for y in range( H ) :
    for x in range( W ) :
        I = img[y,x] * 16 / 255
        
        if mask[y%4,x%4] <= I:
            img_out[y,x] = 255
        elif mask[y%4,x%4] > I:
            img_out[y,x] = 0
    
#出力
cv2.imwrite( fname_out, img_out)
