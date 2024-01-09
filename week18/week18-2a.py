#瘋狂程設 　|SOIT108_Base_006 基礎題：輸入西元y年，判斷該y年是否為閏年

a=int(input())
if a%400==0: ans=1

elif a%100==0: asn=0
elif a%4==0: ans=1

else: ans=0

if ans==1: print(a,'is a leap year.')
else: print(a,'is not a leap year.')