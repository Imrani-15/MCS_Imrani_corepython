class First_Last:
    def __init__(self):
#        self.str = str
        pass
    def capitalize_first_last_letters(self):
#        self.str = str
        str = str.title()
#    print(result)
        result = ""
#    print(result)
        for word in str.split():
#        print(result+word[:-1])
#        print(result+word[-1].upper())
            result += word[:-1] + word[-1].upper()+" "
        print(result)
str = input("Enter your String:")
f = First_Last(str)
f.capitalize_first_last_letters(str)