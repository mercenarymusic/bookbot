import sys
from stats import num_of_words, characters

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents


def main():
    # if there is no path to book entered...
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        book = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {len(num_of_words(book))} total words")
    print("--------- Character Count -------")
    print(characters(book))

main()