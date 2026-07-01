def first_non_repeating_character(data: str) -> str:
    counts = {}

    #step 1: Count Frequency
    for char in data:
        counts[char] = counts.get(char, 0) + 1

    #step2: traverse again sequentially
    for char in data:
        if counts[char] == 1:
            return char
        
    return "" #return empty string if all character repeat

data = "programming"
print(first_non_repeating_character(data))