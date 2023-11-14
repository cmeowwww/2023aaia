class Solution:
    def average(self, salary: List[int]) -> float:
        #print(sum(salary))
        
        total = sum(salary) - max(salary) - min(salary)
        N = len(salary) -2 
        return total / N
        
        #(一樣的，同上)return (sum(salary) -max(salary) -min(salary))/(len(salary)-2))