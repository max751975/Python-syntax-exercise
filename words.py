def print_upper_words(words):
    '''Prints all words from the list in upper case
        each on separate line'''
    for word in words:
        print(word.upper())

def print_upper_with_e(words):
    '''Prints in upper case words that are starting with
        letter "e" in any case'''
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_with_given_first_letter(words,must_start_with):
    '''Prints words from [words] list that are starting with the 
    letters from the[must_start_with] list'''
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())