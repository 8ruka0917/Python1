# モザイク画像の作成
# 第2引数はモザイクのサイズ
import numpy as np
import sys
import cv2

#ファイル名と窓サイズRをコマンドライン引数より取得
fname_in  = sys.argv[1]
R         = int(sys.argv[2])
fname_out = sys.argv[3]

#画像をロードしfloat型へ変換
img = cv2.imread(fname_in)
img = np.float64(img)



#モザイク画像の作成
for y in range( int( img.shape[0] / R + 1) ) :
    for x in range( int( img.shape[1] / R + 1) ) :
        rectR = img[y*R:(y+1)*R, x*R:(x+1)*R, 2]
        rectG = img[y*R:(y+1)*R, x*R:(x+1)*R, 1]
        rectB = img[y*R:(y+1)*R, x*R:(x+1)*R, 0]
        
        meanR = np.mean(rectR)
        meanG = np.mean(rectG)
        meanB = np.mean(rectB)
        
        img[y*R:(y+1)*R, x*R:(x+1)*R, 2] = meanR
        img[y*R:(y+1)*R, x*R:(x+1)*R, 1] = meanG
        img[y*R:(y+1)*R, x*R:(x+1)*R, 0] = meanB
        
#最後に画像を出力して終了
cv2.imwrite(fname_out, np.uint8( img) )
