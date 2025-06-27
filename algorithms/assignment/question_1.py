def word_encoder(word):
    if not word.isalpha():
        raise ValueError("Word must only contain alphabet characters")
    
    # Map that converts values into corresponding numbers
    converter = {}
    converter.update(dict.fromkeys(["b", "f", "p", "v"], 1))
    converter.update(dict.fromkeys(["c", "g", "j", "k", "q", "s", "x", "z"], 2))
    converter.update(dict.fromkeys(["d", "t"], 3))
    converter.update(dict.fromkeys(["l"], 4))
    converter.update(dict.fromkeys(["m", "n"], 5))
    converter.update(dict.fromkeys(["r"], 6))
    # --- Map ends here ---

    first = word[0]
    drop_vowels = ["a", "e", "i", "o", "u"]
    drop_consonants = ["y", "h", "w"]

    converted = ""
    low_word = word.lower()

    # Converts all values into numbers if they map
    for character in low_word:
        if character in drop_vowels:
            converted += character
        elif character in drop_consonants:
            # consonants aren't making it to the converted list
            # so we can compare adjacent values.
            pass
        else:
            converted += str(converter[character])

    result = []

    previous = None
    for current in converted:
        if current != previous:
            result.append(current)
        previous = current
    
    converted = "".join(result)

    # Duplicates decimated now need to just remove vowels

    for vowel in drop_vowels:
        converted = converted.replace(vowel, "")

    converted = first + converted[1:]

    # Covers case where word is too short and needs trailing 0s
    # to make up 3 digits.
    while len(converted) < 4:
        converted += '0'

    return converted

test_list = [
    ["abcdefghijklmnopqrstuvwxyz", "checks none of the values break anything"],
    ["ab", "check for a short sequence, should be a100"],
    ["Rubin", "Rubin should be R150"],
    ["Rupert", "Rupert should be R163"],
    ["Robert", "Robert should be R163"],
    ["Tymczak", "Tymczak should be T522"],
    ["Pfister", "Pfister should be P263"]
    ]

for test in test_list:
    print("-----")
    print(word_encoder(test[0]))
    print(test[1])
    print("-----")