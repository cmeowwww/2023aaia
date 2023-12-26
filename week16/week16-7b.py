#瘋狂程設 　|(SOIT108_Advance_011 進階題：秒數換算


a=int(input())

ss=a%60
mm=a//60%60
hh=a//60//60

print(f'{hh:02}:{mm:02}:{ss:02}',end='')