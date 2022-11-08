# 189 Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)  # for edge case of k > len(nums)
        self.reverse(nums, 0, len(nums)-1)  # reverse whole array [7, 6, 5, 4, 3, 2, 1]
        self.reverse(nums, 0, k-1)  # reverse back original end of the array [5, 6, 7, 4, 3, 2, 1]
        self.reverse(nums, k, len(nums)-1)  # reverse back original beginning of the array [5, 6, 7, 1, 2, 3, 4]
        return nums

    def reverse(self, nums, first, last):
        while first < last:
            nums[first], nums[last] = nums[last], nums[first]
            first += 1
            last -= 1



