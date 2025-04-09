def get_words_array(contents):
    word_array = contents.split()    
    return word_array

def get_num_character_occurrences(word_array):
    character_occurrences = {}
    for word in word_array: 

        word_lowercase = word.lower()
        split_word = list(word_lowercase)         

        for char in split_word:            
            if (char in character_occurrences):
                character_occurrences[char] += 1
            else: 
                character_occurrences[char] = 1
        
    return character_occurrences