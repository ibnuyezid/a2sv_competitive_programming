class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        for i in range(size):
            for j in range(i+1,size):
                if nums[j]<nums[i]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                       
