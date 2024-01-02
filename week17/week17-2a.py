#瘋狂程設　|　SOIT107_ADVANCE_011 進階題：字串中的數字個數


a=input()
ans=0
for c in a:
	if c>='0' and c<='9':
		ans +=1
		
print(ans)