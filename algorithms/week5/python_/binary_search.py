# Recursive Binary Search
# NOTE: Using slices for recursion is inefficient as you're better off just setting low and high
def binary_search(data, target) -> bool:
    if len(data) <= 1:
        return data == target

    mid = int((len(data) - 1) / 2)

    if target == data[mid]:
        return True
    if data[mid] > target:
        return binary_search(data[:mid], target)
    else:
        return binary_search(data[mid+1:], target)

print(binary_search([2, 8, 12, 18], 12))
print(binary_search([2, 8, 12, 18], 11))