def count_words(file_content):
    return len(file_content.split())


def get_num_characters(file_content):
    file_content_to_lower = file_content.lower()
    num_chars_dict = {}
    for char in file_content_to_lower:
        if char not in num_chars_dict:
            num_chars_dict[char] =1
        else:
            num_chars_dict[char] += 1   
    return num_chars_dict


def get_list_of_dicts(dict):
    list_of_dict = []
    for item in dict:
        list_of_dict.append({"char": item, "num": dict[item]})
    return list_of_dict


def sort_on(dict):
    return dict["num"]




