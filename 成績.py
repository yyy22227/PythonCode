S1 = int(input("請輸入第一次成績"))
S2 = int(input("請輸入第二次成績"))
S3 = int(input("請輸入第三次成績"))
Sa = [S1, S2, S3]
Sa.sort()
S = Sa[2]*0.5 + Sa[1]*0.3 + Sa[0]*0.2
print(S)
