
'''
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''
def reverseString(s):
    string_len = len(s)
    i = 0
    j = string_len - 1

    if string_len == 1:
        return s

    print((i != j and string_len % 2 != 0))

    while((i != j and string_len % 2 != 0) or (i < j and string_len % 2 == 0)):
        copy = s[i]
        s[i] = s[j]
        s[j] = copy
        i = i + 1
        j = j - 1

    return s

s = ["h","e","l","l","o"]
output = reverseString(s)
print(output)
