"""A set does not contain any repeating characters"""
def is_isogram(word):
    phrase=[letter for letter in word.lower() if letter.isalpha()]#remove all the none aphabetic letters from the string
    letters=set(phrase)
    return len(letters)==len(phrase)
