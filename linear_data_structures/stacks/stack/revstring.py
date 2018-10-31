# Write a function revstring(mystr) that uses a stack to reverse the characters in a string.

from Stack import Stack

def revstring(mystr):
    newstr = ""
    s = Stack()
    for char in mystr:
        s.push(char)
    for i in range(s.size()):
        newstr += str(s.pop())
    return newstr
