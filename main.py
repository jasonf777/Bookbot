import stats
import sys

def get_book_text(file_path):
    with open(file_path) as book:
        file_content = book.read()
        return file_content
    
def main(path):
    text = get_book_text(path)
    word_count = stats.get_num_words(text)
    character_dictionary = stats.character_count(text)
    dictionary_list = stats.sort_dict(character_dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in dictionary_list:
        for key, value in item.items():
            if key.isalpha():
                print(f"{key}: {value}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]
main(path)
