import string
def is_palindrome(s: str):
    def remove_punctuation(s):
        return ''.join(char for char in s if char not in string.punctuation)
    b = False
    s = str(s)
    cs = remove_punctuation(s)
    words = cs.split()
    js = "".join(words)
    js = js.lower()
    rs = js[::-1]
    print(js)
    print(rs)
    if js == rs:
        b = True
    return b

srt = "A man, a plan, a canal -- Panama"
print(is_palindrome(srt))