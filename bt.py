def permutation(nums, start, end):
    if (start == end):
        print(nums)
    else:
        for i in range(start, end + 1):
            nums[start], nums[i] = nums[i], nums[start]
            permutation(nums, start + 1, end)
            nums[start], nums[i] = nums[i], nums[start]


permutation([1, 2, 3], 0, 2)