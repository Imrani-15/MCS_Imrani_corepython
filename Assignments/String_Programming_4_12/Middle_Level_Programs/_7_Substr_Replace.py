# Substring replacement
class Sub_str:
    def __init__(self):
        pass
    def replace_str(self,test_str,word,replacewith):
        self.test_str = test_str
        self.word = word
        self.replacewith = replacewith
        print(test_str.replace(word,replacewith))

test_str = input("enter your string")
word = input("Enter your Word which word you can change:")
replacewith = input("Enter your word which word you can replace")
s = Sub_str()
s.replace_str(test_str,word,replacewith)