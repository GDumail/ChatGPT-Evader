characters = {
    "A": "А",
    "a": "а",
    "B": "В",
    "S": "Ѕ",
    "s": "ѕ",
    "M": "М",
    "H": "Н",
    "O": "О",
    "o": "о",
    "P": "Р",
    "p": "р",
    "C": "С",
    "c": "с",
    "T": "Т",
    "X": "Х",
    "x": "х",
    "I": "Ι",
    "N": "Ν",
    "Y": "Υ",
    "Z": "Ζ"
}

with open("detected.txt", "r", encoding="utf-8") as detected:
    data = detected.read()
    for i, (k, v) in enumerate(characters.items()):
        data = data.replace(k, v)
    with open("undetected.txt", "w", encoding="utf-8") as undetected:
        undetected.write(data)
    undetected.close()
detected.close()