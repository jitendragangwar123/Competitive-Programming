def find_duplicates(nums):
    visited = set()
    res = []
    for num in nums:
        if num in visited:
            res.append(num)
        else:
            visited.add(num)
    return res

nums = list(map(int, input("Enter space-separated numbers: ").split()))
duplicates = find_duplicates(nums)
print("Duplicate numbers:", duplicates)
