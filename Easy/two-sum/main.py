class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for num in nums:
            x = nums.index(num)
            for i in range(x+1,len(nums)):
                if num + nums[i] == target:
                    return x,i
    
        
#Testing
run = Solution()
print(run.twoSum([2,7,11,15], 9))