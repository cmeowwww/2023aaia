#瘋狂程設 | SOIT106_ADVANCE_006 進階題：漸增數列相加 

a =int(input())

ans=0

for i in range(1,a):
	ans += i * (i+1)



print(ans)