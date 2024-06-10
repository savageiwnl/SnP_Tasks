def combine_anagrams(words_array):
    anagrams = {}

    for word in words_array:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())

# Пример использования
words_array = ["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]
print(combine_anagrams(words_array))