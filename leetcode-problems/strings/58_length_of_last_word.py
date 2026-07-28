"""
58. Length of Last Word

Given a string s consisting words and spaces, return the length ofr the last word in the string.

A word is maximal substring consisting of non-space characters only.


"""

test1 = "Hello World"
test2 = "   fly me to the moon "
test3 = "luffy is still joyboy"

def lengthOfLastWord(s: str) -> int:

    return len(s.strip(" ").split()[-1])

print(lengthOfLastWord(test3))