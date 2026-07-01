def two_sum(nums: list[int], target:int) -> list[int]:
    n = len(nums)
    #outer loops selects the first number
    for i in range(n):
        #inner Loops select the second number (always ahead i to avoid reuse)
        for j in range(i+1, n):
            if nums[i] + nums[j] ==target:
                return [i,j]
            
    return [] #fallback if no pair matches the target

nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))

# Optimized verion using diffenct technique to find two sum

def two_sum_optimized(num: list[int], target: int) -> list[int]:
    #key: the number seen, Value: its index in the array
    lookup = {}

    for current_index, current_num in enumerate(nums):
        needed = target - current_num

        #check if the compliment is already in our memory
        if needed in lookup:
            return [lookup[needed], current_index]
        
        #Store the current numner and index in the future pairs
        lookup[current_num] = current_index

    return []

nums = [2,7,11,15]
target = 9
print(two_sum_optimized(nums, target))