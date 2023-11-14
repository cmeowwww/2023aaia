a = input()
a = a.split()
for i in range(100):
    a[i] = int(a[i])


for i in range(100-1,-1,-1):
    print(a[i])