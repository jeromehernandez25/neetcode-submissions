class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create dictionary to hold each integer and its index being its instances
        # create integer to hold current highest frequent elements
        # create an array to hold the most frequent elements
        # iterate through each elements in integer array
        # at each integer, add an instance to their dictionary entry
        # then check if instance number is greater or equal to current highes frequent elements
        # if greater, empty highest array and put element in
        # if equal, append current element into highest array

        # create dictionary and count frequencies of integer
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Append integer frequency and integer to an array
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        
        # Sort array to find frequent elements easily
        arr.sort()

        # Iterate k times, appending and popping the most frequent integer
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res
        