def get_words_array(contents):
    word_array = contents.split()    
    return word_array

def get_num_character_occurrences(word_array):
    character_occurrences = []

    # Loop through each word
    for word in word_array: 
        word_lowercase = word.lower()
        split_word = list(word_lowercase)         

        # Loop through each character
        for char in split_word:
            char_found = False
            
            if char.isalpha() == False: 
                continue

            for occurence in character_occurrences:            
                if occurence["char"] == char:                
                    occurence["count"] += 1
                    char_found = True       

            if not char_found:
                character_occurrences.append({'char': char, 'count': 1})               
    
    return character_occurrences

def print_character_count_descending(num_char_occurrences):
    num_char_occurrences.sort(reverse=True, key=sort_on)

    for occurence in num_char_occurrences:
        print(f"{occurence["char"]}: {occurence["count"]}")    
    
def sort_on(dict):
    return dict["count"]

