def compress(word):
    count={}
    compressed=''
    for letter in word:
        if letter in count.keys():
            count[letter]+=1
        else:
            count[letter]=1
    
    for letter in sorted(count):
        if count[letter]==1:
            compressed+=letter
        else:
            compressed+=(letter+str(count[letter]))

    return compressed

print compress('aaaabbbbbqvrxv')
