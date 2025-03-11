def letter_count(text):
    letters_dict = {}
    for letter in text.lower():
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict