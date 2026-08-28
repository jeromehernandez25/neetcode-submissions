class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # create hashmap/dictionary
        for i, num in enumerate(nums): #iterate through nums using index and value
            complement = target - num # save complement of current number
            if complement in hashmap: # if its complement is in dictionary, return both
                return [hashmap[complement], i]
            
            hashmap[num] = i #if not, save value as a key with index and value in hashmap
        
        return []