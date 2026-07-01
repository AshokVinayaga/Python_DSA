def find_duplicates(arr: list[int]) -> list[int]:
    seen = set() #0(1) lookups
    duplicates = set() #using a set avoids adding the same duplicate twice

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

arr = [1, 2, 3, 2, 4, 1]
print(find_duplicates(arr))
