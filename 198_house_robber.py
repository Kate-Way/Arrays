def rob(nums):
    start_from_0 = 0
    start_from_1 = 0
    for n in nums:
        max_sum = max(start_from_0 + n, start_from_1)
        start_from_0 = start_from_1
        start_from_1 = max_sum
    return start_from_1

