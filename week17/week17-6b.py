#瘋狂程設　|　 SOIT108_Advance_012 進階題：大於漸增數列總和之最小整數

k=int(input())

total=0

for i in range(1,1001):
	total +=i
	if total>k:
		ans=i
		
		break
		
print(ans,end='')