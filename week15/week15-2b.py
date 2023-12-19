#瘋狂程設 　|SOIT107_ADVANCE_003 進階題：計算一列整數的總和 


ans=0

while True:
	a=input('Enter an integer ( 999 to end ): \n')
	a=int(a)
	if a ==999:
		break
	ans+=a
	
print('The total is:', ans,end='')
