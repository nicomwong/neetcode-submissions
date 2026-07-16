class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenValuesToIndices = dict() # will store num->index mappings
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seenValuesToIndices:
                complIndex = seenValuesToIndices[complement]
                return [complIndex, index] # complIndex < index
            
            seenValuesToIndices[num] = index

        return [-1, -1]