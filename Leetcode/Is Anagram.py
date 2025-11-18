
'''

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.

'''

'''
Answer:


s = "jam"
t = "jar"
if len(s) != len(t):
    print("False)
S = list(s)
T = list(t)
while len(S) != 0:
    if S[0] in T:
        if S.count(S[0]) != T.count(S[0]):
            print("False")
            S = []
        T.remove(S[0])
        S.remove(S[0])

    else:
        print("False")
        S = []
print("True")

'''

'''
Answer 2, 3 (cheating):
    ramefficient

    sjekker om den sorterte stringen er den samme som den andre. 
    return sorted(s) == sorted(t)
    ,

    lager hashmap for begge stringene med bokstaver og antall ganger den dukker opp og sammenligner. 
    tidsefficient
    return Counter(s) == Counter(t)
'''
