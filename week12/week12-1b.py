#瘋狂程設　|　SOIT106_BASE_005 基礎題：因數個數


a = int(input())

ans=0
for i in range(1,a+1):
	if a%i==0:
		ans +=1
		
print(ans)