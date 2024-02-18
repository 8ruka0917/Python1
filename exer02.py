import sys

#1つの数値をコマンドライン引数から受け取る
N = int(sys.argv[1])

for i in range(1, N+1):
    
    if i % 3 == 0 and i % 5 != 0:
        print("hoge")
    elif i % 5 == 0 and i % 3 != 0:
        print("fuga")
    elif i % 3 == 0 and i % 5 == 0:
        print("hogefuga")
    else:
        print(i)
    
