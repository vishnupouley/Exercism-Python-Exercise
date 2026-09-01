def find_anagrams(word, candidates):
    return [candidate for candidate in candidates if sorted(word.lower()) == sorted(candidate.lower()) and not word.lower() == candidate.lower()]
