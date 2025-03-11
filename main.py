from stats import letter_count, sort_characters
def main(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    try:
        with open(filepath) as f:
            booktext = f.read()
            letters_dict = letter_count(booktext)
            words_lst = booktext.split()
            print(f"Found {len(words_lst)} total words")   
            print("--------- Character Count -------")
            char_list = sort_characters(letters_dict)
            for char_info in char_list:
                char = char_info["char"]
                count = char_info["count"]
                print(f"{char}: {count}")
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Double-check the file path and ensure it exists")
    return
if __name__ == "__main__":
    main("books/frankenstein.txt")