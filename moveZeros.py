nums = [0]
re = nums.count(0)
nums.sort()
for i in range(0,re):
    nums.remove(0)

for i in range(0,re):
    nums.append(0)

print(nums)

