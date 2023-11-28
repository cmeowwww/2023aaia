a = 150000000 #把數字變很大 老大
b = 200000000 #把數字變很大 老二

c = a%b #老三
print(a,b,c)
while c!=0:  #輾轉相除法
  a = b  #老二升格為老大
  b = c  #老三升格為老二
  c = a%b #新的老三算出來
  print(a,b,c)

print(b)