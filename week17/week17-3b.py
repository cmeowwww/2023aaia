#瘋狂程設　|　SOIT107_Base_011 基礎題：整數二元四則運算



a,c,b=input().split()

a=int(a)
b=int(b)

if c=='+': ans=a+b
if c=='-': ans=a-b
if c=='*': ans=a*b
if c=='/': ans=a//b

print(ans,end='')