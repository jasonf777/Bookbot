import string

def get_num_words(text):
    words = len(text.split())
    return words

def character_count(text):
    char_dict = {}
    lower_case = text.lower()
    for char in lower_case:
        if char in char_dict:
            char_dict[char] += 1
        elif char not in char_dict:
            char_dict[char] = 1
    return char_dict

def sort_dict(dict):
    dict_list = [{key:value} for key, value in dict.items()]
    dict_list.sort(key = lambda x: list(x.values())[0], reverse = True)
    return dict_list
    
