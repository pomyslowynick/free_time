def twoSum(nums, target):
    arr_length = len(nums)

    for x in nums:
        i = nums.index(x) + 1
        while i < arr_length:
            if x + nums[i] == target:
                return [nums.index(x),i]
            else:
                i += 1
                
    return None

array1 = range(1,11)
array2 = range(2,20,3)

print(array2)
print(twoSum([2,5,5,11], 10))
