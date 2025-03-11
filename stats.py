def sort_on(dict):
    return dict["count"]
def letter_count(text):
    letters_dict = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
    return letters_dict
def sort_characters(char_dict):
    result = []
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}  # Notice count is stored as a number
        result.append(char_info)
    result.sort(reverse=True,key=sort_on)
    return result