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

def rec_sum(numbers, n):
    if n == 0:
        return numbers[0]
    return numbers[n] + rec_sum(numbers, n-1)

assert rec_sum([2, 3, 5], 2) == 10

