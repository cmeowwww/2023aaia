class Solution:
    def isPowerOfThree(self, n: int) -> bool:
      
        if n<=0:  #遇到負的、遇到0也會失敗
            return False

        while n>1:
            if n %3 !=0:   #餘數不是0就失敗了
                return False
            else:
                n = n //3  #要變小

        return True