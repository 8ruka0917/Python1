# 5x5メディアンフィルタ
import numpy as np
import sys
import cv2

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像をロード, グレースケール化, float型へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#出力画像を準備(グレースケール，float型)
img_out = np.zeros_like( img )

# img_outはゼロ初期化されているので周囲2画素分にはアクセスしないでよい
for y in range( 2, img.shape[0]-2 ) :
    for x in range( 2, img.shape[1]-2 ) :
        median = np.median(img[y-2:y+3, x-2:x+3]) #y-2からy+3まで、x-2からx+3まで
        img_out[y,x] = median

#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out, img_out )
