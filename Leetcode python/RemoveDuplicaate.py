class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        n=len(nums)
        while i < n-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                n-=1  
            else:
                i+=1
        return n
nums=[0,0,1,1,1,2,2,3,3,4]
solution=Solution()
k=solution.removeDuplicates(nums)
print(k)
