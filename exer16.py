# ハーフトーン処理(誤差拡散法)
import numpy as np
import cv2
import sys

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像を読み込み、グレースケール化し、float型に変換
img = cv2.imread( fname_in  )
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = np.float64(img)


#出力画像を準備
H = img.shape[0]
W = img.shape[1]
img_out = np.zeros((H,W), np.uint8)



#誤差拡散法の計算
for y in range(H)  :
	for x in range( W)  :
                I = img[y,x]
                if 127 < I:
                        img_out[y,x] = 255
                        e = I - 255
                else:
                        img_out[y,x] = 0
                        e = I - 0
                
                if x + 1 < W:
                        img[y,x+1] += 5 / 16 * e
                if x - 1 >= 0 and y + 1 < H:
                        img[y+1,x-1] += 3 / 16 * e
                if y + 1 < H:
                        img[y+1,x] += 5 / 16 * e
                if x + 1 < W and y + 1 < H:
                        img[y+1,x+1] += 3 / 16 * e
        
cv2.imwrite( fname_out, img_out)
