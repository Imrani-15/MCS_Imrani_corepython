
# Vowels = 'aeiuoAEIUO'
# final = []
# for word in str:
#     if word in Vowels:
#         final.append(word)
# print("Find the vowels from a string:",final)
# print("Count and display the vowels of the given string:",len(final))

print("\n====by using oops======")
class Str_Vowels:
    def __init__(self,str):
        self.str = str
    def result(self):
        Vowels = 'aeiuoAEIUO'
        final = []
        for word in str:
            if word in Vowels:
                final.append(word)
        print("Find the vowels from a string:",final)
        print("Count and display the vowels of the given string:",len(final))
str = input("enter your string:")
s = Str_Vowels(str)
s.result()