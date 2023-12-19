#瘋狂程設 　|SOIT108_Base_007) 基礎題：把數字倒著印出來

a=list(map(int,input().split()))

for i in range(10-1,-1,-1):
	print(a[i],end=' ')