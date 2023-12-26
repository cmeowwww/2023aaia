
#leetcode|1422maximum-score-after-splitting-a-string

#00111想知道左邊幾個0，右邊幾個1 加起來最多
#for left range(1,N-1) 0...left左邊 右邊left+1...N-1

class Solution:
    def maxScore(self, s: str) -> int:
        
        N=len(s) #字串長度
        ans=0 #迴圈前面，答案是0
        for left in range(N-1):
            #接下來測看看左邊幾個0，右邊幾個1
            now=0 #現在這次測試的值是多少

            for i in range(N): #每個字母都檢查
                if i<=left and s[i]=='0':now +=1 #左邊的0，成功
                if i>left and s[i]=='1':now +=1#右邊的1，成功
            if now>ans:ans=now #迴圈中間，更新答案
        return ans #迴圈中間，答案算出來

