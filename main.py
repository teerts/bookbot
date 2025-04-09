from stats import get_words_array, get_num_character_occurrences, print_character_count_descending

def get_booktext(filepath):
    with open(filepath, "r") as f:
        contents = f.read()
        return contents      
   
def main():
    relative_path = 'books/frankenstein.txt'
    contents = get_booktext(relative_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")    

    word_array = get_words_array(contents)
    print("----------- Word Count ----------")
    print("Found", len(word_array), "total words")

    print("--------- Character Count -------")
    num_char_occurrences = get_num_character_occurrences(word_array)
    print_character_count_descending(num_char_occurrences)

if __name__ == '__main__':
    main()