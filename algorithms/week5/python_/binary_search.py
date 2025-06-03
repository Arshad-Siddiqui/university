# Recursive Binary Search

def binary_search(data, target, low, high) -> bool:
    """Returns true if target is contained in data. Low and high mark which part of the data to check"""
    if low > high:
        return False

    mid = int((low + high)/2)

    if target == data[mid]:
        return True
    if data[mid] > target:
        return binary_search(data, target, low, mid)
    else:
        return binary_search(data, target, mid, high)

# print(binary_search([2, 8, 12, 18], 12, 0, 3))
print(binary_search([2, 8, 12, 18], 11, 0, 3))