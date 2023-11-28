#瘋狂程設　|　SOIT108_Base_003A 進階題：兩數之間的3倍數總和 : 


a,b =list(map(int,input().split()))

ans=0
for i in range(a,b+1):
	if i%3==0: ans += i
	
print(ans,end='')