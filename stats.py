def main(filepath):
    try:
        with open(filepath) as f:
            booktext = f.read()
            words = booktext.split()
            print(f"{len(words)} words found in the document")
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Double-check the file path and ensure it exists")
    return
if __name__ == "__main__":
    main("books/frankenstein.txt")