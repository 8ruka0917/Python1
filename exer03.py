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


maxV = 0
minV = 0
meanV = 0

maxV = max(data_array)
minV = min(data_array)
meanV = sum(data_array) / len(data_array)

print(maxV, minV, meanV)



#fileにmaxV minV, meanVを書き出す
f = open(file_out, "w")
f.write( str(maxV) + " " + str(minV) + " " + str(meanV) )
f.close()
