def unpure_function(array):
  array[2] = 7

my_array = [0, 1, 2, 3, 4, 5]
print(my_array)
# Output: [0, 1, 2, 3, 4, 5]

unpure_function(my_array)

print(my_array)
# Output: [0, 1, 7, 3, 4, 5]