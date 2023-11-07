a = [9,8,7,6,5,4,3,2,1,0]
N = len(a)
print(a) #使用前
for k in range(N):

  for i in range(N-1):
      if a[i+1] < a[i]:
        a[i], a[i+1] = a[i+1], a[i]
  print(a) #使用後