class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start =0
        end= len(height)-1
        output = 0
        
        while start < end:
            m = (end-start) * min(height[start], height[end])
            if m > output:
                output = m
            if height[start] < height[end]:
                start+=1
            else:
                end-=1
        return output
