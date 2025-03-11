def main(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    t_counter = 0
    p_counter = 0
    c_counter =0
    try:
        with open(filepath) as f:
            booktext = f.read()
            words_lst = booktext.split()
            print(f"found {len(words_lst)} total words")
            letters_list = list(booktext.lower())
            for letter in letters_list:
                if letter == "t":
                    t_counter += 1
                if letter == "e":
                    p_counter += 1
                if letter == "c":
                    c_counter += 1
        dict_list = [
        {"t" : t_counter},
        {"p" : p_counter},
        {"c" : c_counter}
        ]
        print("--------- Character Count -------")
        print(dict_list)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Double-check the file path and ensure it exists")
    return
if __name__ == "__main__":
    main("books/frankenstein.txt")