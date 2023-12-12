#leetcode | 1464. Maximum Product of Two Elements in an Array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=0

        N=len(nums)
        for i in range(N):
            for j in range(i+1,N):
                ans=max(ans, (nums[i]-1) * (nums[j]-1) )

        return ans