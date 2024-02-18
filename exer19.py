# 画像の離散フーリエ変換
#
# 画像のフーリエ変換結果は，Fuv = Ruv + i * Iuv と複素数画像となる
# 計算結果の Ruv と Iuv をそれぞれ画像として書き出す


import numpy as np
import sys
import cv2
import math

fname_in      = sys.argv[1]
fname_out_Rvu = sys.argv[2]
fname_out_Ivu = sys.argv[3]


#画像をロード, グレースケール化, float型へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = np.float64(img)


#出力画像を準備(グレースケール，float型)
Rvu = np.zeros_like( img )
Ivu = np.zeros_like( img )

H = img.shape[0]
W = img.shape[1]


for v in range( H ) :
    for u in range( W ) :
        Rvu[v,u] = 0
        Ivu[v,u] = 0
    
        for y in range( H ) :
            for x in range( W ) :
                Rvu[v,u] += img[y,x] * (math.cos(2*math.pi*x*u/W)*math.cos(2*math.pi*y*v/H)-math.sin(2*math.pi*x*u/W)*math.sin(2*math.pi*y*v/H)) #オイラーの公式を用いて
                Ivu[v,u] += (-1) * img[y,x] * (math.sin(2*math.pi*y*v/H)*math.cos(2*math.pi*x*u/W)+math.cos(2*math.pi*y*v/H)*math.sin(2*math.pi*x*u/W))  #オイラーの公式を用いて
        Rvu[v,u] = Rvu[v,u] / W * H
        Ivu[v,u] = Ivu[v,u] / W * H

# 直流成分を0にする（他の画素に比べてここだけ非常に大きな値を持ち、正規化がうまくいかないため場当たり的な方法）
Rvu[0,0] = 0


# (値 – 最小値)/(最大値-最小値) * 255 という変換を施すことで，値の範囲を[0,255]にする
# RvuとIvuをそれぞれ個別に正規化する
Rvu_max = np.max(Rvu)
Rvu_min = np.min(Rvu)
Ivu_max = np.max(Ivu)
Ivu_min = np.min(Ivu)

for v in range( H ) :
    for u in range( W ) :
        Rvu[v,u] = (Rvu[v,u]-Rvu_min) / (Rvu_max-Rvu_min) * 255
        Ivu[v,u] = (Ivu[v,u]-Ivu_min) / (Ivu_max-Ivu_min) * 255


#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out_Rvu, np.uint8(Rvu))
cv2.imwrite(fname_out_Ivu, np.uint8(Ivu))
