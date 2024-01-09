#瘋狂程設 　|SOIT106_BASE_012 基礎題：整數轉換為等級

a=int(input())

if a>=90: ans='A'
elif 80<=a<90: ans='B'
elif 60<=a<80: ans='C'

else:ans='F'

print(ans)