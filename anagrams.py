CHECK_WORDS = ['car','tree','dog','god','dog','arc','girl','boy']

def check_anagrams(array):
    word_dict = {}
    for word in array:
        sorted_word = "".join(sorted(word))
        if sorted_word in word_dict: 
            if word in word_dict.get(sorted_word):
                continue
            word_dict[sorted_word].append(word)
        else: 
            word_dict[sorted_word] = [word]
    return word_dict.values()

print(check_anagrams(CHECK_WORDS))

