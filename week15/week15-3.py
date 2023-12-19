#瘋狂程設 　|SOIT107_ADVANCE_004 進階題：最大公因數gcd



a,b=list(map(int,input().split()))

def gcd(a,b):
	if a==0: return b
	if b==0: return a
	return gcd(b,a%b)
	
print('Enter two integers: ')
print('The greatest common divisor of',a,'and',b,'is',gcd(a,b))
