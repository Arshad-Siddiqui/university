import copy

# Exercise 1

def ispalindrome(word, n=0) -> bool:
    m = n + 1
    # Check half the word to save time.
    if n >= len(word) // 2:
        return True

    if word[n] != word[-m]:
        return False
    return ispalindrome(word, n + 1)

assert ispalindrome("racecar") == True
assert ispalindrome("racecarnt") == False

# Exercise 2

def rec_sum(numbers, n=None):
    """n is just for implementation and should be ignored by user. numbers is a list of ints"""
    # Check we aren't just handed an empty list
    if len(numbers) == 0:
        return 0

    # So the user doesn't have to define n themself.
    if n is None:
        n = len(numbers) - 1

    # Base case meaning n has been used to index the entire list.
    if n == 0:
        return numbers[0]
    
    return numbers[n] + rec_sum(numbers, n-1)

assert rec_sum([2, 3, 5]) == 10
assert(rec_sum([])) == 0

# Exercise 3

def sum_digits(number, total=0):
    """Function takes an integer >= 0 and returns the sum of the digits. e.g. 123 -> 6"""
    # Base case
    if number == 0:
        return total
    
    # Give us last number 123 -> 3
    total += number % 10
    # Trims off last number 123 -> 12.3 -> 12
    left = number // 10
    return sum_digits(left, total)

assert sum_digits(123) == 6, f"sum_digits(123) was supposed to give 6 but gave {sum_digits(123)}"

# Exercise 4

def flatten(lst) -> list:
# iterate through list.
# if element is list we flatten it
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened
assert flatten([10, 13, [11, 12]]) == [10, 13, 11, 12]

# Exercise 5

def merge(a, b):
    """a and b are sorted lists. The function returns 1 sorted list"""
    # Come back later
