# *txtファイルから実数の数列を読み込み，フーリエ変換して出力する
# フーリエ変換結果の複素数列 Fk = Rk + i*Ik は，以下の通り書き出すこと
#
# ------fname_out.txt ------
# R0 I0
# R1 I0
# R2 I0
#   :
# Rk Ik
#   :
# --------------------------


import numpy as np
import sys
import math

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#数列データファイル(txt)を開く
file = open( fname_in )
fi = []

while 1 :
    line = file.readline()
    if not line :
        break
    fi.append( float(line) )
file.close()

#Fourie transform
N = len(fi)

#計算結果を入れる空の配列を作製
Rk = []
Ik = []


for k in range(N) :
    rk = 0 #実部
    ik = 0 #虚部
    
    for l in range(N):
      rk += fi[l] * math.cos(2 * math.pi * k * l / N)  
      ik += (-1) * fi[l] * math.sin(2 * math.pi * k * l / N)  
    
    rk = rk / N
    ik = ik / N
    
    Rk.append( rk )
    Ik.append( ik )

# RkとIkをテキストに書き出し
file_out = open(fname_out, 'w')
for i in range( N ) :
    file_out.write( str( Rk[i] ) + " " + str( Ik[i] ) + "\n")
file_out.close()
