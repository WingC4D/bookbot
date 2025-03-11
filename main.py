from stats import letter_count 
import inspect
print(inspect.getsource(letter_count))  
def main(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    try:
        with open(filepath) as f:
            booktext = f.read()
            letters_dict = letter_count(booktext)
            words_lst = booktext.split()
            print(f"found {len(words_lst)} total words")   
            print("--------- Character Count -------")
            print(letters_dict)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Double-check the file path and ensure it exists")
    return
if __name__ == "__main__":
    main("books/frankenstein.txt")