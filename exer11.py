# 画像に縦方向sobel filterをかける
#  - 負値となる画素は-1倍，
#  - 255を超える画素には，オーバーフローを避けるため255を代入
import numpy as np
import sys
import cv2

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像をロード, グレースケール化, float型へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = np.float64(img)

#出力画像を準備(グレースケール，float型)
img_out = np.zeros_like( img )

for y in range( 1, img.shape[0]-1 ) :
    for x in range( 1, img.shape[1]-1 ) :
        img_out[y,x] = 0
        #gaussian filterとほとんど同じ
        #負値のときの処理と255を超えたときの処理を忘れずに！
        #負値でかつ絶対値が255を超える画素にも対応できるように
        sum = img[y-1,x-1]*1 + img[y-1,x]*2 + img[y-1,x+1]*1 + img[y,x-1]*0 + img[y,x]*0 + img[y,x+1]*0 + img[y+1,x-1]*(-1) + img[y+1,x]*(-2) + img[y+1,x+1]*(-1)
        
        if sum < 0:
            sum = sum*(-1)
        if 255 < sum:
            sum = 255
        img_out[y,x] = sum


#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out, np.uint8( img_out) )
