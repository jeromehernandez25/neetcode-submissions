class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Problem is that if there is a 0, then we need to account
        # for it as it will zero out all the other elements in output

        # Iterate through the array, and get the products
        # but whenever a 0 value is encountered, mark its index and move on
        total = 1
        zeroes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes.append(i)
                continue
            total *= nums[i]

        # If more than 1 zero exists, then return array with all 0s
        # If only 1 exists, then replace the 1 zero with the product
        if zeroes:
            # 2 or more zeroes
            if len(zeroes) > 1:
                return [0] * len(nums)

            # 1 zero
            output = [0] * len(nums)
            output[zeroes[0]] = total
            return output

        # If no zeroes, initialize all values to total and divide by each
        # element's value
        output = [total] * len(nums)
        for i in range(len(nums)):
            output[i] = int(output[i] / nums[i])
        
        return output