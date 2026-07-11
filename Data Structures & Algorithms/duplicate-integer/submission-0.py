class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set of numbers dynamically grows during runtime
        # grows from 0 to size(nums)        
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False

        # # set of numbers is consistent across runtime
        # # constant size of size(nums)
        # seen = set(nums)
        
        # for num in nums:
        #     if num in seen:
        #         return True
        
        # return False