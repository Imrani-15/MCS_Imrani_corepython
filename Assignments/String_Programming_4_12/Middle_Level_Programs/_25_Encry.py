# program to create a Caesar encryption
import string
class Caesar:
    def __init__(self):
        pass
    def encryption(self):
        alphabet = string.ascii_lowercase
        shifted = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet, shifted)
        encrypted = txt.translate(table)
        print(encrypted)
txt = input("Enter your string: ")
shift = int(input("Enter the your shift number: "))
c = Caesar()
c.encryption()