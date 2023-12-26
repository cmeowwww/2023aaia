#瘋狂程設 　|SOIT108_Advance_002 進階題：計算質數個數

a,b=list(map(int,input().split()))
ans=0
for N in range(a,b+1):
	bad=0
	for i in range(2,int(N**0.5)+1):
		if N%i==0: bad=1
	if bad==0: ans+=1

print(ans)