#瘋狂程設 　|SOIT107_ADVANCE_010 進階題：判斷迴文


a=input()
N=len(a)
bad=0
for i in range(N):
	if a[i] !=a[N-1-i]:
		bad=1
if bad==0: print('YES',end='')
else: print('NO',end='')