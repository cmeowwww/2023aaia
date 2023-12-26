#瘋狂程設 　|SOIT108_Advance_014 進階題：計算級數的值

a=int(input())

ans=0
for i in range(1,2*a+1+1,2):
	ans+=i
	
print(f'f({a})={ans}',end='')