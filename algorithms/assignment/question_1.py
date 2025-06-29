def word_encoder(word):
    """
    Indexes words by sound so words that are spelt different but produce the same sound are matched.

    Args:
        word (string): A singular word with no spaces. 
    
    Raises:
        ValueError: When word given contains non alphabet characters.

    Returns:
        str: String which is 4 long containing the first character in uppercase and 3 numbers.
    """
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

    # Case insensitive so the first letter is always uppercase to keep output consistent.
    first = word[0].upper()

    drop_vowels = ["a", "e", "i", "o", "u"]
    drop_consonants = ["y", "h", "w"]

    converted = ""
    for character in word.lower():
        if character in drop_vowels:
            converted += character
        elif character in drop_consonants:
            # Drop these to prevent them affecting adjacent sound groupings.
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

    # Ensures final output is 4 characters long by adding trailing 0s or by trimming off excess.
    return (first + tail + "000")[:4]