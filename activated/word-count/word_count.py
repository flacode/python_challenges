def word_count(sentence):
    list_of_words=sentence.split(' ')
    no_of_occurances={}
    for word in list_of_words:
        word=word.casefold()
        if word in no_of_occurances.keys():
            no_of_occurances[word]=no_of_occurances[word]+1
        else:
            no_of_occurances[word]=1
    return no_of_occurances
