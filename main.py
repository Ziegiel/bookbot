from stats import count_words, count_characters, refactor_count_characters

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    char_count = count_characters(book_text)
    refactored_char_count = refactor_count_characters(char_count)
    
    for item in refactored_char_count:
        if item["char"].isalpha():
            print(f"'{item['char']}': {item['num']}")

if __name__ == "__main__":
    main()