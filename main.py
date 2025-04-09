from stats import get_words_array, get_num_character_occurrences

def get_booktext(filepath):
    with open(filepath, "r") as f:
        contents = f.read()
        return contents      
   
def main():
    contents = get_booktext('books/frankenstein.txt')

    word_array = get_words_array(contents)
    print(len(word_array), "words found in the document")

    num_char_occurrences = get_num_character_occurrences(word_array)
    print(num_char_occurrences)

if __name__ == '__main__':
    main()