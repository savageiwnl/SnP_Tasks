import string

class Solution:

    def is_palindrome(self, s: str) -> bool:
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

s = "A man, a plan, a canal -- Panama"
sol = Solution()
res = sol.is_palindrome(s)
print(res)