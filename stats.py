char_dictionary = {}
cleaned_dictionary = {}
deleted_key_list = [] 
keys = []
values = []

def num_of_words(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents.split()

def characters(book):
    with open(book) as f:
        file_contents = f.read()
    file_contents = file_contents.lower()
    
    # count number of each character
    for char in file_contents:
        lowered = char.lower()
        if lowered not in char_dictionary:
            char_dictionary[lowered] = 1
        else: 
            char_dictionary[lowered] += 1

    for char in char_dictionary:
        if(char.isalpha()):
            cleaned_dictionary[char] = char_dictionary[char]
    
    # sort cleaned dictionary 
    my_list = sorted(cleaned_dictionary.items(), key=lambda item: item[1], reverse=True)

    
    for letter, number in my_list:
        print(f"{letter}: {number}")
    