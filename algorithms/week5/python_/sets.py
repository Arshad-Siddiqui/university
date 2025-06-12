shopping_lists = [
    ["milk", "bread", "eggs", "apples"],
    ["bread", "eggs", "bananas", "apples"],
    ["milk", "bread", "apples"]
]

def find_common_items(lists):
  if len(lists) == 0:
    return []

  og_set = set(lists[0])

  for list in lists:
    og_set = og_set.intersection(list)

  return og_set

print(find_common_items(shopping_lists))