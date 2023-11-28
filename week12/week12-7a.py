#瘋狂程設　|　SOIT108_Base_003 基礎題：正整數平方總和 :




a = int(input())

ans=0
for i in range(1,a+1):
	ans += i* i
	
	
print(ans,end='')