a = 57
b = 76
ans = 0
for i in range(1,a+1):
  if a%i==0 and b%i==0:
    print(i,'有整數')
    ans = i
print(ans,'是最大公因數')