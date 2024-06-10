def count_words(string):
    string = ''.join(char.lower() if char.isalnum() else ' ' for char in string)
    words = string.split()

    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
