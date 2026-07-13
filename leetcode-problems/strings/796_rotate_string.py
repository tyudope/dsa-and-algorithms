"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
"""

def rotateString(s:str, goal:str) -> bool:
    if len(s) != len(goal): # There is no possibility to rotate and make them equal.
        return False
    
    length = len(s)
    for _ in range(length):
        # Perform one rotation
        s = s[1:] + s[0]
        print(s)
        if s == goal:
            return True
        
    return False


print(rotateString("selim", "melis"))