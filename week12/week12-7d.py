#瘋狂程設　|　SOIT108_Base_013 基礎題：計算一組任意數目的整數的總和 :

a =list(map(int,input().split()))


ans=0
for i in a:
	if i >0: ans += i
	
print(ans,end='')