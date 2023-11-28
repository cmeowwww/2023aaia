
#瘋狂程設　|　M90H020 最大公因數(2數)


def gcd(a,b):
  if a==0: return b
  if b==0: return a
  return gcd(b, a%b)

a ,b = list(map(int,input().split()))

if a<0:a = -a
if b<0: b =-b


print(gcd (a,b),end='')