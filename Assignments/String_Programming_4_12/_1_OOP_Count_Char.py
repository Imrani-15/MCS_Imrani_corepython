# "Find the count of charater by using the build in function"
# print("Find the count of the charater by using the build in function:")
# str = input("Enter the string:")
# print(str.count("is"))
#
# "Find the count of charater by using for loop"
# print("\nFind the count of the charater by using the For loop")
# word = "are"
# for i in str.split():
#     if i == word:
#         print(str.count(word))

"Find the count of charater by using functions:"
# print("\nFind the count of the charater by using the Functions")
# def count_str(string,word1):
#     for ele in string.split():
#         if ele == word1:
#             pass
#     print(string.count(word1))
# string = input("Enter your string:")
# word1 = input("Enter your charater:")
# count_str(string,word1)



"Find the count of the character by using oops"
print("\n Find the count of the charater by using the oops")
class Count:
    def __init__(self,string,char):
        self.string = string
        self.char = char
    def count_str(self,string,char):
        self.string = string
        self.char = char
        for ele in string.split():
            if ele == char:
                pass
        print(string.count(char))
string = input("Enter your string:")
char = input("Enter your character:")
c = Count(string,char)
c.count_str(string,char)