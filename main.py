def get_booktext(filepath):
    with open(filepath, "r") as f:
        contents = f.read()
        get_word_count(contents)

def get_word_count(contents):
    word_array = contents.split()
    print(len(word_array), "words found in the document")
        
def main():
    get_booktext('books/frankenstein.txt')

if __name__ == '__main__':
    main()