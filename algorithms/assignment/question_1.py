def word_encoder(word):
    if not word.isalpha():
        raise ValueError("Word must only contain alphabet characters")
    
    first = word[0].upper()
    rest = word[1:].lower()

    converter = {}

    converter.update(dict.fromkeys(["b", "f", "p", "v"], 1))
    converter.update(dict.fromkeys(["c", "g", "j", "k", "q", "s", "x", "z"], 2))
    converter.update(dict.fromkeys(["d", "t"], 3))
    converter.update(dict.fromkeys(["l"], 4))
    converter.update(dict.fromkeys(["m", "n"], 5))
    converter.update(dict.fromkeys(["r"], 6))

    drop_list = ["a", "e", "i", "o", "u", "y", "h", "w"]

    converted = ""

    for character in rest:
        if character in drop_list:
            continue
        converted += str(converter[character])
    
    return first + converted

print(word_encoder("abcdefghijklmnopqrstuvwxyz"))