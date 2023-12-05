#瘋狂程設 | SOIT106_ADVANCE_003 進階題：讀入整數反序列印


a=list(map(int,input().split()))

N =len(a)-1

for i in range(N-1,-1,-1):
	print(a[i],end=' ')
	
print()