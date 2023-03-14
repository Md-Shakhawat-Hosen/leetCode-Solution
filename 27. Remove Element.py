nums = [0,1,2,2,3,0,4,2]
#nums = [3,2,2,3]
val = 2
nums.sort()
i = 0
while i < len(nums):
    if nums[i] == val:
        nums.remove(val)
        i = i - 1
    i = i + 1
print(nums)