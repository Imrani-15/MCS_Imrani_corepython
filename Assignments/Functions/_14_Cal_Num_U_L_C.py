# accepts a string and calculate the number of upper case letters and lower case letters
class Cal_Num_Letter:
    def __init__(self):
        pass
    def char_up_low(self):
        count = 0
        count1 = 0
        for chat in text:
            if (chat.islower()):
                count = count+1
            elif (chat.isupper()):
                count1 = count1+1
        print("The number of lowercase character is:",count)
        print("The number of uppercase character is:",count1)
text = input("enter your string:")
c = Cal_Num_Letter()
c.char_up_low()