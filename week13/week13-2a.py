#Fibonacci 費式數列

a =[1, 1]
for i in range(2,100):
  a.append(a[i-1]+a[i-2])
print(a)