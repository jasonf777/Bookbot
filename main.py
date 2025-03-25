def get_book_text(file_path):
    with open(file_path) as book:
        file_content = book.read()
        return file_content
    
def main(path):
    print(get_book_text(path))

def word_count(input_text):
    split_text = get_book_text(input_text).split()
    words = len(split_text)
    print(f"{words} words found in the document")

word_count("./books/frankenstein.txt")
