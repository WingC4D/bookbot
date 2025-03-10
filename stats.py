def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def main():
    booktext = get_book_text("books/frankenstein.txt")
    words = booktext.split()
    print(f"{len(words)} words found in the document")
if __name__ == "__main__":
    main()