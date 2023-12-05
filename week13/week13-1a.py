#最大公因數 vs. 分式化簡

a = 51
b = 58

def gcd(a,b):
  if a==0: return b
  if b==0: return a
  return gcd(b, a%b)

ans=gcd(a,b)
print(a//ans, b//ans)