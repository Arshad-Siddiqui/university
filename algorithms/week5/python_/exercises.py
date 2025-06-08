# Exercise 1

def ispalindrome(word, n=0) -> bool:
    m = n + 1
    if n == len(word):
        return True

    if word[n] != word[-m]:
        return False
    return ispalindrome(word, n + 1)

# I could improve the algorithm by stopping it halfway
print(ispalindrome("racecar"))
print(ispalindrome("racecarnt"))