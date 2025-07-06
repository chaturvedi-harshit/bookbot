from stats import count_words, get_num_characters, sort_on, get_list_of_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    def main():
        file_contents = get_book_text(sys.argv[1])
        count_of_words = count_words(file_contents)
        print(f"{count_of_words} words found in the document")
        count_of_chars = get_num_characters(file_contents)
        print(count_of_chars)
        list_of_dict = get_list_of_dicts(count_of_chars)
        list_of_dict.sort(reverse=True, key=sort_on)
        # print(list_of_dict)


        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {count_of_words} total words")
        print("--------- Character Count -------")
        for item in list_of_dict:
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    main()
    

