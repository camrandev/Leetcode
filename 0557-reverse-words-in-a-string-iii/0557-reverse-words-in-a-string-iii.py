#because it is a string, and is immutable in python, must convert it to a list anyway

#convert the string to a list
#iterate across each string in the list
#reverse each string

#return the list of now reversed strings, joined on a single space


class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")

        reversed_words = [word[::-1] for word in s_list]

        return " ".join(reversed_words)

        
        

        