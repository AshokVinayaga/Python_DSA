def get_frequencies_from_scratch(arr):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    return counts

arr = [1,2,2,3,1,2]
print(get_frequencies_from_scratch(arr))