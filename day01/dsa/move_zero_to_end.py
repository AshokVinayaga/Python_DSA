def move_zero_to_end(arr):
    non_zero_index = 0

    #move non_zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
            
    #Fill the remaining elements with zero
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0
        
    return arr

arr = [0,1,0,3,12]
print(f"before Move Non Zero to End List is: {arr}")
print(f"Move Non Zero to End List is: {move_zero_to_end(arr)}")
