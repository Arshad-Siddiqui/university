# Bubble sort

def BubbleSort(A):
  n = len(A)
  for i in range(n-1):
    for j in range(n-1-i):
      if A[j] > A[j+1]:
        A[j], A[j+1] = A[j+1], A[j]
  return A

# j iterates through the list backwards
# Looks like an O(n^2^) time complexity
print(BubbleSort([3, 2, 7, 5, 6, 3, 1, 7, 4, 8]))

