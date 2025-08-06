def is_pangram(sentence):
    return len(set([letter in [char.lower() for char in sentence if char.isalpha()] 
        for letter in list(map(chr, range(97, 123)))])) == 1 if sentence else False
