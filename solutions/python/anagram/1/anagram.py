def find_anagrams(word, candidates):
    return [candidate for candidate in candidates if sorted(list(word.lower())) == sorted(list(candidate.lower())) and not word.lower() == candidate.lower()]
