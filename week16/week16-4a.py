#瘋狂程設 　|:SOIT107_ADVANCE_014 進階題：奇數之和

N=int(input())
ans=0

for i in range(1,N+1):
	if i%2==1: ans+=i
	
print(ans,end='')