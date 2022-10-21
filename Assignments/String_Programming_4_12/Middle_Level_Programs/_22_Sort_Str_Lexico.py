# program to sort a string lexicographically
class Lexicograh:
    def __init__(self):
        pass
    def alpha(self):
        words = txt.split()
        words.sort()
        for word in words:
            print(word)
txt = input("Enter your String:")
l  = Lexicograh()
l.alpha()
