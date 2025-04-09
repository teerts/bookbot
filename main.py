def get_booktext(filepath):
    with open(filepath, "r") as f:
        contents = f.read()
        print(contents)
        
def main():
    get_booktext('books/frankenstein.txt')

if __name__ == '__main__':
    main()