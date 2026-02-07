
from typing import List
class Solution:
    def sortColorsUsingbobbleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute-force approach using bobble sort
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute-force approach would be to count the number of 0s, 1s and 2s and then overwrite the array.
        count0, count1, count2 = 0, 0, 0
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1
        for i in range(len(nums)):
            if i < count0:
                nums[i] = 0
            elif i < count0 + count1:
                nums[i] = 1
            else:
                nums[i] = 2
    
    def sortColorsOptimal(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Optimal approach using Dutch National Flag Algorithm
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1