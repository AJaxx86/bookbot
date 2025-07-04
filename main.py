from stats import count_words
from stats import count_characters
from stats import sort_chars
import sys

book_filepath = ""

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_filepath = sys.argv[1]

    book_contents = get_book_text(book_filepath)
    num_words = count_words(book_contents)
    sorted_characters = sort_chars(count_characters(book_contents))

    print_report(book_filepath, num_words, sorted_characters)

def get_book_text(filepath):
    contents = ""
    with open(filepath) as text_file:
        contents = text_file.read()

    return contents

def print_report(path_to_book, num_words, chars):
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path_to_book + "...")
    print("----------- Word Count ----------")
    print("Found " + str(num_words) + " total words")
    print("--------- Character Count -------")
    for c in chars:
        print(c["char"] + ": " + str(c["num"]))
    print("============= END ===============")

main()