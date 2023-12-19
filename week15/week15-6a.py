#瘋狂程設 　|SOIT108_Base_011 基礎題：平面兩座標的面積

a,b,c,d=list(map(int,input().split()))

ans=(a-c)*(b-d)

if ans<0:ans=-ans
print(ans,end='')