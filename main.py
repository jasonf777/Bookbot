from stats import get_num_words

def get_book_text(file_path):
    with open(file_path) as book:
        file_content = book.read()
        return file_content
    
def main(path):
    print(get_book_text(path))

get_num_words("./books/frankenstein.txt")

