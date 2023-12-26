#瘋狂程設 　|SOIT108_Advance_002B 進階題：三數組合

a=list(map(int,input().split()))

a.sort()

ans=a[0]+a[1]*10+a[2]*100+1
print(ans,end='')