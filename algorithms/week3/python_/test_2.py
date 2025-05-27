def duplicate_check(values):
  for i in range(len(values)):
    key = values[i]
    for j in range(len(values)):
      if i == j:
        break
      if key == values[j]:
        print("duplicate found")
  print("no duplicates found")

# duplicate_check([10, 3, 2, 6])
duplicate_check([10, 3, 2, 6, 10])

