class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  #先做兩個字串的長度檢查
            return False #如果長度不同,就先失敗了

        d = {} #空字典
        for c in s:
            if c in d:
                d[c] = d[c]+1
            else:
                d[c] = 1
        #print(d)

        for c in t:
            if c not in d: #不再統計的字典裡
                return False  #失敗
            if d[c] <=0:  #不夠
                return False  #失敗
            else:
                d[c] = d [c] -1


        return True