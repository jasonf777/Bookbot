def get_num_words(input_text):
    split_text = get_book_text(input_text).split()
    words = len(split_text)
    print(f"{words} words found in the document")