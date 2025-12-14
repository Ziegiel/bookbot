from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    char_count = count_characters(book_text)
    print(char_count)

if __name__ == "__main__":
    main()