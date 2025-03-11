def main(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    try:
        with open(filepath) as f:
            booktext = f.read()
            words_lst = booktext.split()
            print(f"found {len(words_lst)} total words")
            letters_list = list(booktext.lower())
            letters_dict = {}
            for letter in letters_list:
                if letter in letters_dict:
                    letters_dict[letter] += 1
                else:
                    letters_dict[letter] = 1
        print("--------- Character Count -------")
        print(letters_dict)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Double-check the file path and ensure it exists")
    return
if __name__ == "__main__":
    main("books/frankenstein.txt")