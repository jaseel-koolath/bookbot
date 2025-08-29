from stats import get_num_words, get_character_count, sort_char_dict
import sys

def get_book_text(path):
    with open(path) as f:
        content = f.read()
        return content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        content = get_book_text(sys.argv[1])
        words_count = get_num_words(content)
        char_count = get_character_count(content)
        # print(f"{words_count} words found in the document")
        # print(char_count)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {words_count} total words")
        print("--------- Character Count -------")
        char_counts = sort_char_dict(char_count)
        for item in char_counts:
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")


main()