a =input().split()
for i in range(100):
    a[i] = int(a[i])
    
N = len(a)
for k in range(N):    
    for i in range(N-1):
        if a [i+1] < a[i]:
            a[i],a[i+1] = a[i+1],a[i]
            
for i in range(N):
    print(a[i])