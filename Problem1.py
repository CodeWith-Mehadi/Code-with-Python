class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Dictionary to store the number and its index
        for i, num in enumerate(nums):  # Loop through the list
            complement = target - num  # Calculate the complement
            if complement in num_map:  # If complement exists in the dictionary
                return [num_map[complement], i]  # Return indices of the complement and the current number
            num_map[num] = i  # Otherwise, store the current number and its index
