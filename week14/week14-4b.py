#瘋狂程設 　|　SOIT106_ADVANCE_009) 進階題：函數反序排列數字

a =int(input())

ans=0
while a>0:
	ans = ans*10 +a%10
	a=a//10
	
print(ans)