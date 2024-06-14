def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    words_count = get_words_count(text)
    characters_count = get_char_count(text)
    chars_sorted_list = get_dict_to_sorted_list(characters_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} were found in the document")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        else:
            print(f"The {item["char"]} was found {item["num"]} times")

    
    

def get_book_path(book_path):
    with open(book_path) as f:
        return f.read()
    

def get_words_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    lower_case_text = text.lower()
    char_count = {}
    for character in lower_case_text:
        if character not in char_count:
            char_count[character] = 1
        elif character in char_count:
            char_count[character] += 1
    return char_count


def sort_on(dict):
    return dict["num"]


def get_dict_to_sorted_list(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



main()





#  the idea is to create a function to work with. One function one task






