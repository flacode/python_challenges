def is_isogram(word):
    letters=[] #maintain a list of letters in the word
    phrase=word.lower() #convert all letters into lowercase for comparison
    for letter in phrase:
        if letter in letters:
            return False
        elif letter.isalpha(): #only append letters to the list
            letters.append(letter)
    return True
