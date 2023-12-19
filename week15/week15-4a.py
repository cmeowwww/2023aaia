#瘋狂程設 　|SOIT108_Advance_001: 進階題：判斷平方數 


a=int(input())

import math
b=int(math.sqrt(a))

if a==b*b:
	print(b,end='')
else:
	print(0,end='')