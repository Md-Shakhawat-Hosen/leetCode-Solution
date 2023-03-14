#nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [1,1,2]
i = 0
while i < len(nums)-1:
    if nums[i] == nums[i+1]:
        del nums[i]
        i = i - 1
    i = i + 1

print(nums)