#Find the largest number in an unsorted list
"""
Approch : Iterate through the list while keeping track of the highest number seen so far.

Time Complexity: O(n) you must look at each element once

Space Complexity: O(1) only uses one extra variable.
"""
def find_max(arr):
    if not arr:
        return None

    max_val = arr[0]
    # for num in arr:
    #     if num > max_val:
    #         max_val = num

    i = 0
    while i < len(arr):
        if arr[i] > max_val:
            max_val = arr[i]

        i+=1

    return max_val

arr = [10,5,90,12]
result = find_max(arr)
print(f"Max value in array is: {result}")