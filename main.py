from stats import get_words_array, get_num_character_occurrences, print_character_count_descending
import sys

def get_booktext(filepath):
    with open(filepath, "r") as f:
        contents = f.read()
        return contents      

def main():
    args = sys.argv
    
    expected_num_args = 2
    if len(sys.argv) < expected_num_args:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path_arg = 1
    file_path = args[file_path_arg]
    contents = get_booktext(file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")    

    word_array = get_words_array(contents)
    print("----------- Word Count ----------")
    print("Found", len(word_array), "total words")

    print("--------- Character Count -------")
    num_char_occurrences = get_num_character_occurrences(word_array)
    print_character_count_descending(num_char_occurrences)

if __name__ == '__main__':
    main()


   
