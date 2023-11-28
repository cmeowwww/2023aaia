(SOIT108_Base_005) 基礎題：輸入n (n>0)， 求n之所有因數和 

a = int(input())

ans=0
for i in range(1,a+1):
	if a%i ==0:
		ans += i


print(ans,end='')

