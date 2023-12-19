#瘋狂程設 　|SOIT108_Advance_008 進階題：10數排序，從大到小排好 :

a=list(map(int,input().split()))

a.sort()

for i in range(10-1,-1,-1):
	print(a[i],end=' ')