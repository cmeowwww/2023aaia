# 瘋狂程設 　|　SOIT106_ADVANCE_010 進階題：計算陣列的平方值 

a=list(map(int,input().split()))

N=len(a)
for i in range(1,N):
	print(a[i]*a[i],end=',');
	
print()
	