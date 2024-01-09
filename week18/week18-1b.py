

#瘋狂程設 　|SOIT106_BASE_004 基礎題：計程車資計算




a=int(input())
ans=100

if a>2000:
	ans+=(a-2000)//500*5
	if (a-2000)%500:ans+=5

print(ans)