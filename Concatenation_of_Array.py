class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #optimal solution(TC(n)=O(1)) S(C(n)=O(n)) 
        op=[]#initalizing output array
        #for i in range(p):#iterating output array to p*n Length
        for i in range(2):#iterating output array to 2*n Length
             for n in nums:op.append(n)#appedning the array with 'n' iterative elements
        return op#printing output array
