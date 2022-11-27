class Solution:

    def sort_colors(self, nums):
        i = curr = 0
        j = len(nums)-1
        while curr <= j:
            if nums[curr] == 0:
                nums[i], nums[curr] = nums[curr], nums[i]
                i += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[j] = nums[j], nums[curr]
                j -= 1
            else:
                curr += 1
        return nums





