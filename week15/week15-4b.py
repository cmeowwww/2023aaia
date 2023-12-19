#瘋狂程設 　|SOIT108_Advance_001: 進階題：判斷平方數 

a=int(input())

ans=0
for i in range(1,1001):
	if a==i*i:
		ans=i
		
print(ans,end='')