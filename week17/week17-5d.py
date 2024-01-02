#瘋狂程設　|　SOIT106_BASE_010 基礎題：找倍數

a=list(map(int,input().split()))
ans=0

for b in a:
	if b%3==0: ans += 1
	
print(ans)