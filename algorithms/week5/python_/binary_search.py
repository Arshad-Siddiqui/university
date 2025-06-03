# Recursive Binary Search
# NOTE: Using slices for recursion is inefficient as you're better off just setting low and high. This version is O(n) because of the crazy slicing.
def binary_search_slice(data, target) -> bool:
    if len(data) <= 1:
        return data == target

    mid = int((len(data) - 1) / 2)

    if target == data[mid]:
        return True
    if data[mid] > target:
        return binary_search_slice(data[:mid], target)
    else:
        return binary_search_slice(data[mid+1:], target)

print(binary_search_slice([2, 8, 12, 18], 12))
print(binary_search_slice([2, 8, 12, 18], 11))

def binary_search(data, target, low=0, high=None):
    if high == None:
        high = len(data)

    if low > high:
        return False
    
    mid = int((low + high) / 2)

    if data[mid] == target:
        return True
    elif data[mid] < target:
        return binary_search(data, target, low, mid + 1)
    else:
        return binary_search(data, target, mid - 1, high)

print(binary_search([2, 8, 12, 18], 12))
print(binary_search([2, 8, 12, 18], 11))