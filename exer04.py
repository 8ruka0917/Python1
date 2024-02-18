import sys

#ファイル名をコマンドライン引数から受け取る
file_in  = sys.argv[1]
file_out = sys.argv[2]

# 先ずファイルを読み込む
data_array = [] #dataを入れる配列

f = open(file_in, "r")
lines = f.readlines()
for line in lines:
    data_array.append( float(line) )

maxV1 = 0
maxV2 = 0
maxV3 = 0

maxV1 = max(data_array)
data_array.remove(maxV1)

maxV2 = max(data_array)
data_array.remove(maxV2)

maxV3 = max(data_array)
data_array.remove(maxV3)

print(maxV1, maxV2, maxV3)

#fileにmaxV minV, meanVを書き出す
f = open(file_out, "w")
f.write( str(maxV1) + " " + str(maxV2) + " " + str(maxV3) )
f.close()
