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
    for character in word.lower():
        if character in drop_vowels:
            converted += character
        elif character in drop_consonants:
            # consonants aren't making it to the converted list
            # so we can compare adjacent values.
            pass
        else:
            converted += str(converter[character])

    result = []

    previous = ""
    for current in converted:
        if current != previous:
            result.append(current)
        previous = current
    
    converted = "".join(result)

    tail = converted [1:]
    for vowel in drop_vowels:
        tail = tail.replace(vowel, "")

    return (first + tail + "000")[:4]