class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            if hashmap.get(i) is None:
                hashmap[i] = 1
            else:
                return True

        return False