
'''
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    words = s.split()
    idx = 0

    for word in words:
        string_len = len(word)
        i = 0
        j = string_len - 1

        while((i != j and string_len % 2 != 0) or (i < j and string_len % 2 == 0)):
            word = list(word)
            copy = word[i]
            word[i] = word[j]
            word[j] = copy
            word = "".join(word)
            i = i + 1
            j = j - 1
            words[idx] = word

        idx = idx + 1

    return " ".join(words)


s = "I love u"
output = reverseWords(s)
print(output)
