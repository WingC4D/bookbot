import sys
from stats import letter_count, sort_characters
def main():
    print("script started")
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    try:
        with open(filepath,"r",encoding="utf8") as f:
            booktext = f.read()
            letters_dict = letter_count(booktext)
            words_lst = booktext.split()
            print(f"Found {len(words_lst)} total words")   
            print("--------- Character Count -------")
            char_list = sort_characters(letters_dict)
            for char_info in char_list:
                print(f"{char_info['char']}: {char_info['count']}")
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Double-check the file path and ensure it exists")
        sys.exit(1)
    return
if __name__ == "__main__":
    main()