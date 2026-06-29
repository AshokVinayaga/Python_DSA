def second_largest(arr):
    if not arr:
        return None
    
    largest = second = float('-inf')
   
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
                
    return second if second != float('-inf') else None

arr = [10, 20, 90, 30]
result = second_largest(arr)
print(f"Second Largest number is: {result}")